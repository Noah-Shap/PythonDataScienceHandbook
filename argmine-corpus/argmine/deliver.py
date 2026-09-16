"""Phase 7 - deliver.

Regenerates every deliverable from the registry on each run (they are cheap), including
a changelog of what changed since the previous run. Nothing here reaches outside the
registry: if a fact is not in a record, it does not appear in a deliverable.
"""
from __future__ import annotations

import json
import re

from . import annotate, fieldmap, report
from .util import iso_now, norm_text, truncate

BIB_TYPE = {"journal": "article", "conference": "inproceedings", "workshop": "inproceedings",
            "book": "book", "chapter": "incollection", "thesis": "phdthesis",
            "preprint": "misc", "guideline": "misc", "dataset": "misc", "tool": "misc"}

SIZE_RE = re.compile(
    r"(\d[\d,\.]*)\s+(essays|utterances|arguments|argument pairs|documents|sentences|posts|"
    r"comments|threads|pairs|claims|debates|words|tokens|dialogues|episodes|articles|"
    r"instances|samples|annotations|topics|reviews|discussions|texts)", re.IGNORECASE)
UNIT_RE = re.compile(r"annotat\w*\s+(?:at\s+the\s+)?(\w+)[- ]level", re.IGNORECASE)
SCHEME_MARKERS = [
    ("Inference Anchoring Theory", ("inference anchoring theory", "iat")),
    ("Argument Interchange Format", ("argument interchange format", "aif")),
    ("Walton argumentation schemes", ("argumentation scheme", "walton")),
    ("claim / premise components", ("claim", "premise", "major claim")),
    ("support / attack relations", ("support", "attack", "rebuttal")),
    ("quality dimensions", ("quality dimension", "cogency", "convincing", "sufficiency")),
    ("stance", ("stance", "pro and con", "for and against")),
    ("fallacy types", ("fallac",)),
]


# -- helpers ---------------------------------------------------------------
def citation(rec: dict) -> str:
    authors = [a for a in rec.get("authors", []) if a and a.strip()]
    if len(authors) > 4:
        who = f"{authors[0]} et al."
    elif authors:
        who = ", ".join(authors[:-1]) + (" and " + authors[-1] if len(authors) > 1 else "")
    else:
        who = "[authors not recorded]"
    year = rec.get("year") or "n.d."
    venue = rec.get("venue") or "[venue not recorded]"
    return f"{who} ({year}). *{rec.get('title', '')}*. {venue}."


def bibtex(rec: dict) -> str:
    etype = BIB_TYPE.get(rec.get("doc_type", ""), "misc")
    surname = (rec.get("authors") or ["anon"])[0].split()[-1].lower()
    surname = re.sub(r"[^a-z]", "", surname) or "anon"
    key = f"{surname}{rec.get('year') or 'nd'}{re.sub(r'[^a-z]', '', norm_text(rec.get('title', ''))[:10])}"
    lines = [f"@{etype}{{{key},"]
    lines.append(f"  title = {{{rec.get('title', '')}}},")
    if rec.get("authors"):
        lines.append("  author = {" + " and ".join(rec["authors"]) + "},")
    if rec.get("year"):
        lines.append(f"  year = {{{rec['year']}}},")
    if rec.get("venue"):
        field = "journal" if etype == "article" else ("booktitle" if etype == "inproceedings" else "publisher")
        lines.append(f"  {field} = {{{rec['venue']}}},")
    doi = next((a.split(":", 1)[1] for a in [rec["id"]] + rec.get("aliases", []) if a.startswith("doi:")), "")
    if doi:
        lines.append(f"  doi = {{{doi}}},")
    url = rec.get("urls", {}).get("landing") or rec.get("urls", {}).get("acl", "")
    if url:
        lines.append(f"  url = {{{url}}},")
    lines.append("}")
    return "\n".join(lines)


def primary_area(rec: dict) -> str:
    raw = (rec.get("score") or {}).get("area_raw") or {}
    areas = rec.get("area") or []
    if raw:
        best = max(raw, key=lambda a: raw[a])
        if best in areas or not areas:
            return best
    return areas[0] if areas else "unassigned"


def retrieved_text(cfg, rec: dict) -> str:
    text, _ = annotate.grounding(cfg, rec)
    return text or (rec.get("abstract") or "")


