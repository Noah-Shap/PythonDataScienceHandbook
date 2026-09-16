# 04 - RAG preparation

How the retrievable corpus was built, what a chunk carries, and what to do next.

## Chunking

- target ~800 tokens, 100 tokens of overlap, guidelines and READMEs at ~400 tokens because they are rule-dense
- chunks never split a sentence and never merge across sections
- token counts are estimated at 1.3 tokens per word; no tokenizer is a dependency of this pipeline

## What was produced

- 100 chunks over 139 records
- 0 chunks from extracted full text, 8 from guidelines/READMEs, 92 from abstracts where no full text was available
- token histogram: 0-199: 57, 200-399: 42, 400-599: 1

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

## Recommended retrieval filters

| Filter | Values in this corpus | Use it to |
|---|---|---|
| `tier` | unrecorded: 111, 2: 72, 3: 41, 4: 14, 1: 12 | T1/T2 to ground claims about the field, T3 for schema decisions, T4 for current practice |
| `area` | mining: 125, resources: 71, quality: 57, formal: 54, llm: 53, dialogue: 40 | keep an answer inside one area's literature; `dialogue` is the one upstream of a transcript database |
| `doc_type` | conference: 119, workshop: 87, journal: 38, chapter: 3, book: 2, preprint: 1 | separate a dataset or guideline from a method paper - ask a schema question of `dataset`/`guideline`/`tool` only |
| `downstream_tags` | dialogue, quality, schemes, formal, extraction, dataset, fallacy | `dialogue` and `schemes` are the two that matter most for a transcript database |
| `source_text` | fulltext, guideline, abstract | exclude `abstract` chunks when an answer needs paper-internal detail |
| `year` | per record | the LLM-era area moves fast enough that recency is a real filter |

## The index.py interface

```python
class EmbeddingBackend(Protocol):
    name: str
    dim: int

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Return one vector per input text, in order."""

def register(backend: EmbeddingBackend) -> None: ...   # make a backend available
def get(name: str) -> EmbeddingBackend | None: ...     # look one up by name
def iter_chunks(path: Path) -> Iterable[dict]: ...     # stream corpus/chunks.jsonl
def build(cfg, log=print) -> dict: ...                 # no-op while backend is 'none'
```

`build()` refuses to run rather than guessing: with `index.backend` set to a name that nothing has registered it raises, and with `none` it returns `{'status': 'skipped'}`. Adding a backend touches no other module.
