"""The run report (deliverables/06-run-report.md), in the section 10 format.

Six numbered sections - counts, coverage gaps, seeds, API budget, expansion note,
changelog - followed by an appendix on source availability, caching and reproduction.
Everything here is read back from the registry and the run log; nothing is restated from
memory.
"""
from __future__ import annotations

from .util import iso_now, truncate

PHASE_LABEL = {"scaffold": "0 scaffold", "seed": "1 seed", "snowball": "2 snowball",
               "verify": "3 verify", "tier": "4 tier", "fetch": "5a fetch",
               "extract": "5b extract", "chunk": "6 chunk", "deliver": "7 deliver"}


def _this_run(ctx) -> list[dict]:
    rows = ctx.run_log()
    if not rows:
        return []
    runs, current, started = [], [], False
    for row in rows:
        if row["phase"] == "scaffold" and started:
            runs.append(current)
            current = []
        started = True
        current.append(row)
    runs.append(current)
    return runs[-1]


def _counts(reg) -> tuple[dict, dict, dict, dict]:
    areas, tiers, doc_types, verification = {}, {}, {}, {}
    for rec in reg.records.values():
        for a in rec.get("area", []) or ["unassigned"]:
            areas[a] = areas.get(a, 0) + 1
        if rec.get("tier"):
            tiers[rec["tier"]] = tiers.get(rec["tier"], 0) + 1
        dt = rec.get("doc_type") or "unrecorded"
        doc_types[dt] = doc_types.get(dt, 0) + 1
        st = rec.get("verification", {}).get("status", "unverified")
        verification[st] = verification.get(st, 0) + 1
    return areas, tiers, doc_types, verification


