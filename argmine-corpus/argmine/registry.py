"""The canonical store: corpus/registry.jsonl, plus the frontier and rejection ledgers.

One JSON object per line. Ids follow the documented precedence
``doi: > arxiv: > s2: > openalex: > title:<sha1>``; every other identifier is an alias.

Dedup at upsert: a shared alias, or fuzzy title match >= 0.95 AND |year diff| <= 1 AND at
least one shared author surname. On a match the records are merged, preferring the
published version's metadata over the preprint's while keeping both URLs.
"""
from __future__ import annotations

import json
from pathlib import Path

from rapidfuzz import fuzz

from .util import canonical_id, iso_now, norm_title, surnames

FUZZ_THRESHOLD = 95.0

DOC_TYPES = {
    "journal", "conference", "workshop", "book", "chapter", "thesis",
    "preprint", "guideline", "dataset", "tool",
}
PREPRINT_TYPES = {"preprint"}


def blank_record(**kw) -> dict:
    rec = {
        "id": "",
        "aliases": [],
        "title": "",
        "authors": [],
        "year": None,
        "venue": "",
        "doc_type": "",
        "abstract": "",
        "urls": {},
        "area": [],
        "tier": None,
        "downstream_tags": [],
        "score": {},
        "discovered_from": [],
        "verification": {"status": "unverified", "sources": [], "checked_at": "", "notes": ""},
        "files": {},
        "status": "candidate",
        "annotation": {"text": "", "grounded_on": "none"},
        "criteria_version": 1,
        "updated_at": iso_now(),
    }
    rec.update(kw)
    return rec


