"""Candidate scoring, area assignment and the exclusion rules of section 6.

score = 0.25 cites_norm + 0.35 cocite + 0.25 keyword + 0.15 venue   (weights in config)

``cocite`` carries the most weight on purpose: it measures centrality to *this* corpus
rather than general popularity. It is computed from whichever evidence the run has -
the citation graph when Semantic Scholar / OpenAlex are reachable, otherwise
co-occurrence with already-verified entries inside curated BibTeX bibliographies.
Which evidence was used is recorded per record in ``score.components_source``.
"""
from __future__ import annotations

import datetime as _dt
import math

from .util import norm_text, norm_title

# A vocabulary term is "core" when it is about argumentation itself rather than about
# research infrastructure. "dataset", "corpus", "benchmark" and "toolkit" are in the area
# vocabularies because they separate a resource paper from a method paper - but on their
# own they say nothing about whether a candidate belongs in this corpus at all.
CORE_MARKERS = ("argument", "argumentation", "debate", "fallac", "persuasi", "rhetor",
                "dialectic", "dialogical", "dialogue game", "toulmin", "walton", "aspic",
                "enthymeme", "premise", "convincing", "deliberation", "changemyview",
                "change my view", "kialo", "moral maze", "qt30", "us2016", "critical question",
                "claim detection", "scheme", "defeasible", "nonmonotonic", "aif", "iat",
                "burden of proof", "locution", "illocutionary", "cogency", "counter-argument")

VOLUME_TITLE_RE = __import__("re").compile(
    r"^\s*(proceedings\b|the\s+\d+(st|nd|rd|th)\s+workshop\b|"
    r"(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth)"
    r"\s+workshop\b|workshop\s+on\b.*\(\d{4}\)$|front\s?matter\b)", __import__("re").I)

FOUNDATIONAL_MARKERS = ("survey", "introduction to", "overview", "tutorial", "state of the art",
                        "a review", "systematic review", "foundations")


# -- exclusions -----------------------------------------------------------
def is_core_term(term: str) -> bool:
    t = norm_text(term)
    return any(m in t for m in CORE_MARKERS)


def core_hits(cfg, rec: dict) -> float:
    """Weighted matches against core argumentation vocabulary only."""
    title = norm_text(rec.get("title", ""))
    abstract = norm_text(rec.get("abstract", ""))
    venue = norm_text(rec.get("venue", ""))
    total = 0.0
    for spec in cfg["areas"].values():
        for term, weight in spec["vocabulary"].items():
            if not is_core_term(term):
                continue
            t = norm_text(term)
            if t in title:
                total += 2.0 * float(weight)
            elif t in abstract:
                total += float(weight)
            elif t in venue:
                total += 0.5 * float(weight)
    return total


def off_topic(cfg, rec: dict) -> bool:
    """True when nothing in the candidate is about argumentation itself.

    Bibliographies are curated for *their* paper, not for this corpus, so a general NLP,
    LLM or web-conference bibliography drags in work with no argumentative content. A
    candidate whose only vocabulary matches are infrastructure words ("dataset",
    "benchmark") or the LLM area's generic terms is out; section 6.5 says as much
    explicitly for the LLM area.
    """
    return core_hits(cfg, rec) <= 0


def domain_match(cfg, rec: dict) -> str | None:
    """The excluded-domain pattern this candidate matches, if any."""
    text = norm_text(f"{rec.get('title', '')} {rec.get('abstract', '')}")
    title = norm_text(rec.get("title", ""))
    for pat in cfg["exclusions"]["domain_patterns"]:
        p = norm_text(pat)
        if p in title or text.count(p) >= 2:
            return pat
    return None