def render(ctx, changes: dict | None = None, annotation: dict | None = None) -> str:
    cfg, reg = ctx.cfg, ctx.registry
    by_phase = {row["phase"]: row.get("summary", {}) for row in _this_run(ctx)}
    areas, tiers, doc_types, verification = _counts(reg)
    fetch = by_phase.get("fetch", {})
    extract = by_phase.get("extract", {})
    chunk = by_phase.get("chunk", {})
    seed = by_phase.get("seed", {})
    snow = by_phase.get("snowball", {})

    out = ["# 06 - Run report", "",
           f"Generated {iso_now()} | cap {cfg.cap} | criteria_version {cfg.criteria_version}", ""]

    # -- 1. counts --------------------------------------------------------
    verified = reg.verified()
    rejected_by_reason: dict[str, int] = {}
    for row in reg.rejected.values():
        key = row.get("rejection_reason", "?").split(":")[0]
        rejected_by_reason[key] = rejected_by_reason.get(key, 0) + 1
    hist = chunk.get("histogram", {})
    # Corpus state, not last-run activity: a re-run that correctly does nothing must not
    # report that the corpus has no PDFs or no cloned repositories.
    pdfs_held = sum(1 for r in reg.records.values() if r.get("files", {}).get("pdf"))
    repos_held = len({r["files"]["repo_dir"] for r in reg.records.values()
                      if r.get("files", {}).get("repo_dir")})
    guidelines_held = sum(len(r.get("files", {}).get("guidelines", [])) for r in reg.records.values())
    guideline_texts = sum(len(r.get("files", {}).get("guideline_text", [])) for r in reg.records.values())
    manifest_only = len(reg.records) - pdfs_held

    out += ["## 1. Counts", "",
            f"- **{len(reg.records)} entries** in the registry (cap {cfg.cap}); "
            f"{len(verified)} verified, "
            f"{len(reg.records) - len(verified)} pending verification",
            "- per area: " + ", ".join(f"{k} {v}" for k, v in sorted(areas.items(), key=lambda kv: -kv[1])),
            "- per tier: " + (", ".join(f"T{k} {v}" for k, v in sorted(tiers.items())) or "none"),
            "- per doc_type: " + ", ".join(f"{k} {v}" for k, v in sorted(doc_types.items(), key=lambda kv: -kv[1])),
            "- verification: " + ", ".join(f"{k} {v}" for k, v in sorted(verification.items())),
            "- rejected (" + str(len(reg.rejected)) + " remembered): "
            + ", ".join(f"{k} {v}" for k, v in sorted(rejected_by_reason.items(), key=lambda kv: -kv[1])),
            f"- PDFs: {pdfs_held} held locally, {manifest_only} manifest-only "
            f"({fetch.get('pdfs_fetched', 0)} fetched in this run)",
            f"- repos cloned: {repos_held}; guideline/README documents retrieved: "
            f"{guidelines_held} ({guideline_texts} extracted to text; "
            f"{extract.get('guidelines_extracted', 0)} extracted in this run)",
            f"- chunks: {chunk.get('chunks', 0)} "
            f"({chunk.get('from_fulltext', 0)} full text, {chunk.get('from_guideline', 0)} "
            f"guideline, {chunk.get('from_abstract', 0)} abstract)",
            "- chunk token histogram: " + (", ".join(
                f"{k}: {v}" for k, v in sorted(hist.items(), key=lambda kv: int(kv[0].split('-')[0])))
                or "empty"),
            ""]
    if annotation:
        out += [f"- annotations: {annotation.get('written', 0)} written this run, "
                f"{annotation.get('unchanged', 0)} unchanged; grounding "
                + ", ".join(f"{k} {v}" for k, v in annotation.get("grounded", {}).items())
                + " (an entry with no retrieved text carries no annotation, by rule)", ""]

    # -- 2. coverage gaps -------------------------------------------------
    verified_area: dict[str, int] = {}
    pending_area: dict[str, int] = {}
    for rec in reg.records.values():
        bucket = verified_area if rec.get("verification", {}).get("status") == "verified" else pending_area
        for a in rec.get("area", []):
            bucket[a] = bucket.get(a, 0) + 1
    out += ["## 2. Coverage gaps", "", "| Area | Quota | Verified | Pending | Met |",
            "|---|---|---|---|---|"]
    unmet = []
    for area in cfg["areas"]:
        quota, got = cfg.area_quota(area), verified_area.get(area, 0)
        if got < quota:
            unmet.append((area, quota, got, pending_area.get(area, 0)))
        out.append(f"| {area} | {quota} | {got} | {pending_area.get(area, 0)} | "
                   f"{'yes' if got >= quota else 'no'} |")
    out.append("")
    if unmet:
        out += ["Below quota, and why: " + "; ".join(
            f"**{a}** {g}/{q} verified, {p} more admitted but pending" for a, q, g, p in unmet)
            + ". A pending entry is a registry record at status `candidate`: it was admitted and "
            "scored, but only one independent source could be reached for it. It is not rejected "
            "and needs no re-fetching - phase 3 processes exactly those records on the next run.",
            ""]
    else:
        out += ["Every area met its quota.", ""]

    important = [r for r in reg.records.values()
                 if r.get("verification", {}).get("status") != "verified"
                 and (any(p.get("via") == "seed" for p in r.get("discovered_from", []))
                      or (r.get("score", {}).get("components", {}) or {}).get("cocite", 0) >= 0.5)]
    important.sort(key=lambda r: -(r.get("score", {}).get("total") or 0))
    out += ["**Important works that could not be verified** (seed-derived, or co-listed with this "
            "corpus in at least half as many curated bibliographies as the most co-listed "
            "candidate):", ""]
    if important:
        for rec in important[:15]:
            srcs = ", ".join(rec["verification"].get("sources", [])) or "none"
            out.append(f"- {truncate(rec.get('title', ''), 85)} ({rec.get('year')}) - found by "
                       f"{srcs} - {truncate(rec['verification'].get('notes', ''), 90)}")
        if len(important) > 15:
            out.append(f"- ... and {len(important) - 15} more in `99-unverified-and-rejected.md`")
    else:
        out.append("- none")
    scope_uncertain = [r for r in reg.records.values() if r.get("scope_uncertain")]
    out += ["", f"**Scope-uncertain admissions ({len(scope_uncertain)}).** Admitted at the lowest "
            f"plausible tier and flagged here rather than dropped:", ""]
    for rec in scope_uncertain[:10]:
        out.append(f"- {truncate(rec.get('title', ''), 75)} (T{rec.get('tier')}) - "
                   f"{truncate(rec['scope_uncertain'], 110)}")
    if len(scope_uncertain) > 10:
        out.append(f"- ... and {len(scope_uncertain) - 10} more (`scope_uncertain` in "
                   f"registry.jsonl)")
    if not scope_uncertain:
        out.append("- none")
    out.append("")

    # -- 3. seeds ---------------------------------------------------------
    out += ["## 3. Seeds", "",
            f"{seed.get('seeds', 0)} hypotheses; {seed.get('verified', 0)} verified, "
            f"{seed.get('unverified', 0)} admitted unverified, {seed.get('rejected', 0)} rejected.",
            ""]
    as_given = seed.get("verified_as_given", [])
    if as_given:
        out += ["**Verified as given** (nothing in the hypothesis had to change):", ""]
        for row in as_given:
            out.append(f"- {truncate(row['title'], 90)} - `{row['id']}`")
        out.append("")
    corrections = seed.get("corrections", [])
    if corrections:
        out += ["**Corrected from the sources** (the hypothesis was wrong; the sources win):", "",
                "| Entry | Field | Hypothesis | Verified | Sources |", "|---|---|---|---|---|"]
        for c in corrections:
            out.append(f"| `{c['id']}` | {c['field']} | {truncate(str(c['hypothesis']), 60)} | "
                       f"{truncate(str(c['verified']), 60)} | "
                       f"{truncate(', '.join(c.get('sources', [])), 60)} |")
        out.append("")
    canonical = seed.get("canonicalised", [])
    if canonical:
        out += ["**Recorded in canonical form** (the hypothesis named the same venue, the "
                "sources spell it out):", ""]
        for c in canonical:
            out.append(f"- `{c['id']}` - {c['field']}: {truncate(str(c['hypothesis']), 40)} -> "
                       f"{truncate(str(c['verified']), 80)}")
        out.append("")
    rejected_seeds = seed.get("rejected_seeds", [])
    if rejected_seeds:
        out += ["**Rejected** (no source could resolve them; nothing was invented to fill the "
                "gap):", ""]
        for row in rejected_seeds:
            out.append(f"- {truncate(row['title'], 90)} ({row.get('year')}) - {row['reason']}")
        out.append("")

    # -- 4. api budget ----------------------------------------------------
    http = ctx.http
    out += ["## 4. API budget", "", "| Source | Network | Cache hits | Skipped (unreachable) | Errors |",
            "|---|---|---|---|---|"]
    for name in sorted(http.by_source):
        row = http.by_source[name]
        out.append(f"| {name} | {row['network']} | {row['cache']} | {row['skipped']} | "
                   f"{row['errors']} |")
    if not http.by_source:
        out.append("| (no external request was made in this run) | 0 | 0 | 0 | 0 |")
    out += ["",
            f"Cache hit rate: {http.hit_rate():.0%} over "
            f"{http.calls['network'] + http.calls['cache']} cacheable requests. Every request is "
            f"logged with its URL, hit/miss and status to `corpus/requests.log` (git-ignored).",
            ""]
    creds = http.credentials()
    missing = [k for k, v in creds.items() if not v]
    if missing:
        out += [f"Missing credentials: {', '.join(missing)}. Degradation: "
                + "; ".join(_degradation(k) for k in missing) + ".", ""]
    else:
        out += ["All optional credentials are present.", ""]

    # -- 5. expansion note ------------------------------------------------
    waiting = [r for r in reg.rejected.values()
               if r.get("rejection_reason") in ("below_cutoff", "cap_reached")
               and int(r.get("criteria_version", 0)) >= cfg.criteria_version]
    waiting.sort(key=lambda r: -((r.get("score") or {}).get("total") or 0))
    admitted_min = min((r.get("score", {}).get("total") or 1.0 for r in reg.records.values()
                        if r.get("score", {}).get("total") is not None), default=None)
    out += ["## 5. Expansion note", "",
            f"- {len(waiting)} scored candidates are waiting in `corpus/rejected.jsonl` "
            f"(reason `below_cutoff` or `cap_reached`, at criteria_version "
            f"{cfg.criteria_version}).",
            f"- unexpanded frontier nodes: "
            f"{len(reg.frontier) - sum(1 for n in reg.frontier.values() if n.get('expanded'))} "
            f"of {len(reg.frontier)}."]
    if waiting:
        best = waiting[0]
        comp = (best.get("score") or {}).get("components", {})
        out += [f"- best waiting candidate: **{truncate(best.get('title', ''), 80)}** "
                f"({best.get('year')}), score {best.get('score', {}).get('total')} "
                f"(cocite {comp.get('cocite')}, keyword {comp.get('keyword')}, "
                f"venue {comp.get('venue')})."]
        if admitted_min is not None:
            out += [f"- lowest admitted score in the registry: {round(admitted_min, 4)}. Raising "
                    f"the cap promotes waiting candidates in score order, using metadata already "
                    f"stored - no API call, no re-scoring."]
        out += [f"- `python -m argmine run --cap {cfg.cap + 50}` would consider all "
                f"{len(waiting)} of them."]
    else:
        out += ["- nothing is waiting: every scored candidate was admitted or excluded on its "
                "merits."]
    out.append("")

    # -- 6. changelog -----------------------------------------------------
    out += ["## 6. Changelog", ""]
    if changes:
        out.append(f"Run {changes.get('runs', 1)}; previous run recorded at "
                   f"{changes.get('since') or 'n/a'}.")
        out.append("")
        added = changes.get("added", [])
        if added:
            out.append(f"Added {len(added)} entries:")
            out.append("")
            for rid in added[:60]:
                rec = reg.records.get(rid)
                if rec:
                    out.append(f"- `{rid}` - {truncate(rec.get('title', ''), 85)} "
                               f"({rec.get('year')}, T{rec.get('tier')})")
            if len(added) > 60:
                out.append(f"- ... and {len(added) - 60} more")
        else:
            out.append("No new entries were admitted in this run.")
    else:
        out.append("No run log available.")
    out.append("")

    # -- appendix ---------------------------------------------------------
    out += ["---", "", "## Appendix A - phases in this run", "",
            "| Phase | Seconds | Summary |", "|---|---|---|"]
    for phase, label in PHASE_LABEL.items():
        s = by_phase.get(phase)
        if s is None:
            continue
        head = ", ".join(f"{k}={v}" for k, v in list(s.items())[:4]
                         if not isinstance(v, (dict, list)))
        out.append(f"| {label} | {s.get('seconds', '')} | {truncate(head, 140)} |")
    out.append("")

    out += ["## Appendix B - source availability", "", "| Source | Reachable | Detail |",
            "|---|---|---|"]
    for name, st in sorted(ctx.source_status.items()):
        out.append(f"| {name} | {'yes' if st.get('reachable') else 'no'} | "
                   f"{truncate(str(st.get('reason', '')), 110)} |")
    out.append("")

    queries = snow.get("queries", [])
    if queries:
        out += ["## Appendix C - targeted searches", "", "| Query | From | Source | Hits |",
                "|---|---|---|---|"]
        for row in queries:
            out.append(f"| `{row['query']}` | {row.get('origin', '6.7')} | {row['source']} | "
                       f"{row.get('hits', 0)}"
                       + (f" (error: {truncate(row['error'], 60)})" if row.get("error") else "")
                       + " |")
        out.append("")

    combos: dict[str, int] = {}
    for rec in reg.records.values():
        key = ", ".join(sorted({s.split(":")[0] for s in
                                rec.get("verification", {}).get("sources", [])})) or "none"
        combos[key] = combos.get(key, 0) + 1
    out += ["## Appendix D - verification evidence", "",
            "Source combinations behind the registry. A `bibcorpus` label counts once per "
            "independent repository, and never for a verbatim re-export of the ACL Anthology:", ""]
    for key, n in sorted(combos.items(), key=lambda kv: -kv[1]):
        out.append(f"- {key}: {n}")
    out.append("")

    out += ["## Appendix E - caching layers", "",
            f"- layer 1, HTTP cache: metadata responses expire after "
            f"{cfg['http']['metadata_ttl_days']} days, binaries never",
            "- layer 2, status gating: each phase processes only records at exactly its input "
            "status; fetch also skips a PDF whose sha256 matches, extract skips text whose source "
            "PDF hash is unchanged",
            f"- layer 3, frontier memory: "
            f"{sum(1 for n in reg.frontier.values() if n.get('expanded'))} of {len(reg.frontier)} "
            f"nodes expanded, directions recorded per node",
            f"- layer 4, decision memory: {len(reg.rejected)} rejected candidates kept with their "
            f"scores at criteria_version {cfg.criteria_version}; bumping it re-scores them without "
            f"re-fetching anything", ""]

    unreachable = sorted(k for k, v in ctx.source_status.items() if not v.get("reachable"))
    out += ["## Appendix F - limits of this run", ""]
    if unreachable:
        out += [f"Unreachable sources: {', '.join(unreachable)}. Consequences:", "",
                "- no citation-graph expansion: the `reference` and `citation` directions stay "
                "pending on every frontier node, so a later run with network access expands "
                "exactly those and nothing else;",
                "- no citation counts, so `cites_norm` is computed from how many independent "
                "bibliographies list a work; the substitution is recorded per record in "
                "`score.components_source`;",
                "- no OA PDF could be downloaded, so annotations are grounded on abstracts and "
                "most chunks are abstract chunks. Every entry is in `05-fetch-manifest.csv` with "
                "a resolvable URL, so the PDFs can be fetched elsewhere and "
                "`python -m argmine extract chunk` picks them up;",
                "- every entry that reached only one independent source is still a `candidate` and "
                "is re-examined by phase 3 on the next run.", ""]
    else:
        out += ["All configured sources were reachable.", ""]

    out += ["## Appendix G - reproducing this run", "", "```bash",
            "python -m argmine run            # resume; every phase is idempotent",
            f"python -m argmine run --cap {cfg.cap + 50}  # expand: only new work is done",
            "python -m argmine status         # registry / frontier / rejection counts",
            "python -m argmine report         # print this report", "```", ""]
    return "\n".join(out)


def _degradation(key: str) -> str:
    return {
        "S2_API_KEY": "Semantic Scholar runs unauthenticated, at a lower rate limit "
                      "(config sets a 3 s delay for it)",
        "GITHUB_TOKEN": "GitHub search runs unauthenticated or from the committed search cache; "
                        "repository cloning is unaffected",
        "contact_email": "OpenAlex and Crossref polite pools are unavailable and Unpaywall "
                         "cannot be called at all",
        "UNPAYWALL_EMAIL": "Unpaywall falls back to run.contact_email",
    }.get(key, "unknown")