def resource_facts(cfg, rec: dict) -> dict:
    """Facts about a resource, taken only from text this pipeline retrieved."""
    text = retrieved_text(cfg, rec)
    sizes = ["{} {}".format(m.group(1), m.group(2).lower()) for m in SIZE_RE.finditer(text)][:2]
    unit = UNIT_RE.search(text)
    low = norm_text(text)
    schemes = [name for name, markers in SCHEME_MARKERS if sum(m in low for m in markers) >= 2
               or (len(markers) == 1 and markers[0] in low)]
    files = rec.get("files", {})
    return {
        "size": "; ".join(sizes) or "not stated in retrieved text",
        "unit": (unit.group(1).lower() + "-level") if unit else "not stated in retrieved text",
        "scheme": "; ".join(schemes[:3]) or "not stated in retrieved text",
        "licence": files.get("repo_licence", "") or "not retrieved",
        "guideline": "yes" if files.get("guideline_text") else
                     ("README only" if files.get("guidelines") else "no"),
    }


def changelog(ctx) -> dict:
    """What changed since the previous run, from corpus/run_log.jsonl."""
    rows = ctx.run_log()
    if not rows:
        return {"added": [], "runs": 0, "since": ""}
    runs, current = [], []
    last_phase = None
    for row in rows:
        if last_phase is not None and row["phase"] == "scaffold":
            runs.append(current)
            current = []
        current.append(row)
        last_phase = row["phase"]
    runs.append(current)
    added = []
    for row in runs[-1]:
        added.extend(row.get("summary", {}).get("added_ids", []))
    return {"added": sorted(set(added)), "runs": len(runs),
            "since": runs[-2][0]["at"] if len(runs) > 1 else runs[0][0]["at"]}


# -- documents -------------------------------------------------------------
def bibliography(ctx, changes: dict) -> str:
    cfg, reg = ctx.cfg, ctx.registry
    verified = [r for r in reg.records.values()
                if r.get("verification", {}).get("status") == "verified"]
    out = ["# 01 - Annotated bibliography", "",
           f"{len(verified)} verified entries, grouped by area and then by tier. Every entry here "
           f"agreed across at least two independent metadata sources; anything that did not is in "
           f"`99-unverified-and-rejected.md`. Each annotation says which retrieved text it was "
           f"written from (`grounded_on`), and quotes that text rather than paraphrasing it from "
           f"outside knowledge.", "",
           f"Generated {iso_now()} | criteria_version {cfg.criteria_version} | cap {cfg.cap}", ""]
    if changes["added"]:
        out += [f"**Added in the latest run ({len(changes['added'])}):** "
                + ", ".join(f"`{i}`" for i in changes["added"][:40])
                + (" ..." if len(changes["added"]) > 40 else ""), ""]

    by_area: dict[str, list] = {}
    for rec in verified:
        by_area.setdefault(primary_area(rec), []).append(rec)

    for area, spec in cfg["areas"].items():
        recs = by_area.get(area, [])
        out.append(f"## {spec['number']} {spec['name']} ({len(recs)} entries, quota "
                   f"{cfg.area_quota(area)})")
        out.append("")
        if not recs:
            out.append("_No verified entries in this area._\n")
            continue
        for tier in (1, 2, 3, 4):
            tier_recs = sorted([r for r in recs if r.get("tier") == tier],
                               key=lambda r: (-(r.get("year") or 0), r.get("title", "")))
            if not tier_recs:
                continue
            out.append(f"### T{tier} - {cfg['tiers'][f't{tier}']}")
            out.append("")
            for rec in tier_recs:
                out.extend(entry_block(cfg, rec))
    for area in sorted(set(by_area) - set(cfg["areas"])):
        out.append(f"## Unassigned area ({len(by_area[area])} entries)\n")
        for rec in by_area[area]:
            out.extend(entry_block(cfg, rec))
    return "\n".join(out)