def _jsonl_load(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def _jsonl_save(path: Path, rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    tmp.replace(path)


class Registry:
    """Load / mutate / save the three committed ledgers."""

    def __init__(self, cfg):
        self.cfg = cfg
        self.path = cfg.corpus / "registry.jsonl"
        self.frontier_path = cfg.corpus / "frontier.jsonl"
        self.rejected_path = cfg.corpus / "rejected.jsonl"
        self.records: dict[str, dict] = {}
        self.frontier: dict[str, dict] = {}
        self.rejected: dict[str, dict] = {}
        self._alias_index: dict[str, str] = {}
        self.load()

    # -- io ----------------------------------------------------------------
    def load(self) -> None:
        self.records = {r["id"]: r for r in _jsonl_load(self.path)}
        self.frontier = {r["id"]: r for r in _jsonl_load(self.frontier_path)}
        self.rejected = {r["id"]: r for r in _jsonl_load(self.rejected_path)}
        self._reindex()

    def save(self) -> None:
        _jsonl_save(self.path, [self.records[k] for k in sorted(self.records)])
        _jsonl_save(self.frontier_path, [self.frontier[k] for k in sorted(self.frontier)])
        _jsonl_save(self.rejected_path, [self.rejected[k] for k in sorted(self.rejected)])

    def _reindex(self) -> None:
        self._alias_index = {}
        for rid, rec in self.records.items():
            self._alias_index[rid] = rid
            for a in rec.get("aliases", []):
                self._alias_index[a] = rid

    # -- lookup ------------------------------------------------------------
    def by_alias(self, alias: str) -> dict | None:
        rid = self._alias_index.get(alias)
        return self.records.get(rid) if rid else None

    def find_duplicate(self, rec: dict) -> dict | None:
        for a in [rec.get("id")] + list(rec.get("aliases", [])):
            if a and a in self._alias_index:
                return self.records[self._alias_index[a]]
        nt = norm_title(rec.get("title", ""))
        if not nt:
            return None
        year = rec.get("year")
        auths = surnames(rec.get("authors"))
        for other in self.records.values():
            if fuzz.ratio(nt, norm_title(other.get("title", ""))) < FUZZ_THRESHOLD:
                continue
            oy = other.get("year")
            if year is not None and oy is not None and abs(int(year) - int(oy)) > 1:
                continue
            if auths and surnames(other.get("authors")) and not (auths & surnames(other.get("authors"))):
                continue
            return other
        return None

    # -- mutation ----------------------------------------------------------
    def upsert(self, rec: dict) -> tuple[dict, bool]:
        """Insert or merge. Returns (stored_record, created?)."""
        rec.setdefault("criteria_version", self.cfg.criteria_version)
        if not rec.get("id"):
            rec["id"] = canonical_id(rec.get("aliases", []), rec.get("title", ""), rec.get("year"))
        existing = self.find_duplicate(rec)
        if existing is None:
            rec["updated_at"] = iso_now()
            rec["aliases"] = sorted({a for a in rec.get("aliases", []) if a and a != rec["id"]})
            self.records[rec["id"]] = rec
            self._reindex()
            return rec, True
        merged = merge_records(existing, rec)
        self.records[merged["id"]] = merged
        if merged["id"] != existing["id"]:
            self.records.pop(existing["id"], None)
        self._reindex()
        return merged, False

    # -- frontier (layer 3: expansion memory) ------------------------------
    def frontier_add(self, rid: str, title: str = "") -> None:
        if rid not in self.frontier:
            self.frontier[rid] = {
                "id": rid,
                "title": title,
                "expanded": False,
                "directions": [],
                "expanded_at": "",
            }

    def frontier_pending(self, direction: str) -> list[dict]:
        return [
            n for n in self.frontier.values()
            if direction not in n.get("directions", [])
        ]

    def frontier_mark(self, rid: str, direction: str) -> None:
        node = self.frontier.setdefault(
            rid, {"id": rid, "title": "", "expanded": False, "directions": [], "expanded_at": ""}
        )
        if direction not in node["directions"]:
            node["directions"].append(direction)
        node["expanded"] = True
        node["expanded_at"] = iso_now()

    # -- rejections (layer 4: decision memory) -----------------------------
    def reject(self, rec: dict, reason: str, score: dict | None = None) -> None:
        rid = rec.get("id") or canonical_id(rec.get("aliases", []), rec.get("title", ""), rec.get("year"))
        prior = self.rejected.get(rid, {})
        self.rejected[rid] = {
            "id": rid,
            "aliases": sorted(set(rec.get("aliases", [])) | set(prior.get("aliases", []))),
            "title": rec.get("title", "") or prior.get("title", ""),
            "authors": rec.get("authors", []) or prior.get("authors", []),
            "year": rec.get("year", prior.get("year")),
            "venue": rec.get("venue", "") or prior.get("venue", ""),
            "abstract": rec.get("abstract", "") or prior.get("abstract", ""),
            "urls": rec.get("urls", {}) or prior.get("urls", {}),
            "area": rec.get("area", []) or prior.get("area", []),
            "discovered_from": rec.get("discovered_from", []) or prior.get("discovered_from", []),
            "rejection_reason": reason,
            "score": score or rec.get("score", {}),
            "criteria_version": self.cfg.criteria_version,
            "rejected_at": iso_now(),
        }

    def is_decided(self, rec: dict) -> str | None:
        """'registry' / 'rejected' / None. Rejections only bind at the current criteria_version."""
        if self.find_duplicate(rec) is not None:
            return "registry"
        ids = [rec.get("id")] + list(rec.get("aliases", []))
        for rid in ids:
            if rid and rid in self.rejected:
                if int(self.rejected[rid].get("criteria_version", 0)) >= self.cfg.criteria_version:
                    return "rejected"
                return None
        nt = norm_title(rec.get("title", ""))
        if nt:
            for other in self.rejected.values():
                if fuzz.ratio(nt, norm_title(other.get("title", ""))) >= FUZZ_THRESHOLD:
                    if int(other.get("criteria_version", 0)) >= self.cfg.criteria_version:
                        return "rejected"
                    return None
        return None

    # -- views -------------------------------------------------------------
    def with_status(self, status: str) -> list[dict]:
        return [r for r in self.records.values() if r.get("status") == status]

    def verified(self) -> list[dict]:
        return [r for r in self.records.values() if r.get("verification", {}).get("status") == "verified"]

    def counts(self) -> dict:
        out: dict[str, int] = {}
        for r in self.records.values():
            out[r.get("status", "?")] = out.get(r.get("status", "?"), 0) + 1
        return out

    def area_counts(self) -> dict:
        out: dict[str, int] = {}
        for r in self.records.values():
            for a in r.get("area", []) or ["unassigned"]:
                out[a] = out.get(a, 0) + 1
        return out


def _is_preprint(rec: dict) -> bool:
    if rec.get("doc_type") in PREPRINT_TYPES:
        return True
    venue = (rec.get("venue") or "").lower()
    return venue.startswith("arxiv") or venue in {"corr", "preprint"}


def merge_records(a: dict, b: dict) -> dict:
    """Merge b into a. The published version's metadata wins; both URLs are kept."""
    primary, secondary = (a, b)
    if _is_preprint(a) and not _is_preprint(b):
        primary, secondary = (b, a)

    out = dict(primary)
    aliases = set(a.get("aliases", [])) | set(b.get("aliases", []))
    aliases |= {a.get("id"), b.get("id")}
    aliases.discard("")
    aliases.discard(None)

    out["id"] = canonical_id(aliases, out.get("title", ""), out.get("year"))
    out["aliases"] = sorted(x for x in aliases if x and x != out["id"])

    for field in ("title", "venue", "doc_type", "abstract", "year"):
        if not out.get(field) and secondary.get(field):
            out[field] = secondary[field]
    if len(secondary.get("abstract") or "") > len(out.get("abstract") or ""):
        out["abstract"] = secondary["abstract"]
    if len(secondary.get("authors") or []) > len(out.get("authors") or []):
        out["authors"] = secondary["authors"]

    urls = dict(secondary.get("urls", {}))
    urls.update({k: v for k, v in primary.get("urls", {}).items() if v})
    for k, v in secondary.get("urls", {}).items():
        urls.setdefault(k, v)
    out["urls"] = urls

    out["area"] = sorted(set(a.get("area", [])) | set(b.get("area", [])))
    out["downstream_tags"] = sorted(set(a.get("downstream_tags", [])) | set(b.get("downstream_tags", [])))

    seen, prov = set(), []
    for item in list(a.get("discovered_from", [])) + list(b.get("discovered_from", [])):
        key = (item.get("id"), item.get("via"))
        if key not in seen:
            seen.add(key)
            prov.append(item)
    out["discovered_from"] = prov

    va, vb = a.get("verification", {}), b.get("verification", {})
    sources = sorted(set(va.get("sources", [])) | set(vb.get("sources", [])))
    status = "verified" if "verified" in (va.get("status"), vb.get("status")) else (
        va.get("status") or vb.get("status") or "unverified")
    notes = " ".join(n for n in {va.get("notes", ""), vb.get("notes", "")} if n).strip()
    out["verification"] = {
        "status": status,
        "sources": sources,
        "checked_at": max(va.get("checked_at", ""), vb.get("checked_at", "")),
        "notes": notes,
    }

    files = dict(a.get("files", {}))
    files.update({k: v for k, v in b.get("files", {}).items() if v})
    out["files"] = files

    # Never move a record backward through the phase pipeline.
    from .cache import PHASE_ORDER
    sa, sb = a.get("status", "candidate"), b.get("status", "candidate")
    out["status"] = max((sa, sb), key=lambda s: PHASE_ORDER.index(s) if s in PHASE_ORDER else -1)

    out["tier"] = a.get("tier") or b.get("tier")
    ann_a, ann_b = a.get("annotation", {}), b.get("annotation", {})
    out["annotation"] = ann_a if ann_a.get("text") else ann_b
    out["score"] = a.get("score") or b.get("score") or {}
    out["updated_at"] = iso_now()
    return out
