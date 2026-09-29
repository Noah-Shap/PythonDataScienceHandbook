# Handoff: moving `argmine-corpus` into its own repository

Everything in this directory is self-contained: no file outside it is imported, and all 115
commits on `claude/argmine-corpus-pipeline-fj5b4u` touch only paths under
`argmine-corpus/`. It was built inside `Noah-Shap/PythonDataScienceHandbook` only because
that was the attached repo; nothing ties it there.

This document is the whole handoff: how to move it with history intact, what to do in the
first hour on the other side, what the corpus currently contains, which design contracts
must not be broken casually, and what is left undone.

---

## 1. What you are moving

| | |
|---|---|
| Tracked files | 53 (code, config, registry, deliverables) |
| Working tree | 2.5 MB |
| History | 115 commits, all confined to this directory |
| `.git` after extraction | 19 MB |
| Local state **not** committed | ~2.9 GB, all regenerable (see §3) |

**Committed — the reproducibility contract.** These are the files that make a re-run cheap
and auditable, so they belong in git even though some of them are outputs:

```
config.yaml                     cap, quotas, weights, vocabulary, seeds, criteria_version
pyproject.toml                  Python >= 3.11, five pinned deps
README.md                       how to run, how to expand, the four caching layers
argmine/                        one module per phase, one per source
corpus/registry.jsonl           250 records, one JSON object per line (680 KB)
corpus/frontier.jsonl           139 snowball nodes with per-direction expansion flags
corpus/rejected.jsonl           722 decided candidates with reasons and scores (904 KB)
corpus/bib_repos.json           51 bibliography repos, every one pinned by commit SHA
corpus/github_search_cache.json 16 GitHub queries with their results, so a run reproduces offline
corpus/source_status.json       which sources the last run could actually reach
corpus/run_log.jsonl            per-phase summaries for every run, in order
deliverables/00..99             8 deliverables, regenerated in full on every run
```

**Not committed, and deliberately so** (`.gitignore`): `corpus/pdfs/`, `corpus/text/`,
`corpus/repos/`, `corpus/chunks.jsonl`, `corpus/http_cache.sqlite`,
`corpus/acl_index.sqlite`, `corpus/bib_index.json`, `corpus/requests.log`, `.venv/`.

---

## 2. The move

### Option A — keep the history (recommended, verified)

`git subtree split` rewrites the 115 commits so this directory becomes the repository root.
I ran this end to end in the source repo: 1.6 s, 115 commits, and the resulting tree is
identical to the current working directory (file list plus sha256 of `config.yaml`,
`README.md`, `argmine/verify.py`, `corpus/registry.jsonl`,
`deliverables/06-run-report.md`).

```bash
# in a clone of PythonDataScienceHandbook, on the argmine branch
git checkout claude/argmine-corpus-pipeline-fj5b4u
git subtree split -P argmine-corpus -b argmine-split     # ~2 s, 115 commits

# create the new empty repo first (no README, no .gitignore, no licence), then:
git push git@github.com:<owner>/argmine-corpus.git argmine-split:main
```

Then clone it fresh and check it stands alone. I did exactly this, and both commands worked
from a clean clone with no caches present:

```bash
git clone git@github.com:<owner>/argmine-corpus.git && cd argmine-corpus
python -m venv .venv && .venv/bin/pip install -e .
.venv/bin/python -m argmine status                          # 250 records, 139 verified
.venv/bin/python -m argmine deliver --dry-run --no-commit    # regenerates all 8 deliverables
```

**One thing to know before you keep that history.** It contains roughly ten full
`phase 0 … phase 7` cycles, because the corpus was rebuilt from scratch each time a scoring
or verification rule changed. It is honest provenance — you can see which rule change moved
which number — but it is not a tidy feature history. If you would rather start clean,
Option B.

### Option B — start clean

```bash
git subtree split -P argmine-corpus -b argmine-split
git checkout --orphan main argmine-split
git commit -m "argmine-corpus: verified, tiered, annotated argument-mining corpus pipeline"
```

You lose the ability to answer "when did the `llm` verified count change, and which rule
did it", which is answerable today from the phase commits and `corpus/run_log.jsonl`.

### After the push, in the old repo

`argmine-corpus/` is pure addition to `PythonDataScienceHandbook` — the 153 files of the
original handbook are untouched on this branch. Once the new repo is up, either delete the
branch or `git rm -r argmine-corpus` on it; nothing else needs unpicking. Don't merge it
into `master` first: that would put a research pipeline inside a teaching handbook.

---

## 3. First hour in the new repo

### Install and confirm the committed state

```bash
python -m venv .venv && .venv/bin/pip install -e .
.venv/bin/python -m argmine status
.venv/bin/python -m argmine report | head -40
```

