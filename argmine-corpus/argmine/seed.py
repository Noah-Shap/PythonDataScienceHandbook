"""Phase 1 - seed.

The seed list in config.yaml is a list of *hypotheses*. Each one is resolved against at
least two independent sources; titles, years and venues are corrected from what the
sources say; anything that cannot be resolved is written to rejected.jsonl with reason
``seed_unresolved`` and never silently carried forward.
"""
from __future__ import annotations

from rapidfuzz import fuzz

from .registry import blank_record
from .util import iso_now, norm_title, surnames
from .verify import resolve_views, venue_compatible, views_agree

TITLE_MATCH = 88.0


def _plausible(view: dict, seed: dict) -> bool:
    """Guard against a source answering with a different work.

    The year check is deliberately skipped when the title matches almost exactly and an
    author surname matches: classics are re-issued (Toulmin 1958 / 2003), and a later
    edition is the same work, not a different one.
    """
    title_sim = fuzz.token_set_ratio(norm_title(view["title"]), norm_title(seed["title"]))
    if title_sim < TITLE_MATCH:
        return False
    want = {s.lower() for s in seed.get("authors", [])}
    have = surnames(view.get("authors"))
    author_ok = bool(want and have and ({w.split()[-1] for w in want} & have))
    if want and have and not author_ok:
        return False
    strong = title_sim >= 97 and not (want and have and not author_ok)
    if not strong and seed.get("year") and view.get("year") \
            and abs(int(view["year"]) - int(seed["year"])) > 3:
        return False
    return True


def run(ctx) -> dict:
    cfg, reg = ctx.cfg, ctx.registry
    prep = ctx.prepare_local_sources()
    summary = {"seeds": len(cfg["seeds"]), "verified": 0, "unverified": 0, "rejected": 0,
               "added_ids": [], "corrections": [], "canonicalised": [],
               "verified_as_given": [], "rejected_seeds": [], "prepared": prep}

    for seed in cfg["seeds"]:
        views = [v for v in resolve_views(ctx, seed["title"], seed.get("year"),
                                          authors=seed.get("authors"))
                 if _plausible(v, seed)]
        if not views:
            reg.reject({"title": seed["title"], "year": seed.get("year"),
                        "authors": seed.get("authors", []), "area": seed.get("area", []),
                        "discovered_from": [{"id": "seed", "via": "seed"}]},
                       "seed_unresolved")
            summary["rejected"] += 1
            summary["rejected_seeds"].append(
                {"title": seed["title"], "year": seed.get("year"),
                 "reason": "seed_unresolved: no source returned a plausible match for this "
                           "title, author and year"})
            ctx.log(f"  [unresolved] {seed['title'][:70]}")
            continue

        rec, agreement = build_record(ctx, seed, views)
        stored, created = reg.upsert(rec)
        if created:
            summary["added_ids"].append(stored["id"])
        if stored["verification"]["status"] == "verified":
            summary["verified"] += 1
        else:
            summary["unverified"] += 1
        reg.frontier_add(stored["id"], stored["title"])

        for field in ("title", "year", "venue"):
            hypothesis, actual = seed.get(field), stored.get(field)
            if hypothesis and actual and str(hypothesis).strip().lower() != str(actual).strip().lower():
                if field == "title" and fuzz.ratio(norm_title(str(hypothesis)), norm_title(str(actual))) > 97:
                    continue
                if field == "venue" and venue_compatible(str(hypothesis), str(actual))[0]:
                    # "LREC" -> "Proceedings of the Thirteenth ... Conference" is the same
                    # venue written out, not a corrected hypothesis.
                    summary["canonicalised"].append(
                        {"id": stored["id"], "field": field, "hypothesis": hypothesis,
                         "verified": actual})
                    continue
                summary["corrections"].append(
                    {"id": stored["id"], "field": field, "hypothesis": hypothesis, "verified": actual,
                     "sources": stored["verification"]["sources"]})
        if not any(c["id"] == stored["id"] for c in summary["corrections"]):
            summary["verified_as_given"].append(
                {"id": stored["id"], "title": stored["title"],
                 "status": stored["verification"]["status"]})
        ctx.log(f"  [{stored['verification']['status']:10}] {stored['id'][:48]:48} "
                f"{stored['title'][:52]} ({', '.join(agreement)})")

    return summary


def build_record(ctx, seed: dict, views: list[dict]):
    """Fold the source views into one registry record, preferring the richest fields."""
    from .verify import merge_views
    rec = blank_record(**merge_views(views))
    rec["area"] = sorted(set(seed.get("area", [])))
    rec["discovered_from"] = [{"id": "seed", "via": "seed"}]
    status, sources, notes = views_agree(views)
    rec["verification"] = {"status": status, "sources": sources, "checked_at": iso_now(),
                           "notes": notes}
    rec["status"] = "verified" if status == "verified" else "candidate"
    rec["criteria_version"] = ctx.cfg.criteria_version
    if seed.get("note"):
        rec["verification"]["notes"] = (rec["verification"]["notes"] + " " + seed["note"]).strip()
    return rec, sources
