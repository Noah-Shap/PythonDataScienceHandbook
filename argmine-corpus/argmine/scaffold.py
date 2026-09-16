"""Phase 0 - scaffold.

Creates the layout, validates config.yaml and writes the coverage contract
(deliverables/00-field-map.md) *before any searching happens*.
"""
from __future__ import annotations

from . import fieldmap

DIRS = ["corpus", "corpus/pdfs", "corpus/text", "corpus/text/guidelines", "corpus/repos",
        "deliverables", "argmine/sources"]

README_STUB = """# argmine-corpus

Run `python -m argmine run` to build the corpus. See `deliverables/00-field-map.md` for
the coverage contract and `deliverables/06-run-report.md` for what the last run did.
"""


def run(ctx) -> dict:
    cfg = ctx.cfg
    made = []
    for d in DIRS:
        p = cfg.path(d)
        if not p.exists():
            p.mkdir(parents=True, exist_ok=True)
            made.append(d)
    for empty in ("registry.jsonl", "frontier.jsonl", "rejected.jsonl"):
        p = cfg.corpus / empty
        if not p.exists():
            p.touch()
            made.append(f"corpus/{empty}")
    readme = cfg.path("README.md")
    if not readme.exists():
        readme.write_text(README_STUB)
        made.append("README.md")

    status = ctx.probe_sources()
    path = cfg.deliverables / "00-field-map.md"
    path.write_text(fieldmap.render(cfg, ctx.registry, ctx.source_status))
    reachable = sorted(k for k, v in status.items() if v.get("reachable"))
    unreachable = sorted(k for k, v in status.items() if not v.get("reachable"))
    return {"created": made, "field_map": str(path.relative_to(cfg.root)),
            "sources_reachable": reachable, "sources_unreachable": unreachable,
            "areas": list(cfg["areas"]), "cap": cfg.cap}
