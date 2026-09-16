"""GitHub: dataset/tool discovery, repository cloning, READMEs and annotation guidelines.

Search results are cached in ``corpus/github_search_cache.json`` (committed). The cache
is authoritative: if a query is already answered there the pipeline never re-queries it,
which keeps re-runs free and makes the run reproducible in an environment whose egress
policy blocks the GitHub search API. When the REST API is reachable and a query is not
yet cached, it is fetched with ``GITHUB_TOKEN``/``GH_TOKEN`` if either is set.
"""
from __future__ import annotations

import fnmatch
import json
import os
import subprocess
from pathlib import Path

from ..util import iso_now

API = "https://api.github.com"
README_NAMES = ("README.md", "README.rst", "README.txt", "README", "readme.md")
LICENCE_NAMES = ("LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "LICENCE.md", "COPYING")


class GitHub:
    name = "github"
    probe_url = f"{API}/rate_limit"

    def __init__(self, cfg, http=None):
        self.cfg, self.http = cfg, http
        spec = cfg["sources"]["github"]
        self.cache_path = cfg.path(spec["search_cache"])
        self.clone_root = cfg.path(spec["clone_root"])
        self.cache = self._load_cache()

    # -- search cache ------------------------------------------------------
    def _load_cache(self) -> dict:
        if self.cache_path.exists():
            return json.loads(self.cache_path.read_text())
        return {"repo_queries": {}, "code_queries": {}, "missing": []}

    def save_cache(self) -> None:
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        self.cache["missing"] = sorted(set(self.cache.get("missing", [])))
        self.cache_path.write_text(json.dumps(self.cache, indent=2, sort_keys=True) + "\n")

    @property
    def token(self) -> str:
        tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
        return "" if tok == "proxy-injected" else tok

    def _headers(self) -> dict:
        h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        return h

    def search_repositories(self, query: str, limit: int = 20) -> list[dict]:
        """Cached repository search. Returns [{full_name, description, stars, topics, url}]."""
        hit = self.cache["repo_queries"].get(query)
        if hit:
            return hit["items"][:limit]
        data = None
        if self.http is not None:
            data = self.http.json(self.name, f"{API}/search/repositories",
                                  {"q": query, "per_page": min(limit, 50), "sort": "stars"},
                                  self._headers())
        if not data or "items" not in data:
            self.cache.setdefault("missing", []).append(f"repo:{query}")
            self.save_cache()
            return []
        items = [{
            "full_name": r["full_name"], "description": r.get("description") or "",
            "stars": r.get("stargazers_count", 0), "topics": r.get("topics", []),
            "url": r.get("html_url", ""), "language": r.get("language") or "",
            "updated_at": r.get("updated_at", ""), "archived": r.get("archived", False),
        } for r in data["items"]]
        self.cache["repo_queries"][query] = {
            "fetched_at": iso_now(), "via": "rest", "total_count": data.get("total_count", len(items)),
            "items": items}
        self.save_cache()
        return items[:limit]

    def record_search(self, query: str, items: list[dict], via: str, total: int | None = None,
                      kind: str = "repo") -> None:
        """Store results obtained through another authenticated client (e.g. the GitHub
        MCP server) so the pipeline can reuse them offline and the run stays reproducible."""
        bucket = "repo_queries" if kind == "repo" else "code_queries"
        self.cache.setdefault(bucket, {})[query] = {
            "fetched_at": iso_now(), "via": via,
            "total_count": total if total is not None else len(items), "items": items}
        self.cache["missing"] = [m for m in self.cache.get("missing", [])
                                 if m != f"{kind}:{query}"]
        self.save_cache()

    def code_hits(self, query: str) -> list[dict]:
        return self.cache.get("code_queries", {}).get(query, {}).get("items", [])

    def queries_logged(self) -> dict:
        return {q: v.get("total_count", len(v.get("items", [])))
                for q, v in self.cache.get("repo_queries", {}).items()}

    # -- clones ------------------------------------------------------------
    def clone_dir(self, full_name: str) -> Path:
        return self.clone_root / full_name.replace("/", "__")

    def clone(self, full_name: str, depth: int = 1, log=print) -> Path | None:
        """Shallow-clone once; an existing clone is reused untouched."""
        path = self.clone_dir(full_name)
        if (path / ".git").exists():
            return path
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            subprocess.run(["git", "clone", "--depth", str(depth),
                            f"https://github.com/{full_name}.git", str(path)],
                           capture_output=True, text=True, check=True, timeout=600)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError) as exc:
            log(f"  clone failed {full_name}: {str(exc)[:120]}")
            return None
        return path

    def head(self, full_name: str) -> str:
        path = self.clone_dir(full_name)
        try:
            return subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"],
                                  capture_output=True, text=True, check=True).stdout.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return ""

    # -- files in a clone --------------------------------------------------
    @staticmethod
    def readme(path: Path) -> tuple[str, str]:
        for name in README_NAMES:
            f = path / name
            if f.exists():
                return name, f.read_text(encoding="utf-8", errors="replace")
        for f in sorted(path.glob("*.md"))[:1]:
            return f.name, f.read_text(encoding="utf-8", errors="replace")
        return "", ""

    @staticmethod
    def licence(path: Path) -> str:
        for name in LICENCE_NAMES:
            f = path / name
            if f.exists():
                head = f.read_text(encoding="utf-8", errors="replace")[:400].lower()
                for key, label in (("apache license", "Apache-2.0"), ("mit license", "MIT"),
                                   ("gnu general public", "GPL"), ("gnu lesser", "LGPL"),
                                   ("bsd ", "BSD"), ("creative commons attribution-sharealike", "CC-BY-SA"),
                                   ("creative commons attribution-noncommercial", "CC-BY-NC"),
                                   ("creative commons attribution", "CC-BY"),
                                   ("creative commons", "CC"), ("mozilla public", "MPL")):
                    if key in head:
                        return label
                return "see LICENSE"
        return "unstated"

    @staticmethod
    def guideline_files(path: Path, patterns, limit: int = 12) -> list[Path]:
        """Files that look like annotation manuals, guidelines, schemes or codebooks."""
        out = []
        for f in sorted(path.rglob("*")):
            if not f.is_file() or ".git/" in str(f):
                continue
            if f.suffix.lower() not in {".md", ".txt", ".rst", ".pdf", ".tex", ".html"}:
                continue
            name = f.name.lower()
            if any(fnmatch.fnmatch(name, pat) for pat in patterns):
                out.append(f)
            if len(out) >= limit:
                break
        return out
