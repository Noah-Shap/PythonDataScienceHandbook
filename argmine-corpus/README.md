# argmine-corpus

An idempotent pipeline that assembles a **verified, tiered, annotated bibliography and
full-text corpus of argumentation mining / computational argumentation**, prepared for RAG
ingestion.

It exists as groundwork for a system that stores and evaluates arguments extracted from
debate transcripts at the dialogue level: who said what, in reply to what, with what
inferential and conflict relations, and how strong it is. Everything about the corpus -
which areas it must cover, how candidates are scored, what counts as verified - is written
down in `config.yaml` and `deliverables/00-field-map.md` rather than decided ad hoc.

## Hard rules the pipeline enforces

1. **Cap.** `run.cap` in `config.yaml` (250 for this run). The cap is enforced at admission.
2. **Two independent sources or it is not in the bibliography.** Title, first author, year
   and venue must agree across two independent metadata sources. Anything else lands in
   `deliverables/99-unverified-and-rejected.md`.
3. **Fully cached and resumable.** Re-running a phase, or raising the cap, never repeats
   work: no repeated API calls, no re-downloads, no re-extraction, no re-scoring of decided
   candidates, no re-expansion of expanded frontier nodes. Four layers, below.
4. **Annotations are grounded.** Each annotation is written from retrieved text - full text
   if a PDF was fetched, otherwise the abstract - quotes it, and records which in
   `grounded_on`. Where nothing was retrieved, the annotation says so and asserts nothing.
5. **Polite retrieval.** Descriptive User-Agent with a contact address, documented rate
   limits respected, exponential backoff on 429/5xx, open-access PDFs only, no paywall is
   ever touched.
6. **Git-tracked, PDFs excluded.** Registry, config, code and deliverables are committed;
   PDFs, extracted text, the HTTP cache and cloned repos are not.

## Running it

```bash
python -m venv .venv && .venv/bin/pip install -e .
.venv/bin/python -m argmine run            # all phases, in order
.venv/bin/python -m argmine status         # registry / frontier / rejection counts
.venv/bin/python -m argmine report         # print the run report
```

Individual phases: `scaffold`, `seed`, `snowball`, `verify`, `tier`, `fetch`, `extract`,
`chunk`, `deliver`. Flags: `--cap N`, `--retier`, `--dry-run`, `--offline`, `--no-commit`,
`--force-index`.

Optional environment: `S2_API_KEY` (higher Semantic Scholar rate limit), `GITHUB_TOKEN`
(GitHub search), `ARGMINE_COMMIT_TRAILERS` (trailers appended to each phase commit).

## Expanding the corpus

```bash
.venv/bin/python -m argmine run --cap 400
```

This resumes from the current state. Only frontier nodes that have not been expanded in a
given direction are expanded; only never-seen candidates are scored; only newly admitted
entries are verified, fetched, extracted, chunked and annotated. Previously rejected
candidates are promoted from `corpus/rejected.jsonl` using the score they already have -
no metadata is re-fetched. Deliverables are regenerated in full (they are cheap) with a
changelog of what was added.

To re-decide old rejections under new rules, bump `run.criteria_version` in `config.yaml`.
That triggers re-scoring only; it never re-fetches or re-extracts anything. To recompute
tiers, pass `--retier` - tiers are otherwise stable so the reading order does not churn.

## The four caching layers

| Layer | Mechanism | Where |
|---|---|---|
| 1. HTTP | `requests-cache` on SQLite; metadata TTL 30 days, binaries never expire; key = method + URL + sorted params | `argmine/cache.py`, `corpus/http_cache.sqlite` |
| 2. Status gating | every phase processes only records whose `status` is exactly its input state; `fetch` also skips a PDF whose sha256 matches, `extract` skips text whose source PDF hash is unchanged | `argmine/cache.py`, each phase |
| 3. Frontier memory | every expanded node recorded with the directions expanded and when | `corpus/frontier.jsonl` |
| 4. Decision memory | every rejected candidate kept with its reason, score and `criteria_version` | `corpus/rejected.jsonl` |

Local sources are cached the same way: the ACL Anthology clone is re-indexed only when its
commit changes, and BibTeX repositories are cloned once, pruned to their `.bib` files and
pinned by commit in `corpus/bib_repos.json`.

## Sources

Metadata and citation graph: **Semantic Scholar Graph API**, **OpenAlex**, **Crossref**,
**arXiv**, and the **ACL Anthology** read locally from a sparse clone of
`acl-org/acl-anthology` rather than scraped. OA PDF resolution: OpenAlex `best_oa_location`
-> Unpaywall -> arXiv -> ACL Anthology. GitHub supplies dataset/tool repositories, READMEs
and annotation guidelines.

Two further local sources make the pipeline work in environments where the scholarly APIs
are blocked:

- **ACL Anthology index** (`argmine/sources/acl.py`) - 127k papers with titles, authors,
  years, venues, DOIs and abstracts, searchable through SQLite FTS5.
- **BibTeX corroboration corpus** (`argmine/sources/bibcorpus.py`) - bibliographies shipped
  inside GitHub repositories. Each `.bib` file is an independently curated reference list,
  which gives both a second metadata record for a work and a co-citation signal. Verbatim
  re-exports of the Anthology's own BibTeX are excluded from the independence count, and
  only small files (real reference lists, not whole-venue dumps) count for co-citation.

`corpus/source_status.json` records which sources a run could actually reach, and
`deliverables/06-run-report.md` says what the unreachable ones cost.

## Layout

```
argmine/          pipeline package - one module per phase, one per source
corpus/           registry.jsonl, frontier.jsonl, rejected.jsonl (committed);
                  pdfs/, text/, repos/, chunks.jsonl, http_cache.sqlite (ignored)
deliverables/     00-field-map, 01-bibliography, 02-datasets-and-tools, 03-reading-order,
                  04-rag-prep, 05-fetch-manifest.csv, 06-run-report, 99-unverified-and-rejected
```

`corpus/registry.jsonl` is the canonical store: one JSON object per entry, canonical id
precedence `doi: > arxiv: > s2: > openalex: > title:<sha1>`, every other identifier in
`aliases`. Duplicates merge on a shared alias, or on a fuzzy title match >= 0.95 with a
year within one and at least one shared author surname, preferring the published version's
metadata over the preprint's while keeping both URLs.

## What is out of scope here

Embedding and indexing. `argmine/index.py` is the hook: implement `EmbeddingBackend`,
`register()` it, set `index.backend` in `config.yaml`. The chunk format in
`corpus/chunks.jsonl` is the contract, and `deliverables/04-rag-prep.md` documents it.