def exclusion_reason(cfg, rec: dict) -> str | None:
    """Global exclusions (section 6). Foundational work survives them (section 6 allows it
    at T1); such a rescue is recorded as scope-uncertain rather than waved through."""
    if VOLUME_TITLE_RE.match(rec.get("title", "")):
        # A bibliography sometimes cites a whole proceedings volume. The volume is not a
        # work in this field's literature; its papers are, and they are reachable anyway.
        return "proceedings_volume:not an individual work"
    if off_topic(cfg, rec):
        return "off_topic:no argumentation vocabulary in title, abstract or venue"
    pat = domain_match(cfg, rec)
    if pat:
        if any(m in norm_text(rec.get("title", "")) for m in FOUNDATIONAL_MARKERS):
            return None
        return f"excluded_domain:{pat}"
    return None


def scope_uncertainty(cfg, rec: dict, keyword: float) -> str:
    """Why this candidate's membership of the corpus is a judgement call, or "".

    Section 9: where scope is uncertain, admit at the lowest plausible tier and flag it in
    the report rather than silently dropping it.
    """
    reasons = []
    if domain_match(cfg, rec):
        reasons.append(f"matches the excluded domain '{domain_match(cfg, rec)}' but reads as "
                       f"foundational")
    if keyword < float(cfg["scoring"].get("scope_uncertain_keyword", 0.3)):
        reasons.append(f"weak vocabulary match (keyword {keyword:.2f})")
    if not (rec.get("abstract") or "").strip():
        reasons.append("no abstract retrieved, so scope was judged from the title and venue")
    return "; ".join(reasons)


# -- components -----------------------------------------------------------
def keyword_scores(cfg, rec: dict) -> dict[str, float]:
    """Raw per-area vocabulary score: sum of matched term weights (title counts double)."""
    title = norm_text(rec.get("title", ""))
    abstract = norm_text(rec.get("abstract", ""))
    venue = norm_text(rec.get("venue", ""))
    out = {}
    for area, spec in cfg["areas"].items():
        raw = 0.0
        for term, weight in spec["vocabulary"].items():
            t = norm_text(term)
            if t in title:
                raw += 2.0 * float(weight)
            elif t in abstract:
                raw += float(weight)
            elif t in venue:
                raw += 0.5 * float(weight)
        out[area] = raw
    return out


def assign_areas(cfg, rec: dict) -> tuple[list[str], float, dict[str, float]]:
    raws = keyword_scores(cfg, rec)
    best = max(raws.values()) if raws else 0.0
    share = float(cfg["scoring"].get("area_share", 0.6))
    saturation = float(cfg["scoring"].get("keyword_saturation", 12.0))
    min_norm = float(cfg["scoring"].get("area_min_norm", 0.4))
    areas = sorted(a for a, v in raws.items()
                   if v > 0 and (v >= share * best or v / saturation >= min_norm))
    keyword = min(best / saturation, 1.0)
    # 6.5 is defined by date as well as by vocabulary.
    year = rec.get("year")
    if year and int(year) >= 2023 and "llm" not in areas and raws.get("llm", 0) > 0:
        areas.append("llm")
    return areas, keyword, raws


def venue_score(cfg, rec: dict) -> float:
    venue = norm_text(rec.get("venue", ""))
    doc_type = rec.get("doc_type", "")
    scores = cfg["scoring"]["venue_score"]
    if not venue:
        return float(scores["preprint"]) if doc_type == "preprint" else 0.4
    for pat in cfg["venues"]["preprint_patterns"]:
        if norm_text(pat) in venue:
            return float(scores["preprint"])
    for pat in cfg["venues"]["whitelist_patterns"]:
        p = norm_text(pat)
        if p in venue or (len(p) <= 6 and p in venue.split()):
            return float(scores["whitelisted"])
    if doc_type in ("journal", "conference", "workshop", "book", "chapter"):
        return float(scores["peer_reviewed"])
    return float(scores["preprint"])


def cites_raw(rec: dict, now_year: int | None = None) -> float:
    """log1p(citations) / log1p(age+1) - recent work is not punished for being recent."""
    now_year = now_year or _dt.date.today().year
    cites = float(rec.get("_cited_by", 0) or 0)
    year = rec.get("year") or now_year
    age = max(now_year - int(year), 0)
    return math.log1p(cites) / math.log1p(age + 1)


