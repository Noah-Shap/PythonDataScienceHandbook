# 06 - Run report

Generated 2026-09-16T01:33:48+00:00 | cap 250 | criteria_version 1 | registry 250 entries

## Phases in this run

| Phase | Seconds | Summary |
|---|---|---|
| 0 scaffold | 0.3 | cap=250, field_map=deliverables/00-field-map.md |
| 1 seed | 5.5 |  |
| 2 snowball | 8.1 | admitted=231, admitted_corroborated=137, already_decided=15 |
| 3 verify | 0.0 | considered=232, oa_resolved=172, seconds=0.0 |
| 4 tier | 0.0 | considered=137, retiered=0, seconds=0.0 |
| 5a fetch | 7.6 | guidelines=12, manifest=deliverables/05-fetch-manifest.csv, manifest_rows=250 |
| 5b extract | 0.0 | guidelines_extracted=8, no_pdf=137 |
| 6 chunk | 0.0 | chunks=132, from_abstract=80, from_fulltext=0, from_guideline=52 |

## Corpus state

- status: {'chunked': 88, 'extracted': 49, 'candidate': 113}
- verification: {'verified': 137, 'unverified': 113}
- tiers: T1: 14, T2: 57, T3: 48, T4: 18
- doc types: conference: 162, workshop: 39, journal: 38, book: 3, preprint: 3, chapter: 3, unrecorded: 2
- frontier: 138 nodes, 18 expanded
- rejected ledger: 422 candidates remembered

## Area quotas

| Area | Quota | In registry | Verified | Met |
|---|---|---|---|---|
| formal | 30 | 38 | 18 | no |
| mining | 60 | 84 | 52 | no |
| quality | 40 | 58 | 25 | no |
| dialogue | 40 | 44 | 20 | no |
| llm | 40 | 54 | 22 | no |
| resources | 30 | 88 | 49 | yes |

Areas below quota and why: **formal** (18/30); **mining** (52/60); **quality** (25/40); **dialogue** (20/40); **llm** (22/40). See *Limits of this run* below.

## Source availability

