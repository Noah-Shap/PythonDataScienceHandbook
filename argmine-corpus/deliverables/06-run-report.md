# 06 - Run report

Generated 2026-09-16T03:25:39+00:00 | cap 250 | criteria_version 1

## 1. Counts

- **250 entries** in the registry (cap 250); 139 verified, 111 pending verification
- per area: mining 125, resources 71, quality 57, formal 54, llm 53, dialogue 40
- per tier: T1 12, T2 72, T3 41, T4 14
- per doc_type: conference 119, workshop 87, journal 38, chapter 3, book 2, preprint 1
- verification: unverified 111, verified 139
- rejected (723 remembered): off_topic 434, below_cutoff 202, cap_reached 73, excluded_domain 11, seed_unresolved 2, proceedings_volume 1
- PDFs: 0 fetched, 250 manifest-only
- repos cloned: 3; guideline/README documents retrieved: 3 (3 extracted to text)
- chunks: 100 (0 full text, 8 guideline, 92 abstract)
- chunk token histogram: 0-199: 57, 200-399: 42, 400-599: 1

- annotations: 250 written this run, 0 unchanged; grounding fulltext 0, abstract 187, none 63 (an entry with no retrieved text carries no annotation, by rule)

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
- Towards Argument Mining from Dialogue (2014) - found by bibcorpus:davidar/dblp.yaml - bibcorpus:lmlearning/AFGraphLib: venue mismatch ('COMMA' vs 'Frontiers in Artificial Inte…
- Reasoning on conflicting information: An empirical study of Formal Argumentation (2022) - found by bibcorpus:CogSciPrag/project_ideas - only one independent source could be reached
- MARGOT: A web server for argumentation mining (2016) - found by bibcorpus:NeWildeSache/argument-mining-in-the-web-archive - only one independent source could be reached
- ArgumenText: Argument Classification and Clustering in a Generalized Search Scenario (2020) - found by bibcorpus:NeWildeSache/argument-mining-in-the-web-archive - only one independent source could be reached

**Scope-uncertain admissions (62).** Admitted at the lowest plausible tier and flagged here rather than dropped:

- Corpus Wide Argument Mining - A Working Solution (T3) - no abstract retrieved, so scope was judged from the title and venue
- Transformer-Based Argument Mining for Healthcare Applications (T2) - no abstract retrieved, so scope was judged from the title and venue
- Identifying Argumentative Discourse Structures in Persuasive Essays (T2) - no abstract retrieved, so scope was judged from the title and venue
- Modeling Frames in Argumentation (T3) - weak vocabulary match (keyword 0.25)
- Modeling Deliberative Argumentation Strategies on Wikipedia (T3) - weak vocabulary match (keyword 0.25)
- Argumentation Mining (T2) - no abstract retrieved, so scope was judged from the title and venue
- Context-Independent Claim Detection for Argument Mining (T2) - no abstract retrieved, so scope was judged from the title and venue
- Building an Argument Search Engine for the Web (T3) - weak vocabulary match (keyword 0.17)
- The CASS Technique for Evaluating the Performance of Argument Mining (T2) - no abstract retrieved, so scope was judged from the title and venue
- Fill the Gap! Analyzing Implicit Premises between Claims from Online Debat… (T2) - no abstract retrieved, so scope was judged from the title and venue
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
- best waiting candidate: **Predicting the Usefulness of Amazon Reviews Using Off-The-Shelf Argumentation M…** (2018), score 0.3479 (cocite 0.0, keyword 0.7917, venue 1.0).
- lowest admitted score in the registry: 0.2. Raising the cap promotes waiting candidates in score order, using metadata already stored - no API call, no re-scoring.
- `python -m argmine run --cap 300` would consider all 275 of them.

## 6. Changelog

Run 1; previous run recorded at 2026-09-16T03:25:03+00:00.

Added 250 entries:

- `doi:10.1007/978-0-387-98197-0_19` - The Argument Interchange Format (2009, TNone)
- `doi:10.1007/978-3-642-23963-2_10` - Argumentation Frameworks as Constraint Satisfaction Problems (2011, TNone)
- `doi:10.1007/s10458-009-9116-7` - On judgment aggregation in abstract argumentation (2011, T2)
- `doi:10.1007/s10506-010-9104-x` - Argumentation Mining (2011, T2)
- `doi:10.1007/s10579-019-09446-8` - Argumentation in the 2016 US presidential elections: annotated corpora of television… (2019, T2)
- `doi:10.1007/s13222-020-00347-7` - ArgumenText: Argument Classification and Clustering in a Generalized Search Scenario (2020, TNone)
- `doi:10.1016/0004-3702(94)00041-x` - On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning… (1995, T1)
- `doi:10.1016/j.artint.2007.04.010` - The Carneades model of argument and burden of proof (2007, T2)
- `doi:10.1016/j.artint.2015.12.004` - Argument Graphs and Assumption-based Argumentation (2016, T2)
- `doi:10.1017/cbo9780511802034` - Argumentation Schemes (2008, T1)
- `doi:10.1017/s0269888906001044` - Towards an Argument Interchange Format (2006, T1)
- `doi:10.1017/s0269888911000166` - An introduction to argumentation semantics (2011, T1)
- `doi:10.1038/s41586-021-03215-w` - An autonomous debating system (2021, T2)
- `doi:10.1057/palgrave.ap.5500115` - Online Forums and Deliberative Democracy (2005, T2)
- `doi:10.1080/19462160903564592` - An abstract framework for argumentation with structured arguments (2010, T2)
- `doi:10.1080/19462166.2010.486479` - Answer-set programming encodings for argumentation frameworks (2010, T2)
- `doi:10.1080/19462166.2012.661766` - Relating Carneades with abstract argumentation via the ASPIC+ framework for structur… (2012, TNone)
- `doi:10.1080/19462166.2012.708670` - Distinctive features of persuasion and deliberation dialogues (2013, TNone)
- `doi:10.1080/19462166.2013.862303` - A natural language bipolar argumentation approach to support users in online debate… (2013, TNone)
- `doi:10.1080/19462166.2013.869764` - Introduction to structured argumentation (2014, T2)
- `doi:10.1080/19462166.2013.869766` - The ASPIC+ framework for structured argumentation: a tutorial (2014, T1)
- `doi:10.1080/19462166.2013.869767` - Defeasible logic programming: DeLP-servers, contextual queries, and explanations for… (2014, T2)
- `doi:10.1080/19462166.2013.869878` - A tutorial on assumption-based argumentation (2014, T2)
- `doi:10.1080/19462166.2014.1001790` - Context-aware reconfiguration of large-scale surveillance systems: argumentative app… (2015, T2)
- `doi:10.1093/logcom/14.5.675` - Argumentation Semantics for Defeasible Logic (2004, T2)
- `doi:10.1093/oso/9780198862536.003.0005` - Mining Property-driven Graphical Explanations for Data-centric AI from Argumentation… (2022, TNone)
- `doi:10.1111/coin.12111` - Assumption-Based Argumentation Equipped with Preferences and its Application to Deci… (2017, T2)
- `doi:10.1145/2850417` - Argumentation Mining: State of the Art and Emerging Trends (2016, T1)
- `doi:10.1145/2872427.2883081` - Winning Arguments: Interaction Dynamics and Persuasion Strategies in Good-Faith Onli… (2016, T2)
- `doi:10.1145/3308558.3314127` - Can You Give Me a Reason?: Argument-Inducing Online Forum by Argument Mining (2019, T2)
- `doi:10.1162/coli_a_00276` - Argumentation Mining in User-Generated Web Discourse (2017, T3)
- `doi:10.1162/coli_a_00295` - Parsing Argumentation Structures in Persuasive Essays (2017, T3)
- `doi:10.1162/coli_a_00364` - Argument Mining: A Survey (2019, T1)
- `doi:10.1162/coli_a_00553` - UniASA: A Unified Generative Framework for Argument Structure Analysis (2025, TNone)
- `doi:10.1162/tacl_a_00481` - End-to-end Argument Mining with Cross-corpora Multi-task Learning (2022, TNone)
- `doi:10.1371/journal.pone.0273225` - Reasoning on conflicting information: An empirical study of Formal Argumentation (2022, TNone)
- `doi:10.1609/aaai.v34i05.6270` - Corpus Wide Argument Mining - A Working Solution (2020, T3)
- `doi:10.1609/aaai.v34i05.6285` - A large-scale dataset for argument quality ranking: Construction and analysis (2020, T3)
- `doi:10.18653/v1/2020.acl-main.298` - Towards Better Non-Tree Argument Mining: Proposition-Level Biaffine Parsing with Tas… (2020, T2)
- `doi:10.18653/v1/2020.coling-main.128` - Contextual Argument Component Classification for Class Discussions (2020, T2)
- `doi:10.18653/v1/2020.coling-main.402` - Rhetoric, Logic, and Dialectic: Advancing Theory-based Argument Quality Assessment i… (2020, TNone)
- `doi:10.18653/v1/2021.acl-long.107` - Towards Argument Mining for Social Good: A Survey (2021, T1)
- `doi:10.18653/v1/2021.acl-long.497` - A Neural Transition-based Model for Argumentation Mining (2021, TNone)
- `doi:10.18653/v1/2021.acl-long.53` - Breaking Down the Invisible Wall of Informal Fallacies in Online Discussions (2021, T3)
- `doi:10.18653/v1/2021.argmining-1.1` - Argument Mining on Twitter: A Case Study on the Planned Parenthood Debate (2021, T2)
- `doi:10.18653/v1/2021.argmining-1.10` - Argumentation Mining in Scientific Literature for Sustainable Development (2021, TNone)
- `doi:10.18653/v1/2021.argmining-1.13` - Predicting Moderation of Deliberative Arguments: Is Argument Quality the Key? (2021, T2)
- `doi:10.18653/v1/2021.argmining-1.16` - Overview of the 2021 Key Point Analysis Shared Task (2021, T3)
- `doi:10.18653/v1/2021.argmining-1.19` - Key Point Analysis via Contrastive Learning and Extractive Argument Summarization (2021, T2)
- `doi:10.18653/v1/2021.argmining-1.4` - Image Retrieval for Arguments Using Stance-Aware Query Expansion (2021, T2)
- `doi:10.18653/v1/2021.argmining-1.9` - Citizen Involvement in Urban Planning - How Can Municipalities Be Supported in Evalu… (2021, TNone)
- `doi:10.18653/v1/2021.eacl-main.55` - End-to-End Argument Mining as Biaffine Dependency Parsing (2021, T2)
- `doi:10.18653/v1/2021.emnlp-main.515` - Hitting your MARQ: Multimodal ARgument Quality Assessment in Long Debate Video (2021, TNone)
- `doi:10.18653/v1/2022.emnlp-main.713` - A Generative Model for End-to-End Argument Mining with Reconstructed Positional Enco… (2022, TNone)
- `doi:10.18653/v1/2022.findings-emnlp.306` - Graph Embeddings for Argumentation Quality Assessment (2022, TNone)
- `doi:10.18653/v1/2022.findings-emnlp.532` - Logical Fallacy Detection (2022, T2)
- `doi:10.18653/v1/2023.acl-long.238` - Modeling Appropriate Language in Argumentation (2023, TNone)
- `doi:10.18653/v1/2023.argmining-1.1` - Detecting Argumentative Fallacies in the Wild: Problems and Limitations of Large Lan… (2023, T4)
- `doi:10.18653/v1/2023.argmining-1.13` - IUST at ImageArg: The First Shared Task in Multimodal Argument Mining (2023, TNone)
- `doi:10.18653/v1/2023.argmining-1.26` - SuryaKiran at PragTag 2023 - Benchmarking Domain Adaptation using Masked Language Mo… (2023, TNone)
- ... and 190 more

---

## Appendix A - phases in this run

| Phase | Seconds | Summary |
|---|---|---|
| 0 scaffold | 0.0 | cap=250, field_map=deliverables/00-field-map.md |
| 1 seed | 13.0 |  |
| 2 snowball | 21.7 | admitted=231, admitted_corroborated=120, already_decided=15 |
| 3 verify | 0.0 | considered=231, oa_resolved=176, seconds=0.0 |
| 4 tier | 0.0 | considered=139, retiered=0, scope_uncertain=62 |
| 5a fetch | 0.0 | guidelines=3, manifest=deliverables/05-fetch-manifest.csv, manifest_rows=250 |
| 5b extract | 0.0 | guidelines_extracted=3, no_pdf=139 |
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

## Appendix C - targeted searches

| Query | From | Source | Hits |
|---|---|---|---|
| `argument mining` | 6.7 | acl | 80 |
| `argument mining` | 6.7 | bibcorpus | 80 |
| `argumentation mining survey` | 6.7 | acl | 0 |
| `argumentation mining survey` | 6.7 | bibcorpus | 1 |
| `argument quality assessment` | 6.7 | acl | 23 |
| `argument quality assessment` | 6.7 | bibcorpus | 7 |
| `fallacy detection` | 6.7 | acl | 26 |
| `fallacy detection` | 6.7 | bibcorpus | 7 |
| `argumentation scheme classification` | 6.7 | acl | 3 |
| `argumentation scheme classification` | 6.7 | bibcorpus | 1 |
| `inference anchoring theory` | 6.7 | acl | 9 |
| `inference anchoring theory` | 6.7 | bibcorpus | 3 |
| `dialogical argument mining` | 6.7 | acl | 2 |
| `dialogical argument mining` | 6.7 | bibcorpus | 1 |
| `argument interchange format` | 6.7 | acl | 0 |
| `argument interchange format` | 6.7 | bibcorpus | 8 |
| `large language models argument mining` | 6.7 | acl | 0 |
| `large language models argument mining` | 6.7 | bibcorpus | 1 |
| `LLM argument quality evaluation` | 6.7 | acl | 0 |
| `LLM argument quality evaluation` | 6.7 | bibcorpus | 0 |
| `argument mining dataset` | 6.7 | acl | 10 |
| `argument mining dataset` | 6.7 | bibcorpus | 1 |
| `argument annotation guidelines` | 6.7 | acl | 0 |
| `argument annotation guidelines` | 6.7 | bibcorpus | 0 |
| `debate transcript argument corpus` | 6.7 | acl | 0 |
| `debate transcript argument corpus` | 6.7 | bibcorpus | 0 |
| `persuasive essays corpus` | 6.7 | acl | 1 |
| `persuasive essays corpus` | 6.7 | bibcorpus | 0 |
| `IBM Debater` | 6.7 | acl | 2 |
| `IBM Debater` | 6.7 | bibcorpus | 0 |
| `args.me argument search` | 6.7 | acl | 0 |
| `args.me argument search` | 6.7 | bibcorpus | 1 |
| `Webis argument quality` | 6.7 | acl | 0 |
| `Webis argument quality` | 6.7 | bibcorpus | 0 |
| `Kialo` | 6.7 | acl | 5 |
| `Kialo` | 6.7 | bibcorpus | 0 |
| `internet argument corpus` | 6.7 | acl | 5 |
| `internet argument corpus` | 6.7 | bibcorpus | 1 |
| `moral maze` | 6.7 | acl | 0 |
| `moral maze` | 6.7 | bibcorpus | 0 |
| `abstract argumentation semantics` | supplementary:formal | acl | 0 |
| `abstract argumentation semantics` | supplementary:formal | bibcorpus | 19 |
| `structured argumentation ASPIC` | supplementary:formal | acl | 0 |
| `structured argumentation ASPIC` | supplementary:formal | bibcorpus | 2 |
| `assumption-based argumentation` | supplementary:formal | acl | 0 |
| `assumption-based argumentation` | supplementary:formal | bibcorpus | 29 |
| `defeasible logic programming argumentation` | supplementary:formal | acl | 0 |
| `defeasible logic programming argumentation` | supplementary:formal | bibcorpus | 6 |
| `argumentation framework acceptability` | supplementary:formal | acl | 0 |
| `argumentation framework acceptability` | supplementary:formal | bibcorpus | 3 |
| `Toulmin model of argument` | supplementary:formal | acl | 0 |
| `Toulmin model of argument` | supplementary:formal | bibcorpus | 2 |
| `argumentation scheme critical questions` | supplementary:formal | acl | 0 |
| `argumentation scheme critical questions` | supplementary:formal | bibcorpus | 0 |
| `argument component classification` | supplementary:mining | acl | 8 |
| `argument component classification` | supplementary:mining | bibcorpus | 2 |
| `argument relation identification` | supplementary:mining | acl | 4 |
| `argument relation identification` | supplementary:mining | bibcorpus | 3 |
| `end-to-end argument mining` | supplementary:mining | acl | 11 |
| `end-to-end argument mining` | supplementary:mining | bibcorpus | 11 |
| `argumentative discourse unit segmentation` | supplementary:mining | acl | 0 |
| `argumentative discourse unit segmentation` | supplementary:mining | bibcorpus | 0 |
| `cross-domain argument mining` | supplementary:mining | acl | 0 |
| `cross-domain argument mining` | supplementary:mining | bibcorpus | 1 |
| `argument convincingness prediction` | supplementary:quality | acl | 0 |
| `argument convincingness prediction` | supplementary:quality | bibcorpus | 0 |
| `argument strength prediction` | supplementary:quality | acl | 0 |
| `argument strength prediction` | supplementary:quality | bibcorpus | 0 |
| `argumentation quality dimensions` | supplementary:quality | acl | 3 |
| `argumentation quality dimensions` | supplementary:quality | bibcorpus | 0 |
| `fallacy classification argumentation` | supplementary:quality | acl | 0 |
| `fallacy classification argumentation` | supplementary:quality | bibcorpus | 0 |
| `dialogical argumentation corpus` | supplementary:dialogue | acl | 0 |
| `dialogical argumentation corpus` | supplementary:dialogue | bibcorpus | 0 |
| `broadcast debate argument corpus` | supplementary:dialogue | acl | 0 |
| `broadcast debate argument corpus` | supplementary:dialogue | bibcorpus | 1 |
| `burden of proof dialogue` | supplementary:dialogue | acl | 0 |
| `burden of proof dialogue` | supplementary:dialogue | bibcorpus | 2 |
| `online debate persuasion corpus` | supplementary:dialogue | acl | 0 |
| `online debate persuasion corpus` | supplementary:dialogue | bibcorpus | 0 |
| `argument mining in dialogue` | supplementary:dialogue | acl | 0 |
| `argument mining in dialogue` | supplementary:dialogue | bibcorpus | 5 |
| `large language models argument quality` | supplementary:llm | acl | 0 |
| `large language models argument quality` | supplementary:llm | bibcorpus | 1 |
| `LLM fallacy detection` | supplementary:llm | acl | 0 |
| `LLM fallacy detection` | supplementary:llm | bibcorpus | 0 |
| `argument generation large language model` | supplementary:llm | acl | 0 |
| `argument generation large language model` | supplementary:llm | bibcorpus | 0 |
| `prompting for argument mining` | supplementary:llm | acl | 0 |
| `prompting for argument mining` | supplementary:llm | bibcorpus | 0 |
| `LLM as a judge argument` | supplementary:llm | acl | 0 |
| `LLM as a judge argument` | supplementary:llm | bibcorpus | 0 |
| `argument annotation scheme corpus` | supplementary:resources | acl | 0 |
| `argument annotation scheme corpus` | supplementary:resources | bibcorpus | 0 |
| `AIFdb argument corpus` | supplementary:resources | acl | 0 |
| `AIFdb argument corpus` | supplementary:resources | bibcorpus | 0 |
| `argument search engine corpus` | supplementary:resources | acl | 0 |
| `argument search engine corpus` | supplementary:resources | bibcorpus | 0 |
| `argument quality dataset` | supplementary:resources | acl | 2 |
| `argument quality dataset` | supplementary:resources | bibcorpus | 2 |
| `venue:argmining` | venue sweep | acl | 227 |
| `TARGER argument tagging neural` | github discovery | github | 1 |
| `TweetyProject argumentation java library` | github discovery | github | 1 |
| `argument mining dataset` | github discovery | github | 27 |
| `argument quality corpus` | github discovery | github | 3 |
| `argumentation framework solver tweety aspic` | github discovery | github | 0 |
| `computational argumentation` | github discovery | github | 103 |
| `fallacy detection dataset` | github discovery | github | 4 |
| `org:UKPLab argument` | github discovery | github | 23 |
| `org:webis-de argument` | github discovery | github | 24 |

## Appendix D - verification evidence

Source combinations behind the registry. A `bibcorpus` label counts once per independent repository, and never for a verbatim re-export of the ACL Anthology:

- acl, bibcorpus: 93
- acl: 89
- bibcorpus: 68

## Appendix E - caching layers

- layer 1, HTTP cache: metadata responses expire after 30 days, binaries never
- layer 2, status gating: each phase processes only records at exactly its input status; fetch also skips a PDF whose sha256 matches, extract skips text whose source PDF hash is unchanged
- layer 3, frontier memory: 19 of 139 nodes expanded, directions recorded per node
- layer 4, decision memory: 723 rejected candidates kept with their scores at criteria_version 1; bumping it re-scores them without re-fetching anything

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
