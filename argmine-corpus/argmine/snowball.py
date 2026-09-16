"""Phase 2 - snowball.

Breadth-first expansion from the frontier in both directions, plus the targeted searches
of section 6.7 for coverage the citation graph cannot reach. Candidates are scored,
filtered by the global exclusions, and admitted by score subject to the cap and the
per-area minimum quotas. Everything scored but not admitted is written to
``rejected.jsonl`` with its score, so raising the cap later promotes it without a single
new API call.

Expansion memory (layer 3): a frontier node is expanded once per direction. Where the
citation-graph APIs are reachable the directions are ``reference`` and ``citation``;
where they are not, the pipeline expands the ``bibliography`` direction instead (works
co-listed in curated BibTeX bibliographies) and leaves the two citation directions
pending, so a later run with network access picks up exactly the work that was missed.
"""
from __future__ import annotations

from .cache import advance
from .registry import blank_record
from .score import exclusion_reason, score_batch
from .util import iso_now, norm_title

MAX_PER_NODE = 60


def _record_from_view(view: dict, provenance: dict) -> dict:
    rec = blank_record(
        title=view["title"], authors=view.get("authors", []), year=view.get("year"),
        venue=view.get("venue", ""), doc_type=view.get("doc_type", ""),
        abstract=view.get("abstract", ""), aliases=list(view.get("aliases", [])),
        urls=dict(view.get("urls", {})), discovered_from=[provenance],
    )
    extra = view.get("extra", {})
    rec["_cited_by"] = extra.get("cited_by_count", 0)
    linked = extra.get("referenced_works")
    if linked is not None:
        rec["_linked_ids"] = [f"openalex:{x}" for x in linked]
    return rec


def _strip_private(rec: dict) -> dict:
    return {k: v for k, v in rec.items() if not k.startswith("_")}


def _merge_candidate(pool: dict, rec: dict) -> None:
    key = norm_title(rec["title"])
    if not key:
        return
    prior = pool.get(key)
    if prior is None:
        pool[key] = rec
        return
    for field in ("abstract", "venue", "doc_type"):
        if len(str(rec.get(field) or "")) > len(str(prior.get(field) or "")):
            prior[field] = rec[field]
    if len(rec.get("authors") or []) > len(prior.get("authors") or []):
        prior["authors"] = rec["authors"]
    prior["year"] = prior.get("year") or rec.get("year")
    prior["aliases"] = sorted(set(prior.get("aliases", [])) | set(rec.get("aliases", [])))
    prior["urls"] = {**rec.get("urls", {}), **{k: v for k, v in prior.get("urls", {}).items() if v}}
    seen = {(p.get("id"), p.get("via")) for p in prior["discovered_from"]}
    for p in rec["discovered_from"]:
        if (p.get("id"), p.get("via")) not in seen:
            prior["discovered_from"].append(p)
    prior["_cited_by"] = max(prior.get("_cited_by", 0), rec.get("_cited_by", 0))


# -- expansion ------------------------------------------------------------
def expand_frontier(ctx, pool: dict) -> dict:
    """Expand every frontier node that has not been expanded in each available direction."""
    reg = ctx.registry
    graph_live = ctx.live("semanticscholar") or ctx.live("openalex")
    directions = ["reference", "citation"] if graph_live else ["bibliography"]
    stats = {d: {"nodes": 0, "candidates": 0} for d in directions}

    for direction in directions:
        for node in list(reg.frontier_pending(direction)):
            rec = reg.records.get(node["id"])
            if rec is None or rec.get("verification", {}).get("status") != "verified":
                continue
            views = _expand_one(ctx, rec, direction)
            stats[direction]["nodes"] += 1
            for view in views[:MAX_PER_NODE]:
                cand = _record_from_view(view, {"id": rec["id"], "via": direction})
                _merge_candidate(pool, cand)
                stats[direction]["candidates"] += 1
            reg.frontier_mark(node["id"], direction)
    return stats


