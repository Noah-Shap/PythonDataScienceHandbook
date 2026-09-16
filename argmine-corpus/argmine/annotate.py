"""Grounded annotations.

Every annotation is written from text this pipeline actually retrieved - the full text
when a PDF was fetched and extracted, otherwise the abstract - and says which. Nothing
about a work's content is asserted from anywhere else: the contribution sentence is
quoted verbatim from the retrieved text, and the relevance clause is derived from the
record's own downstream tags (which are themselves derived from that text).

Where neither full text nor an abstract was retrieved, ``grounded_on`` is ``none`` and
the annotation says so instead of inventing a description.

An LLM-written annotation would be richer. The seam for it is :func:`set_writer`: supply
a callable taking (record, grounding_text, grounded_on) and returning a paragraph, and it
replaces the extractive writer without touching the pipeline.
"""
from __future__ import annotations

import json

from .util import iso_now, sentences, truncate

CUES = (
    ("we present", 5), ("we introduce", 5), ("we propose", 5), ("we release", 5),
    ("this paper presents", 5), ("this paper introduces", 5), ("in this paper", 3),
    ("we describe", 4), ("we define", 4), ("this survey", 5), ("we annotate", 4),
    ("we construct", 4), ("we build", 3), ("we develop", 3), ("we study", 3),
    ("we investigate", 3), ("we show", 3), ("we report", 2), ("our results", 2),
    ("we argue", 3), ("corpus", 2), ("dataset", 2), ("annotation", 2), ("task of", 2),
    ("framework", 2), ("we evaluate", 2), ("benchmark", 2), ("we compare", 2),
)

TAG_RELEVANCE = {
    "dialogue": ("supplies dialogue-level structure - who said what, in reply to what - which is "
                 "exactly the relation layer a debate-transcript database has to store"),
    "schemes": ("supplies argumentation-scheme and critical-question structure, which is how stored "
                "inferences can be typed rather than left as untyped support links"),
    "formal": ("supplies the formal semantics for deciding what stands once arguments and attacks "
               "are stored, so strength is computed rather than asserted"),
    "quality": ("gives quality dimensions or a scoring target, which is what an argument-strength "
                "field in the database would be measured against"),
    "extraction": ("defines the extraction step that turns raw transcript text into stored "
                   "components and relations"),
    "dataset": ("is a reusable resource whose annotation structure a transcript schema can copy "
                "rather than reinvent"),
    "fallacy": ("types defective inference, which is what a quality flag on a stored argument "
                "would have to recognise"),
}

_WRITER = None


def set_writer(fn) -> None:
    """Install an alternative annotation writer, e.g. an LLM-backed one."""
    global _WRITER
    _WRITER = fn


def grounding(cfg, rec: dict) -> tuple[str, str]:
    """Return (text, grounded_on) using the richest text actually retrieved."""
    text_rel = rec.get("files", {}).get("text")
    if text_rel:
        path = cfg.path(text_rel)
        if path.exists():
            body = _from_text_file(path)
            if len(body) > 400:
                return body, "fulltext"
    abstract = (rec.get("abstract") or "").strip()
    if abstract:
        return abstract, "abstract"
    return "", "none"


def _from_text_file(path) -> str:
    """Prefer abstract + introduction + conclusion: where a paper states its contribution."""
    sections = {}
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            if "sections" in row:
                sections = row["sections"]
                break
    parts = []
    for name in ("abstract", "introduction", "conclusion"):
        sec = sections.get(name)
        if isinstance(sec, dict):
            parts.append(sec.get("text", ""))
        elif isinstance(sec, str):
            parts.append(sec)
    return "\n".join(p for p in parts if p).strip()


def pick_sentences(text: str, n: int = 2) -> list[str]:
    scored = []
    for i, sent in enumerate(sentences(text)):
        words = len(sent.split())
        if words < 6 or words > 60:
            continue
        low = sent.lower()
        score = sum(w for cue, w in CUES if cue in low)
        score += max(0.0, 1.5 - i * 0.3)        # early sentences state the contribution
        scored.append((score, i, sent))
    scored.sort(key=lambda t: (-t[0], t[1]))
    picked = sorted(scored[:n], key=lambda t: t[1])
    return [s for _score, _i, s in picked]


def relevance_clause(rec: dict) -> str:
    tags = [t for t in rec.get("downstream_tags", []) if t in TAG_RELEVANCE]
    if not tags:
        return ("Its bearing on a debate-transcript argument database is indirect: no downstream "
                "tag was assigned from the retrieved text.")
    order = ["dialogue", "schemes", "quality", "fallacy", "formal", "extraction", "dataset"]
    tags.sort(key=lambda t: order.index(t) if t in order else 99)
    lead = TAG_RELEVANCE[tags[0]]
    rest = [TAG_RELEVANCE[t].split(",")[0] for t in tags[1:2]]
    clause = f"For a debate-transcript argument database it {lead}"
    if rest:
        clause += f"; and it {rest[0]}"
    return clause + "."


def write(cfg, rec: dict) -> dict:
    text, grounded_on = grounding(cfg, rec)
    if _WRITER is not None:
        return {"text": _WRITER(rec, text, grounded_on), "grounded_on": grounded_on,
                "written_at": iso_now(), "writer": "custom"}
    if grounded_on == "none":
        body = (f"No abstract or full text was retrieved for this entry, so nothing about its "
                f"content is asserted here. It is recorded from bibliographic metadata only "
                f"({rec.get('doc_type') or 'work'}, {rec.get('venue') or 'venue unrecorded'}, "
                f"{rec.get('year') or 'year unrecorded'}), verified against "
                f"{len(rec.get('verification', {}).get('sources', []))} sources. "
                + relevance_clause(rec))
        return {"text": body, "grounded_on": "none", "written_at": iso_now(),
                "writer": "extractive"}

    picked = pick_sentences(text)
    quoted = " ".join(f'"{truncate(s, 320)}"' for s in picked) or f'"{truncate(text, 320)}"'
    where = "its full text" if grounded_on == "fulltext" else "its abstract"
    body = (f"Contribution, in the work's own words from {where}: {quoted} "
            f"{relevance_clause(rec)}")
    return {"text": body, "grounded_on": grounded_on, "written_at": iso_now(),
            "writer": "extractive"}


def annotate_all(ctx, force: bool = False) -> dict:
    """Write an annotation for every record whose grounding changed (or is missing)."""
    cfg, reg = ctx.cfg, ctx.registry
    summary = {"written": 0, "unchanged": 0, "grounded": {"fulltext": 0, "abstract": 0, "none": 0}}
    for rec in reg.records.values():
        current = rec.get("annotation") or {}
        _text, grounded_on = grounding(cfg, rec)
        if current.get("text") and current.get("grounded_on") == grounded_on and not force:
            summary["unchanged"] += 1
        else:
            rec["annotation"] = write(cfg, rec)
            rec["updated_at"] = iso_now()
            summary["written"] += 1
        summary["grounded"][rec["annotation"]["grounded_on"]] = \
            summary["grounded"].get(rec["annotation"]["grounded_on"], 0) + 1
    return summary
