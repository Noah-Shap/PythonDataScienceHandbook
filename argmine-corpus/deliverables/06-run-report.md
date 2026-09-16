# 06 - Run report

Generated 2026-09-16T03:27:15+00:00 | cap 250 | criteria_version 1

## 1. Counts

- **250 entries** in the registry (cap 250); 139 verified, 111 pending verification
- per area: mining 125, resources 71, quality 57, formal 54, llm 53, dialogue 40
- per tier: T1 12, T2 72, T3 41, T4 14
- per doc_type: conference 119, workshop 87, journal 38, chapter 3, book 2, preprint 1
- verification: unverified 111, verified 139
- rejected (722 remembered): off_topic 433, below_cutoff 202, cap_reached 73, excluded_domain 11, seed_unresolved 2, proceedings_volume 1
- PDFs: 0 fetched, 250 manifest-only
- repos cloned: 0; guideline/README documents retrieved: 0 (0 extracted to text)
- chunks: 100 (0 full text, 8 guideline, 92 abstract)
- chunk token histogram: 0-199: 57, 200-399: 42, 400-599: 1

- annotations: 63 written this run, 187 unchanged; grounding fulltext 0, abstract 187, none 63 (an entry with no retrieved text carries no annotation, by rule)

## 2. Coverage gaps

| Area | Quota | Verified | Pending | Met |
|---|---|---|---|---|
| formal | 30 | 30 | 24 | yes |
| mining | 60 | 73 | 52 | yes |
| quality | 40 | 29 | 28 | no |
| dialogue | 40 | 28 | 12 | no |
| llm | 40 | 13 | 40 | no |
| resources | 30 | 40 | 31 | yes |

Below quota, and why: **quality** 29/40 verified, 28 more admitted but pending; **dialogue** 28/40 verified, 12 more admitted but pending; **llm** 13/40 verified, 40 more admitted but pending. A pending entry is a registry record at status `candidate`: it was admitted and scored, but only one independent source could be reached for it. It is not rejected and needs no re-fetching - phase 3 processes exactly those records on the next run.

**Important works that could not be verified** (seed-derived, or co-listed with this corpus in at least half as many curated bibliographies as the most co-listed candidate):