`status` reads only committed files, so it works before any cache exists.

### Rebuild the local sources (one command, network-bound)

```bash
.venv/bin/python -m argmine seed          # also prepares both local sources
```

That does all of this, idempotently:

| Step | Disk | Time measured here |
|---|---|---|
| Sparse-clone `acl-org/acl-anthology` (`data/` only) | 233 MB | a few minutes, network-bound |
| Build `corpus/acl_index.sqlite` (FTS5 over title + abstract) | 349 MB | **13.6 s** for 1,719 collections / 127,851 papers |
| Clone the 51 pinned bibliography repos, prune each to its `.bib` files | 2.1 GB in `corpus/repos/` | ~10 min, network-bound |
| Build `corpus/bib_index.json` | 415 MB | **200 s** for 572,055 entries / 69,929 bibliographies |

None of it is re-fetched on later runs: a pruned clone leaves a `.argmine_clone.json`
marker with its commit, and each index is rebuilt only when its clone's commit moves.
Budget ~3 GB of disk.

### Set what the sandbox could not have

```bash
export S2_API_KEY=...        # Semantic Scholar: higher rate limit
export GITHUB_TOKEN=...      # GitHub repo/code search (cloning works without it)
export UNPAYWALL_EMAIL=...   # defaults to run.contact_email
```

`config.yaml` already carries `run.contact_email` (OpenAlex/Crossref polite pool,
Unpaywall). Whatever is missing gets named in the run report's API budget with what it
degrades — nothing fails silently.

### The first real run

```bash
.venv/bin/python -m argmine run
```

---

## 4. What that first networked run will change

The sandbox this was built in blocked every scholarly API at the network-policy level:
`api.semanticscholar.org`, `api.openalex.org`, `api.crossref.org`, `api.unpaywall.org`,
`export.arxiv.org` and `aclanthology.org` itself all answered 403 to CONNECT. That verdict
is recorded per source in `corpus/source_status.json`. On a machine that can reach them,
and without repeating any earlier work:

1. **111 pending records get verified.** They sit at status `candidate` because only one
   independent source could be reached for them. Phase 3 processes exactly those records
   and nothing else. Expect most to verify immediately, and the `quality`, `dialogue` and
   `llm` quotas to close (§5).
2. **The citation graph gets used for the first time.** All 139 frontier nodes still have
   their `reference` and `citation` directions flagged unexpanded — only the `bibliography`
   direction has run. Phase 2 will expand those and nothing else. It won't run at all until
   you raise the cap: the registry is at 250/250, and expanding a frontier you can't admit
   from is paid-for work with no possible outcome.
3. **`cites_norm` switches from proxy to real citation counts.** Each record says which it
   used in `score.components_source`; today that reads
   `bibliography-frequency-proxy`.
4. **PDFs start arriving.** 183 of 250 records already have a resolved OA URL, and
   `deliverables/05-fetch-manifest.csv` carries a URL for every entry. Phase 5a downloads
   only from the allowlist in `config.yaml` (`fetch.oa_hosts`) plus anything Unpaywall or
   OpenAlex resolved as open access — no publisher paywall is ever requested.
5. **Annotations and chunks improve.** Today 0 annotations are grounded on full text, 187
   on abstracts, and 63 are empty (no retrieved text means no annotation, by rule). Once
   PDFs extract, phase 6 produces full-text section chunks with page numbers instead of
   today's 100 abstract/guideline chunks, and phase 7 rewrites only the annotations whose
   grounding changed.

To grow the corpus: `python -m argmine run --cap 400`. 276 scored candidates are waiting in
`corpus/rejected.jsonl` and get promoted on the score they already have — no API call, no
re-scoring. Verified here with `snowball --cap 300 --dry-run`: it expanded only the 120
unexpanded nodes, skipped 516 already-decided candidates, scored 38 new ones, and promoted
37 from the ledger.

---

## 5. State as handed over

| | |
|---|---|
| Registry | 250 / cap 250 |
| Verified (two independent agreeing sources) | **139** → `01-bibliography.md` |
| Pending (one source reachable) | **111** → `99-unverified-and-rejected.md`, status `candidate` |
| Tiers | T1 12, T2 72, T3 41, T4 14 |
| Evidence | ACL Anthology + BibTeX corpus 93, ACL only 89, BibTeX only 68 |
| Scope-uncertain admissions | 62, none at T1, all listed in the run report |
| Rejections remembered | 722: off_topic 433, below_cutoff 202, cap_reached 73, excluded_domain 11, seed_unresolved 2, proceedings_volume 1 |
| Chunks | 100 (0 full text, 8 guideline, 92 abstract) |
| PDFs held locally | 0 (183 records have a resolved OA URL) |
| Resource repos cloned | 3, with licence and commit recorded |

