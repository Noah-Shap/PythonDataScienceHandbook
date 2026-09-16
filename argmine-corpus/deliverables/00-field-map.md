# 00 - Field map

The coverage contract for this corpus. Written in phase 0 **before any searching**, and
regenerated with live counts by every subsequent run. Six areas, each with a definition,
inclusion and exclusion criteria, the vocabulary used for keyword scoring, and a minimum
quota out of the 250-entry cap.

Generated: 2026-09-16T01:33:48+00:00 | criteria_version: 1


## Areas

| # | Area | Quota | In corpus |
|---|------|-------|-----------|
| 6.1 | Formal foundations (`formal`) | 30 | 38 |
| 6.2 | Argument mining (NLP) (`mining`) | 60 | 84 |
| 6.3 | Argument quality and evaluation (`quality`) | 40 | 58 |
| 6.4 | Dialogue and debate (`dialogue`) | 40 | 44 |
| 6.5 | LLM era, 2023-2026 (`llm`) | 40 | 54 |
| 6.6 | Datasets, tools, annotation guidelines (`resources`) | 30 | 88 |

### 6.1 Formal foundations  `formal`  (quota >= 30, currently 38)

**Definition.** Representational theory of argument: Toulmin layout; Walton argumentation schemes and critical questions; Dung abstract argumentation and its semantics (grounded, preferred, stable, semi-stable, ideal); structured argumentation (ASPIC+, assumption-based argumentation, DeLP); the Argument Interchange Format (AIF) ontology; Inference Anchoring Theory (IAT).

**Include.** The defining papers and the standard tutorials/surveys for each formalism.

**Exclude.** Pure proof-theory or complexity results with no representational payoff.

**Vocabulary.** weight 3: `abstract argumentation`, `admissible set`, `argument interchange format`, `argumentation framework`, `argumentation scheme`, `argumentation semantics`, `aspic`, `assumption-based argumentation`, `critical questions`, `defeasible logic programming`, `formal argumentation`, `grounded extension`, `inference anchoring theory`, `preferred extension`, `semi-stable`, `stable extension`, `structured argumentation`, `toulmin`; weight 2: `acceptability`, `aif`, `argument graph`, `attack relation`, `defeasible reasoning`, `delp`, `enthymeme`, `nonmonotonic`; weight 1: `dialectical`, `warrant`

### 6.2 Argument mining (NLP)  `mining`  (quota >= 60, currently 84)

**Definition.** Extraction of argument structure from text: argumentative discourse unit segmentation; component classification (claim, premise, major claim); relation classification (support, attack); argument structure parsing; scheme classification; cross-domain and cross-lingual transfer.

**Include.** Task-defining papers, the shared tasks, strong baselines.

**Exclude.** Papers whose only contribution is a leaderboard delta on a standard benchmark.

**Vocabulary.** weight 3: `argument component`, `argument extraction`, `argument mining`, `argument relation`, `argument segmentation`, `argument structure parsing`, `argumentation mining`, `argumentative discourse unit`, `claim detection`, `cross-domain argument`, `cross-lingual argument`, `premise`, `scheme classification`; weight 2: `argumentative`, `end-to-end argument`, `evidence detection`, `support and attack`; weight 1: `claim`, `discourse`, `sequence tagging`, `shared task`

### 6.3 Argument quality and evaluation  `quality`  (quota >= 40, currently 58)

**Definition.** Quality taxonomies (logical, rhetorical, dialectical); convincingness and pairwise ranking; argument strength; fallacy detection and classification; stance and stance-taking as they bear on quality.

**Include.** Taxonomy papers, dataset papers with annotation studies, evaluation-metric papers.

**Exclude.** Persuasion research aimed at marketing or compliance outcomes.

**Vocabulary.** weight 3: `argument quality`, `argument ranking`, `argument strength`, `argumentation quality`, `cogency`, `convincingness`, `fallacious`, `fallacy`, `logical fallacy`, `more convincing`, `quality dimensions`, `quality ranking`; weight 2: `ad hominem`, `pairwise ranking`, `persuasiveness`, `quality assessment`, `reasonableness`, `stance`, `stance detection`; weight 1: `effectiveness`, `taxonomy`

### 6.4 Dialogue and debate  `dialogue`  (quota >= 40, currently 44)

**Definition.** Dialogue games and protocols; IAT-annotated broadcast debates (Moral Maze, US2016, QT30); dialogical argument mining; reply structure and burden of proof; level-shifting and question-dodging phenomena; online argumentative dialogue (CMV, IAC, Kialo).

**Include.** Work that models who said what, in reply to what, with what dialogical force.

**Exclude.** Task-oriented dialogue systems with no argumentative representation.

**Vocabulary.** weight 3: `broadcast debate`, `burden of proof`, `change my view`, `changemyview`, `dialogical`, `dialogue game`, `dialogue protocol`, `illocutionary`, `inference anchoring theory`, `internet argument corpus`, `kialo`, `locution`, `moral maze`, `online debate`, `qt30`, `reply structure`, `televised debate`, `us2016`; weight 2: `cmv`, `debate`, `deliberation`, `disagreement`, `ethos`, `persuasive dialogue`, `question time`, `turn-taking`; weight 1: `conversation`, `transition`

### 6.5 LLM era, 2023-2026  `llm`  (quota >= 40, currently 54)

**Definition.** Large language models for argument mining, quality assessment, fallacy detection and argument generation; LLM-as-judge for argument quality; argument-based reasoning with LLMs; debate as an oversight or evaluation mechanism where it produces reusable argument representations.

