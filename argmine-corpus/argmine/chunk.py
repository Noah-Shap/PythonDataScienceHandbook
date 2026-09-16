"""Phase 6 - chunk.

Section-aware chunking for RAG ingestion: target ~800 tokens with 100 tokens of overlap,
never splitting mid-sentence and never merging across sections. Guidelines and READMEs
are chunked at ~400 tokens because they are rule-dense and a retriever should be able to
return a single rule.

Every entry contributes at least its abstract, so the retrievable corpus covers the whole
bibliography rather than only the entries whose PDF this environment could fetch. Each
chunk records whether it came from full text or from the abstract.

Embedding and indexing are out of scope for this run; ``argmine/index.py`` is the hook.
"""
from __future__ import annotations

import json

from .cache import advance
from .util import approx_tokens, iso_now, safe_id, sentences

SKIP_SECTIONS = {"references"}


def chunk_text(text: str, target: int, overlap: int, tokens_per_word: float) -> list[str]:
    """Greedy sentence packing with a sentence-aligned overlap tail."""
    sents = sentences(text)
    if not sents:
        return []
    chunks, current, current_tokens = [], [], 0.0
    for sent in sents:
        n = len(sent.split()) * tokens_per_word      # float: per-sentence rounding would drift
        if current and current_tokens + n > target:
            chunks.append(" ".join(current))
            tail, tail_tokens = [], 0.0
            for prev in reversed(current):
                t = len(prev.split()) * tokens_per_word
                if tail_tokens + t > overlap:
                    break
                tail.insert(0, prev)
                tail_tokens += t
            current, current_tokens = tail, tail_tokens
        current.append(sent)
        current_tokens += n
    if current:
        chunks.append(" ".join(current))
    return [c for c in chunks if c.strip()]


def _load_text_file(path) -> tuple[list[dict], dict, dict]:
    pages, sections, meta = [], {}, {}
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            if "_meta" in row:
                meta = row["_meta"]
            elif "sections" in row:
                sections = row["sections"]
            elif "references" in row:
                continue
            else:
                pages.append(row)
    return pages, sections, meta


def run(ctx) -> dict:
    cfg, reg = ctx.cfg, ctx.registry
    spec = cfg["chunking"]
    tpw = float(spec.get("tokens_per_word", 1.3))
    out_path = cfg.corpus / "chunks.jsonl"
    summary = {"records": 0, "chunks": 0, "from_fulltext": 0, "from_abstract": 0,
               "from_guideline": 0, "histogram": {}, "no_text_no_abstract": 0}

    rows = []
    for rec in sorted(reg.records.values(), key=lambda r: r["id"]):
        if rec.get("status") not in ("extracted", "chunked"):
            continue
        summary["records"] += 1
        base = {
            "id": rec["id"], "title": rec.get("title", ""), "year": rec.get("year"),
            "tier": rec.get("tier"), "area": rec.get("area", []),
            "downstream_tags": rec.get("downstream_tags", []),
            "doc_type": rec.get("doc_type", ""), "venue": rec.get("venue", ""),
        }
        produced = 0

        for text_rel, origin in _text_files(rec):
            path = cfg.path(text_rel)
            if not path.exists():
                continue
            guideline = origin.startswith("guideline")
            target = int(spec["guideline_target_tokens"] if guideline else spec["target_tokens"])
            pages, sections, _meta = _load_text_file(path)
            if not sections and pages:
                sections = {"body": {"text": "\n".join(p.get("text", "") for p in pages),
                                     "page_start": pages[0].get("page", 1),
                                     "page_end": pages[-1].get("page", 1)}}
            for name, sec in sections.items():
                if name in SKIP_SECTIONS:
                    continue
                body = sec["text"] if isinstance(sec, dict) else str(sec)
                page_start = sec.get("page_start") if isinstance(sec, dict) else None
                page_end = sec.get("page_end") if isinstance(sec, dict) else None
                for i, piece in enumerate(chunk_text(body, target,
                                                     int(spec["overlap_tokens"]), tpw)):
                    tokens = approx_tokens(piece, tpw)
                    rows.append({**base, "chunk_id": f"{safe_id(rec['id'])}:{origin}:{name}:{i}",
                                 "section": name, "page_start": page_start, "page_end": page_end,
                                 "source_text": "guideline" if guideline else "fulltext",
                                 "origin": origin, "tokens": tokens, "text": piece})
                    produced += 1
                    summary["from_guideline" if guideline else "from_fulltext"] += 1
                    _bucket(summary["histogram"], tokens)

        if produced == 0:
            abstract = (rec.get("abstract") or "").strip()
            if not abstract:
                summary["no_text_no_abstract"] += 1
            else:
                for i, piece in enumerate(chunk_text(abstract, int(spec["target_tokens"]),
                                                     int(spec["overlap_tokens"]), tpw)):
                    tokens = approx_tokens(piece, tpw)
                    rows.append({**base, "chunk_id": f"{safe_id(rec['id'])}:abstract:{i}",
                                 "section": "abstract", "page_start": None, "page_end": None,
                                 "source_text": "abstract", "origin": "abstract",
                                 "tokens": tokens, "text": piece})
                    produced += 1
                    summary["from_abstract"] += 1
                    _bucket(summary["histogram"], tokens)

        if produced:
            advance(rec, "chunked")
            rec["files"]["chunks"] = produced
            rec["updated_at"] = iso_now()

    if not ctx.dry_run:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    summary["chunks"] = len(rows)
    summary["output"] = str(out_path.relative_to(cfg.root))
    return summary


def _text_files(rec: dict):
    files = rec.get("files", {})
    if files.get("text"):
        yield files["text"], "pdf"
    for g in files.get("guideline_text", []):
        yield g, f"guideline:{g.rsplit('__', 1)[-1]}"


def _bucket(hist: dict, tokens: int) -> None:
    lo = (tokens // 200) * 200
    key = f"{lo}-{lo + 199}"
    hist[key] = hist.get(key, 0) + 1


def paragraph(summary: dict) -> str:
    hist = ", ".join(f"{k}: {v}" for k, v in sorted(summary.get("histogram", {}).items(),
                                                    key=lambda kv: int(kv[0].split("-")[0])))
    return (f"Phase chunk: wrote {summary.get('chunks', 0)} chunks for "
            f"{summary.get('records', 0)} records to {summary.get('output')} "
            f"({summary.get('from_fulltext', 0)} from full text, "
            f"{summary.get('from_guideline', 0)} from guidelines/READMEs, "
            f"{summary.get('from_abstract', 0)} from abstracts where no full text was "
            f"available). Token histogram: {hist or 'empty'}. "
            f"{summary.get('no_text_no_abstract', 0)} records had neither full text nor an "
            f"abstract to chunk.")
