"""OpenAlex works API (polite pool via ``mailto``).

Used for metadata cross-checks, the citation graph (``referenced_works`` / ``cited_by``)
and OA PDF resolution via ``best_oa_location``.
"""
from __future__ import annotations

from ..util import normalise_doi
from .base import candidate

BASE = "https://api.openalex.org"
TYPE_MAP = {
    "article": "journal", "journal-article": "journal", "proceedings-article": "conference",
    "book": "book", "book-chapter": "chapter", "dissertation": "thesis",
    "preprint": "preprint", "posted-content": "preprint", "dataset": "dataset",
    "report": "guideline", "monograph": "book",
}


class OpenAlex:
    name = "openalex"
    probe_url = f"{BASE}/works?per-page=1"

    def __init__(self, cfg, http):
        self.cfg, self.http = cfg, http
        self.mailto = cfg.contact

    def _params(self, **kw) -> dict:
        kw["mailto"] = self.mailto
        return {k: v for k, v in kw.items() if v is not None}

    def _work(self, w: dict) -> dict:
        oa_id = (w.get("id") or "").rsplit("/", 1)[-1]
        loc = w.get("best_oa_location") or {}
        primary = w.get("primary_location") or {}
        venue = ((primary.get("source") or {}).get("display_name")
                 or (w.get("host_venue") or {}).get("display_name") or "")
        return candidate(
            self.name,
            title=w.get("display_name") or w.get("title") or "",
            authors=[(a.get("author") or {}).get("display_name", "")
                     for a in (w.get("authorships") or [])],
            year=w.get("publication_year"),
            venue=venue,
            doc_type=TYPE_MAP.get((w.get("type") or "").lower(), ""),
            abstract=_abstract(w.get("abstract_inverted_index")),
            doi=w.get("doi") or "",
            aliases=[f"openalex:{oa_id}"] if oa_id else [],
            urls={"landing": (primary.get("landing_page_url") or w.get("doi") or ""),
                  "pdf_oa": loc.get("pdf_url") or ""},
            extra={
                "cited_by_count": w.get("cited_by_count", 0),
                "referenced_works": [r.rsplit("/", 1)[-1] for r in (w.get("referenced_works") or [])],
                "cited_by_api_url": w.get("cited_by_api_url", ""),
                "is_oa": bool(loc.get("is_oa")),
            },
        )

    # -- lookups -----------------------------------------------------------
    def by_doi(self, doi: str) -> dict | None:
        d = normalise_doi(doi)
        if not d:
            return None
        data = self.http.json(self.name, f"{BASE}/works/https://doi.org/{d}", self._params())
        return self._work(data) if data and data.get("id") else None

    def by_id(self, oa_id: str) -> dict | None:
        data = self.http.json(self.name, f"{BASE}/works/{oa_id}", self._params())
        return self._work(data) if data and data.get("id") else None

    def search_title(self, title: str, year=None) -> list[dict]:
        params = self._params(filter=f"title.search:{title}", per_page=10)
        data = self.http.json(self.name, f"{BASE}/works", params)
        hits = [self._work(w) for w in (data or {}).get("results", [])]
        if year:
            hits.sort(key=lambda h: abs((h["year"] or 0) - int(year)))
        return hits

    def search(self, query: str, limit: int = 50, from_year: int | None = None) -> list[dict]:
        params = self._params(search=query, per_page=min(limit, 200),
                              filter=f"from_publication_date:{from_year}-01-01" if from_year else None)
        data = self.http.json(self.name, f"{BASE}/works", params)
        return [self._work(w) for w in (data or {}).get("results", [])][:limit]

    # -- citation graph ----------------------------------------------------
    def references(self, oa_id: str, limit: int = 200) -> list[dict]:
        work = self.http.json(self.name, f"{BASE}/works/{oa_id}", self._params())
        ids = [r.rsplit("/", 1)[-1] for r in (work or {}).get("referenced_works", [])][:limit]
        out = []
        for chunk in _chunks(ids, 50):
            data = self.http.json(self.name, f"{BASE}/works",
                                  self._params(filter="openalex_id:" + "|".join(chunk), per_page=50))
            out.extend(self._work(w) for w in (data or {}).get("results", []))
        return out

    def citations(self, oa_id: str, limit: int = 200) -> list[dict]:
        out, cursor = [], "*"
        while len(out) < limit and cursor:
            data = self.http.json(self.name, f"{BASE}/works",
                                  self._params(filter=f"cites:{oa_id}", per_page=50, cursor=cursor))
            if not data:
                break
            out.extend(self._work(w) for w in data.get("results", []))
            cursor = (data.get("meta") or {}).get("next_cursor")
        return out[:limit]


def _abstract(inverted) -> str:
    if not inverted:
        return ""
    positions = [(pos, word) for word, poss in inverted.items() for pos in poss]
    return " ".join(w for _, w in sorted(positions))


def _chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]