Quotas — verified counts against the minimums in `config.yaml`:

| Area | Quota | Verified | Pending | Met |
|---|---|---|---|---|
| formal | 30 | 30 | 24 | yes |
| mining | 60 | 73 | 52 | yes |
| quality | 40 | 29 | 28 | no |
| dialogue | 40 | 28 | 12 | no |
| llm | 40 | 13 | 40 | no |
| resources | 30 | 40 | 31 | yes |

Seeds: 21 hypotheses → 17 verified as given, 2 genuinely corrected (Lawrence & Reed is
*Computational Linguistics* 45(4) **2019**, not 2020; Toulmin resolved to a later edition,
1960 rather than the 1958 first printing), 11 venue strings recorded in canonical form
(`LREC` → *Proceedings of the Thirteenth …*), and 2 rejected as unresolvable:

- **"Whence inference"** (Budzynska & Reed, Inference Anchoring Theory) — the brief flagged
  this title as needing verification, and no reachable source matched it. IAT itself is
  well covered through ArgMining papers that use it.
- **US2016 annotated corpora** (Visser et al.) — same situation. QT30 covers much of the
  same ground and is in the bibliography.

Neither was invented to fill the gap; both are in `rejected.jsonl` with reason
`seed_unresolved`. Resolving them is the second item in §7.

---

## 6. Contracts not to break casually

Each of these is load-bearing. Change them by all means — but know what depends on them.

1. **Two independent agreeing sources, or it is not in the bibliography.** Title, first
   author, year and venue must agree (`argmine/verify.py`). The BibTeX corpus counts once
   per *distinct repository*, and never for a verbatim re-export of the ACL Anthology —
   that test uses the Anthology's own bibkeys, not a guess from key shape.
2. **The four caching layers** (`README.md` has the table). Layer 2 especially: each phase
   processes only records at exactly its input status. Loosen that and you lose the
   guarantee that re-running a phase does no work twice — which you will pay for in API
   calls once the graph endpoints are live.
3. **Canonical id precedence** `doi: > arxiv: > s2: > openalex: > title:<sha1>`. A `title:`
   id is derived from the normalised title plus year, so changing `util.norm_title` renames
   records. If you must, migrate `registry.jsonl` in the same commit.
4. **Cap discipline.** A phase that would leave the registry above `run.cap` stops without
   committing. Raise the cap explicitly; don't remove the guard.
5. **Grounded annotations.** An annotation quotes the text it was written from and names it
   in `grounded_on`. No retrieved text means an empty annotation, not a generated one.
   `annotate.set_writer()` is the seam for an LLM-written annotation later: it receives
   `(record, grounding_text, grounded_on)` and nothing else has to move.
6. **Tier stability.** Tiers don't change without `--retier`, so the reading order doesn't
   churn between runs.
7. **Nothing is silently dropped.** A candidate whose scope is a judgement call is
   admitted, flagged in `scope_uncertain`, never promoted to T1, and listed in the report.
8. **Rejections are memory, not rubbish.** `criteria_version` in `config.yaml` is the only
   thing that makes a previously rejected candidate eligible for re-scoring. Bumping it
   re-scores; it never re-fetches.

---

## 7. Backlog, in the order I would do it

1. **Run it with network access** (§3, §4). Everything below is easier afterwards, and
   three of the quota gaps probably close on their own.
2. **Resolve the two rejected seeds** against Crossref and the LRE journal — then let them
   in *as seeds* rather than hand-editing the registry: correct the hypothesis in
   `config.yaml` and re-run `seed`, which re-resolves every seed on every run.
3. **Second-source coverage for post-2017 ACL papers.** This is the real ceiling on the
   139/111 split: the DBLP mirror in the BibTeX corpus (`davidar/dblp.yaml`) stops around
   2016, so recent ArgMining papers have the Anthology and nothing else. Crossref and
   OpenAlex make this disappear. If you ever need it offline again, the lever is more
   bibliography repos through `github_search_cache.json`.
4. **Fill the resources table.** Only 6 records have a linked repo, so most rows of
   `02-datasets-and-tools.md` read "none linked" / "not retrieved". The matcher
   (`fetch.link_repos`) wants two distinctive shared tokens; an explicit
   `paper id → repo` map in `config.yaml` for the canonical corpora (AAEC, UKP, IBM
   Debater, args.me, IAC, CMV, QT30) would beat inference, and would pull their annotation
   guidelines in as T3 documents.
5. **Embeddings.** `argmine/index.py` is a documented hook only: implement
   `EmbeddingBackend`, `register()` it, set `index.backend` in `config.yaml`. The chunk
   format in `corpus/chunks.jsonl` is the contract, and `04-rag-prep.md` documents it
   including which metadata fields are worth filtering on.