def entry_block(cfg, rec: dict) -> list[str]:
    urls = rec.get("urls", {})
    ann = rec.get("annotation", {})
    also = [a for a in rec.get("area", []) if a != primary_area(rec)]
    lines = [f"#### {citation(rec)}", ""]
    meta = [f"`{rec['id']}`"]
    if rec.get("aliases"):
        meta.append("aliases: " + ", ".join(f"`{a}`" for a in rec["aliases"][:6]))
    lines.append("- " + " | ".join(meta))
    lines.append(f"- doc_type: `{rec.get('doc_type') or 'unrecorded'}` | tier: T{rec.get('tier')} "
                 f"| tags: {', '.join(rec.get('downstream_tags', [])) or 'none'}"
                 + (f" | also in: {', '.join(also)}" if also else ""))
    link_bits = []
    if urls.get("landing"):
        link_bits.append(f"[landing]({urls['landing']})")
    if urls.get("pdf_oa"):
        link_bits.append(f"[OA PDF]({urls['pdf_oa']})"
                         + (f" (via {urls['pdf_oa_source']})" if urls.get("pdf_oa_source") else ""))
    if urls.get("repo"):
        link_bits.append(f"[repo]({urls['repo']})")
    lines.append("- " + (" | ".join(link_bits) if link_bits else "no URL recorded"))
    ver = rec.get("verification", {})
    lines.append(f"- verified against: {', '.join(ver.get('sources', [])) or 'none'}"
                 + (f" | note: {truncate(ver.get('notes', ''), 200)}" if ver.get("notes") else ""))
    score = rec.get("score", {})
    if score:
        comp = score.get("components", {})
        lines.append(f"- score {score.get('total')} (cites {comp.get('cites_norm')}, "
                     f"cocite {comp.get('cocite')}, keyword {comp.get('keyword')}, "
                     f"venue {comp.get('venue')})")
    lines.append(f"- annotation (`grounded_on: {ann.get('grounded_on', 'none')}`): "
                 f"{ann.get('text', '')}")
    lines.append("")
    lines.append("<details><summary>BibTeX</summary>")
    lines.append("")
    lines.append("```bibtex")
    lines.append(bibtex(rec))
    lines.append("```")
    lines.append("")
    lines.append("</details>")
    lines.append("")
    return lines


def datasets_and_tools(ctx) -> str:
    cfg, reg = ctx.cfg, ctx.registry
    recs = [r for r in reg.records.values()
            if r.get("verification", {}).get("status") == "verified"
            and (r.get("tier") == 3 or "dataset" in r.get("downstream_tags", []))]
    recs.sort(key=lambda r: (-(r.get("year") or 0), r.get("title", "")))
    out = ["# 02 - Datasets, tools and annotation guidelines", "",
           f"{len(recs)} resource entries. Every column is filled from text this pipeline "
           f"retrieved (abstract or full text) or from a cloned repository; where the retrieved "
           f"text does not state something, the cell says so rather than guessing.", "",
           "| Resource | Paper id | Repo | Licence | Size (as stated) | Unit of annotation | "
           "Annotation scheme | Guideline retrieved |",
           "|---|---|---|---|---|---|---|---|"]
    for rec in recs:
        f = resource_facts(cfg, rec)
        repo = rec.get("urls", {}).get("repo", "")
        repo_cell = f"[{repo.split('github.com/')[-1]}]({repo})" if repo else "none linked"
        out.append(f"| {truncate(rec.get('title', ''), 80)} | `{rec['id']}` | {repo_cell} | "
                   f"{f['licence']} | {f['size']} | {f['unit']} | {f['scheme']} | {f['guideline']} |")
    out.append("")
    out.append("## Guideline documents retrieved")
    out.append("")
    any_g = False
    for rec in recs:
        for g in rec.get("files", {}).get("guidelines", []):
            any_g = True
            out.append(f"- `{g}` - from {rec['id']} ({truncate(rec.get('title', ''), 70)})")
    if not any_g:
        out.append("_No guideline document could be retrieved in this run; "
                   "see `06-run-report.md` for why._")
    out.append("")
    return "\n".join(out)