def cocite_raw(ctx, rec: dict, verified_titles: set[str], registry_aliases: set[str]) -> tuple[float, str]:
    """Distinct verified registry entries connected to this candidate."""
    if ctx.live("semanticscholar") or ctx.live("openalex"):
        linked = set(rec.get("_linked_ids") or [])
        hits = len(linked & registry_aliases)
        if rec.get("_linked_ids") is not None:
            return float(hits), "citation-graph"
    if ctx.live("bibcorpus"):
        co = ctx.bib.cocited_titles(rec.get("title", ""))
        return float(len({t for t in co if t in verified_titles})), "curated-bibliographies"
    return 0.0, "none"


def corroboration(ctx, rec: dict) -> tuple[int, bool]:
    """Run the phase-3 agreement test now: (independent sources, would verify?).

    Applied at admission time so a capped slot is not spent on a candidate that provably
    cannot reach two agreeing independent sources - such an entry can only ever reach the
    appendix. It never changes a score; it decides which of two candidates takes a slot.
    The work is not wasted: every lookup it makes is already cached for phase 3.
    """
    from .verify import resolve_views, views_agree
    views = resolve_views(ctx, rec.get("title", ""), rec.get("year"), rec.get("authors"),
                          aliases=rec.get("aliases", []))
    status, sources, _notes = views_agree(views)
    return len(sources), status == "verified"


def minmax(values: list[float]) -> list[float]:
    if not values:
        return []
    lo, hi = min(values), max(values)
    if hi - lo < 1e-9:
        return [0.0 if hi == 0 else 1.0 for _ in values]
    return [(v - lo) / (hi - lo) for v in values]


def score_batch(cfg, ctx, candidates: list[dict], verified_titles: set[str],
                registry_aliases: set[str]) -> None:
    """Fill rec['score'] and rec['area'] in place, scaling cites/cocite within the batch."""
    weights = cfg["scoring"]["weights"]
    multipliers = cfg["scoring"].get("area_cocite_multiplier", {})
    cites = [cites_raw(r) for r in candidates]
    cocites, cocite_sources = [], []
    for r in candidates:
        raw, src = cocite_raw(ctx, r, verified_titles, registry_aliases)
        cocites.append(raw)
        cocite_sources.append(src)
    cites_n, cocites_n = minmax(cites), minmax(cocites)

    for rec, cn, con, csrc in zip(candidates, cites_n, cocites_n, cocite_sources):
        areas, keyword, raws = assign_areas(cfg, rec)
        rec["area"] = areas
        mult = max([float(multipliers.get(a, 1.0)) for a in areas] or [1.0])
        con_w = min(con * mult, 1.0)
        venue = venue_score(cfg, rec)
        total = (float(weights["cites_norm"]) * cn + float(weights["cocite"]) * con_w
                 + float(weights["keyword"]) * keyword + float(weights["venue"]) * venue)
        n_sources, would_verify = corroboration(ctx, rec)
        rec["_corroboration"] = n_sources
        rec["_would_verify"] = would_verify
        uncertainty = scope_uncertainty(cfg, rec, keyword)
        if uncertainty:
            rec["scope_uncertain"] = uncertainty
        rec["score"] = {
            "total": round(total, 4),
            "corroborating_sources": n_sources,
            "would_verify": would_verify,
            "components": {"cites_norm": round(cn, 4), "cocite": round(con_w, 4),
                           "keyword": round(keyword, 4), "venue": round(venue, 4)},
            "components_source": {"cites_norm": "citation-counts" if any(
                r.get("_cited_by") for r in candidates) else "bibliography-frequency-proxy",
                "cocite": csrc},
            "area_raw": {a: round(v, 2) for a, v in raws.items() if v > 0},
        }