def _expand_one(ctx, rec: dict, direction: str) -> list[dict]:
    ids = [rec["id"]] + list(rec.get("aliases", []))
    s2_id = next((a.split(":", 1)[1] for a in ids if a.startswith("s2:")), "")
    oa_id = next((a.split(":", 1)[1] for a in ids if a.startswith("openalex:")), "")
    doi = next((a.split(":", 1)[1] for a in ids if a.startswith("doi:")), "")

    if direction in ("reference", "citation"):
        views = []
        if ctx.live("semanticscholar"):
            ident = s2_id or (f"DOI:{doi}" if doi else "")
            if ident:
                views = (ctx.s2.references(ident) if direction == "reference"
                         else ctx.s2.citations(ident))
        if not views and ctx.live("openalex"):
            ident = oa_id
            if not ident and doi:
                view = ctx.openalex.by_doi(doi)
                ident = next((a.split(":", 1)[1] for a in (view or {}).get("aliases", [])
                              if a.startswith("openalex:")), "")
            if ident:
                views = (ctx.openalex.references(ident) if direction == "reference"
                         else ctx.openalex.citations(ident))
        return views

    # bibliography direction: works co-listed with this one in curated bibliographies
    co = ctx.bib.cocited_titles(rec["title"])
    ranked = sorted(co.items(), key=lambda kv: -kv[1])[:MAX_PER_NODE]
    out = []
    for ntitle, _count in ranked:
        view = ctx.bib.best_record(ntitle)
        if not view:
            continue
        acl_hit = ctx.acl.lookup_title(view["title"], view.get("year")) if ctx.live("acl") else []
        out.append(acl_hit[0] if acl_hit else view)
    return out


# -- targeted searches ----------------------------------------------------
def targeted_searches(ctx, pool: dict) -> list[dict]:
    """Section 6.7. Every query is run against every reachable source and logged."""
    cfg = ctx.cfg
    log_rows = []
    per_query_limit = int(cfg["scoring"].get("search_limit", 40))
    queries = [(q, "6.7") for q in cfg["searches"]]
    for area, extra in (cfg.get("searches_supplementary") or {}).items():
        queries.extend((q, f"supplementary:{area}") for q in extra)
    for query, origin in queries:
        for source, fn in _search_fns(ctx).items():
            try:
                views = fn(query, per_query_limit)
            except Exception as exc:                      # a single flaky source must not stop the run
                ctx.log(f"  search failed ({source}, {query!r}): {str(exc)[:120]}")
                log_rows.append({"query": query, "origin": origin, "source": source,
                                 "hits": 0, "error": str(exc)[:120]})
                continue
            for view in views:
                _merge_candidate(pool, _record_from_view(view, {"id": f"search:{query}",
                                                                "via": f"search:{query}"}))
            log_rows.append({"query": query, "origin": origin, "source": source,
                             "hits": len(views)})
    for venue in cfg["scoring"].get("acl_venue_sweeps", []):
        if not ctx.live("acl"):
            break
        views = ctx.acl.venue_papers(venue)
        for view in views:
            _merge_candidate(pool, _record_from_view(view, {"id": f"venue:{venue}",
                                                            "via": f"search:venue:{venue}"}))
        log_rows.append({"query": f"venue:{venue}", "origin": "venue sweep", "source": "acl",
                         "hits": len(views)})
    for query, total in ctx.gh.queries_logged().items():
        log_rows.append({"query": query, "origin": "github discovery", "source": "github",
                         "hits": total})
    return log_rows


def _search_fns(ctx) -> dict:
    fns = {}
    if ctx.live("acl"):
        fns["acl"] = lambda q, n: ctx.acl.search(q, limit=n)
    if ctx.live("openalex"):
        fns["openalex"] = lambda q, n: ctx.openalex.search(q, limit=n)
    if ctx.live("semanticscholar"):
        fns["semanticscholar"] = lambda q, n: ctx.s2.search(q, limit=n)
    if ctx.live("arxiv"):
        fns["arxiv"] = lambda q, n: ctx.arxiv.search(q, limit=min(n, 20))
    if ctx.live("bibcorpus"):
        fns["bibcorpus"] = lambda q, n: ctx.bib.search(q, limit=n)
    return fns