**Include.** Work published 2023 or later that changes how the pipeline downstream of this corpus should be built.

**Exclude.** Safety-via-debate work that does not touch representation or evaluation of natural-language arguments.

**Vocabulary.** weight 3: `argument generation`, `chatgpt`, `counter-argument generation`, `gpt-4`, `large language model`, `large language models`, `llm`, `llm as a judge`, `llm-as-judge`, `multi-agent debate`; weight 2: `chain-of-thought`, `gpt-3`, `in-context learning`, `instruction-tuned`, `prompting`, `retrieval-augmented`; weight 1: `few-shot`, `generative`, `zero-shot`

### 6.6 Datasets, tools, annotation guidelines  `resources`  (quota >= 30, currently 88)

**Definition.** Corpora, software and the annotation manuals behind them, treated as documents in their own right. Corpora include AAEC (persuasive essays), UKP sentential argument mining, IBM Debater datasets (ArgQ, evidence, claims), CMV (Tan et al.), IAC, args.me, Webis argument quality corpora, US2016, QT30, Moral Maze corpora, ArgMining shared-task data, Kialo-derived datasets and logical-fallacy datasets. Tools include AIFdb, OVA, ArgumenText, TARGER, Tweety and other argumentation libraries, and ASPIC+/DeLP implementations.

**Include.** Dataset papers and the primary repo / README / guideline document.

**Exclude.** Derivative repackagings of an existing corpus.

**Vocabulary.** weight 3: `aifdb`, `annotated corpus`, `annotation guidelines`, `annotation scheme`, `annotation study`, `args.me`, `argumentext`, `corpus`, `dataset`, `ibm debater`, `inter-annotator agreement`, `persuasive essays`, `targer`, `toolkit`, `tweety`; weight 2: `benchmark`, `ova`, `resource`, `shared task data`, `ukp`, `we release`, `webis`; weight 1: `publicly available`


## Global exclusions

Applied before scoring, to every candidate:

- legal argument mining and scientific-abstract argument mining, **unless** the work is
  foundational to an area (admitted only at tier 1);
- sentiment / opinion mining;
- persuasion research aimed at marketing or compliance outcomes;
- non-English-only resources, unless the resource is a major multilingual benchmark.

Pattern list actually used by the scorer: `legal argument`, `legal reasoning`, `court`, `judicial`, `scientific abstract`, `biomedical`, `clinical`, `sentiment analysis`, `opinion mining`, `aspect-based sentiment`, `product review`, `marketing`, `advertis`.


## How an area is assigned

`keyword` score: title and abstract are matched against the per-area vocabulary below.
Each term carries a weight (3 = defining, 2 = strong, 1 = weak), doubled for a match in
the title and halved for one in the venue name; an area's raw score is the sum of the
weights it matches. The record's `keyword` component is its best area's raw score divided
by a saturation constant (12), capped at 1. A candidate is assigned its best
area plus every other area scoring at least 60% of the best or at least
40% of saturation, so genuinely cross-area work (a dialogue corpus paper, say)
counts toward both quotas.

Total candidate score = cites_norm 0.25, cocite 0.35, keyword 0.25, venue 0.15. `cocite` is multiplied by dialogue x1.25 for the areas
listed, because those areas sit closest to the downstream debate-transcript database.


## Targeted searches (6.7)

Run in phase 2 across every reachable source; each query and its hit count is logged in `06-run-report.md`.

- `argument mining`
- `argumentation mining survey`
- `argument quality assessment`
- `fallacy detection`
- `argumentation scheme classification`
- `inference anchoring theory`
- `dialogical argument mining`
- `argument interchange format`
- `large language models argument mining`
- `LLM argument quality evaluation`
- `argument mining dataset`
- `argument annotation guidelines`
- `debate transcript argument corpus`
- `persuasive essays corpus`
- `IBM Debater`
- `args.me argument search`
- `Webis argument quality`
- `Kialo`
- `internet argument corpus`
- `moral maze`

## Tier rubric

- **T1** - Foundational / survey. Read in full: theory anchors, major surveys, canonical papers. (14 in corpus)
- **T2** - Core method. Defines a task formulation, model, or evaluation still in use. (57 in corpus)
- **T3** - Dataset / tool / annotation guideline, including the guideline documents themselves. (48 in corpus)
- **T4** - Recent (2023-2026). LLM-era work; lower durability confidence, high build relevance. (18 in corpus)

## Downstream tags

`dialogue`, `quality`, `schemes`, `formal`, `extraction`, `dataset`, `fallacy`

## Evidence sources available to this run

| Source | Reachable | Detail |
|--------|-----------|--------|
| acl | yes | local clone at corpus/repos/acl-org__acl-anthology |
| acl_web | no | ProxyError: HTTPSConnectionPool(host='aclanthology.org', port=443): Max retries exceeded w |
| arxiv | no | ProxyError: HTTPSConnectionPool(host='export.arxiv.org', port=443): Max retries exceeded w |
| bibcorpus | yes | 40 bibliography repositories configured |
| crossref | no | ProxyError: HTTPSConnectionPool(host='api.crossref.org', port=443): Max retries exceeded w |
| github | yes | HTTP 200 |
| openalex | no | ProxyError: HTTPSConnectionPool(host='api.openalex.org', port=443): Max retries exceeded w |
| semanticscholar | no | ProxyError: HTTPSConnectionPool(host='api.semanticscholar.org', port=443): Max retries exc |
| unpaywall | no | ProxyError: HTTPSConnectionPool(host='api.unpaywall.org', port=443): Max retries exceeded  |
