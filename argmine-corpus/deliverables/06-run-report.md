# 06 - Run report

Generated 2026-09-16T02:03:12+00:00 | cap 250 | criteria_version 1 | registry 250 entries

## Phases in this run

| Phase | Seconds | Summary |
|---|---|---|
| 0 scaffold | 0.0 | cap=250, field_map=deliverables/00-field-map.md |
| 1 seed | 5.8 |  |
| 2 snowball | 21.9 | admitted=231, admitted_corroborated=121, already_decided=14 |
| 3 verify | 0.0 | considered=231, oa_resolved=179, seconds=0.0 |
| 4 tier | 0.0 | considered=140, retiered=0, seconds=0.0 |
| 5a fetch | 1.0 | guidelines=3, manifest=deliverables/05-fetch-manifest.csv, manifest_rows=250 |
| 5b extract | 0.0 | guidelines_extracted=3, no_pdf=140 |
| 6 chunk | 0.0 | chunks=101, from_abstract=93, from_fulltext=0, from_guideline=8 |

## Corpus state

- status: {'chunked': 96, 'extracted': 44, 'candidate': 110}
- verification: {'verified': 140, 'unverified': 110}
- tiers: T1: 15, T2: 71, T3: 39, T4: 15
- doc types: conference: 121, workshop: 87, journal: 37, book: 2, preprint: 1, chapter: 1, unrecorded: 1
- frontier: 140 nodes, 19 expanded
- rejected ledger: 725 candidates remembered

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

## Targeted searches

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

## Verification evidence

Source combinations backing the registry (a `bibcorpus` label counts once per independent repository, and never for a verbatim re-export of the ACL Anthology):

- acl, bibcorpus: 95
- acl: 90
- bibcorpus: 65

## Retrieval, extraction, chunking

- PDFs: 0 fetched, 0 already cached, 140 unavailable
- repositories cloned: 3; guideline/README documents copied: 3
- extraction: 0 PDFs (0 pages), 3 guideline documents, 0 failures
- chunks: 101 (0 full text, 8 guideline, 93 abstract-only)

Why PDFs were not fetched:

