"""Embedding / vector-index hook. Deliberately not implemented in this run.

The brief puts embedding and indexing out of scope, but the seam belongs in the pipeline
now so adding it later touches nothing else. Implement :class:`EmbeddingBackend` for the
backend of your choice, register it, and run ``python -m argmine index`` (add the phase
to ``cli.PHASES``) - the chunk format in ``corpus/chunks.jsonl`` is the contract.

    class MyBackend(EmbeddingBackend):
        name = "my-backend"
        dim = 1024

        def embed(self, texts): ...          # -> list[list[float]]

    register(MyBackend())

Configure the choice in config.yaml::

    index:
      backend: "my-backend"
      model: "..."
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, Protocol


class EmbeddingBackend(Protocol):
    name: str
    dim: int

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Return one vector per input text, in order."""


_BACKENDS: dict[str, EmbeddingBackend] = {}


def register(backend: EmbeddingBackend) -> None:
    _BACKENDS[backend.name] = backend


def get(name: str) -> EmbeddingBackend | None:
    return _BACKENDS.get(name)


def iter_chunks(path: Path) -> Iterable[dict]:
    """Stream corpus/chunks.jsonl. Each row carries id, title, year, tier, area,
    downstream_tags, section, page_start, page_end, doc_type, source_text and text."""
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                yield json.loads(line)


def build(cfg, log=print) -> dict:
    """Entry point a future phase would call. No-op while index.backend is 'none'."""
    name = cfg["index"].get("backend", "none")
    if name in ("", "none"):
        log("  index: backend is 'none' - embedding and indexing are out of scope for this run")
        return {"status": "skipped", "reason": "index.backend is 'none'"}
    backend = get(name)
    if backend is None:
        raise RuntimeError(f"index.backend {name!r} is configured but no backend is registered; "
                           f"call argmine.index.register() first")
    chunks = list(iter_chunks(cfg.corpus / "chunks.jsonl"))
    vectors = backend.embed([c["text"] for c in chunks])
    return {"status": "embedded", "backend": name, "chunks": len(chunks),
            "dim": getattr(backend, "dim", len(vectors[0]) if vectors else 0)}
