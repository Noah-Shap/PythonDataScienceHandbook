"""Normalised shape returned by every source module."""
from __future__ import annotations

from ..util import normalise_arxiv, normalise_doi


def candidate(source: str, *, title: str, authors=None, year=None, venue: str = "",
              doc_type: str = "", abstract: str = "", doi: str = "", arxiv: str = "",
              aliases=None, urls=None, extra=None) -> dict:
    """A single source's view of one work. Never merged here - verify.py compares views."""
    al = set(aliases or [])
    doi_n = normalise_doi(doi)
    if doi_n:
        al.add(f"doi:{doi_n}")
    ax = normalise_arxiv(arxiv)
    if ax:
        al.add(f"arxiv:{ax}")
    return {
        "source": source,
        "title": (title or "").strip(),
        "authors": list(authors or []),
        "year": int(year) if str(year or "").isdigit() else None,
        "venue": (venue or "").strip(),
        "doc_type": doc_type,
        "abstract": (abstract or "").strip(),
        "aliases": sorted(a for a in al if a),
        "urls": {k: v for k, v in (urls or {}).items() if v},
        "extra": extra or {},
    }