- acl_web unreachable from this environment (ProxyError: HTTPSConnectionPool(host='aclanthology.org', por): 94
- no open-access PDF url resolved: 44
- arxiv unreachable from this environment (ProxyError: HTTPSConnectionPool(host='export.arxiv.org', por): 2

## Annotations

- written this run: 250; unchanged: 0
- grounding: {'fulltext': 0, 'abstract': 188, 'none': 62}
- every annotation quotes the retrieved text it was written from and names it in `grounded_on`; where nothing was retrieved the annotation says so and asserts nothing about content.

## Cost and caching

- HTTP: 0 network calls, 0 cache hits, 0 skipped because the source is unreachable, 0 retried errors
- layer 1 (HTTP cache): metadata responses expire after 30 days, PDFs never expire
- layer 2 (status gating): every phase processes only records at exactly its input status; fetch additionally skips a PDF whose sha256 matches, extract skips text whose source PDF hash is unchanged
- layer 3 (frontier memory): 19 of 140 nodes expanded; directions recorded per node
- layer 4 (decision memory): 725 rejected candidates kept with their scores at criteria_version 1; bumping it re-scores them without re-fetching anything

## Changelog

Run 1; previous run recorded at 2026-09-16T02:02:43+00:00.

Added 250 entries:

- `doi:10.1007/978-0-387-98197-0_19` - The Argument Interchange Format (2009, TNone)
- `doi:10.1007/978-3-642-23963-2_10` - Argumentation Frameworks as Constraint Satisfaction Problems (2011, TNone)
- `doi:10.1007/s10458-009-9116-7` - On judgment aggregation in abstract argumentation (2011, T2)
- `doi:10.1007/s10506-010-9104-x` - Argumentation Mining (2011, T2)
- `doi:10.1007/s10579-019-09446-8` - Argumentation in the 2016 US presidential elections: annotated corpora of television deba… (2019, T2)
- `doi:10.1016/0004-3702(94)00041-x` - On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Log… (1995, T1)
- `doi:10.1016/j.artint.2007.04.010` - The Carneades model of argument and burden of proof (2007, T2)
- `doi:10.1016/j.artint.2015.12.004` - Argument Graphs and Assumption-based Argumentation (2016, T2)
- `doi:10.1017/cbo9780511802034` - Argumentation Schemes (2008, T1)
- `doi:10.1017/s0269888906001044` - Towards an Argument Interchange Format (2006, T1)
- `doi:10.1017/s0269888911000166` - An introduction to argumentation semantics (2011, T1)
- `doi:10.1038/s41586-021-03215-w` - An autonomous debating system (2021, T2)
- `doi:10.1080/19462160903564592` - An abstract framework for argumentation with structured arguments (2010, T2)
- `doi:10.1080/19462166.2010.486479` - Answer-set programming encodings for argumentation frameworks (2010, T2)
- `doi:10.1080/19462166.2012.661766` - Relating Carneades with abstract argumentation via the ASPIC+ framework for structured ar… (2012, TNone)
- `doi:10.1080/19462166.2012.708670` - Distinctive features of persuasion and deliberation dialogues (2013, TNone)
- `doi:10.1080/19462166.2013.862303` - A natural language bipolar argumentation approach to support users in online debate inter… (2013, TNone)
- `doi:10.1080/19462166.2013.869764` - Introduction to structured argumentation (2014, T1)
- `doi:10.1080/19462166.2013.869766` - The ASPIC+ framework for structured argumentation: a tutorial (2014, T1)
- `doi:10.1080/19462166.2013.869767` - Defeasible logic programming: DeLP-servers, contextual queries, and explanations for answ… (2014, T2)
- `doi:10.1080/19462166.2013.869878` - A tutorial on assumption-based argumentation (2014, T1)
- `doi:10.1080/19462166.2014.1001790` - Context-aware reconfiguration of large-scale surveillance systems: argumentative approach (2015, T2)
- `doi:10.1093/logcom/14.5.675` - Argumentation Semantics for Defeasible Logic (2004, T2)
- `doi:10.1111/coin.12111` - Assumption-Based Argumentation Equipped with Preferences and its Application to Decision… (2017, T2)
- `doi:10.1145/2850417` - Argumentation Mining: State of the Art and Emerging Trends (2016, T1)
- `doi:10.1145/2872427.2883081` - Winning Arguments: Interaction Dynamics and Persuasion Strategies in Good-Faith Online Di… (2016, T2)
- `doi:10.1145/3308558.3314127` - Can You Give Me a Reason?: Argument-Inducing Online Forum by Argument Mining (2019, T2)
- `doi:10.1162/coli_a_00276` - Argumentation Mining in User-Generated Web Discourse (2017, T3)
- `doi:10.1162/coli_a_00295` - Parsing Argumentation Structures in Persuasive Essays (2017, T3)
- `doi:10.1162/coli_a_00364` - Argument Mining: A Survey (2019, T1)
- `doi:10.1162/coli_a_00553` - UniASA: A Unified Generative Framework for Argument Structure Analysis (2025, TNone)
- `doi:10.1162/tacl_a_00481` - End-to-end Argument Mining with Cross-corpora Multi-task Learning (2022, TNone)
- `doi:10.1177/1461444807081230` - Democracy, deliberation and design: the case of online discussion forums (2007, T2)
- `doi:10.1609/aaai.v34i05.6270` - Corpus Wide Argument Mining - A Working Solution (2020, T3)
- `doi:10.1609/aaai.v34i05.6285` - A large-scale dataset for argument quality ranking: Construction and analysis (2020, T3)
- `doi:10.18653/v1/2020.acl-main.298` - Towards Better Non-Tree Argument Mining: Proposition-Level Biaffine Parsing with Task-Spe… (2020, T2)
- `doi:10.18653/v1/2020.coling-main.128` - Contextual Argument Component Classification for Class Discussions (2020, T2)
- `doi:10.18653/v1/2020.coling-main.402` - Rhetoric, Logic, and Dialectic: Advancing Theory-based Argument Quality Assessment in Nat… (2020, TNone)
- `doi:10.18653/v1/2021.acl-long.107` - Towards Argument Mining for Social Good: A Survey (2021, T1)
- `doi:10.18653/v1/2021.acl-long.497` - A Neural Transition-based Model for Argumentation Mining (2021, TNone)
- `doi:10.18653/v1/2021.acl-long.53` - Breaking Down the Invisible Wall of Informal Fallacies in Online Discussions (2021, T3)
- `doi:10.18653/v1/2021.argmining-1.1` - Argument Mining on Twitter: A Case Study on the Planned Parenthood Debate (2021, T2)
- `doi:10.18653/v1/2021.argmining-1.10` - Argumentation Mining in Scientific Literature for Sustainable Development (2021, TNone)
- `doi:10.18653/v1/2021.argmining-1.13` - Predicting Moderation of Deliberative Arguments: Is Argument Quality the Key? (2021, T2)
- `doi:10.18653/v1/2021.argmining-1.16` - Overview of the 2021 Key Point Analysis Shared Task (2021, T3)
- `doi:10.18653/v1/2021.argmining-1.19` - Key Point Analysis via Contrastive Learning and Extractive Argument Summarization (2021, T2)
- `doi:10.18653/v1/2021.argmining-1.4` - Image Retrieval for Arguments Using Stance-Aware Query Expansion (2021, T2)
- `doi:10.18653/v1/2021.argmining-1.9` - Citizen Involvement in Urban Planning - How Can Municipalities Be Supported in Evaluating… (2021, TNone)
- `doi:10.18653/v1/2021.eacl-main.55` - End-to-End Argument Mining as Biaffine Dependency Parsing (2021, T2)
- `doi:10.18653/v1/2021.emnlp-main.515` - Hitting your MARQ: Multimodal ARgument Quality Assessment in Long Debate Video (2021, TNone)
- `doi:10.18653/v1/2021.naacl-main.34` - Aspect-Controlled Neural Argument Generation (2021, T2)
- `doi:10.18653/v1/2022.emnlp-main.560` - Multitask Instruction-based Prompting for Fallacy Recognition (2022, T2)
- `doi:10.18653/v1/2022.emnlp-main.713` - A Generative Model for End-to-End Argument Mining with Reconstructed Positional Encoding… (2022, TNone)
- `doi:10.18653/v1/2022.findings-emnlp.306` - Graph Embeddings for Argumentation Quality Assessment (2022, TNone)
- `doi:10.18653/v1/2022.findings-emnlp.532` - Logical Fallacy Detection (2022, T2)
- `doi:10.18653/v1/2023.acl-long.238` - Modeling Appropriate Language in Argumentation (2023, TNone)
- `doi:10.18653/v1/2023.argmining-1.1` - Detecting Argumentative Fallacies in the Wild: Problems and Limitations of Large Language… (2023, T4)
- `doi:10.18653/v1/2023.argmining-1.13` - IUST at ImageArg: The First Shared Task in Multimodal Argument Mining (2023, TNone)
- `doi:10.18653/v1/2023.argmining-1.26` - SuryaKiran at PragTag 2023 - Benchmarking Domain Adaptation using Masked Language Modelin… (2023, TNone)
- `doi:10.18653/v1/2023.argmining-1.9` - Dimensionality Reduction for Machine Learning-based Argument Mining (2023, TNone)
- `doi:10.18653/v1/2023.emnlp-main.684` - Argument-based Detection and Classification of Fallacies in Political Debates (2023, T4)
- `doi:10.18653/v1/2023.findings-acl.209` - End-to-End Argument Mining over Varying Rhetorical Structures (2023, TNone)
- `doi:10.18653/v1/2023.findings-eacl.187` - Bridging Argument Quality and Deliberative Quality Annotations with Adapters (2023, T3)
- `doi:10.18653/v1/2023.findings-emnlp.724` - Argument mining as a multi-hop generative machine reading comprehension task (2023, TNone)
- `doi:10.18653/v1/2024.acl-long.240` - Missci: Reconstructing Fallacies in Misrepresented Science (2024, TNone)
- `doi:10.18653/v1/2024.acl-long.275` - PITA: Prompting Task Interaction for Argumentation Mining (2024, TNone)
- `doi:10.18653/v1/2024.argmining-1.10` - KnowComp at DialAM-2024: Fine-tuning Pre-trained Language Models for Dialogical Argument… (2024, T4)
- `doi:10.18653/v1/2024.argmining-1.11` - KNOWCOMP POKEMON Team at DialAM-2024: A Two-Stage Pipeline for Detecting Relations in Dia… (2024, T4)
- `doi:10.18653/v1/2024.argmining-1.12` - Pungene at DialAM-2024: Identification of Propositional and Illocutionary Relations (2024, T4)
- `doi:10.18653/v1/2024.argmining-1.13` - Turiya at DialAM-2024: Inference Anchoring Theory Based LLM Parsers (2024, T4)
- `doi:10.18653/v1/2024.argmining-1.15` - Sövereign at The Perspective Argument Retrieval Shared Task 2024: Using LLMs with Argumen… (2024, TNone)
- `doi:10.18653/v1/2024.argmining-1.4` - Exploiting Dialogue Acts and Context to Identify Argumentative Relations in Online Debates (2024, TNone)
- `doi:10.18653/v1/2024.argmining-1.7` - MAMKit: A Comprehensive Multimodal Argument Mining Toolkit (2024, T3)
- `doi:10.18653/v1/2024.argmining-1.8` - Overview of DialAM-2024: Argument Mining in Natural Language Dialogues (2024, T1)
- `doi:10.18653/v1/2024.argmining-1.9` - DFKI-MLST at DialAM-2024 Shared Task: System Description (2024, T3)
- `doi:10.18653/v1/2024.conll-1.9` - Critical Questions Generation: Motivation and Challenges (2024, T3)
- `doi:10.18653/v1/2024.eacl-long.121` - Argument Mining as a Text-to-Text Generation Task (2024, T3)
- `doi:10.18653/v1/2024.emnlp-main.1155` - Let’s discuss! Quality Dimensions and Annotated Datasets for Computational Argument Quali… (2024, TNone)
- `doi:10.18653/v1/2024.emnlp-main.16` - Systematic Biases in LLM Simulations of Debates (2024, T4)
- `doi:10.18653/v1/2024.emnlp-main.39` - CoCoLoFa: A Dataset of News Comments with Common Logical Fallacies Written by LLM-Assiste… (2024, T3)
- ... and 170 more

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
