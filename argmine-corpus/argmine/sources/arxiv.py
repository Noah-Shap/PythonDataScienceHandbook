"""arXiv Atom API. Metadata for preprints and a PDF link for OA resolution.

The arXiv API terms ask for at least three seconds between calls; that delay is
configured in ``config.yaml`` under ``http.min_delay_seconds.arxiv``.
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET

from ..util import normalise_arxiv
from .base import candidate

BASE = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


class ArXiv:
    name = "arxiv"
    probe_url = f"{BASE}?search_query=all:argument+mining&max_results=1"

    def __init__(self, cfg, http):
        self.cfg, self.http = cfg, http

    def _entries(self, xml_text: str) -> list[dict]:
        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError:
            return []
        out = []
        for e in root.findall("a:entry", NS):
            aid = normalise_arxiv((e.findtext("a:id", "", NS) or ""))
            title = re.sub(r"\s+", " ", e.findtext("a:title", "", NS) or "").strip()
            if not title:
                continue
            published = e.findtext("a:published", "", NS) or ""
            doi = e.findtext("arxiv:doi", "", NS) or ""
            journal_ref = e.findtext("arxiv:journal_ref", "", NS) or ""
            pdf = next((l.get("href") for l in e.findall("a:link", NS)
                        if l.get("title") == "pdf"), f"https://arxiv.org/pdf/{aid}")
            out.append(candidate(
                self.name,
                title=title,
                authors=[a.findtext("a:name", "", NS) for a in e.findall("a:author", NS)],
                year=published[:4],
                venue=journal_ref or "arXiv",
                doc_type="preprint" if not journal_ref else "",
                abstract=re.sub(r"\s+", " ", e.findtext("a:summary", "", NS) or "").strip(),
                doi=doi,
                arxiv=aid or "",
                urls={"landing": f"https://arxiv.org/abs/{aid}", "pdf_oa": pdf},
                extra={"categories": [c.get("term") for c in e.findall("a:category", NS)]},
            ))
        return out

    def by_id(self, arxiv_id: str) -> dict | None:
        aid = normalise_arxiv(arxiv_id)
        if not aid:
            return None
        resp = self.http.get(self.name, BASE, {"id_list": aid, "max_results": 1})
        entries = self._entries(resp.text) if resp is not None and resp.status_code == 200 else []
        return entries[0] if entries else None

    def search(self, query: str, limit: int = 50, title_only: bool = False) -> list[dict]:
        field = "ti" if title_only else "all"
        resp = self.http.get(self.name, BASE, {
            "search_query": f'{field}:"{query}"', "max_results": min(limit, 100),
            "sortBy": "relevance"})
        return self._entries(resp.text) if resp is not None and resp.status_code == 200 else []
