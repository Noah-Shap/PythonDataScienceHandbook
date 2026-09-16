"""Semantic Scholar Graph API: metadata, references and citations.

Uses ``S2_API_KEY`` when the environment provides one (higher rate limit); otherwise
falls back to the unauthenticated endpoint with a deliberately polite delay.
"""
from __future__ import annotations

import os

from .base import candidate

BASE = "https://api.semanticscholar.org/graph/v1"
FIELDS = ("title,abstract,year,venue,publicationTypes,externalIds,citationCount,"
          "referenceCount,authors.name,openAccessPdf,url")
TYPE_MAP = {"JournalArticle": "journal", "Conference": "conference", "Book": "book",
            "BookSection": "chapter", "Dataset": "dataset", "Review": "journal",
            "Thesis": "thesis", "Editorial": "journal"}


class SemanticScholar:
    name = "semanticscholar"
    probe_url = f"{BASE}/paper/search?query=argument+mining&limit=1"

    def __init__(self, cfg, http):
        self.cfg, self.http = cfg, http
        self.key = os.environ.get("S2_API_KEY", "")

    @property
    def headers(self) -> dict:
        return {"x-api-key": self.key} if self.key else {}

    def _paper(self, p: dict) -> dict:
        ext = p.get("externalIds") or {}
        types = p.get("publicationTypes") or []
        doc_type = next((TYPE_MAP[t] for t in types if t in TYPE_MAP), "")
        if ext.get("ArXiv") and not doc_type:
            doc_type = "preprint"
        aliases = [f"s2:{p['paperId']}"] if p.get("paperId") else []
        if ext.get("CorpusId"):
            aliases.append(f"s2corpus:{ext['CorpusId']}")
        if ext.get("ACL"):
            aliases.append(f"acl:{ext['ACL']}")
        return candidate(
            self.name,
            title=p.get("title") or "",
            authors=[a.get("name", "") for a in (p.get("authors") or [])],
            year=p.get("year"),
            venue=p.get("venue") or "",
            doc_type=doc_type,
            abstract=p.get("abstract") or "",
            doi=ext.get("DOI", ""),
            arxiv=ext.get("ArXiv", ""),
            aliases=aliases,
            urls={"landing": p.get("url", ""),
                  "pdf_oa": (p.get("openAccessPdf") or {}).get("url", "")},
            extra={"cited_by_count": p.get("citationCount", 0),
                   "reference_count": p.get("referenceCount", 0)},
        )

    def paper(self, ident: str) -> dict | None:
        data = self.http.json(self.name, f"{BASE}/paper/{ident}", {"fields": FIELDS}, self.headers)
        return self._paper(data) if data and data.get("paperId") else None

    def by_doi(self, doi: str) -> dict | None:
        return self.paper(f"DOI:{doi}")

    def by_arxiv(self, arxiv_id: str) -> dict | None:
        return self.paper(f"arXiv:{arxiv_id}")

    def search(self, query: str, limit: int = 50, year: str | None = None) -> list[dict]:
        params = {"query": query, "limit": min(limit, 100), "fields": FIELDS}
        if year:
            params["year"] = year
        data = self.http.json(self.name, f"{BASE}/paper/search", params, self.headers)
        return [self._paper(p) for p in (data or {}).get("data", [])]

    def references(self, ident: str, limit: int = 200) -> list[dict]:
        out, offset = [], 0
        while len(out) < limit:
            data = self.http.json(self.name, f"{BASE}/paper/{ident}/references",
                                  {"fields": FIELDS, "limit": 100, "offset": offset}, self.headers)
            rows = (data or {}).get("data", [])
            if not rows:
                break
            out.extend(self._paper(r["citedPaper"]) for r in rows if r.get("citedPaper", {}).get("paperId"))
            offset += 100
            if (data or {}).get("next") is None:
                break
        return out[:limit]

    def citations(self, ident: str, limit: int = 200) -> list[dict]:
        out, offset = [], 0
        while len(out) < limit:
            data = self.http.json(self.name, f"{BASE}/paper/{ident}/citations",
                                  {"fields": FIELDS, "limit": 100, "offset": offset}, self.headers)
            rows = (data or {}).get("data", [])
            if not rows:
                break
            out.extend(self._paper(r["citingPaper"]) for r in rows if r.get("citingPaper", {}).get("paperId"))
            offset += 100
            if (data or {}).get("next") is None:
                break
        return out[:limit]
