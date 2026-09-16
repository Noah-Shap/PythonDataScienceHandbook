"""python -m argmine <phase> [--cap N] [--retier] [--dry-run]

Every phase is idempotent, is a pure function of record ``status``, ends with a git
commit and prints a one-paragraph summary. ``run`` executes all of them in order.
"""
from __future__ import annotations

import argparse
import importlib
import sys
import time

from . import config, gitops
from .context import Context

PHASES = ["scaffold", "seed", "snowball", "verify", "tier", "fetch", "extract", "chunk", "deliver"]
COMMIT_MESSAGE = {
    "scaffold": "argmine: phase 0 scaffold - layout, config, field map",
    "seed": "argmine: phase 1 seed - resolve seed hypotheses against sources",
    "snowball": "argmine: phase 2 snowball - expand frontier, score and admit candidates",
    "verify": "argmine: phase 3 verify - two-source agreement and OA resolution",
    "tier": "argmine: phase 4 tier - tier rubric and downstream tags",
    "fetch": "argmine: phase 5a fetch - OA PDFs, repos, fetch manifest",
    "extract": "argmine: phase 5b extract - text, sections, references",
    "chunk": "argmine: phase 6 chunk - section-aware RAG chunks",
    "deliver": "argmine: phase 7 deliver - regenerate deliverables",
}


def summarise(phase: str, summary: dict) -> str:
    """One paragraph, no tables: what this phase did to the corpus."""
    mod = importlib.import_module(f".{phase}", __package__)
    if hasattr(mod, "paragraph"):
        return mod.paragraph(summary)
    bits = []
    for k, v in summary.items():
        if isinstance(v, list):
            bits.append(f"{k}={len(v)}")
        elif isinstance(v, dict):
            bits.append(f"{k}={{{', '.join(f'{a}: {b}' for a, b in list(v.items())[:6])}}}")
        else:
            bits.append(f"{k}={v}")
    return f"Phase {phase}: " + ", ".join(bits) + "."


def commit_counts(phase: str, summary: dict, ctx) -> str:
    """The counts that belong in the commit message for this phase."""
    reg = ctx.registry
    keys = {
        "scaffold": ["sources_reachable", "sources_unreachable"],
        "seed": ["seeds", "verified", "unverified", "rejected", "corrections"],
        "snowball": ["pool", "excluded", "scored", "promoted", "admitted", "below_cutoff"],
        "verify": ["considered", "verified", "unverified", "oa_resolved"],
        "tier": ["tiered", "retiered", "scope_uncertain"],
        "fetch": ["repos_linked", "pdfs_fetched", "pdfs_unavailable", "repos_cloned", "guidelines"],
        "extract": ["pdfs_extracted", "guidelines_extracted", "no_pdf"],
        "chunk": ["records", "chunks", "from_fulltext", "from_abstract"],
        "deliver": [],
    }.get(phase, [])
    bits = [f"{k}={summary[k] if not isinstance(summary.get(k), list) else len(summary[k])}"
            for k in keys if k in summary]
    bits.append(f"registry={len(reg.records)}/{ctx.cfg.cap}")
    bits.append(f"verified={len(reg.verified())}")
    return ", ".join(bits)


def run_phase(phase: str, ctx, commit: bool = True) -> dict:
    ctx.log(f"\n== {phase} ==")
    started = time.time()
    mod = importlib.import_module(f".{phase}", __package__)
    summary = mod.run(ctx)
    summary["seconds"] = round(time.time() - started, 1)
    summary["http"] = dict(ctx.http.calls)
    ctx.save()
    if not ctx.dry_run:
        ctx.log_phase(phase, summary)
    ctx.log(summarise(phase, summary))
    if len(ctx.registry.records) > ctx.cfg.cap:
        # Section 9: if a phase would exceed the cap, stop and ask.
        ctx.log(f"\nSTOP: phase {phase} left the registry at {len(ctx.registry.records)} "
                f"entries, over the cap of {ctx.cfg.cap}. Nothing has been committed. Re-run "
                f"with an explicit --cap once that increase has been agreed.")
        raise SystemExit(2)
    if commit and not ctx.dry_run and ctx.cfg["run"].get("git_commit_each_phase", True):
        message = f"{COMMIT_MESSAGE.get(phase, f'argmine: {phase}')}\n\n" \
                  f"{commit_counts(phase, summary, ctx)}"
        gitops.commit(ctx.cfg, message, paths=["."], log=ctx.log)
    return summary


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="python -m argmine", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("phase", choices=PHASES + ["run", "report", "status"])
    p.add_argument("--cap", type=int, help="override run.cap for this invocation")
    p.add_argument("--retier", action="store_true",
                   help="recompute tiers for records that already have one")
    p.add_argument("--dry-run", action="store_true",
                   help="do everything except writing the registry, deliverables and commits")
    p.add_argument("--offline", action="store_true", help="make no network calls at all")
    p.add_argument("--no-commit", action="store_true", help="skip the per-phase git commit")
    p.add_argument("--force-index", action="store_true",
                   help="rebuild the local ACL Anthology and BibTeX indexes")
    p.add_argument("--limit", type=int, default=0, help="cap work per phase (debugging)")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    cfg = config.load()
    if args.cap:
        cfg["run"]["cap"] = args.cap
    ctx = Context(cfg, args)

    if args.phase == "status":
        reg = ctx.registry
        print(f"registry: {len(reg.records)} records  {reg.counts()}")
        print(f"areas:    {reg.area_counts()}")
        print(f"frontier: {len(reg.frontier)} nodes, "
              f"{sum(1 for n in reg.frontier.values() if n['expanded'])} expanded")
        print(f"rejected: {len(reg.rejected)}")
        return 0

    if args.phase == "report":
        from . import report
        print(report.render(ctx))
        return 0

    phases = PHASES if args.phase == "run" else [args.phase]
    for phase in phases:
        run_phase(phase, ctx, commit=not args.no_commit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
