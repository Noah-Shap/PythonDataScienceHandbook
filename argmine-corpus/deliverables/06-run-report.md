# 06 - Run report

Generated 2026-09-16T02:06:29+00:00 | cap 250 | criteria_version 1 | registry 250 entries

## Phases in this run

| Phase | Seconds | Summary |
|---|---|---|
| 0 scaffold | 0.0 | cap=250, field_map=deliverables/00-field-map.md |
| 1 seed | 5.7 |  |
| 2 snowball | 0.0 | admitted=0, already_decided=0, at_cap=True |
| 3 verify | 3.4 | considered=110, oa_resolved=90, seconds=3.4 |
| 4 tier | 0.0 | considered=0, retiered=0, seconds=0.0 |
| 5a fetch | 0.0 | guidelines=0, manifest=deliverables/05-fetch-manifest.csv, manifest_rows=250 |
| 5b extract | 0.0 | guidelines_extracted=0, no_pdf=44 |
| 6 chunk | 0.0 | chunks=101, from_abstract=93, from_fulltext=0, from_guideline=8 |

## Corpus state

- status: {'candidate': 110, 'extracted': 44, 'chunked': 96}
- verification: {'unverified': 110, 'verified': 140}
- tiers: T1: 15, T2: 71, T3: 39, T4: 15
- doc types: conference: 121, workshop: 87, journal: 37, book: 2, chapter: 1, preprint: 1, unrecorded: 1
- frontier: 140 nodes, 19 expanded
- rejected ledger: 724 candidates remembered

## Area quotas

| Area | Quota | In registry | Verified | Met |
|---|---|---|---|---|
| formal | 30 | 51 | 30 | yes |
| mining | 60 | 125 | 72 | yes |
| quality | 40 | 58 | 30 | no |
| dialogue | 40 | 40 | 27 | no |
| llm | 40 | 56 | 15 | no |
| resources | 30 | 70 | 39 | yes |

Areas below quota: **quality** (30 verified of 40, 28 more admitted but pending verification); **dialogue** (27 verified of 40, 13 more admitted but pending verification); **llm** (15 verified of 40, 41 more admitted but pending verification).

A pending entry is a registry record at status `candidate`: it was admitted and scored, but only one independent source could be reached for it. It is not rejected and needs no re-fetching - phase 3 processes exactly those records on the next run, so a run with the scholarly APIs reachable closes these gaps without repeating any earlier work.

## Source availability

| Source | Reachable | Detail |
|---|---|---|
| acl | yes | local clone at corpus/repos/acl-org__acl-anthology |
| acl_web | no | ProxyError: HTTPSConnectionPool(host='aclanthology.org', port=443): Max retries exceeded with url: / (Caused… |
| arxiv | no | ProxyError: HTTPSConnectionPool(host='export.arxiv.org', port=443): Max retries exceeded with url: /api/query… |
| bibcorpus | yes | 51 bibliography repositories configured |
| crossref | no | ProxyError: HTTPSConnectionPool(host='api.crossref.org', port=443): Max retries exceeded with url: /works?row… |
| github | yes | HTTP 200 |
| openalex | no | ProxyError: HTTPSConnectionPool(host='api.openalex.org', port=443): Max retries exceeded with url: /works?per… |
| semanticscholar | no | ProxyError: HTTPSConnectionPool(host='api.semanticscholar.org', port=443): Max retries exceeded with url: /gr… |
| unpaywall | no | ProxyError: HTTPSConnectionPool(host='api.unpaywall.org', port=443): Max retries exceeded with url: /v2/10.11… |

## Verification evidence

Source combinations backing the registry (a `bibcorpus` label counts once per independent repository, and never for a verbatim re-export of the ACL Anthology):

- acl, bibcorpus: 95
- acl: 90
- bibcorpus: 65

## Retrieval, extraction, chunking

- PDFs: 0 fetched, 0 already cached, 0 unavailable
- repositories cloned: 0; guideline/README documents copied: 0
- extraction: 0 PDFs (0 pages), 0 guideline documents, 0 failures
- chunks: 101 (0 full text, 8 guideline, 93 abstract-only)

## Annotations

- written this run: 0; unchanged: 250
- grounding: {'fulltext': 0, 'abstract': 188, 'none': 62}
- every annotation quotes the retrieved text it was written from and names it in `grounded_on`; where nothing was retrieved the annotation says so and asserts nothing about content.

## Cost and caching

- HTTP: 0 network calls, 0 cache hits, 0 skipped because the source is unreachable, 0 retried errors
- layer 1 (HTTP cache): metadata responses expire after 30 days, PDFs never expire
- layer 2 (status gating): every phase processes only records at exactly its input status; fetch additionally skips a PDF whose sha256 matches, extract skips text whose source PDF hash is unchanged
- layer 3 (frontier memory): 19 of 140 nodes expanded; directions recorded per node
- layer 4 (decision memory): 724 rejected candidates kept with their scores at criteria_version 1; bumping it re-scores them without re-fetching anything

## Changelog

Run 2; previous run recorded at 2026-09-16T02:02:43+00:00.

No new entries were admitted in this run.

## Limits of this run

Unreachable sources: acl_web, arxiv, crossref, openalex, semanticscholar, unpaywall. Consequences:

- no citation-graph expansion (`reference` / `citation` directions stay pending in `frontier.jsonl`; a later run with network access expands exactly those nodes and nothing else);
- no citation counts, so the `cites_norm` component is computed from how many independent bibliographies list a work rather than from a citation count - the substitution is recorded per record in `score.components_source`;
- OA PDFs could not be downloaded, so most annotations are grounded on abstracts rather than full text, and most chunks are abstract chunks. Every entry is still in `05-fetch-manifest.csv` with a resolvable URL, so the PDFs can be fetched elsewhere and `python -m argmine extract chunk` picks them up without re-running anything else.

The same applies to verification: every entry that reached only one independent source is still a `candidate` in the registry, listed in `99-unverified-and-rejected.md`, and is re-examined by phase 3 on the next run. Nothing about it has to be fetched again.

## Reproducing this run

```bash
python -m argmine run            # resume; every phase is idempotent
python -m argmine run --cap 400  # expand: only new work is done
python -m argmine status         # registry / frontier / rejection counts
```