| Source | Reachable | Detail |
|---|---|---|
| acl | yes | local clone at corpus/repos/acl-org__acl-anthology |
| acl_web | no | ProxyError: HTTPSConnectionPool(host='aclanthology.org', port=443): Max retries exceeded with url: / (Caused… |
| arxiv | no | ProxyError: HTTPSConnectionPool(host='export.arxiv.org', port=443): Max retries exceeded with url: /api/query… |
| bibcorpus | yes | 40 bibliography repositories configured |
| crossref | no | ProxyError: HTTPSConnectionPool(host='api.crossref.org', port=443): Max retries exceeded with url: /works?row… |
| github | yes | HTTP 200 |
| openalex | no | ProxyError: HTTPSConnectionPool(host='api.openalex.org', port=443): Max retries exceeded with url: /works?per… |
| semanticscholar | no | ProxyError: HTTPSConnectionPool(host='api.semanticscholar.org', port=443): Max retries exceeded with url: /gr… |
| unpaywall | no | ProxyError: HTTPSConnectionPool(host='api.unpaywall.org', port=443): Max retries exceeded with url: /v2/10.11… |

## Targeted searches (6.7)

| Query | Source | Hits |
|---|---|---|
| `argument mining` | acl | 40 |
| `argument mining` | bibcorpus | 40 |
| `argumentation mining survey` | acl | 0 |
| `argumentation mining survey` | bibcorpus | 1 |
| `argument quality assessment` | acl | 23 |
| `argument quality assessment` | bibcorpus | 7 |
| `fallacy detection` | acl | 26 |
| `fallacy detection` | bibcorpus | 6 |
| `argumentation scheme classification` | acl | 3 |
| `argumentation scheme classification` | bibcorpus | 1 |
| `inference anchoring theory` | acl | 9 |
| `inference anchoring theory` | bibcorpus | 3 |
| `dialogical argument mining` | acl | 2 |
| `dialogical argument mining` | bibcorpus | 1 |
| `argument interchange format` | acl | 0 |
| `argument interchange format` | bibcorpus | 7 |
| `large language models argument mining` | acl | 0 |
| `large language models argument mining` | bibcorpus | 0 |
| `LLM argument quality evaluation` | acl | 0 |
| `LLM argument quality evaluation` | bibcorpus | 0 |
| `argument mining dataset` | acl | 10 |
| `argument mining dataset` | bibcorpus | 1 |
| `argument annotation guidelines` | acl | 0 |
| `argument annotation guidelines` | bibcorpus | 0 |
| `debate transcript argument corpus` | acl | 0 |
| `debate transcript argument corpus` | bibcorpus | 0 |
| `persuasive essays corpus` | acl | 1 |
| `persuasive essays corpus` | bibcorpus | 0 |
| `IBM Debater` | acl | 2 |
| `IBM Debater` | bibcorpus | 0 |
| `args.me argument search` | acl | 0 |
| `args.me argument search` | bibcorpus | 1 |
| `Webis argument quality` | acl | 0 |
| `Webis argument quality` | bibcorpus | 0 |
| `Kialo` | acl | 5 |
| `Kialo` | bibcorpus | 0 |
| `internet argument corpus` | acl | 5 |
| `internet argument corpus` | bibcorpus | 1 |
| `moral maze` | acl | 0 |
| `moral maze` | bibcorpus | 0 |
| `TARGER argument tagging neural` | github | 1 |
| `TweetyProject argumentation java library` | github | 1 |
| `argument mining dataset` | github | 27 |
| `argument quality corpus` | github | 3 |
| `argumentation framework solver tweety aspic` | github | 0 |
| `computational argumentation` | github | 103 |
| `fallacy detection dataset` | github | 4 |
| `org:UKPLab argument` | github | 23 |
| `org:webis-de argument` | github | 24 |

## Verification evidence

Source combinations backing the registry (a `bibcorpus` label counts once per independent repository, and never for a verbatim re-export of the ACL Anthology):

- acl, bibcorpus: 98
- acl: 79
- bibcorpus: 73

## Retrieval, extraction, chunking

- PDFs: 0 fetched, 0 already cached, 137 unavailable
- repositories cloned: 8; guideline/README documents copied: 12
- extraction: 0 PDFs (0 pages), 8 guideline documents, 0 failures
- chunks: 132 (0 full text, 52 guideline, 80 abstract-only)

Why PDFs were not fetched:

- acl_web unreachable from this environment (ProxyError: HTTPSConnectionPool(host='aclanthology.org', por): 92
- no open-access PDF url resolved: 37
- arxiv unreachable from this environment (ProxyError: HTTPSConnectionPool(host='export.arxiv.org', por): 8

## Annotations

- written this run: 250; unchanged: 0
- grounding: {'fulltext': 0, 'abstract': 165, 'none': 85}
- every annotation quotes the retrieved text it was written from and names it in `grounded_on`; where nothing was retrieved the annotation says so and asserts nothing about content.

## Cost and caching

- HTTP: 0 network calls, 0 cache hits, 0 skipped because the source is unreachable, 0 retried errors
- layer 1 (HTTP cache): metadata responses expire after 30 days, PDFs never expire
- layer 2 (status gating): every phase processes only records at exactly its input status; fetch additionally skips a PDF whose sha256 matches, extract skips text whose source PDF hash is unchanged
- layer 3 (frontier memory): 18 of 138 nodes expanded; directions recorded per node
- layer 4 (decision memory): 422 rejected candidates kept with their scores at criteria_version 1; bumping it re-scores them without re-fetching anything

## Changelog

Run 1; previous run recorded at 2026-09-16T01:33:26+00:00.

Added 250 entries:

- `doi:10.1007/978-0-387-98197-0_19` - The Argument Interchange Format (2009, TNone)
- `doi:10.1007/978-3-030-30179-8_4` - Data Acquisition for Argument Search: The args.me corpus (2019, T3)
- `doi:10.1007/978-3-030-85251-1_4` - SubjectivITA: An Italian Corpus for Subjectivity Detection in Newspapers (2021, T3)
- `doi:10.1007/978-3-642-23963-2_10` - Argumentation Frameworks as Constraint Satisfaction Problems (2011, TNone)
- `doi:10.1007/s10458-009-9116-7` - On judgment aggregation in abstract argumentation (2011, T2)
- `doi:10.1007/s10506-010-9104-x` - Argumentation Mining (2011, T2)
- `doi:10.1016/0004-3702(94)00041-x` - On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Log… (1995, T1)
- `doi:10.1016/j.artint.2007.04.009` - Practical reasoning as presumptive argumentation using action based alternating transitio… (2007, TNone)
- `doi:10.1016/j.ipm.2019.102055` - The evolution of argumentation mining: From models to social media and emerging tools (2019, TNone)
- `doi:10.1017/cbo9780511802034` - Argumentation Schemes (2008, T1)
- `doi:10.1017/s0269888906001044` - Towards an Argument Interchange Format (2006, T1)
- `doi:10.1017/s0269888911000166` - An introduction to argumentation semantics (2011, T1)
- `doi:10.1038/s41586-021-03215-w` - An autonomous debating system (2021, T2)
- `doi:10.1080/19462166.2010.485698` - Assessing debate strategies via computational agents (2010, TNone)
- `doi:10.1080/19462166.2010.486479` - Answer-set programming encodings for argumentation frameworks (2010, T2)
- `doi:10.1080/19462166.2012.661766` - Relating Carneades with abstract argumentation via the ASPIC+ framework for structured ar… (2012, TNone)
- `doi:10.1080/19462166.2012.708670` - Distinctive features of persuasion and deliberation dialogues (2013, TNone)
- `doi:10.1080/19462166.2012.729861` - A corpus-based deconstructive strategy for critically engaging with arguments (2013, TNone)
- `doi:10.1080/19462166.2013.862303` - A natural language bipolar argumentation approach to support users in online debate inter… (2013, TNone)
- `doi:10.1080/19462166.2013.869764` - Introduction to structured argumentation (2014, T1)
- `doi:10.1080/19462166.2013.869766` - The ASPIC+ framework for structured argumentation: a tutorial (2014, T1)
- `doi:10.1080/19462166.2013.869767` - Defeasible logic programming: DeLP-servers, contextual queries, and explanations for answ… (2014, T2)
- `doi:10.1080/19462166.2013.869878` - A tutorial on assumption-based argumentation (2014, T1)
- `doi:10.1080/19462166.2014.1001790` - Context-aware reconfiguration of large-scale surveillance systems: argumentative approach (2015, T2)
- `doi:10.1080/19462166.2014.1002535` - Senses of 'argument' in instantiated argumentation frameworks (2015, TNone)
- `doi:10.1080/19462166.2015.1107134` - Probabilistic abstract argumentation: an investigation with Boltzmann machines (2015, TNone)
- `doi:10.1093/logcom/14.5.675` - Argumentation Semantics for Defeasible Logic (2004, TNone)
- `doi:10.1093/logcom/exp064` - A Relevance-theoretic Framework for Constructing and Deconstructing Enthymemes (2012, T2)
- `doi:10.1093/oso/9780198862536.003.0005` - Mining Property-driven Graphical Explanations for Data-centric AI from Argumentation Fram… (2022, TNone)
- `doi:10.1145/2701336.2701635` - Argumentation Mining: Where Are We Now, Where Do We Want to Be and How Do We Get There? (2013, T2)
- `doi:10.1145/2850417` - Argumentation Mining: State of the Art and Emerging Trends (2016, T1)
- `doi:10.1145/2872427.2883039` - Remedying Web Hijacking: Notification Effectiveness and Webmaster Comprehension (2016, T2)
- `doi:10.1145/2872427.2883081` - Winning Arguments: Interaction Dynamics and Persuasion Strategies in Good-Faith Online Di… (2016, T2)
- `doi:10.1145/2872427.2883091` - A Robust Framework for Estimating Linguistic Alignment in Twitter Conversations (2016, T2)
- `doi:10.1145/3308558.3314127` - Can You Give Me a Reason?: Argument-Inducing Online Forum by Argument Mining (2019, T2)
- `doi:10.1145/3350546.3352506` - TACAM: Topic And Context Aware Argument Mining (2019, TNone)
- `doi:10.1162/coli_a_00295` - Parsing Argumentation Structures in Persuasive Essays (2017, T3)
- `doi:10.1162/coli_a_00364` - Argument Mining: A Survey (2019, T1)
- `doi:10.1162/coli_a_00502` - Can Large Language Models Transform Computational Social Science? (2024, TNone)
- `doi:10.1162/tacl.a.38` - Elements of World Knowledge ( EWoK ): A Cognition-Inspired Framework for Evaluating Basic… (2025, TNone)
- `doi:10.1162/tacl_a_00481` - End-to-end Argument Mining with Cross-corpora Multi-task Learning (2022, TNone)
- `doi:10.1162/tacl_a_00718` - Holmes ⌕ A Benchmark to Assess the Linguistic Competence of Language Models (2024, TNone)
- `doi:10.1177/1461444807081230` - Democracy, deliberation and design: the case of online discussion forums (2007, T2)
- `doi:10.1609/aaai.v34i05.6270` - Corpus Wide Argument Mining - A Working Solution (2020, T3)
- `doi:10.18653/v1/2020.acl-main.447` - S2ORC: The Semantic Scholar Open Research Corpus (2020, TNone)
- `doi:10.18653/v1/2020.coling-main.402` - Rhetoric, Logic, and Dialectic: Advancing Theory-based Argument Quality Assessment in Nat… (2020, TNone)
- `doi:10.18653/v1/2020.coling-main.540` - Fact vs. Opinion: the Role of Argumentation Features in News Classification (2020, T2)
- `doi:10.18653/v1/2020.findings-emnlp.243` - Unsupervised Expressive Rules Provide Explainability and Assist Human Experts Grasping Ne… (2020, T3)
- `doi:10.18653/v1/2021.acl-long.107` - Towards Argument Mining for Social Good: A Survey (2021, T1)
- `doi:10.18653/v1/2021.acl-long.53` - Breaking Down the Invisible Wall of Informal Fallacies in Online Discussions (2021, T3)
- `doi:10.18653/v1/2021.argmining-1.8` - M-Arg: Multimodal Argument Mining Dataset for Political Debates with Audio and Transcripts (2021, TNone)
- `doi:10.18653/v1/2021.eacl-main.147` - Learning From Revisions: Quality Assessment of Claims in Argumentation at Scale (2021, TNone)
- `doi:10.18653/v1/2021.eacl-main.173` - I Beg to Differ: A study of constructive disagreement in online conversations (2021, TNone)
- `doi:10.18653/v1/2021.eacl-main.55` - End-to-End Argument Mining as Biaffine Dependency Parsing (2021, T2)
- `doi:10.18653/v1/2021.eacl-main.74` - Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering (2021, T3)
- `doi:10.18653/v1/2021.emnlp-main.461` - Efficient Nearest Neighbor Language Models (2021, TNone)
- `doi:10.18653/v1/2021.emnlp-main.515` - Hitting your MARQ: Multimodal ARgument Quality Assessment in Long Debate Video (2021, TNone)
- `doi:10.18653/v1/2021.emnlp-main.619` - Q^{2}: Evaluating Factual Consistency in Knowledge-Grounded Dialogues via Question Genera… (2021, T3)
- `doi:10.18653/v1/2021.naacl-main.8` - Mediators in Determining what Processing BERT Performs First (2021, T3)
- `doi:10.18653/v1/2021.semeval-1.7` - SemEval-2021 Task 6: Detection of Persuasion Techniques in Texts and Images (2021, T3)
- `doi:10.18653/v1/2022.acl-long.121` - Fully-Semantic Parsing and Generation: the BabelNet Meaning Representation (2022, T3)
- `doi:10.18653/v1/2022.acl-long.526` - Cluster & Tune: Boost Cold Start Performance in Text Classification (2022, T2)
- `doi:10.18653/v1/2022.conll-1.27` - Enhancing the Transformer Decoder with Transition-based Syntax (2022, T3)
- `doi:10.18653/v1/2022.emnlp-main.252` - How to disagree well: Investigating the dispute tactics used on Wikipedia (2022, T2)
- `doi:10.18653/v1/2022.emnlp-main.560` - Multitask Instruction-based Prompting for Fallacy Recognition (2022, T2)
- `doi:10.18653/v1/2022.findings-emnlp.306` - Graph Embeddings for Argumentation Quality Assessment (2022, TNone)
- `doi:10.18653/v1/2022.findings-emnlp.532` - Logical Fallacy Detection (2022, T2)
- `doi:10.18653/v1/2022.naacl-main.13` - Two Contrasting Data Annotation Paradigms for Subjective NLP Tasks (2022, T3)
- `doi:10.18653/v1/2023.acl-long.238` - Modeling Appropriate Language in Argumentation (2023, TNone)
- `doi:10.18653/v1/2023.acl-long.46` - ColD Fusion: Collaborative Descent for Distributed Multitask Finetuning (2023, T3)
- `doi:10.18653/v1/2023.acl-long.559` - DisentQA: Disentangling Parametric and Contextual Knowledge with Counterfactual Question… (2023, T3)
- `doi:10.18653/v1/2023.acl-long.708` - Understanding In-Context Learning via Supportive Pretraining Data (2023, T4)
- `doi:10.18653/v1/2023.argmining-1.14` - TILFA: A Unified Framework for Text, Image, and Layout Fusion in Argument Mining (2023, TNone)
- `doi:10.18653/v1/2023.argmining-1.9` - Dimensionality Reduction for Machine Learning-based Argument Mining (2023, TNone)
- `doi:10.18653/v1/2023.emnlp-main.128` - VivesDebate-Speech: A Corpus of Spoken Argumentation to Leverage Audio Features for Argum… (2023, TNone)
- `doi:10.18653/v1/2023.emnlp-main.645` - Contextual Interaction for Argument Post Quality Assessment (2023, TNone)
- `doi:10.18653/v1/2023.emnlp-main.684` - Argument-based Detection and Classification of Fallacies in Political Debates (2023, T4)
- `doi:10.18653/v1/2023.findings-acl.321` - Coupling Large Language Models with Logic Programming for Robust and General Reasoning fr… (2023, T4)
- `doi:10.18653/v1/2023.findings-emnlp.624` - In-Context Learning Creates Task Vectors (2023, TNone)
- `doi:10.18653/v1/2024.acl-long.240` - Missci: Reconstructing Fallacies in Misrepresented Science (2024, TNone)
- ... and 170 more

## Limits of this run

Unreachable sources: acl_web, arxiv, crossref, openalex, semanticscholar, unpaywall. Consequences:

- no citation-graph expansion (`reference` / `citation` directions stay pending in `frontier.jsonl`; a later run with network access expands exactly those nodes and nothing else);
- no citation counts, so the `cites_norm` component is computed from how many independent bibliographies list a work rather than from a citation count - the substitution is recorded per record in `score.components_source`;
- OA PDFs could not be downloaded, so most annotations are grounded on abstracts rather than full text, and most chunks are abstract chunks. Every entry is still in `05-fetch-manifest.csv` with a resolvable URL, so the PDFs can be fetched elsewhere and `python -m argmine extract chunk` picks them up without re-running anything else.

## Reproducing this run

```bash
python -m argmine run            # resume; every phase is idempotent
python -m argmine run --cap 400  # expand: only new work is done
python -m argmine status         # registry / frontier / rejection counts
```
