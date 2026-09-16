"""Layer 1 (HTTP cache) and layer 2 (status gating) of the idempotency design.

Every outbound call goes through :class:`Http`:

* responses are cached in a SQLite requests-cache database (metadata 30 days,
  binaries forever), keyed on method + URL + sorted params, so a re-run of any
  phase makes no repeat network call for anything already seen;
* a descriptive User-Agent with a contact address identifies the client;
* per-host minimum delays implement the documented rate limits;
* 429 / 5xx are retried with exponential backoff, honouring ``Retry-After``;
* every host is probed once per run, and a host that the sandbox cannot reach is
  recorded in ``corpus/source_status.json`` and skipped instead of retried, so a
  degraded environment slows nothing down and is visible in the run report.
"""
from __future__ import annotations

import json
import random
import time
from pathlib import Path
from urllib.parse import urlsplit

import requests
import requests_cache

from .util import iso_now

NEVER = requests_cache.NEVER_EXPIRE

BINARY_HINTS = ("application/pdf", "application/octet-stream", "application/zip")


class Http:
    def __init__(self, cfg, offline: bool = False):
        self.cfg = cfg
        http = cfg["http"]
        self.offline = offline
        self.timeout = float(http.get("timeout_seconds", 30))
        self.max_retries = int(http.get("max_retries", 5))
        self.backoff_base = float(http.get("backoff_base_seconds", 2.0))
        self.backoff_max = float(http.get("backoff_max_seconds", 64.0))
        self.probe_timeout = float(http.get("probe_timeout_seconds", 12))
        self.min_delay = dict(http.get("min_delay_seconds", {}))
        self._last_call: dict[str, float] = {}
        self._fail_streak: dict[str, int] = {}
        self.calls = {"network": 0, "cache": 0, "skipped_unreachable": 0, "errors": 0}
        # Section 9: every external request is logged with its URL, cache hit/miss and
        # status, and counted per source so the run report can show an API budget.
        self.by_source: dict[str, dict] = {}
        self.request_log = cfg.corpus / "requests.log"
        self.request_log.parent.mkdir(parents=True, exist_ok=True)

        cache_path = cfg.path(http["cache_path"])
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        self.session = requests_cache.CachedSession(
            cache_name=str(cache_path.with_suffix("")),
            backend="sqlite",
            expire_after=int(http.get("metadata_ttl_days", 30)) * 86400,
            allowable_codes=(200, 203, 404, 410),
            allowable_methods=("GET", "HEAD"),
            match_headers=False,
            stale_if_error=True,
        )
        self.session.headers.update(
            {
                "User-Agent": cfg.user_agent,
                "From": cfg.contact,
                "Accept": "application/json",
            }
        )
        self.status_path = cfg.corpus / "source_status.json"
        self.status = self._load_status()

    def _account(self, source: str, url: str, outcome: str, status=None,
                 params: dict | None = None) -> None:
        row = self.by_source.setdefault(
            source, {"network": 0, "cache": 0, "skipped": 0, "errors": 0})
        key = {"hit": "cache", "miss": "network", "skipped": "skipped"}.get(outcome, "errors")
        row[key] += 1
        try:
            with open(self.request_log, "a", encoding="utf-8") as fh:
                full = url
                if params:
                    from urllib.parse import urlencode
                    full = f"{url}?{urlencode({k: v for k, v in params.items() if v is not None})}"
                fh.write(f"{iso_now()}\t{source}\t{outcome}\t{status if status is not None else '-'}"
                         f"\t{full}\n")
        except OSError:
            pass

    def hit_rate(self) -> float:
        total = self.calls["network"] + self.calls["cache"]
        return (self.calls["cache"] / total) if total else 0.0

    # -- reachability ------------------------------------------------------
    def _load_status(self) -> dict:
        if self.status_path.exists():
            try:
                return json.loads(self.status_path.read_text())
            except json.JSONDecodeError:
                return {}
        return {}

    def save_status(self) -> None:
        self.status_path.parent.mkdir(parents=True, exist_ok=True)
        self.status_path.write_text(json.dumps(self.status, indent=2, sort_keys=True) + "\n")

    def credentials(self) -> dict:
        """Which optional credentials this run has, so the report can name what is degraded."""
        import os
        return {
            "S2_API_KEY": bool(os.environ.get("S2_API_KEY")),
            "GITHUB_TOKEN": bool(os.environ.get("GITHUB_TOKEN")
                                 and os.environ.get("GITHUB_TOKEN") != "proxy-injected"),
            "contact_email": bool(self.cfg.contact),
            "UNPAYWALL_EMAIL": bool(os.environ.get("UNPAYWALL_EMAIL") or self.cfg.contact),
        }

    def probe(self, source: str, url: str) -> bool:
        """Probe a source once per process; remember the verdict for the report."""
        entry = self.status.get(source)
        if entry and entry.get("_probed_this_run"):
            return bool(entry["reachable"])
        if self.offline:
            self.status[source] = {"reachable": False, "reason": "offline mode", "_probed_this_run": True}
            return False
        reachable, reason = True, "ok"
        try:
            with self.session.cache_disabled():
                resp = self.session.get(url, timeout=self.probe_timeout)
            reason = f"HTTP {resp.status_code}"
            if resp.status_code >= 400:
                # A probe URL that does not answer 2xx/3xx is not usable, whether the
                # refusal comes from the service or from an egress policy in front of it.
                reachable = False
                if resp.status_code in (401, 403, 405, 407) and _is_proxy_denial(resp):
                    reason = f"egress policy denied ({resp.status_code})"
        except requests.RequestException as exc:  # DNS, TLS, refused CONNECT, timeout
            reachable, reason = False, f"{type(exc).__name__}: {str(exc)[:160]}"
        self.status[source] = {
            "reachable": reachable,
            "reason": reason,
            "probe_url": url,
            "_probed_this_run": True,
        }
        return reachable

    def unreachable(self, source: str) -> bool:
        entry = self.status.get(source)
        return bool(entry) and not entry.get("reachable", True)

    # -- requests ----------------------------------------------------------
    def _throttle(self, source: str) -> None:
        delay = float(self.min_delay.get(source, self.min_delay.get("default", 1.0)))
        last = self._last_call.get(source)
        if last is not None:
            wait = delay - (time.monotonic() - last)
            if wait > 0:
                time.sleep(wait)
        self._last_call[source] = time.monotonic()

    def get(self, source: str, url: str, params: dict | None = None, *, binary: bool = False,
            headers: dict | None = None, allow_error: bool = True) -> requests.Response | None:
        """Cached GET. Returns None when the source is unreachable or exhausted."""
        if self.unreachable(source) or self.offline:
            self.calls["skipped_unreachable"] += 1
            self._account(source, url, "skipped", params=params)
            return None
        expire = NEVER if binary else None
        attempt = 0
        while True:
            try:
                kwargs = {"params": params, "timeout": self.timeout, "headers": headers or {}}
                if expire is not None:
                    kwargs["expire_after"] = expire
                # Only throttle when the answer is not already cached.
                key = self.session.cache.create_key(
                    requests.Request("GET", url, params=params, headers=headers or {}).prepare()
                )
                cached = self.session.cache.contains(key)
                if cached:
                    self.calls["cache"] += 1
                else:
                    self._throttle(source)
                    self.calls["network"] += 1
                resp = self.session.get(url, **kwargs)
                self._account(source, url, "hit" if cached else "miss", resp.status_code, params)
            except requests.RequestException as exc:
                attempt += 1
                self.calls["errors"] += 1
                self._account(source, url, "error", type(exc).__name__, params)
                streak = self._fail_streak.get(source, 0) + 1
                self._fail_streak[source] = streak
                if streak >= 3 and source not in self.status:
                    # A host that refuses three connections in a row is not going to
                    # answer the next two hundred; stop paying the backoff for it.
                    self.status[source] = {"reachable": False, "_probed_this_run": True,
                                           "reason": f"{type(exc).__name__}: {str(exc)[:120]}"}
                    return None
                if attempt > self.max_retries:
                    if allow_error:
                        return None
                    raise
                self._sleep_backoff(attempt)
                continue
            if resp.status_code in (429,) or 500 <= resp.status_code < 600:
                attempt += 1
                self.calls["errors"] += 1
                if attempt > self.max_retries:
                    return None if allow_error else resp
                self._sleep_backoff(attempt, resp.headers.get("Retry-After"))
                continue
            self._fail_streak[source] = 0
            return resp

    def _sleep_backoff(self, attempt: int, retry_after: str | None = None) -> None:
        if retry_after:
            try:
                time.sleep(min(float(retry_after), self.backoff_max))
                return
            except (TypeError, ValueError):
                pass
        delay = min(self.backoff_base ** attempt, self.backoff_max)
        time.sleep(delay * (0.75 + 0.5 * random.random()))

    def json(self, source: str, url: str, params: dict | None = None, headers: dict | None = None):
        resp = self.get(source, url, params, headers=headers)
        if resp is None or resp.status_code != 200:
            return None
        try:
            return resp.json()
        except ValueError:
            return None

    def download(self, source: str, url: str, dest: Path) -> bool:
        """Download a binary (PDF) through the never-expiring binary cache."""
        resp = self.get(source, url, binary=True, headers={"Accept": "application/pdf,*/*"})
        if resp is None or resp.status_code != 200 or not resp.content:
            return False
        ctype = resp.headers.get("Content-Type", "").lower()
        if "pdf" not in ctype and not resp.content[:5].startswith(b"%PDF"):
            return False
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(resp.content)
        return True


def _is_proxy_denial(resp: requests.Response) -> bool:
    body = (resp.text or "")[:400].lower()
    return any(s in body for s in ("policy", "not allowed", "denied", "forbidden by", "not available"))


# -- layer 2: status gating -----------------------------------------------
PHASE_ORDER = ["candidate", "verified", "tiered", "fetched", "extracted", "chunked"]


def at_state(record: dict, state: str) -> bool:
    """A phase processes only records whose status is exactly its input state."""
    return record.get("status") == state


def at_or_past(record: dict, state: str) -> bool:
    try:
        return PHASE_ORDER.index(record.get("status", "candidate")) >= PHASE_ORDER.index(state)
    except ValueError:
        return False


def advance(record: dict, state: str) -> None:
    """Move a record forward, never backward."""
    if not at_or_past(record, state):
        record["status"] = state