- Modeling Appropriate Language in Argumentation (2023) - found by acl - only one independent source could be reached
- Reasoning on conflicting information: An empirical study of Formal Argumentation (2022) - found by bibcorpus:CogSciPrag/project_ideas - only one independent source could be reached
- Towards Argument Mining from Dialogue (2014) - found by bibcorpus:davidar/dblp.yaml - bibcorpus:lmlearning/AFGraphLib: venue mismatch ('COMMA' vs 'Frontiers in Artificial Inte…
- ArgumenText: Argument Classification and Clustering in a Generalized Search Scenario (2020) - found by bibcorpus:NeWildeSache/argument-mining-in-the-web-archive - only one independent source could be reached
- MARGOT: A web server for argumentation mining (2016) - found by bibcorpus:NeWildeSache/argument-mining-in-the-web-archive - only one independent source could be reached

**Scope-uncertain admissions (62).** Admitted at the lowest plausible tier and flagged here rather than dropped:

- The Argument Interchange Format (TNone) - no abstract retrieved, so scope was judged from the title and venue
- Argumentation Frameworks as Constraint Satisfaction Problems (TNone) - no abstract retrieved, so scope was judged from the title and venue
- On judgment aggregation in abstract argumentation (T2) - no abstract retrieved, so scope was judged from the title and venue
- Argumentation Mining (T2) - no abstract retrieved, so scope was judged from the title and venue
- Argumentation in the 2016 US presidential elections: annotated corpora of… (T2) - no abstract retrieved, so scope was judged from the title and venue
- ArgumenText: Argument Classification and Clustering in a Generalized Searc… (TNone) - no abstract retrieved, so scope was judged from the title and venue
- The Carneades model of argument and burden of proof (T2) - no abstract retrieved, so scope was judged from the title and venue
- Argument Graphs and Assumption-based Argumentation (T2) - no abstract retrieved, so scope was judged from the title and venue
- Online Forums and Deliberative Democracy (T2) - weak vocabulary match (keyword 0.25)
- Answer-set programming encodings for argumentation frameworks (T2) - no abstract retrieved, so scope was judged from the title and venue
- ... and 52 more (`scope_uncertain` in registry.jsonl)

## 3. Seeds

21 hypotheses; 19 verified, 0 admitted unverified, 2 rejected.

**Verified as given** (nothing in the hypothesis had to change):

- Argumentation Mining: State of the Art and Emerging Trends - `doi:10.1145/2850417`
- Argumentation mining - `doi:10.2200/s00883ed1v01y201811hlt040`
- Five Years of Argument Mining: a Data-driven Analysis - `doi:10.24963/ijcai.2018/766`
- Argumentation Schemes - `doi:10.1017/cbo9780511802034`
- On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Log… - `doi:10.1016/0004-3702(94)00041-x`
- An introduction to argumentation semantics - `doi:10.1017/s0269888911000166`
- The ASPIC+ framework for structured argumentation: a tutorial - `doi:10.1080/19462166.2013.869766`
- Towards an Argument Interchange Format - `doi:10.1017/s0269888906001044`
- Parsing Argumentation Structures in Persuasive Essays - `doi:10.1162/coli_a_00295`
- Computational Argumentation Quality Assessment in Natural Language - `title:55893f7c5565660a055d8f689db3e97c66843203`
- Which argument is more convincing? Analyzing and predicting convincingness of Web argumen… - `doi:10.18653/v1/p16-1150`
- A large-scale dataset for argument quality ranking: Construction and analysis - `doi:10.1609/aaai.v34i05.6285`
- Logical Fallacy Detection - `doi:10.18653/v1/2022.findings-emnlp.532`
- An autonomous debating system - `doi:10.1038/s41586-021-03215-w`
- QT30: A Corpus of Argument and Conflict in Broadcast Debate - `title:e4827cf79a5103f624f48b2e7d4a4ccc7ab6c0ea`
- Winning Arguments: Interaction Dynamics and Persuasion Strategies in Good-Faith Online Di… - `doi:10.1145/2872427.2883081`
- A Corpus for Research on Deliberation and Debate - `title:ae7588dc60be7ab8f03855ae779ec0f0519a8728`

**Corrected from the sources** (the hypothesis was wrong; the sources win):

| Entry | Field | Hypothesis | Verified | Sources |
|---|---|---|---|---|
| `doi:10.1162/coli_a_00364` | year | 2020 | 2019 | acl, bibcorpus:CogSciPrag/project_ideas, bibcorpus:ljvmiran… |
| `title:df299e3284c272f02cac357fba80718526676f2a` | year | 1958 | 1960 | bibcorpus:IKMLab/arct2, bibcorpus:NeWildeSache/argument-min… |

**Recorded in canonical form** (the hypothesis named the same venue, the sources spell it out):

- `doi:10.1145/2850417` - venue: ACM Transactions on Internet Technology -> ACM Transactions on Internet Technology (TOIT)
- `doi:10.24963/ijcai.2018/766` - venue: IJCAI -> Proceedings of the Twenty-Seventh International Joint Conference on Artificial…
- `doi:10.1017/s0269888911000166` - venue: Knowledge Engineering Review -> The Knowledge Engineering Review
- `doi:10.1017/s0269888906001044` - venue: Knowledge Engineering Review -> The Knowledge Engineering Review
- `title:55893f7c5565660a055d8f689db3e97c66843203` - venue: EACL -> Proceedings of the 15th Conference of the European Chapter of the Association f…
- `doi:10.18653/v1/p16-1150` - venue: ACL -> Proceedings of the 54th Annual Meeting of the Association for Computational Lin…
- `doi:10.1609/aaai.v34i05.6285` - venue: AAAI -> Proceedings of the Thirty-Fourth AAAI Conference on Artificial Intelligence, AA…
- `doi:10.18653/v1/2022.findings-emnlp.532` - venue: Findings of EMNLP -> Findings of the Association for Computational Linguistics: EMNLP 2022
- `title:e4827cf79a5103f624f48b2e7d4a4ccc7ab6c0ea` - venue: LREC -> Proceedings of the Thirteenth Language Resources and Evaluation Conference
- `doi:10.1145/2872427.2883081` - venue: WWW -> Proceedings of the 25th International Conference on World Wide Web, WWW 2016, M…
- `title:ae7588dc60be7ab8f03855ae779ec0f0519a8728` - venue: LREC -> Proceedings of the Eighth International Conference on Language Resources and Ev…

**Rejected** (no source could resolve them; nothing was invented to fill the gap):

- Whence inference (2011) - seed_unresolved: no source returned a plausible match for this title, author and year
- Visser US2016 annotated corpus of televised election debates and social media reaction (2020) - seed_unresolved: no source returned a plausible match for this title, author and year

## 4. API budget

| Source | Network | Cache hits | Skipped (unreachable) | Errors |
|---|---|---|---|---|
| (no external request was made in this run) | 0 | 0 | 0 | 0 |

Cache hit rate: 0% over 0 cacheable requests. Every request is logged with its URL, hit/miss and status to `corpus/requests.log` (git-ignored).

Missing credentials: S2_API_KEY, GITHUB_TOKEN. Degradation: Semantic Scholar runs unauthenticated, at a lower rate limit (config sets a 3 s delay for it); GitHub search runs unauthenticated or from the committed search cache; repository cloning is unaffected.

## 5. Expansion note

- 275 scored candidates are waiting in `corpus/rejected.jsonl` (reason `below_cutoff` or `cap_reached`, at criteria_version 1).
- unexpanded frontier nodes: 120 of 139.
- best waiting candidate: **Multi-Agent LLM Debate Unveils the Premise Left Unsaid** (2025), score 0.3479 (cocite 0.0, keyword 0.7917, venue 1.0).
- lowest admitted score in the registry: 0.2. Raising the cap promotes waiting candidates in score order, using metadata already stored - no API call, no re-scoring.
- `python -m argmine run --cap 300` would consider all 275 of them.

## 6. Changelog

Run 2; previous run recorded at 2026-09-16T03:25:03+00:00.

No new entries were admitted in this run.

---

## Appendix A - phases in this run

| Phase | Seconds | Summary |
|---|---|---|
| 0 scaffold | 0.0 | cap=250, field_map=deliverables/00-field-map.md |
| 1 seed | 10.8 |  |
| 2 snowball | 0.0 | admitted=0, already_decided=0, at_cap=True |
| 3 verify | 3.4 | considered=111, oa_resolved=89, seconds=3.4 |
| 4 tier | 0.0 | considered=0, retiered=0, scope_uncertain=62 |
| 5a fetch | 0.0 | guidelines=0, manifest=deliverables/05-fetch-manifest.csv, manifest_rows=250 |
| 5b extract | 0.0 | guidelines_extracted=0, no_pdf=44 |
| 6 chunk | 0.0 | chunks=100, from_abstract=92, from_fulltext=0, from_guideline=8 |

## Appendix B - source availability

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

## Appendix D - verification evidence

Source combinations behind the registry. A `bibcorpus` label counts once per independent repository, and never for a verbatim re-export of the ACL Anthology:

- acl, bibcorpus: 93
- acl: 89
- bibcorpus: 68

## Appendix E - caching layers

- layer 1, HTTP cache: metadata responses expire after 30 days, binaries never
- layer 2, status gating: each phase processes only records at exactly its input status; fetch also skips a PDF whose sha256 matches, extract skips text whose source PDF hash is unchanged
- layer 3, frontier memory: 19 of 139 nodes expanded, directions recorded per node
- layer 4, decision memory: 722 rejected candidates kept with their scores at criteria_version 1; bumping it re-scores them without re-fetching anything

## Appendix F - limits of this run

Unreachable sources: acl_web, arxiv, crossref, openalex, semanticscholar, unpaywall. Consequences:

- no citation-graph expansion: the `reference` and `citation` directions stay pending on every frontier node, so a later run with network access expands exactly those and nothing else;
- no citation counts, so `cites_norm` is computed from how many independent bibliographies list a work; the substitution is recorded per record in `score.components_source`;
- no OA PDF could be downloaded, so annotations are grounded on abstracts and most chunks are abstract chunks. Every entry is in `05-fetch-manifest.csv` with a resolvable URL, so the PDFs can be fetched elsewhere and `python -m argmine extract chunk` picks them up;
- every entry that reached only one independent source is still a `candidate` and is re-examined by phase 3 on the next run.

## Appendix G - reproducing this run

```bash
python -m argmine run            # resume; every phase is idempotent
python -m argmine run --cap 300  # expand: only new work is done
python -m argmine status         # registry / frontier / rejection counts
python -m argmine report         # print this report
```
