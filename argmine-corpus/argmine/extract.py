"""Phase 5b - extract.

Per entry: ``corpus/text/<safe-id>.jsonl`` with one object per page ``{page, text}``,
plus a ``sections`` object (heuristic split on headings) and the references block kept
separately for later cross-checking against the registry. Page numbers are preserved
because a RAG answer about this corpus has to be citable down to the page.

Guideline documents and READMEs copied in phase 5a are extracted the same way, as
documents in their own right (they matter more than the papers describing them when a
downstream annotation schema is being designed).

Idempotency: an entry is skipped when its text file already exists and the PDF hash has
not changed.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from .cache import advance
from .util import iso_now, safe_id

SECTION_PATTERNS = [
    ("abstract", r"^\s*(abstract)\b"),
    ("introduction", r"^\s*(\d+\.?\s*)?(introduction)\b"),
    ("related work", r"^\s*(\d+\.?\s*)?(related work|background|previous work|prior work)\b"),
    ("method", r"^\s*(\d+\.?\s*)?(method|methodology|approach|model|our model|system|framework|architecture)\b"),
    ("data", r"^\s*(\d+\.?\s*)?(data|dataset|corpus|corpora|annotation|materials)\b"),
    ("evaluation", r"^\s*(\d+\.?\s*)?(evaluation|experiments?|results|analysis|discussion)\b"),
    ("conclusion", r"^\s*(\d+\.?\s*)?(conclusions?|future work|summary)\b"),
    ("references", r"^\s*(references|bibliography)\s*$"),
]
COMPILED = [(name, re.compile(pat, re.IGNORECASE)) for name, pat in SECTION_PATTERNS]
HEADING_MAX_WORDS = 9


def split_sections(pages: list[dict]) -> tuple[dict, str]:
    """Heuristic heading split that keeps page spans.

    Returns ({section: {text, page_start, page_end}}, references_block). The page span is
    what makes a RAG answer citable: every chunk can name the pages it came from.
    """
    current = "front matter"
    sections: dict[str, dict] = {}
    refs: list[str] = []
    for page in pages:
        pno = page.get("page", 0)
        for line in (page.get("text") or "").splitlines():
            stripped = line.strip()
            if stripped and len(stripped.split()) <= HEADING_MAX_WORDS:
                for name, rx in COMPILED:
                    if rx.match(stripped):
                        current = name
                        break
            if current == "references":
                refs.append(line)
                continue
            sec = sections.setdefault(current, {"lines": [], "page_start": pno, "page_end": pno})
            sec["lines"].append(line)
            sec["page_end"] = pno
    out = {}
    for name, sec in sections.items():
        text = re.sub(r"\n{3,}", "\n\n", "\n".join(sec["lines"])).strip()
        if text:
            out[name] = {"text": text, "page_start": sec["page_start"], "page_end": sec["page_end"]}
    return out, "\n".join(refs).strip()


def split_reference_entries(block: str) -> list[str]:
    """Split a references block into individual entries, for later registry cross-checks."""
    if not block:
        return []
    lines = [l.rstrip() for l in block.splitlines() if l.strip()]
    entries, current = [], []
    for line in lines:
        starts_entry = bool(re.match(r"^\s*(\[\d+\]|\(\d+\)|[A-Z][A-Za-z'\-]+,\s)", line))
        if starts_entry and current:
            entries.append(" ".join(current).strip())
            current = [line.strip()]
        else:
            current.append(line.strip())
    if current:
        entries.append(" ".join(current).strip())
    return [e for e in entries if len(e) > 25]


def extract_pdf(path: Path) -> list[dict]:
    import pymupdf
    pages = []
    with pymupdf.open(path) as doc:
        for n, page in enumerate(doc, 1):
            pages.append({"page": n, "text": page.get_text("text")})
    return pages


def extract_markdown(path: Path, page_chars: int = 3000) -> list[dict]:
    """Guidelines and READMEs have no pages; paginate them so citations stay uniform."""
    text = path.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)          # images
    text = re.sub(r"<[^>]{1,120}>", " ", text)                  # inline html
    pages, buf, n = [], [], 1
    size = 0
    for para in text.split("\n\n"):
        buf.append(para)
        size += len(para)
        if size >= page_chars:
            pages.append({"page": n, "text": "\n\n".join(buf).strip()})
            buf, size, n = [], 0, n + 1
    if buf:
        pages.append({"page": n, "text": "\n\n".join(buf).strip()})
    return [p for p in pages if p["text"]]


def write_text(cfg, rec_id: str, pages: list[dict], sections: dict, refs: list[str],
               origin: str, suffix: str = "") -> Path:
    path = cfg.corpus / "text" / f"{safe_id(rec_id)}{suffix}.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(json.dumps({"_meta": {"id": rec_id, "origin": origin, "pages": len(pages),
                                       "extracted_at": iso_now()}}, ensure_ascii=False) + "\n")
        for page in pages:
            fh.write(json.dumps(page, ensure_ascii=False) + "\n")
        fh.write(json.dumps({"sections": sections}, ensure_ascii=False) + "\n")
        fh.write(json.dumps({"references": refs}, ensure_ascii=False) + "\n")
    return path


def run(ctx) -> dict:
    cfg, reg = ctx.cfg, ctx.registry
    summary = {"pdfs_extracted": 0, "skipped_unchanged": 0, "no_pdf": 0, "failures": [],
               "guidelines_extracted": 0, "pages": 0, "reference_entries": 0}

    for rec in [r for r in reg.records.values() if r.get("status") in ("fetched", "extracted")]:
        files = rec.setdefault("files", {})
        pdf_rel = files.get("pdf")
        text_rel = files.get("text")
        if pdf_rel and text_rel and cfg.path(text_rel).exists() \
                and files.get("text_pdf_sha256") == files.get("pdf_sha256"):
            summary["skipped_unchanged"] += 1                # layer 2: nothing changed
        elif pdf_rel and cfg.path(pdf_rel).exists():
            try:
                pages = extract_pdf(cfg.path(pdf_rel))
                sections, refs_block = split_sections(pages)
                refs = split_reference_entries(refs_block)
                path = write_text(cfg, rec["id"], pages, sections, refs, origin="pdf")
                files["text"] = str(path.relative_to(cfg.root))
                files["text_pdf_sha256"] = files.get("pdf_sha256", "")
                files["pages"] = len(pages)
                summary["pdfs_extracted"] += 1
                summary["pages"] += len(pages)
                summary["reference_entries"] += len(refs)
            except Exception as exc:
                summary["failures"].append({"id": rec["id"], "error": str(exc)[:200]})
        else:
            summary["no_pdf"] += 1

        for guideline in files.get("guidelines", []):
            gpath = cfg.path(guideline)
            if not gpath.exists() or gpath.suffix.lower() not in (".md", ".txt", ".rst"):
                continue
            key = f"__{gpath.stem.split('__', 1)[-1]}"
            out = cfg.corpus / "text" / f"{safe_id(rec['id'])}{key}.jsonl"
            if out.exists():
                continue
            pages = extract_markdown(gpath)
            if not pages:
                continue
            sections, refs_block = split_sections(pages)
            write_text(cfg, rec["id"], pages, sections, split_reference_entries(refs_block),
                       origin=f"guideline:{gpath.name}", suffix=key)
            files.setdefault("guideline_text", []).append(str(out.relative_to(cfg.root)))
            summary["guidelines_extracted"] += 1

        rec["updated_at"] = iso_now()
        advance(rec, "extracted")
    return summary


def paragraph(summary: dict) -> str:
    return (f"Phase extract: extracted {summary.get('pdfs_extracted', 0)} PDFs to per-page "
            f"JSONL ({summary.get('pages', 0)} pages, {summary.get('reference_entries', 0)} "
            f"reference entries kept for cross-checking), skipped "
            f"{summary.get('skipped_unchanged', 0)} whose PDF hash was unchanged, and "
            f"extracted {summary.get('guidelines_extracted', 0)} guideline/README documents. "
            f"{summary.get('no_pdf', 0)} entries had no local PDF to extract; "
            f"{len(summary.get('failures', []))} extractions failed.")
