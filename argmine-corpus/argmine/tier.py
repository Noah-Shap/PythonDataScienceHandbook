"""Phase 4 - tier.

T1 foundational / survey, T2 core method, T3 dataset / tool / annotation guideline,
T4 recent (2023-2026). Tiers are stable once assigned: a record is only re-tiered when
``--retier`` is passed, so the reading order does not churn between runs.
"""
from __future__ import annotations

from .cache import advance
from .util import iso_now, norm_text

FOUNDATIONAL_TITLE = ("survey", "a review", "systematic review", "overview", "tutorial",
                      "introduction to", "state of the art", "foundations of", "handbook",
                      "five years of", "an introduction")
RESOURCE_MARKERS = ("corpus", "dataset", "data set", "annotation guideline", "annotation scheme",
                    "annotated corpus", "we release", "shared task", "benchmark", "treebank",
                    "annotation manual", "codebook", "toolkit", "we present a tool",
                    "demonstration", "resource")
SCHEME_MARKERS = ("argumentation scheme", "critical question", "walton", "scheme classification")
FALLACY_MARKERS = ("fallac", "ad hominem", "straw man", "slippery slope")
DIALOGUE_MARKERS = ("dialogue", "dialogical", "debate", "conversation", "reply", "interaction")
EXTRACTION_MARKERS = ("argument mining", "argumentation mining", "component classification",
                      "relation classification", "parsing", "segmentation", "extraction",
                      "identification", "detection")

AREA_TAGS = {"formal": "formal", "mining": "extraction", "quality": "quality",
             "dialogue": "dialogue", "resources": "dataset"}


def _text(rec: dict) -> str:
    return norm_text(f"{rec.get('title', '')} {rec.get('abstract', '')} {rec.get('venue', '')}")


def choose_tier(cfg, rec: dict) -> int:
    title = norm_text(rec.get("title", ""))
    text = _text(rec)
    year = int(rec.get("year") or 0)
    doc_type = rec.get("doc_type", "")

    # T1: theory anchors, surveys, the canonical paper an area is built on.
    if any(m in title for m in FOUNDATIONAL_TITLE):
        return 1
    if doc_type == "book" or (doc_type == "chapter" and "handbook" in text):
        return 1
    if any(p.get("via") == "seed" for p in rec.get("discovered_from", [])) and (
            "formal" in rec.get("area", []) or year <= 2011):
        return 1

    # T3: the resource itself, including the guideline document.
    if doc_type in ("dataset", "tool", "guideline"):
        return 3
    if "resources" in rec.get("area", []) and any(m in text for m in RESOURCE_MARKERS):
        return 3

    # T4: LLM-era work, judged by date as the rubric specifies.
    if year >= 2023:
        return 4
    return 2


def choose_tags(cfg, rec: dict, tier: int) -> list[str]:
    text = _text(rec)
    tags = {AREA_TAGS[a] for a in rec.get("area", []) if a in AREA_TAGS}
    if any(m in text for m in SCHEME_MARKERS):
        tags.add("schemes")
    if any(m in text for m in FALLACY_MARKERS):
        tags.add("fallacy")
    if any(m in text for m in DIALOGUE_MARKERS):
        tags.add("dialogue")
    if any(m in text for m in EXTRACTION_MARKERS):
        tags.add("extraction")
    if tier == 3:
        tags.add("dataset")
    if "llm" in rec.get("area", []) and not tags:
        tags.add("extraction")
    if not tags:
        tags.add("extraction")
    allowed = set(cfg["downstream_tags"])
    return sorted(t for t in tags if t in allowed)


def run(ctx) -> dict:
    cfg, reg = ctx.cfg, ctx.registry
    retier = bool(getattr(ctx.args, "retier", False))
    todo = [r for r in reg.records.values()
            if r.get("verification", {}).get("status") == "verified"
            and (r.get("status") == "verified" or (retier and r.get("tier")))]
    summary = {"considered": len(todo), "tiered": 0, "retiered": 0, "tiers": {}, "tags": {}}
    for rec in todo:
        old = rec.get("tier")
        tier = choose_tier(cfg, rec)
        if old and not retier:
            tier = old
        rec["tier"] = tier
        rec["downstream_tags"] = choose_tags(cfg, rec, tier)
        rec["updated_at"] = iso_now()
        advance(rec, "tiered")
        summary["tiers"][tier] = summary["tiers"].get(tier, 0) + 1
        for t in rec["downstream_tags"]:
            summary["tags"][t] = summary["tags"].get(t, 0) + 1
        if old and old != tier:
            summary["retiered"] += 1
        summary["tiered"] += 1
    summary["untagged"] = sum(1 for r in reg.records.values()
                              if r.get("tier") and not r.get("downstream_tags"))
    return summary


def paragraph(summary: dict) -> str:
    tiers = ", ".join(f"T{k}: {v}" for k, v in sorted(summary.get("tiers", {}).items()))
    tags = ", ".join(f"{k}: {v}" for k, v in sorted(summary.get("tags", {}).items(),
                                                    key=lambda kv: -kv[1]))
    return (f"Phase tier: assigned a tier and downstream tags to {summary.get('tiered', 0)} "
            f"verified records ({tiers or 'none'}); {summary.get('retiered', 0)} changed tier "
            f"(only possible with --retier). Tag counts: {tags or 'none'}. "
            f"{summary.get('untagged', 0)} tiered records carry no tag.")