def reading_order(ctx) -> str:
    cfg, reg = ctx.cfg, ctx.registry
    verified = [r for r in reg.records.values()
                if r.get("verification", {}).get("status") == "verified"]

    def pick(area=None, tiers=(1,), tag=None, limit=12):
        out = []
        for r in sorted(verified, key=lambda r: (r.get("tier") or 9, -(r.get("year") or 0))):
            if r.get("tier") not in tiers:
                continue
            if area and primary_area(r) != area and area not in r.get("area", []):
                continue
            if tag and tag not in r.get("downstream_tags", []):
                continue
            out.append(r)
            if len(out) >= limit:
                break
        return out

    stages = [
        ("Stage 1 - orient", "Surveys and field maps. Read these first; they give the vocabulary "
         "the rest of the corpus assumes.", pick(tiers=(1,), limit=10)),
        ("Stage 2 - representation", "What an argument *is* formally, and how a stored argument "
         "can be typed and scored.", pick(area="formal", tiers=(1, 2), limit=12)),
        ("Stage 3 - dialogue structure", "The layer closest to a debate transcript: who said "
         "what, in reply to what, with what dialogical force.", pick(area="dialogue", tiers=(1, 2, 3), limit=14)),
        ("Stage 4 - extraction", "How text becomes components and relations.",
         pick(area="mining", tiers=(2,), limit=14)),
        ("Stage 5 - quality", "How a stored argument's strength can be measured, and how it fails.",
         pick(area="quality", tiers=(1, 2), limit=12)),
        ("Stage 6 - resources", "Corpora, tools and the annotation guidelines behind them - the "
         "schema decisions have mostly been made before, here.", pick(tiers=(3,), limit=18)),
        ("Stage 7 - current practice", "2023-2026 work. Lower durability, highest relevance to "
         "build decisions being taken now.", pick(tiers=(4,), limit=16)),
    ]
    out = ["# 03 - Reading order", "",
           "Ordered for one purpose: building a database that stores arguments extracted from "
           "debate transcripts, with their reply structure, inferential and conflict relations, "
           "and strength. Within a stage, read top to bottom.", ""]
    seen = set()
    for title, why, recs in stages:
        out.append(f"## {title}")
        out.append("")
        out.append(why)
        out.append("")
        if not recs:
            out.append("_Nothing in the corpus for this stage yet._\n")
            continue
        for rec in recs:
            mark = " (already listed above)" if rec["id"] in seen else ""
            seen.add(rec["id"])
            rel = annotate.relevance_clause(rec)
            out.append(f"1. **{truncate(rec.get('title', ''), 90)}** ({rec.get('year')}, "
                       f"T{rec.get('tier')}, `{rec['id']}`){mark} - {rel}")
        out.append("")
    return "\n".join(out)


def rag_prep(ctx, chunk_summary: dict) -> str:
    cfg, reg = ctx.cfg, ctx.registry
    spec = cfg["chunking"]
    hist = chunk_summary.get("histogram", {})
    out = ["# 04 - RAG preparation", "",
           "How the retrievable corpus was built, what a chunk carries, and what to do next.", "",
           "## Chunking", "",
           f"- target ~{spec['target_tokens']} tokens, {spec['overlap_tokens']} tokens of overlap, "
           f"guidelines and READMEs at ~{spec['guideline_target_tokens']} tokens because they are "
           f"rule-dense",
           "- chunks never split a sentence and never merge across sections",
           f"- token counts are estimated at {spec['tokens_per_word']} tokens per word; no "
           f"tokenizer is a dependency of this pipeline",
           "",
           "## What was produced", "",
           f"- {chunk_summary.get('chunks', 0)} chunks over {chunk_summary.get('records', 0)} records",
           f"- {chunk_summary.get('from_fulltext', 0)} chunks from extracted full text, "
           f"{chunk_summary.get('from_guideline', 0)} from guidelines/READMEs, "
           f"{chunk_summary.get('from_abstract', 0)} from abstracts where no full text was available",
           f"- token histogram: " + (", ".join(f"{k}: {v}" for k, v in sorted(
               hist.items(), key=lambda kv: int(kv[0].split('-')[0]))) or "empty"),
           "",
           "## Chunk metadata", "",
           "```json",
           json.dumps({"id": "doi:10.1162/coli_a_00364", "title": "...", "year": 2019, "tier": 1,
                       "area": ["mining"], "downstream_tags": ["extraction"], "section": "introduction",
                       "page_start": 3, "page_end": 4, "doc_type": "journal", "venue": "...",
                       "source_text": "fulltext|guideline|abstract", "origin": "pdf",
                       "chunk_id": "...", "tokens": 812, "text": "..."}, indent=2),
           "```", "",
           "`source_text` is the honesty field: a chunk marked `abstract` is all that could be "
           "retrieved for that entry, so an answer built on it should not claim to cite the paper's "
           "body. `page_start`/`page_end` are present for full-text chunks precisely so a generated "
           "answer can cite a page.", "",
           "## Ingestion", "",
           "```python",
           "from argmine import config, index",
           "cfg = config.load()",
           "for chunk in index.iter_chunks(cfg.corpus / 'chunks.jsonl'):",
           "    ...  # embed chunk['text'], store the rest as metadata",
           "```", "",
           "Embedding and indexing are out of scope for this run. `argmine/index.py` holds the "
           "hook: implement `EmbeddingBackend`, `register()` it, set `index.backend` in "
           "config.yaml, and nothing else in the pipeline changes.", "",
           "## Retrieval filters worth having", "",
           "- `tier` - T1/T2 for grounding claims about the field, T3 for schema decisions, "
           "T4 for current practice",
           "- `downstream_tags` - `dialogue` and `schemes` are the two that matter most for a "
           "transcript database",
           "- `source_text` - exclude `abstract` chunks when an answer needs paper-internal detail",
           "- `year` - the LLM-era area moves fast enough that recency is a real filter",
           ""]
    return "\n".join(out)