# -- admission ------------------------------------------------------------
def admit(ctx, scored: list[dict]) -> dict:
    """Admit by score, honouring the cap and the per-area minimum quotas."""
    cfg, reg = ctx.cfg, ctx.registry
    room = cfg.cap - len(reg.records)
    threshold = float(cfg["scoring"].get("admit_threshold", 0.3))
    summary = {"room": room, "admitted": 0, "quota_admitted": 0, "below_cutoff": 0,
               "added_ids": [], "by_area": {}}
    if room <= 0:
        for rec in scored:
            reg.reject(_strip_private(rec), "cap_reached", rec.get("score"))
        summary["below_cutoff"] = len(scored)
        return summary

    # Rank by score, but let a candidate that can already reach two independent sources
    # take a slot ahead of one that cannot: an unverifiable entry can never enter the
    # bibliography, only the appendix, so spending a capped slot on it is waste.
    ranked = sorted(scored, key=lambda r: (-(1 if r.get("_would_verify") else 0),
                                           -r["score"]["total"]))
    counts = dict(reg.area_counts())
    chosen: list[dict] = []
    taken: set[int] = set()

    # Quota pass: starve no area because another one has more volume. Two rounds - the
    # first fills each area only with candidates that will actually reach the bibliography,
    # the second falls back to the best of the rest where an area cannot be filled that way.
    deficits = {a: max(cfg.area_quota(a) - counts.get(a, 0), 0) for a in cfg["areas"]}
    for verifiable_only in (True, False):
        for area in sorted(deficits, key=lambda a: -deficits[a]):
            need = deficits[area] - sum(1 for r in chosen if area in r.get("area", []))
            if need <= 0:
                continue
            for idx, rec in enumerate(ranked):
                if need <= 0 or len(chosen) >= room:
                    break
                if idx in taken or area not in rec.get("area", []):
                    continue
                if verifiable_only and not rec.get("_would_verify"):
                    continue
                taken.add(idx)
                chosen.append(rec)
                summary["quota_admitted"] += 1
                need -= 1
                for a in rec.get("area", []):
                    counts[a] = counts.get(a, 0) + 1

    # Score pass: fill what is left with the best of the rest.
    for idx, rec in enumerate(ranked):
        if len(chosen) >= room:
            break
        if idx in taken or rec["score"]["total"] < threshold:
            continue
        taken.add(idx)
        chosen.append(rec)
    summary["admitted_corroborated"] = sum(1 for r in chosen if r.get("_would_verify"))

    for idx, rec in enumerate(ranked):
        if idx in taken:
            continue
        reason = "below_cutoff" if rec["score"]["total"] < threshold else "cap_reached"
        reg.reject(_strip_private(rec), reason, rec.get("score"))
        summary["below_cutoff"] += 1

    for rec in chosen:
        rec["criteria_version"] = cfg.criteria_version
        rec["updated_at"] = iso_now()
        stored, created = reg.upsert(_strip_private(rec))
        if created:
            summary["added_ids"].append(stored["id"])
            summary["admitted"] += 1
            for a in stored.get("area", []):
                summary["by_area"][a] = summary["by_area"].get(a, 0) + 1
    return summary


# -- phase ----------------------------------------------------------------
def run(ctx) -> dict:
    cfg, reg = ctx.cfg, ctx.registry
    prep = ctx.prepare_local_sources()
    pool: dict[str, dict] = {}

    expansion = expand_frontier(ctx, pool)
    ctx.log(f"  frontier expansion: {expansion}")
    queries = targeted_searches(ctx, pool)
    ctx.log(f"  targeted searches: {len(queries)} query/source pairs, "
            f"{sum(r.get('hits', 0) for r in queries)} hits")

    fresh, excluded, known = [], 0, 0
    for rec in pool.values():
        reason = exclusion_reason(cfg, rec)
        if reason:
            reg.reject(_strip_private(rec), reason)
            excluded += 1
            continue
        decided = reg.is_decided(_strip_private(rec))
        if decided:
            known += 1
            continue
        fresh.append(rec)

    verified_titles = {norm_title(r["title"]) for r in reg.verified()}
    registry_aliases = set()
    for r in reg.records.values():
        registry_aliases.add(r["id"])
        registry_aliases.update(r.get("aliases", []))
    score_batch(cfg, ctx, fresh, verified_titles, registry_aliases)

    result = admit(ctx, fresh)
    result.update({"pool": len(pool), "excluded": excluded, "already_decided": known,
                   "scored": len(fresh), "expansion": expansion, "queries": queries,
                   "prepared": prep})
    return result


def paragraph(summary: dict) -> str:
    exp = summary.get("expansion", {})
    directions = ", ".join(f"{d}: {v['nodes']} nodes -> {v['candidates']} candidates"
                           for d, v in exp.items()) or "no pending frontier nodes"
    qs = summary.get("queries", [])
    return (f"Phase snowball: expanded the frontier ({directions}) and ran "
            f"{len({q['query'] for q in qs})} targeted queries across "
            f"{len({q['source'] for q in qs})} sources for {sum(q.get('hits', 0) for q in qs)} hits; "
            f"pooled {summary.get('pool', 0)} distinct candidates, of which "
            f"{summary.get('already_decided', 0)} were already decided and "
            f"{summary.get('excluded', 0)} hit a global exclusion. "
            f"Scored {summary.get('scored', 0)}; admitted {summary.get('admitted', 0)} "
            f"({summary.get('quota_admitted', 0)} to meet area quotas) with "
            f"{summary.get('room', 0)} slots of room under the cap; "
            f"{summary.get('below_cutoff', 0)} were written to rejected.jsonl with their "
            f"scores so a later cap increase can promote them without re-fetching.")