6. **Reading-order hours are a heuristic** from document type and tier, stated as such in
   `03-reading-order.md`. If you read a few and they're wrong, adjust
   `deliver.HOURS_BY_TYPE` rather than living with the noise.
7. **`verify` re-examines the 111 pending records on every run.** Correct, and free while
   the APIs are unreachable; once they're live each run spends real calls on records that
   may never verify. A "give up after N attempts" counter on the record would cap it.

---

## 8. Gotchas

- **`corpus/bib_index.json` is 415 MB** and every process that touches the BibTeX corpus
  loads it. Gitignored, rebuilt in 200 s. If it becomes a bottleneck, SQLite with an FTS
  table — the shape `sources/acl.py` already uses — is the obvious move.
- **Pinned repos can disappear.** `bib_repos.json` pins all 51 by SHA, but GitHub still has
  to serve them. A vanished repo shows as `cloned: false` with an error and contributes
  nothing — no crash, but corroboration silently weakens, so check that field after a
  rebuild.
- **The ACL Anthology clone is pinned by whatever commit you cloned** (`f27fde6433cf` here,
  recorded in each run's `prepared` summary). Delete the clone to move it forward; the
  index rebuilds itself when the commit changes.
- **`requests-cache` gives PDFs `NEVER_EXPIRE` and metadata a 30-day TTL.** An upstream
  metadata correction won't be seen for up to 30 days: `config.yaml` →
  `http.metadata_ttl_days`.
- **`ARGMINE_COMMIT_TRAILERS`** is how the per-phase commits got their co-authorship
  trailers. Unset, commits are plain — which is what you want for your own runs.
- **`ARGMINE_ROOT`** overrides project-root detection. It's how I tested the extracted
  clone without moving anything.
- **Venue strings are deliberately the fullest form** any agreeing source gave ("Nature",
  not "Nat."), and `doc_type` is a majority vote across sources. Both live in
  `verify.merge_views`; loosen them and citations degrade in ways that are hard to notice.

---

## 9. Verification checklist for the other side

Run this after the move. Every assertion held at handoff.

```bash
.venv/bin/python - <<'PY'
import csv, json
recs = [json.loads(l) for l in open('corpus/registry.jsonl')]
rej  = [json.loads(l) for l in open('corpus/rejected.jsonl')]
ver  = [r for r in recs if r['verification']['status'] == 'verified']
ids  = [r['id'] for r in recs]
rows = list(csv.DictReader(open('deliverables/05-fetch-manifest.csv')))
assert len(recs) <= 250, 'cap exceeded'
assert len(ids) == len(set(ids)), 'duplicate ids'
assert not [a for r in recs for a in r['aliases'] if a in set(ids) - {r['id']}], 'alias collision'
assert all(r['verification']['status'] for r in recs), 'missing verification status'
assert all(r['tier'] and r['downstream_tags'] for r in ver), 'verified record without tier/tags'
assert all(r['annotation']['grounded_on'] == 'none'
           for r in recs if not r['annotation']['text']), 'annotation without grounding'
assert not [r for r in recs if r.get('scope_uncertain') and r['tier'] == 1], 'uncertain at T1'
assert len(rows) == len(recs), 'manifest does not cover every entry'
assert any(r['rejection_reason'] == 'seed_unresolved' for r in rej), 'seed rejections lost'
print(f"OK: {len(recs)} records, {len(ver)} verified, {len(rej)} rejections, "
      f"{len(rows)} manifest rows")
PY
```

Then the idempotency check that matters most — run the pipeline twice and confirm the
second run does nothing:

```bash
.venv/bin/python -m argmine run    # expect: seed added_ids=0, snowball at-cap no-op,
.venv/bin/python -m argmine run    # deliver "0 annotations written, 250 unchanged"
```

---

## 10. Where the reasoning is written down

- `deliverables/00-field-map.md` — the coverage contract: six areas, inclusion and
  exclusion criteria, the scoring vocabulary, the quotas. Generated from `config.yaml`, so
  the document and the scorer can't drift apart.
- `deliverables/06-run-report.md` — what the last run did and what it could not do: counts,
  coverage gaps, seed corrections, API budget, expansion note, changelog.
- `deliverables/99-unverified-and-rejected.md` — every pending record with the note saying
  what disagreed, and every rejection grouped by reason with its score.
- `corpus/run_log.jsonl` — per-phase summaries for every run, in order. This is the file
  that answers "why did that number change".
- `README.md` — how to run, how to expand, the four caching layers, the source list.
- Module docstrings carry the judgement calls: `score.py` (why `cocite` is weighted highest
  and what it falls back to), `verify.py` (what independence means), `sources/bibcorpus.py`
  (why a bibliography is evidence at all, and when it isn't), `annotate.py` (why
  annotations are extractive).