def unverified_and_rejected(ctx) -> str:
    cfg, reg = ctx.cfg, ctx.registry
    unver = [r for r in reg.records.values()
             if r.get("verification", {}).get("status") != "verified"]
    out = ["# 99 - Unverified and rejected", "",
           "Nothing here is part of the bibliography. Unverified entries could not be confirmed "
           "against two independent sources; rejected candidates were scored and not admitted, or "
           "hit an exclusion rule. Both lists are kept so that raising the cap or bumping "
           "`criteria_version` re-decides them without a single new API call.", "",
           f"## Unverified ({len(unver)})", ""]
    if unver:
        out += ["| id | title | year | sources | why |", "|---|---|---|---|---|"]
        for rec in sorted(unver, key=lambda r: r.get("title", "")):
            ver = rec.get("verification", {})
            out.append(f"| `{rec['id']}` | {truncate(rec.get('title', ''), 70)} | "
                       f"{rec.get('year') or ''} | {', '.join(ver.get('sources', [])) or 'none'} | "
                       f"{truncate(ver.get('notes', ''), 120)} |")
    else:
        out.append("_None._")
    out.append("")

    by_reason: dict[str, list] = {}
    for row in reg.rejected.values():
        by_reason.setdefault(row.get("rejection_reason", "?"), []).append(row)
    out.append(f"## Rejected ({len(reg.rejected)})")
    out.append("")
    for reason, rows in sorted(by_reason.items(), key=lambda kv: -len(kv[1])):
        rows.sort(key=lambda r: -(r.get("score", {}) or {}).get("total", 0))
        out.append(f"### `{reason}` ({len(rows)})")
        out.append("")
        if reason == "below_cutoff":
            out.append("Ranked by score: these are the first candidates a higher cap would admit.")
            out.append("")
        out += ["| score | title | year | venue | criteria_version |", "|---|---|---|---|---|"]
        for row in rows[:60]:
            score = (row.get("score") or {}).get("total")
            out.append(f"| {score if score is not None else '-'} | "
                       f"{truncate(row.get('title', ''), 70)} | {row.get('year') or ''} | "
                       f"{truncate(row.get('venue', ''), 40)} | {row.get('criteria_version')} |")
        if len(rows) > 60:
            out.append(f"| ... | _{len(rows) - 60} more in `corpus/rejected.jsonl`_ | | | |")
        out.append("")
    return "\n".join(out)


# -- phase -----------------------------------------------------------------
def run(ctx) -> dict:
    cfg = ctx.cfg
    ann = annotate.annotate_all(ctx)
    changes = changelog(ctx)
    chunk_summary = {}
    for row in reversed(ctx.run_log()):
        if row["phase"] == "chunk":
            chunk_summary = row.get("summary", {})
            break

    written = {}
    docs = {
        "00-field-map.md": fieldmap.render(cfg, ctx.registry, ctx.source_status),
        "01-bibliography.md": bibliography(ctx, changes),
        "02-datasets-and-tools.md": datasets_and_tools(ctx),
        "03-reading-order.md": reading_order(ctx),
        "04-rag-prep.md": rag_prep(ctx, chunk_summary),
        "99-unverified-and-rejected.md": unverified_and_rejected(ctx),
    }
    for name, body in docs.items():
        path = cfg.deliverables / name
        if not ctx.dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
        written[name] = len(body.splitlines())

    report_body = report.render(ctx, changes=changes, annotation=ann)
    if not ctx.dry_run:
        (cfg.deliverables / "06-run-report.md").write_text(report_body, encoding="utf-8")
    written["06-run-report.md"] = len(report_body.splitlines())
    return {"documents": written, "annotations": ann, "changelog": changes}


def paragraph(summary: dict) -> str:
    docs = summary.get("documents", {})
    ann = summary.get("annotations", {})
    ch = summary.get("changelog", {})
    return (f"Phase deliver: regenerated {len(docs)} deliverables from the registry "
            f"({', '.join(f'{k} ({v} lines)' for k, v in list(docs.items())[:3])}, ...). "
            f"Wrote {ann.get('written', 0)} annotations and left {ann.get('unchanged', 0)} "
            f"unchanged; grounding: {ann.get('grounded', {})}. "
            f"The changelog records {len(ch.get('added', []))} entries added in this run "
            f"(run {ch.get('runs', 1)}).")
