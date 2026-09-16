# 04 - RAG preparation

How the retrievable corpus was built, what a chunk carries, and what to do next.

## Chunking

- target ~800 tokens, 100 tokens of overlap, guidelines and READMEs at ~400 tokens because they are rule-dense
- chunks never split a sentence and never merge across sections
- token counts are estimated at 1.3 tokens per word; no tokenizer is a dependency of this pipeline

## What was produced

- 121 chunks over 126 records
- 0 chunks from extracted full text, 38 from guidelines/READMEs, 83 from abstracts where no full text was available
- token histogram: 0-199: 53, 200-399: 67, 400-599: 1

## Chunk metadata

```json
{
  "id": "doi:10.1162/coli_a_00364",
  "title": "...",
  "year": 2019,
  "tier": 1,
  "area": [
    "mining"
  ],
  "downstream_tags": [
    "extraction"
  ],
  "section": "introduction",
  "page_start": 3,
  "page_end": 4,
  "doc_type": "journal",
  "venue": "...",
  "source_text": "fulltext|guideline|abstract",
  "origin": "pdf",
  "chunk_id": "...",
  "tokens": 812,
  "text": "..."
}
```

`source_text` is the honesty field: a chunk marked `abstract` is all that could be retrieved for that entry, so an answer built on it should not claim to cite the paper's body. `page_start`/`page_end` are present for full-text chunks precisely so a generated answer can cite a page.

## Ingestion

```python
from argmine import config, index
cfg = config.load()
for chunk in index.iter_chunks(cfg.corpus / 'chunks.jsonl'):
    ...  # embed chunk['text'], store the rest as metadata
```

Embedding and indexing are out of scope for this run. `argmine/index.py` holds the hook: implement `EmbeddingBackend`, `register()` it, set `index.backend` in config.yaml, and nothing else in the pipeline changes.

## Retrieval filters worth having

- `tier` - T1/T2 for grounding claims about the field, T3 for schema decisions, T4 for current practice
- `downstream_tags` - `dialogue` and `schemes` are the two that matter most for a transcript database
- `source_text` - exclude `abstract` chunks when an answer needs paper-internal detail
- `year` - the LLM-era area moves fast enough that recency is a real filter
