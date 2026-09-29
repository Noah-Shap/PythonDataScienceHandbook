# argmine-corpus

Read `HANDOFF.md` before changing anything here. It has the current state of the corpus,
the design contracts that are load-bearing, the backlog in priority order, and a
verification checklist that passes today.

Run the pipeline through the project venv: `.venv/bin/python -m argmine <phase>`, or
`run` for every phase in order. Every phase is idempotent — re-running does no work twice,
and `status` works before any cache exists.

Do not hand-edit `corpus/registry.jsonl`, `corpus/frontier.jsonl` or
`corpus/rejected.jsonl`. They are the pipeline's memory: the registry is the canonical
store, the frontier records what has been expanded in which direction, and the rejection
ledger is what makes raising the cap cheap. Change `config.yaml` and re-run the phase
instead.
