"""Small pure helpers shared by every phase. No I/O, no network."""
from __future__ import annotations

import datetime as _dt
import hashlib
import re
import unicodedata

_PUNCT = re.compile(r"[^\w\s]", re.UNICODE)
_WS = re.compile(r"\s+")


def iso_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat()


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def norm_title(title: str) -> str:
    """Normalised title used for dedup, fuzzy matching and cross-source agreement."""
    t = strip_accents(title or "").lower()
    t = t.replace("&", " and ")
    t = _PUNCT.sub(" ", t)
    return _WS.sub(" ", t).strip()


def norm_text(s: str) -> str:
    return _WS.sub(" ", strip_accents(s or "").lower())


def sha1(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()


def title_id(title: str, year) -> str:
    """Last-resort canonical id when no external identifier exists."""
    return "title:" + sha1(f"{norm_title(title)}|{year if year is not None else ''}")


ID_PRECEDENCE = ("doi", "arxiv", "s2", "openalex", "title")


def canonical_id(aliases, title: str = "", year=None) -> str:
    """Pick the canonical id from a set of identifiers, honouring the documented precedence."""
    by_scheme: dict[str, list[str]] = {}
    for a in aliases:
        if not a or ":" not in a:
            continue
        scheme = a.split(":", 1)[0].lower()
        by_scheme.setdefault(scheme, []).append(a)
    for scheme in ID_PRECEDENCE:
        options = by_scheme.get(scheme)
        if not options:
            continue
        if scheme == "doi":
            # Bibliographies sometimes carry a truncated DOI ("10.1162/coli"). A DOI that
            # is a strict prefix of another DOI for the same work is that truncation, and
            # must never become the canonical id - it still survives as an alias.
            options = [o for o in options
                       if not any(other != o and other.startswith(o) for other in options)]
        return sorted(options)[0] if options else title_id(title, year)
    return title_id(title, year)


def normalise_doi(doi: str) -> str | None:
    if not doi:
        return None
    d = doi.strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    d = re.sub(r"^doi:\s*", "", d)
    return d if d.startswith("10.") else None


def normalise_arxiv(aid: str) -> str | None:
    if not aid:
        return None
    a = aid.strip().lower()
    a = re.sub(r"^https?://arxiv\.org/(abs|pdf)/", "", a)
    a = re.sub(r"^arxiv:", "", a)
    a = re.sub(r"\.pdf$", "", a)
    a = re.sub(r"v\d+$", "", a)
    return a or None


_SAFE = re.compile(r"[^A-Za-z0-9._-]+")


def safe_id(rid: str) -> str:
    """Filesystem-safe rendering of a canonical id (stable, collision-free within a run)."""
    s = _SAFE.sub("_", rid)
    return s[:150] if len(s) > 150 else s


def surname(author: str) -> str:
    """Best-effort surname from 'First Last' or 'Last, First'."""
    a = (author or "").strip()
    if not a:
        return ""
    if "," in a:
        return norm_text(a.split(",", 1)[0]).strip()
    parts = [p for p in norm_text(a).split() if p]
    return parts[-1] if parts else ""


def surnames(authors) -> set[str]:
    return {s for s in (surname(a) for a in (authors or [])) if s}


def approx_tokens(text: str, tokens_per_word: float = 1.3) -> int:
    """Cheap token estimate; the pipeline never depends on an exact tokenizer."""
    return int(len((text or "").split()) * tokens_per_word)


def sentences(text: str) -> list[str]:
    """Conservative sentence split: never splits on common abbreviations or initials."""
    if not text:
        return []
    protected = re.sub(
        r"\b(e\.g|i\.e|cf|et al|vs|Fig|Eq|Sec|Tab|Dr|Prof|approx|resp|St|No)\.",
        lambda m: m.group(0).replace(".", "\x00"),
        text,
    )
    protected = re.sub(r"\b([A-Z])\.", lambda m: m.group(1) + "\x00", protected)
    parts = re.split(r"(?<=[.!?])\s+(?=[\"'(\[]?[A-Z0-9])", protected)
    return [p.replace("\x00", ".").strip() for p in parts if p.strip()]


def truncate(s: str, n: int) -> str:
    s = (s or "").strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"
