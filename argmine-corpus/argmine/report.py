"""The run report: what this run did, what it cost, and what it could not do."""
from __future__ import annotations

from .util import iso_now, truncate

PHASE_LABEL = {"scaffold": "0 scaffold", "seed": "1 seed", "snowball": "2 snowball",
               "verify": "3 verify", "tier": "4 tier", "fetch": "5a fetch",
               "extract": "5b extract", "chunk": "6 chunk", "deliver": "7 deliver"}


def _last_runs(ctx) -> list[dict]:
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


def render(ctx, changes: dict | None = None, annotation: dict | None = None) -> str:
    cfg, reg = ctx.cfg, ctx.registry
    this_run = _last_runs(ctx)
    by_phase = {row["phase"]: row for row in this_run}

    out = ["# 06 - Run report", "",
           f"Generated {iso_now()} | cap {cfg.cap} | criteria_version {cfg.criteria_version} | "
           f"registry {len(reg.records)} entries", ""]

    # -- what ran ---------------------------------------------------------
    out += ["## Phases in this run", "", "| Phase | Seconds | Summary |", "|---|---|---|"]
    for phase, label in PHASE_LABEL.items():
        row = by_phase.get(phase)
        if not row:
            continue
        s = row.get("summary", {})
        head = ", ".join(f"{k}={v}" for k, v in list(s.items())[:4]
                         if not isinstance(v, (dict, list)))
        out.append(f"| {label} | {s.get('seconds', '')} | {truncate(head, 140)} |")
    out.append("")

    # -- corpus state -----------------------------------------------------
    counts = reg.counts()
    tiers, doc_types, ver_counts = {}, {}, {}
    for rec in reg.records.values():
        if rec.get("tier"):
            tiers[rec["tier"]] = tiers.get(rec["tier"], 0) + 1
        dt = rec.get("doc_type") or "unrecorded"
        doc_types[dt] = doc_types.get(dt, 0) + 1
        vs = rec.get("verification", {}).get("status", "unverified")
        ver_counts[vs] = ver_counts.get(vs, 0) + 1
    out += ["## Corpus state", "",
            f"- status: {counts}",
            f"- verification: {ver_counts}",
            f"- tiers: " + ", ".join(f"T{k}: {v}" for k, v in sorted(tiers.items())),
            f"- doc types: " + ", ".join(f"{k}: {v}" for k, v in sorted(doc_types.items(),
                                                                       key=lambda kv: -kv[1])),
            f"- frontier: {len(reg.frontier)} nodes, "
            f"{sum(1 for n in reg.frontier.values() if n.get('expanded'))} expanded",
            f"- rejected ledger: {len(reg.rejected)} candidates remembered",
            ""]

    # -- quotas -----------------------------------------------------------
    area_counts = reg.area_counts()
    verified_area: dict[str, int] = {}
    for rec in reg.records.values():
        if rec.get("verification", {}).get("status") == "verified":
            for a in rec.get("area", []):
                verified_area[a] = verified_area.get(a, 0) + 1
    out += ["## Area quotas", "", "| Area | Quota | In registry | Verified | Met |",
            "|---|---|---|---|---|"]
    unmet = []
    for area in cfg["areas"]:
        quota = cfg.area_quota(area)
        got = verified_area.get(area, 0)
        met = "yes" if got >= quota else "no"
        if got < quota:
            unmet.append((area, quota, got))
        out.append(f"| {area} | {quota} | {area_counts.get(area, 0)} | {got} | {met} |")
    out.append("")
    if unmet:
        out += ["Areas below quota and why: " + "; ".join(
            f"**{a}** ({g}/{q})" for a, q, g in unmet) + ". See *Limits of this run* below.", ""]

    # -- sources ----------------------------------------------------------
    out += ["## Source availability", "", "| Source | Reachable | Detail |", "|---|---|---|"]
    for name, st in sorted(ctx.source_status.items()):
        out.append(f"| {name} | {'yes' if st.get('reachable') else 'no'} | "
                   f"{truncate(str(st.get('reason', '')), 110)} |")
    out.append("")

    # -- searches ---------------------------------------------------------
    queries = (by_phase.get("snowball", {}).get("summary", {}) or {}).get("queries", [])
    if queries:
        out += ["## Targeted searches (6.7)", "", "| Query | Source | Hits |", "|---|---|---|"]
        for row in queries:
            out.append(f"| `{row['query']}` | {row['source']} | {row.get('hits', 0)}"
                       + (f" (error: {truncate(row['error'], 60)})" if row.get("error") else "")
                       + " |")
        out.append("")

    # -- verification evidence -------------------------------------------
    combos: dict[str, int] = {}
    for rec in reg.records.values():
        srcs = rec.get("verification", {}).get("sources", [])
        key = ", ".join(sorted({s.split(":")[0] for s in srcs})) or "none"
        combos[key] = combos.get(key, 0) + 1
    out += ["## Verification evidence", "",
            "Source combinations backing the registry (a `bibcorpus` label counts once per "
            "independent repository, and never for a verbatim re-export of the ACL Anthology):", ""]
    for key, n in sorted(combos.items(), key=lambda kv: -kv[1]):
        out.append(f"- {key}: {n}")
    out.append("")

    # -- retrieval --------------------------------------------------------
    fetch = (by_phase.get("fetch", {}).get("summary", {}) or {})
    extract = (by_phase.get("extract", {}).get("summary", {}) or {})
    chunk = (by_phase.get("chunk", {}).get("summary", {}) or {})
    if fetch or extract or chunk:
        out += ["## Retrieval, extraction, chunking", "",
                f"- PDFs: {fetch.get('pdfs_fetched', 0)} fetched, "
                f"{fetch.get('pdfs_cached', 0)} already cached, "
                f"{fetch.get('pdfs_unavailable', 0)} unavailable",
                f"- repositories cloned: {fetch.get('repos_cloned', 0)}; "
                f"guideline/README documents copied: {fetch.get('guidelines', 0)}",
                f"- extraction: {extract.get('pdfs_extracted', 0)} PDFs "
                f"({extract.get('pages', 0)} pages), "
                f"{extract.get('guidelines_extracted', 0)} guideline documents, "
                f"{len(extract.get('failures', []))} failures",
                f"- chunks: {chunk.get('chunks', 0)} "
                f"({chunk.get('from_fulltext', 0)} full text, "
                f"{chunk.get('from_guideline', 0)} guideline, "
                f"{chunk.get('from_abstract', 0)} abstract-only)", ""]
        reasons = fetch.get("reasons", {})
        if reasons:
            out += ["Why PDFs were not fetched:", ""]
            for reason, n in sorted(reasons.items(), key=lambda kv: -kv[1]):
                out.append(f"- {reason}: {n}")
            out.append("")

    # -- annotations ------------------------------------------------------
    if annotation:
        out += ["## Annotations", "",
                f"- written this run: {annotation.get('written', 0)}; "
                f"unchanged: {annotation.get('unchanged', 0)}",
                f"- grounding: {annotation.get('grounded', {})}",
                "- every annotation quotes the retrieved text it was written from and names it "
                "in `grounded_on`; where nothing was retrieved the annotation says so and asserts "
                "nothing about content.", ""]

    # -- cost and caching -------------------------------------------------
    http = ctx.http.calls
    out += ["## Cost and caching", "",
            f"- HTTP: {http['network']} network calls, {http['cache']} cache hits, "
            f"{http['skipped_unreachable']} skipped because the source is unreachable, "
            f"{http['errors']} retried errors",
            "- layer 1 (HTTP cache): metadata responses expire after "
            f"{cfg['http']['metadata_ttl_days']} days, PDFs never expire",
            "- layer 2 (status gating): every phase processes only records at exactly its input "
            "status; fetch additionally skips a PDF whose sha256 matches, extract skips text whose "
            "source PDF hash is unchanged",
            f"- layer 3 (frontier memory): "
            f"{sum(1 for n in reg.frontier.values() if n.get('expanded'))} of "
            f"{len(reg.frontier)} nodes expanded; directions recorded per node",
            f"- layer 4 (decision memory): {len(reg.rejected)} rejected candidates kept with their "
            f"scores at criteria_version {cfg.criteria_version}; bumping it re-scores them without "
            f"re-fetching anything", ""]

    # -- changelog --------------------------------------------------------
    if changes:
        out += ["## Changelog", "",
                f"Run {changes.get('runs', 1)}; previous run recorded at "
                f"{changes.get('since') or 'n/a'}.", ""]
        added = changes.get("added", [])
        if added:
            out.append(f"Added {len(added)} entries:")
            out.append("")
            for rid in added[:80]:
                rec = reg.records.get(rid)
                if rec:
                    out.append(f"- `{rid}` - {truncate(rec.get('title', ''), 90)} "
                               f"({rec.get('year')}, T{rec.get('tier')})")
            if len(added) > 80:
                out.append(f"- ... and {len(added) - 80} more")
        else:
            out.append("No new entries were admitted in this run.")
        out.append("")

    # -- limits -----------------------------------------------------------
    unreachable = sorted(k for k, v in ctx.source_status.items() if not v.get("reachable"))
    out += ["## Limits of this run", ""]
    if unreachable:
        out += [f"Unreachable sources: {', '.join(unreachable)}. Consequences:", "",
                "- no citation-graph expansion (`reference` / `citation` directions stay pending in "
                "`frontier.jsonl`; a later run with network access expands exactly those nodes and "
                "nothing else);",
                "- no citation counts, so the `cites_norm` component is computed from how many "
                "independent bibliographies list a work rather than from a citation count - the "
                "substitution is recorded per record in `score.components_source`;",
                "- OA PDFs could not be downloaded, so most annotations are grounded on abstracts "
                "rather than full text, and most chunks are abstract chunks. Every entry is still "
                "in `05-fetch-manifest.csv` with a resolvable URL, so the PDFs can be fetched "
                "elsewhere and `python -m argmine extract chunk` picks them up without re-running "
                "anything else.", ""]
    else:
        out += ["All configured sources were reachable.", ""]
    out += ["## Reproducing this run", "",
            "```bash",
            "python -m argmine run            # resume; every phase is idempotent",
            "python -m argmine run --cap 400  # expand: only new work is done",
            "python -m argmine status         # registry / frontier / rejection counts",
            "```", ""]
    return "\n".join(out)
