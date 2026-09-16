"""Renders deliverables/00-field-map.md from config.yaml.

The field map is the coverage contract: it is written in phase 0, before any searching,
and regenerated (with live counts) by every later run. Because both the document and the
keyword scorer read the same ``areas`` block of config.yaml, the contract and the code
cannot drift apart.
"""
from __future__ import annotations

from .util import iso_now

HEADER = """# 00 - Field map

The coverage contract for this corpus. Written in phase 0 **before any searching**, and
regenerated with live counts by every subsequent run. Six areas, each with a definition,
inclusion and exclusion criteria, the vocabulary used for keyword scoring, and a minimum
quota out of the {cap}-entry cap.

Generated: {ts} | criteria_version: {cv}
"""

GLOBAL = """
## Global exclusions

Applied before scoring, to every candidate:

- legal argument mining and scientific-abstract argument mining, **unless** the work is
  foundational to an area (admitted only at tier 1);
- sentiment / opinion mining;
- persuasion research aimed at marketing or compliance outcomes;
- non-English-only resources, unless the resource is a major multilingual benchmark.

Pattern list actually used by the scorer: {patterns}.
"""

SCORING = """
## How an area is assigned

`keyword` score: title and abstract are matched against the per-area vocabulary below.
Each term carries a weight (3 = defining, 2 = strong, 1 = weak), doubled for a match in
the title and halved for one in the venue name; an area's raw score is the sum of the
weights it matches. The record's `keyword` component is its best area's raw score divided
by a saturation constant ({saturation:g}), capped at 1. A candidate is assigned its best
area plus every other area scoring at least {share:.0%} of the best or at least
{min_norm:.0%} of saturation, so genuinely cross-area work (a dialogue corpus paper, say)
counts toward both quotas.

Total candidate score = {weights}. `cocite` is multiplied by {multipliers} for the areas
listed, because those areas sit closest to the downstream debate-transcript database.
"""


def render(cfg, registry=None, source_status: dict | None = None) -> str:
    area_counts, tier_counts = {}, {}
    if registry is not None:
        area_counts = registry.area_counts()
        for r in registry.records.values():
            if r.get("tier"):
                tier_counts[r["tier"]] = tier_counts.get(r["tier"], 0) + 1

    out = [HEADER.format(cap=cfg.cap, ts=iso_now(), cv=cfg.criteria_version)]
    out.append("\n## Areas\n")
    out.append("| # | Area | Quota | In corpus |")
    out.append("|---|------|-------|-----------|")
    for key, spec in cfg["areas"].items():
        out.append(f"| {spec['number']} | {spec['name']} (`{key}`) | {cfg.area_quota(key)} | "
                   f"{area_counts.get(key, 0)} |")
    out.append("")
    for key, spec in cfg["areas"].items():
        out.append(f"### {spec['number']} {spec['name']}  `{key}`  (quota >= {cfg.area_quota(key)}, "
                   f"currently {area_counts.get(key, 0)})\n")
        out.append(f"**Definition.** {spec['definition'].strip()}\n")
        out.append(f"**Include.** {spec['include'].strip()}\n")
        out.append(f"**Exclude.** {spec['exclude'].strip()}\n")
        vocab = spec["vocabulary"]
        by_weight: dict[int, list[str]] = {}
        for term, w in vocab.items():
            by_weight.setdefault(int(w), []).append(term)
        parts = []
        for w in sorted(by_weight, reverse=True):
            parts.append(f"weight {w}: " + ", ".join(f"`{t}`" for t in sorted(by_weight[w])))
        out.append("**Vocabulary.** " + "; ".join(parts) + "\n")

    out.append(GLOBAL.format(patterns=", ".join(f"`{p}`" for p in cfg["exclusions"]["domain_patterns"])))
    out.append(SCORING.format(
        share=float(cfg["scoring"].get("area_share", 0.6)),
        saturation=float(cfg["scoring"].get("keyword_saturation", 12.0)),
        min_norm=float(cfg["scoring"].get("area_min_norm", 0.4)),
        weights=", ".join(f"{k} {v}" for k, v in cfg["scoring"]["weights"].items()),
        multipliers=", ".join(f"{k} x{v}" for k, v in cfg["scoring"].get("area_cocite_multiplier", {}).items())
        or "nothing"))

    out.append("\n## Targeted searches (6.7)\n")
    out.append("Run in phase 2 across every reachable source; each query and its hit count is "
               "logged in `06-run-report.md`.\n")
    for q in cfg["searches"]:
        out.append(f"- `{q}`")
    supplementary = cfg.get("searches_supplementary") or {}
    if supplementary:
        out.append("\nSupplementary per-area queries, added so the quotas in under-served "
                   "areas have a fair chance (logged separately in the run report):\n")
        for area, qs in supplementary.items():
            out.append(f"- **{area}**: " + ", ".join(f"`{q}`" for q in qs))

    out.append("\n## Tier rubric\n")
    for key in ("t1", "t2", "t3", "t4"):
        n = tier_counts.get(int(key[1]), 0)
        out.append(f"- **{key.upper()}** - {cfg['tiers'][key]} ({n} in corpus)")

    out.append("\n## Downstream tags\n")
    out.append(", ".join(f"`{t}`" for t in cfg["downstream_tags"]))

    if source_status:
        out.append("\n## Evidence sources available to this run\n")
        out.append("| Source | Reachable | Detail |")
        out.append("|--------|-----------|--------|")
        for name in sorted(source_status):
            st = source_status[name]
            mark = "yes" if st.get("reachable") else "no"
            out.append(f"| {name} | {mark} | {str(st.get('reason', ''))[:90]} |")
    out.append("")
    return "\n".join(out)
