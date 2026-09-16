"""Crossref: DOI resolution and an independent cross-check of title/author/year/venue."""
from __future__ import annotations

from ..util import normalise_doi
from .base import candidate

BASE = "https://api.crossref.org"
TYPE_MAP = {"journal-article": "journal", "proceedings-article": "conference",
            "book": "book", "monograph": "book", "book-chapter": "chapter",
            "dissertation": "thesis", "posted-content": "preprint",
            "dataset": "dataset", "report": "guideline", "reference-book": "book"}


class Crossref:
    name = "crossref"
    probe_url = f"{BASE}/works?rows=1"

    def __init__(self, cfg, http):
        self.cfg, self.http = cfg, http

    def _params(self, **kw) -> dict:
        kw["mailto"] = self.cfg.contact
        return {k: v for k, v in kw.items() if v is not None}

    def _item(self, it: dict) -> dict:
        titles = it.get("title") or []
        container = it.get("container-title") or []
        issued = ((it.get("issued") or {}).get("date-parts") or [[None]])[0]
        year = issued[0] if issued else None
        authors = [" ".join(x for x in [a.get("given", ""), a.get("family", "")] if x).strip()
                   for a in (it.get("author") or [])]
        return candidate(
            self.name,
            title=titles[0] if titles else "",
            authors=authors,
            year=year,
            venue=(container[0] if container else it.get("publisher", "")),
            doc_type=TYPE_MAP.get(it.get("type", ""), ""),
            abstract=_strip_jats(it.get("abstract", "")),
            doi=it.get("DOI", ""),
            urls={"landing": it.get("URL", "")},
            extra={"cited_by_count": it.get("is-referenced-by-count", 0),
                   "publisher": it.get("publisher", ""),
                   "subtitle": (it.get("subtitle") or [""])[0]},
        )

    def by_doi(self, doi: str) -> dict | None:
        d = normalise_doi(doi)
        if not d:
            return None
        data = self.http.json(self.name, f"{BASE}/works/{d}", self._params())
        msg = (data or {}).get("message")
        return self._item(msg) if msg else None

    def search_bibliographic(self, title: str, author: str = "", year=None, rows: int = 5) -> list[dict]:
        params = self._params(**{"query.bibliographic": title, "rows": rows})
        if author:
            params["query.author"] = author
        data = self.http.json(self.name, f"{BASE}/works", params)
        hits = [self._item(i) for i in ((data or {}).get("message") or {}).get("items", [])]
        if year:
            hits.sort(key=lambda h: abs((h["year"] or 0) - int(year)))
        return hits


def _strip_jats(text: str) -> str:
    import re
    return re.sub(r"<[^>]+>", " ", text or "").strip()
