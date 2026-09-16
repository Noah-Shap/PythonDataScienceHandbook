# 01 - Annotated bibliography

154 verified entries, grouped by area and then by tier. Every entry here agreed across at least two independent metadata sources; anything that did not is in `99-unverified-and-rejected.md`. Each annotation says which retrieved text it was written from (`grounded_on`), and quotes that text rather than paraphrasing it from outside knowledge.

Generated 2026-09-16T01:41:16+00:00 | criteria_version 1 | cap 250

**Added in the latest run (250):** `doi:10.1007/978-0-387-98197-0_19`, `doi:10.1007/978-3-030-30179-8_4`, `doi:10.1007/978-3-030-85251-1_4`, `doi:10.1007/978-3-642-16952-6_5`, `doi:10.1007/978-3-642-23963-2_10`, `doi:10.1007/978-3-642-40381-1_7`, `doi:10.1007/s10458-009-9116-7`, `doi:10.1007/s10506-010-9104-x`, `doi:10.1007/s13218-021-00714-w`, `doi:10.1016/0004-3702(94)00041-x`, `doi:10.1016/j.artint.2007.04.009`, `doi:10.1016/j.artint.2007.04.010`, `doi:10.1016/j.engappai.2024.108231`, `doi:10.1017/cbo9780511802034`, `doi:10.1017/s0269888906001044`, `doi:10.1017/s0269888911000166`, `doi:10.1038/s41586-021-03215-w`, `doi:10.1080/19462160903564592`, `doi:10.1080/19462166.2010.485698`, `doi:10.1080/19462166.2010.486479`, `doi:10.1080/19462166.2012.661766`, `doi:10.1080/19462166.2012.708670`, `doi:10.1080/19462166.2013.862303`, `doi:10.1080/19462166.2013.869764`, `doi:10.1080/19462166.2013.869766`, `doi:10.1080/19462166.2013.869767`, `doi:10.1080/19462166.2013.869878`, `doi:10.1080/19462166.2014.1001790`, `doi:10.1093/logcom/14.5.675`, `doi:10.1093/logcom/exp064`, `doi:10.1145/2850417`, `doi:10.1145/2872427.2874816`, `doi:10.1145/2872427.2882972`, `doi:10.1145/2872427.2882979`, `doi:10.1145/2872427.2882983`, `doi:10.1145/2872427.2882987`, `doi:10.1145/2872427.2882998`, `doi:10.1145/2872427.2883007`, `doi:10.1145/2872427.2883018`, `doi:10.1145/2872427.2883033` ...

## 6.1 Formal foundations (19 entries, quota 30)

### T1 - Foundational / survey. Read in full: theory anchors, major surveys, canonical papers.

#### John Lawrence and Chris Reed (2019). *Argument Mining: A Survey*. Computational Linguistics, Volume 45, Issue 4 - December 2019.

- `doi:10.1162/coli_a_00364` | aliases: `acl:J19-4006`, `doi:10.1162/coli`
- doc_type: `journal` | tier: T1 | tags: extraction, formal | also in: mining
- [landing](https://aclanthology.org/J19-4006/) | [OA PDF](https://aclanthology.org/J19-4006.pdf)
- verified against: acl, bibcorpus:CogSciPrag/project_ideas, bibcorpus:ljvmiranda921/ljvmiranda921.github.io, bibcorpus:lmlearning/AFGraphLib, bibcorpus:m0re4u/paper-database, bibcorpus:mystreamer/lt2326-final-project
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Argument mining is the automatic identification and extraction of the structure of inference and reasoning expressed as arguments presented in natural language." "This survey explores the techniques that establish the foundations for argument mining, provides a review of recent advances in argument mining techniques, and discusses the challenges faced in automatically extracting a deeper understanding of reasoning expressed in language in general." For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@article{lawrence2019argumentm,
  title = {Argument Mining: A Survey},
  author = {John Lawrence and Chris Reed},
  year = {2019},
  journal = {Computational Linguistics, Volume 45, Issue 4 - December 2019},
  doi = {10.1162/coli_a_00364},
  url = {https://aclanthology.org/J19-4006/},
}
```

</details>

#### Pietro Baroni, Dov Gabbay, Massimiliano Giacomin and Leendert van der Torre (2018). *Handbook of Formal Argumentation*. College Publications.

- `title:c01257ffd78768bab2a908ba8509b177ebd2f015`
- doc_type: `book` | tier: T1 | tags: formal
- no URL recorded
- verified against: bibcorpus:KWARC/bibs, bibcorpus:lmlearning/AFGraphLib, bibcorpus:p4s3r0/argumentation-framework-clustering, bibcorpus:slatex/sTeX | note: author list missing from one source; venue not corroborated by both sources
- score 0.2875 (cites 0.0, cocite 0.25, keyword 0.5, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (book, College Publications, 2018), verified against 4 sources. For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

<details><summary>BibTeX</summary>

```bibtex
@book{baroni2018handbooko,
  title = {Handbook of Formal Argumentation},
  author = {Pietro Baroni and Dov Gabbay and Massimiliano Giacomin and Leendert van der Torre},
  year = {2018},
  publisher = {College Publications},
}
```

</details>

####  (2014). *A tutorial on assumption-based argumentation*. Argument & Computation.

- `doi:10.1080/19462166.2013.869878`
- doc_type: `journal` | tier: T1 | tags: formal
- no URL recorded
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:p4s3r0/argumentation-framework-clustering
- score 0.4062 (cites 0.0, cocite 0.375, keyword 0.5, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Argument & Computation, 2014), verified against 2 sources. For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

<details><summary>BibTeX</summary>

```bibtex
@article{toni2014atutorial,
  title = {A tutorial on assumption-based argumentation},
  author = {Francesca Toni},
  year = {2014},
  journal = {Argument & Computation},
  doi = {10.1080/19462166.2013.869878},
}
```

</details>

#### Philippe Besnard et al. (2014). *Introduction to structured argumentation*. Argument & Computation.

- `doi:10.1080/19462166.2013.869764`
- doc_type: `journal` | tier: T1 | tags: formal
- no URL recorded
- verified against: bibcorpus:KWARC/bibs, bibcorpus:davidar/dblp.yaml, bibcorpus:slatex/sTeX
- score 0.3187 (cites 0.0, cocite 0.125, keyword 0.5, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Argument & Computation, 2014), verified against 3 sources. For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

<details><summary>BibTeX</summary>

```bibtex
@article{besnard2014introducti,
  title = {Introduction to structured argumentation},
  author = {Philippe Besnard and Alejandro Garcia and Anthony Hunter and Sanjay Modgil and Henry Prakken and Guillermo Simari and Francesca Toni},
  year = {2014},
  journal = {Argument & Computation},
  doi = {10.1080/19462166.2013.869764},
}
```

</details>

#### Sanjay Modgil and Henry Prakken (2014). *The ASPIC+ framework for structured argumentation: a tutorial*. Argument & Computation.

- `doi:10.1080/19462166.2013.869766` | aliases: `doi:10.1080/1946216yyxxxxxxxx`
- doc_type: `journal` | tier: T1 | tags: formal
- [landing](http://www.informaworld.com)
- verified against: bibcorpus:KWARC/bibs, bibcorpus:davidar/dblp.yaml, bibcorpus:lmlearning/AFGraphLib, bibcorpus:slatex/sTeX
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This article gives a tutorial introduction to the ASPIC + framework for structured argumentation." "The philosophical and conceptual underpinnings of ASPIC + are discussed, the main definitions are illustrated with examples and several ways are discussed to instantiate the framework and to reconstruct other approaches as special cases of the framework." For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

<details><summary>BibTeX</summary>

```bibtex
@article{modgil2014theaspic,
  title = {The ASPIC+ framework for structured argumentation: a tutorial},
  author = {Sanjay Modgil and Henry Prakken},
  year = {2014},
  journal = {Argument & Computation},
  doi = {10.1080/19462166.2013.869766},
  url = {http://www.informaworld.com},
}
```

</details>

#### Pietro Baroni, Martin Caminada and Massimiliano Giacomin (2011). *An introduction to argumentation semantics*. Knowledge Eng. Review.

- `doi:10.1017/s0269888911000166`
- doc_type: `journal` | tier: T1 | tags: extraction, formal
- no URL recorded
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:p4s3r0/argumentation-framework-clustering, bibcorpus:ttmassa/ter
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "One-class classification (OCC) algorithms aim to build classification models when the negative class is either absent, poorly sampled or not well defined." "In this paper, we present a unified view of the general problem of OCC by presenting a taxonomy of study for OCC problems, which is based on the availability of training data, algorithms used and the application domains applied." For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@article{baroni2011anintrodu,
  title = {An introduction to argumentation semantics},
  author = {Pietro Baroni and Martin Caminada and Massimiliano Giacomin},
  year = {2011},
  journal = {Knowledge Eng. Review},
  doi = {10.1017/s0269888911000166},
}
```

</details>

#### Douglas Walton, Christopher Reed and Fabrizio Macagno (2008). *Argumentation Schemes*. Cambridge University Press.

- `doi:10.1017/cbo9780511802034`
- doc_type: `book` | tier: T1 | tags: formal, schemes
- [landing](http://www.cambridge.org/us/academic/subjects/philosophy/logic/argumentation-schemes)
- verified against: bibcorpus:KWARC/bibs, bibcorpus:carneades/carneades-3, bibcorpus:davidar/dblp.yaml, bibcorpus:slatex/sTeX
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (book, Cambridge University Press, 2008), verified against 4 sources. For a debate-transcript argument database it supplies argumentation-scheme and critical-question structure, which is how stored inferences can be typed rather than left as untyped support links; and it supplies the formal semantics for deciding what stands once arguments and attacks are stored.

<details><summary>BibTeX</summary>

```bibtex
@book{walton2008argumentat,
  title = {Argumentation Schemes},
  author = {Douglas Walton and Christopher Reed and Fabrizio Macagno},
  year = {2008},
  publisher = {Cambridge University Press},
  doi = {10.1017/cbo9780511802034},
  url = {http://www.cambridge.org/us/academic/subjects/philosophy/logic/argumentation-schemes},
}
```

</details>

#### Carlos Chesñevar et al. (2006). *Towards an Argument Interchange Format*. The Knowledge Engineering Review.

- `doi:10.1017/s0269888906001044`
- doc_type: `journal` | tier: T1 | tags: formal
- [landing](http://dx.doi.org/10.1017/s0269888906001044)
- verified against: bibcorpus:KWARC/bibs, bibcorpus:davidar/dblp.yaml, bibcorpus:slatex/sTeX
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, The Knowledge Engineering Review, 2006), verified against 3 sources. For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

<details><summary>BibTeX</summary>

```bibtex
@article{chesevar2006towardsan,
  title = {Towards an Argument Interchange Format},
  author = {Carlos Chesñevar and Jarred McGinnis and Sanjay Modgil and Iyad Rahwan and Chris Reed and Guillermo Simari and Matthew South and Gerard Vreeswijk and Steven Willmott},
  year = {2006},
  journal = {The Knowledge Engineering Review},
  doi = {10.1017/s0269888906001044},
  url = {http://dx.doi.org/10.1017/s0269888906001044},
}
```

</details>

####  (1995). *On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Logic Programming and n-Person Games*. Artificial Intelligence.

- `doi:10.1016/0004-3702(94)00041-x`
- doc_type: `journal` | tier: T1 | tags: formal
- [landing](https://www.sciencedirect.com/science/article/pii/000437029400041X)
- verified against: bibcorpus:KWARC/bibs, bibcorpus:aig-hagen/aig-templates, bibcorpus:lmlearning/AFGraphLib, bibcorpus:ochyai/open-japan-politech-platform, bibcorpus:p4s3r0/argumentation-framework-clustering, bibcorpus:slatex/sTeX, bibcorpus:smucclaw/complaw, bibcorpus:ttmassa/ter | note: bibcorpus:davidar/dblp.yaml: venue mismatch ('Artificial Intelligence' vs 'Artif. Intell.')
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Then we argue for the "correctness" or "appropriateness" of our theory with two strong arguments." "By showing that argumentation can be viewed as a special form of logic programming with negation as failure, we introduce a general logic-programming-based method for generating meta-interpreters for argumentation systems, a method very much similar to the compiler-compiler idea in conventional programming. © 1995." For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

<details><summary>BibTeX</summary>

```bibtex
@article{dung1995ontheacc,
  title = {On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Logic Programming and n-Person Games},
  author = {P.M. Dung},
  year = {1995},
  journal = {Artificial Intelligence},
  doi = {10.1016/0004-3702(94)00041-x},
  url = {https://www.sciencedirect.com/science/article/pii/000437029400041X},
}
```

</details>

### T2 - Core method. Defines a task formulation, model, or evaluation still in use.

#### Meiqian Zhao et al. (2018). *BLCU_NLP at SemEval-2018 Task 12: An Ensemble Model for Argument Reasoning Based on Hierarchical Attention*. Proceedings of the 12th International Workshop on Semantic Evaluation.

- `doi:10.18653/v1/s18-1186` | aliases: `acl:S18-01186`
- doc_type: `workshop` | tier: T2 | tags: extraction, formal | also in: mining
- [landing](https://aclanthology.org/S18-01186/) | [OA PDF](https://aclanthology.org/S18-01186.pdf) (via acl)
- verified against: acl, bibcorpus:IKMLab/arct2
- score 0.1833 (cites 0.0, cocite 0.25, keyword 0.0833, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "To comprehend an argument and fill the gap between claims and reasons, it is vital to find the implicit supporting warrants behind." "In this paper, we propose a hierarchical attention model to identify the right warrant which explains why the reason stands for the claim." For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{zhao2018blcunlpa,
  title = {BLCU_NLP at SemEval-2018 Task 12: An Ensemble Model for Argument Reasoning Based on Hierarchical Attention},
  author = {Meiqian Zhao and Chunhua Liu and Lu Liu and Yan Zhao and Dong Yu},
  year = {2018},
  booktitle = {Proceedings of the 12th International Workshop on Semantic Evaluation},
  doi = {10.18653/v1/s18-1186},
  url = {https://aclanthology.org/S18-01186/},
}
```

</details>

#### Fabrizio Macagno, Douglas Walton and Chris Reed (2017). *Argumentation Schemes. History, Classifications, and Computational Applications*. IFCoLog Journal of Logics and Their Applications.

- `title:156478672e00c4f4e6cb6079e97120915f66c518`
- doc_type: `journal` | tier: T2 | tags: formal, schemes
- [landing](http://dougwalton.ca/papers in pdf/17IFColog SCHEMES.pdf)
- verified against: bibcorpus:KWARC/bibs, bibcorpus:slatex/sTeX
- score 0.2 (cites 0.0, cocite 0.0, keyword 0.5, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, IFCoLog Journal of Logics and Their Applications, 2017), verified against 2 sources. For a debate-transcript argument database it supplies argumentation-scheme and critical-question structure, which is how stored inferences can be typed rather than left as untyped support links; and it supplies the formal semantics for deciding what stands once arguments and attacks are stored.

<details><summary>BibTeX</summary>

```bibtex
@article{macagno2017argumentat,
  title = {Argumentation Schemes. History, Classifications, and Computational Applications},
  author = {Fabrizio Macagno and Douglas Walton and Chris Reed},
  year = {2017},
  journal = {IFCoLog Journal of Logics and Their Applications},
  url = {http://dougwalton.ca/papers in pdf/17IFColog SCHEMES.pdf},
}
```

</details>

#### Pavithra Rajendran, Danushka Bollegala and Simon Parsons (2016). *Contextual stance classification of opinions: A step towards enthymeme reconstruction in online reviews*. Proceedings of the Third Workshop on Argument Mining (ArgMining2016).

- `doi:10.18653/v1/w16-2804` | aliases: `acl:W16-2804`
- doc_type: `workshop` | tier: T2 | tags: extraction, formal, quality | also in: quality
- [landing](https://aclanthology.org/W16-2804/) | [OA PDF](https://aclanthology.org/W16-2804.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.2333 (cites 0.0, cocite 0.0, keyword 0.3333, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (workshop, Proceedings of the Third Workshop on Argument Mining (ArgMining2016), 2016), verified against 2 sources. For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it supplies the formal semantics for deciding what stands once arguments and attacks are stored.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{rajendran2016contextual,
  title = {Contextual stance classification of opinions: A step towards enthymeme reconstruction in online reviews},
  author = {Pavithra Rajendran and Danushka Bollegala and Simon Parsons},
  year = {2016},
  booktitle = {Proceedings of the Third Workshop on Argument Mining (ArgMining2016)},
  doi = {10.18653/v1/w16-2804},
  url = {https://aclanthology.org/W16-2804/},
}
```

</details>

#### Peter Novák 0001 and Cees Witteveen (2015). *Context-aware reconfiguration of large-scale surveillance systems: argumentative approach*. Argument & Computation.

- `doi:10.1080/19462166.2014.1001790`
- doc_type: `journal` | tier: T2 | tags: extraction, formal
- [landing](http://content.iospress.com/doi/10.1080/19462166.2014.1001790)
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:lmlearning/AFGraphLib | note: author order differs (0001 / novak)
- score 0.3812 (cites 0.0, cocite 0.125, keyword 0.75, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Here, we describe the Metis system prototype and introduce a theoretical framework for modelling scalable information-aggregation systems." "The proposed continuous reconfiguration algorithm relies on standard results from abstract argumentation and corresponds to computation of a grounded extension of the argumentation framework associated with the system." For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@article{anon2015contextaw,
  title = {Context-aware reconfiguration of large-scale surveillance systems: argumentative approach},
  author = {Peter Novák 0001 and Cees Witteveen},
  year = {2015},
  journal = {Argument & Computation},
  doi = {10.1080/19462166.2014.1001790},
  url = {http://content.iospress.com/doi/10.1080/19462166.2014.1001790},
}
```

</details>

#### Alejandro J. García and Guillermo R. Simari (2014). *Defeasible logic programming: DeLP-servers, contextual queries, and explanations for answers*. Argument & Computation.

- `doi:10.1080/19462166.2013.869767`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:KWARC/bibs, bibcorpus:davidar/dblp.yaml, bibcorpus:slatex/sTeX
- score 0.4021 (cites 0.0, cocite 0.125, keyword 0.8333, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Argument & Computation, 2014), verified against 3 sources. For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

<details><summary>BibTeX</summary>

```bibtex
@article{garca2014defeasible,
  title = {Defeasible logic programming: DeLP-servers, contextual queries, and explanations for answers},
  author = {Alejandro J. García and Guillermo R. Simari},
  year = {2014},
  journal = {Argument & Computation},
  doi = {10.1080/19462166.2013.869767},
}
```

</details>

#### Elizabeth Black and Anthony Hunter (2012). *A Relevance-theoretic Framework for Constructing and Deconstructing Enthymemes*. J. Log. Comput..

- `doi:10.1093/logcom/exp064`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:IKMLab/arct2, bibcorpus:davidar/dblp.yaml
- score 0.2458 (cites 0.0, cocite 0.25, keyword 0.3333, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, J. Log. Comput., 2012), verified against 2 sources. For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

<details><summary>BibTeX</summary>

```bibtex
@article{black2012arelevanc,
  title = {A Relevance-theoretic Framework for Constructing and Deconstructing Enthymemes},
  author = {Elizabeth Black and Anthony Hunter},
  year = {2012},
  journal = {J. Log. Comput.},
  doi = {10.1093/logcom/exp064},
}
```

</details>

#### Martin Caminada and Gabriella Pigozzi (2011). *On judgment aggregation in abstract argumentation*. Autonomous Agents and Multi-Agent Systems.

- `doi:10.1007/s10458-009-9116-7`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:ttmassa/ter
- score 0.2875 (cites 0.0, cocite 0.25, keyword 0.5, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Autonomous Agents and Multi-Agent Systems, 2011), verified against 2 sources. For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

<details><summary>BibTeX</summary>

```bibtex
@article{caminada2011onjudgmen,
  title = {On judgment aggregation in abstract argumentation},
  author = {Martin Caminada and Gabriella Pigozzi},
  year = {2011},
  journal = {Autonomous Agents and Multi-Agent Systems},
  doi = {10.1007/s10458-009-9116-7},
}
```

</details>

#### João Leite and João Martins (2011). *Social Abstract Argumentation*. IJCAI.

- `title:64dc8586a606c06f88cadd787c29a74d629851a5`
- doc_type: `conference` | tier: T2 | tags: formal
- [landing](http://ijcai.org/papers11/Papers/IJCAI11-381.pdf)
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:lihebi/biber-dist, bibcorpus:ttmassa/ter
- score 0.3625 (cites 0.0, cocite 0.25, keyword 0.5, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, IJCAI, 2011), verified against 3 sources. For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{leite2011socialabs,
  title = {Social Abstract Argumentation},
  author = {João Leite and João Martins},
  year = {2011},
  booktitle = {IJCAI},
  url = {http://ijcai.org/papers11/Papers/IJCAI11-381.pdf},
}
```

</details>

####  (2010). *An abstract framework for argumentation with structured arguments*. Argument & Computation.

- `doi:10.1080/19462160903564592`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:carneades/carneades-3, bibcorpus:davidar/dblp.yaml
- score 0.425 (cites 0.0, cocite 0.25, keyword 0.75, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "An abstract framework for structured arguments is presented that instantiates Dung's (1995) abstract argumentation frameworks." "The resulting framework integrates work of Pollock, Vreeswijk and others on the structure of arguments and the nature of defeat, and extends it in several respects." For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

<details><summary>BibTeX</summary>

```bibtex
@article{prakken2010anabstrac,
  title = {An abstract framework for argumentation with structured arguments},
  author = {Henry Prakken},
  year = {2010},
  journal = {Argument & Computation},
  doi = {10.1080/19462160903564592},
}
```

</details>

#### Uwe Egly, Sarah Alice Gaggl and Stefan Woltran (2010). *Answer-set programming encodings for argumentation frameworks*. Argument & Computation.

- `doi:10.1080/19462166.2010.486479`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:p4s3r0/argumentation-framework-clustering
- score 0.4062 (cites 0.0, cocite 0.375, keyword 0.5, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Argument & Computation, 2010), verified against 2 sources. For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

<details><summary>BibTeX</summary>

```bibtex
@article{egly2010answerset,
  title = {Answer-set programming encodings for argumentation frameworks},
  author = {Uwe Egly and Sarah Alice Gaggl and Stefan Woltran},
  year = {2010},
  journal = {Argument & Computation},
  doi = {10.1080/19462166.2010.486479},
}
```

</details>

## 6.2 Argument mining (NLP) (51 entries, quota 60)

### T1 - Foundational / survey. Read in full: theory anchors, major surveys, canonical papers.

#### Eva Maria Vecchi, Neele Falk, Iman Jundi and Gabriella Lapesa (2021). *Towards Argument Mining for Social Good: A Survey*. Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers).

- `doi:10.18653/v1/2021.acl-long.107` | aliases: `acl:2021.acl-long.107`
- doc_type: `conference` | tier: T1 | tags: dialogue, extraction
- [landing](https://aclanthology.org/2021.acl-long.107/) | [OA PDF](https://aclanthology.org/2021.acl-long.107.pdf) (via acl)
- verified against: acl, bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments, bibcorpus:m0re4u/paper-database
- score 0.5146 (cites 0.0, cocite 0.625, keyword 0.5833, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This survey builds an interdisciplinary picture of Argument Mining (AM), with a strong focus on its potential to address issues related to Social and Political Science." "We propose a novel definition of argument quality which is integrated with that of deliberative quality from the Social Science literature." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{vecchi2021towardsar,
  title = {Towards Argument Mining for Social Good: A Survey},
  author = {Eva Maria Vecchi and Neele Falk and Iman Jundi and Gabriella Lapesa},
  year = {2021},
  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},
  doi = {10.18653/v1/2021.acl-long.107},
  url = {https://aclanthology.org/2021.acl-long.107/},
}
```

</details>

#### Elena Cabrio and Serena Villata (2018). *Five Years of Argument Mining: a Data-driven Analysis*. Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence, IJCAI-18.

- `doi:10.24963/ijcai.2018/766`
- doc_type: `conference` | tier: T1 | tags: extraction
- [landing](https://doi.org/10.24963/ijcai.2018/766)
- verified against: bibcorpus:KWARC/bibs, bibcorpus:m0re4u/paper-database, bibcorpus:slatex/sTeX
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence, IJCAI-18, 2018), verified against 3 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{cabrio2018fiveyears,
  title = {Five Years of Argument Mining: a Data-driven Analysis},
  author = {Elena Cabrio and Serena Villata},
  year = {2018},
  booktitle = {Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence, IJCAI-18},
  doi = {10.24963/ijcai.2018/766},
  url = {https://doi.org/10.24963/ijcai.2018/766},
}
```

</details>

#### Marco Lippi and Paolo Torroni (2016). *Argumentation Mining: State of the Art and Emerging Trends*. ACM Trans. Internet Technol..

- `doi:10.1145/2850417` | aliases: `doi:10.1145/2897213`
- doc_type: `journal` | tier: T1 | tags: extraction
- [landing](https://doi.org/10.1145/2850417)
- verified against: bibcorpus:Danysan1/ai-unibo-nlp-project, bibcorpus:m0re4u/paper-database, bibcorpus:nshkrdotcom/research_papers | note: bibcorpus:CogSciPrag/project_ideas: venue mismatch ('ACM Transactions on Internet Technology' vs 'ACM Trans. Internet Technol.'); bibcorpus:IKMLab/arct2: venue mismatch ('ACM Transactions on Internet…
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Argumentation mining aims at automatically extracting structured arguments from unstructured textual documents." "In this survey article, we introduce argumentation models and methods, review existing systems and applications, and discuss challenges and perspectives of this exciting new research area." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@article{lippi2016argumentat,
  title = {Argumentation Mining: State of the Art and Emerging Trends},
  author = {Marco Lippi and Paolo Torroni},
  year = {2016},
  journal = {ACM Trans. Internet Technol.},
  doi = {10.1145/2850417},
  url = {https://doi.org/10.1145/2850417},
}
```

</details>

#### Andreas Peldszus and Manfred Stede (2013). *From Argument Diagrams to Argumentation Mining in Texts: A Survey*. Int. J. Cogn. Informatics Nat. Intell..

- `doi:10.4018/jcini.2013010101`
- doc_type: `journal` | tier: T1 | tags: extraction
- [landing](https://doi.org/10.4018/jcini.2013010101)
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:m0re4u/paper-database | note: bibcorpus:CogSciPrag/project_ideas: venue mismatch ('IJCINI' vs 'Int. J. Cogn. Informatics Nat. Intell.')
- score 0.4354 (cites 0.0, cocite 0.375, keyword 0.9167, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, the authors consider argument mining as the task of building a formal representation for an argumentative piece of text." "Their goal is to provide a critical survey of the literature on both the resulting representations i.e., argument diagramming techniques and on the various aspects of the automatic analysis process." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@article{peldszus2013fromargum,
  title = {From Argument Diagrams to Argumentation Mining in Texts: A Survey},
  author = {Andreas Peldszus and Manfred Stede},
  year = {2013},
  journal = {Int. J. Cogn. Informatics Nat. Intell.},
  doi = {10.4018/jcini.2013010101},
  url = {https://doi.org/10.4018/jcini.2013010101},
}
```

</details>

#### Jurg Steiner, Andre Bachtiger, Markus Sporndli and Marco R. Steenbergen (2005). *Deliberative Politics in Action. Analysing Parliamentary Discourse*. Cambridge University Press.

- `title:4a05589139b6cbf7c16297f25037cc3d32c6f35a`
- doc_type: `book` | tier: T1 | tags: extraction
- no URL recorded
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments
- score 0.3354 (cites 0.0, cocite 0.625, keyword 0.1667, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (book, Cambridge University Press, 2005), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@book{steiner2005deliberati,
  title = {Deliberative Politics in Action. Analysing Parliamentary Discourse},
  author = {Jurg Steiner and Andre Bachtiger and Markus Sporndli and Marco R. Steenbergen},
  year = {2005},
  publisher = {Cambridge University Press},
}
```

</details>

### T2 - Core method. Defines a task formulation, model, or evaluation still in use.

#### Terne Sasha Thorn Jakobsen, Maria Barrett, Anders Sogaard and David Lassen (2022). *The Sensitivity of Annotator Bias to Task Definitions in Argument Mining*. Proceedings of the 16th Linguistic Annotation Workshop (LAW-XVI) within LREC2022.

- `title:61fadcac208eb3f58c0f9834cf909c5aaa5c7972` | aliases: `acl:2022.law-1.6`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/2022.law-1.6/) | [OA PDF](https://aclanthology.org/2022.law-1.6.pdf) (via acl)
- verified against: acl, bibcorpus:ljvmiranda921/ljvmiranda921.github.io
- score 0.3187 (cites 0.0, cocite 0.125, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we present an annotation experiment that is the first to examine the extent to which social bias is sensitive to how data is annotated." "We release a dataset that is small in the number of instances but large in the number of annotations with demographic information, and our results encourage an increased awareness of annotator bias." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{jakobsen2022thesensit,
  title = {The Sensitivity of Annotator Bias to Task Definitions in Argument Mining},
  author = {Terne Sasha Thorn Jakobsen and Maria Barrett and Anders Sogaard and David Lassen},
  year = {2022},
  booktitle = {Proceedings of the 16th Linguistic Annotation Workshop (LAW-XVI) within LREC2022},
  url = {https://aclanthology.org/2022.law-1.6/},
}
```

</details>

#### Muhammad Mahad Afzal Bhatti, Ahsan Suheer Ahmad and Joonsuk Park (2021). *Argument Mining on Twitter: A Case Study on the Planned Parenthood Debate*. Proceedings of the 8th Workshop on Argument Mining.

- `doi:10.18653/v1/2021.argmining-1.1` | aliases: `acl:2021.argmining-1.1`
- doc_type: `workshop` | tier: T2 | tags: dialogue, extraction
- [landing](https://aclanthology.org/2021.argmining-1.1/) | [OA PDF](https://aclanthology.org/2021.argmining-1.1.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.3583 (cites 0.0, cocite 0.0, keyword 0.8333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we propose a novel problem formulation to mine arguments from Twitter: We formulate argument mining on Twitter as a text classification task to identify tweets that serve as premises for a hashtag that represents a claim of interest." "We first present a new dataset of 24,100 tweets containing hashtag #StandWithPP or #DefundPP, manually labeled as SUPPORT WITH REASON, SUPPORT WITHOUT REASON, and NO EXPLICIT SUPPORT." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{bhatti2021argumentm,
  title = {Argument Mining on Twitter: A Case Study on the Planned Parenthood Debate},
  author = {Muhammad Mahad Afzal Bhatti and Ahsan Suheer Ahmad and Joonsuk Park},
  year = {2021},
  booktitle = {Proceedings of the 8th Workshop on Argument Mining},
  doi = {10.18653/v1/2021.argmining-1.1},
  url = {https://aclanthology.org/2021.argmining-1.1/},
}
```

</details>

#### Yuxiao Ye and Simone Teufel (2021). *End-to-End Argument Mining as Biaffine Dependency Parsing*. Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume.

- `doi:10.18653/v1/2021.eacl-main.55` | aliases: `acl:2021.eacl-main.55`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/2021.eacl-main.55/) | [OA PDF](https://aclanthology.org/2021.eacl-main.55.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.4896 (cites 0.0, cocite 0.375, keyword 0.8333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we propose a neural end-to-end approach to AM which is based on dependency parsing, in contrast to the current state-of-the-art which relies on relation extraction." "In a thorough analysis, we investigate the factors that contribute to the success of our model: the biaffine model itself, our representation for the dependency structure of arguments, different encoders in the biaffine model, and syntactic information additionally fed to the model." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{ye2021endtoend,
  title = {End-to-End Argument Mining as Biaffine Dependency Parsing},
  author = {Yuxiao Ye and Simone Teufel},
  year = {2021},
  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},
  doi = {10.18653/v1/2021.eacl-main.55},
  url = {https://aclanthology.org/2021.eacl-main.55/},
}
```

</details>

#### Juri Opitz et al. (2021). *Explainable Unsupervised Argument Similarity Rating with Abstract Meaning Representation and Conclusion Generation*. Proceedings of the 8th Workshop on Argument Mining.

- `doi:10.18653/v1/2021.argmining-1.3` | aliases: `acl:2021.argmining-1.3`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/2021.argmining-1.3/) | [OA PDF](https://aclanthology.org/2021.argmining-1.3.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.2854 (cites 0.0, cocite 0.0, keyword 0.5417, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We show that Abstract Meaning Representation (AMR) graphs can be useful for representing arguments, and that novel AMR graph metrics can offer explanations for argument similarity ratings." "We show that AMR similarity metrics make argument similarity judgements more interpretable and may even support argument quality judgements." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{opitz2021explainabl,
  title = {Explainable Unsupervised Argument Similarity Rating with Abstract Meaning Representation and Conclusion Generation},
  author = {Juri Opitz and Philipp Heinisch and Philipp Wiesenbach and Philipp Cimiano and Anette Frank},
  year = {2021},
  booktitle = {Proceedings of the 8th Workshop on Argument Mining},
  doi = {10.18653/v1/2021.argmining-1.3},
  url = {https://aclanthology.org/2021.argmining-1.3/},
}
```

</details>

#### Johannes Kiesel, Nico Reichenbach, Benno Stein and Martin Potthast (2021). *Image Retrieval for Arguments Using Stance-Aware Query Expansion*. Proceedings of the 8th Workshop on Argument Mining.

- `doi:10.18653/v1/2021.argmining-1.4` | aliases: `acl:2021.argmining-1.4`
- doc_type: `workshop` | tier: T2 | tags: extraction, quality | also in: quality
- [landing](https://aclanthology.org/2021.argmining-1.4/) | [OA PDF](https://aclanthology.org/2021.argmining-1.4.pdf) (via acl)
- verified against: acl, bibcorpus:allenai/ir_datasets
- score 0.2979 (cites 0.0, cocite 0.125, keyword 0.4167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "By exploiting the sophisticated image representations of keyword-based image search, we propose to use semantic query expansion for both the pro and the con stance to retrieve “argumentative images” for the respective stance." "Our results indicate that even simple expansions provide a strong baseline, reaching a precision@10 of 0.49 for images being (1) on-topic, (2) argumentative, and (3) on-stance." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{kiesel2021imageretr,
  title = {Image Retrieval for Arguments Using Stance-Aware Query Expansion},
  author = {Johannes Kiesel and Nico Reichenbach and Benno Stein and Martin Potthast},
  year = {2021},
  booktitle = {Proceedings of the 8th Workshop on Argument Mining},
  doi = {10.18653/v1/2021.argmining-1.4},
  url = {https://aclanthology.org/2021.argmining-1.4/},
}
```

</details>

#### Yohan Jo, Jacky Visser, Chris Reed and Eduard Hovy (2019). *A Cascade Model for Proposition Extraction in Argumentation*. Proceedings of the 6th Workshop on Argument Mining.

- `doi:10.18653/v1/w19-4502` | aliases: `acl:W19-4502`
- doc_type: `workshop` | tier: T2 | tags: dialogue, extraction
- [landing](https://aclanthology.org/W19-4502/) | [OA PDF](https://aclanthology.org/W19-4502.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.3375 (cites 0.0, cocite 0.0, keyword 0.75, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We present a model to tackle a fundamental but understudied problem in computational argumentation: proposition extraction." "We show promising performance for some tasks and discuss main challenges in proposition extraction." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{jo2019acascade,
  title = {A Cascade Model for Proposition Extraction in Argumentation},
  author = {Yohan Jo and Jacky Visser and Chris Reed and Eduard Hovy},
  year = {2019},
  booktitle = {Proceedings of the 6th Workshop on Argument Mining},
  doi = {10.18653/v1/w19-4502},
  url = {https://aclanthology.org/W19-4502/},
}
```

</details>

#### Tuhin Chakrabarty et al. (2019). *AMPERSAND: Argument Mining for PERSuAsive oNline Discussions*. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP).

- `doi:10.18653/v1/d19-1291` | aliases: `acl:D19-1291`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/D19-1291/) | [OA PDF](https://aclanthology.org/D19-1291.pdf) (via acl)
- verified against: bibcorpus:harisont/biboba, bibcorpus:m0re4u/paper-database | note: acl: venue mismatch ('arXiv preprint arXiv:2004.14677' vs 'Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural…
- score 0.3604 (cites 0.0, cocite 0.125, keyword 0.6667, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Argumentation is a type of discourse where speakers try to persuade their audience about the reasonableness of a claim by presenting supportive arguments." "We propose a computational model for argument mining in online persuasive discussion forums that brings together the micro-level (argument as product) and macro-level (argument as process) models of argumentation." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{chakrabarty2019ampersand,
  title = {AMPERSAND: Argument Mining for PERSuAsive oNline Discussions},
  author = {Tuhin Chakrabarty and Christopher Hidey and Smaranda Muresan and Kathy McKeown and Alyssa Hwang},
  year = {2019},
  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
  doi = {10.18653/v1/d19-1291},
  url = {https://aclanthology.org/D19-1291/},
}
```

</details>

#### Xinyu Hua, Mitko Nikolov, Nikhil Badugu and Lu Wang (2019). *Argument Mining for Understanding Peer Reviews*. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers).

- `doi:10.18653/v1/n19-1219` | aliases: `acl:N19-1219`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/N19-1219/) | [OA PDF](https://aclanthology.org/N19-1219.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist | note: author order differs (hua / mitko nikolov)
- score 0.3167 (cites 0.0, cocite 0.0, keyword 0.6667, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Peer-review plays a critical role in the scientific writing and publication ecosystem." "In this work, we study the content and structure of peer reviews under the argument mining framework, through automatically detecting (1) the argumentative propositions put forward by reviewers, and (2) their types (e.g., evaluating the work or making suggestions for improvement)." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{hua2019argumentm,
  title = {Argument Mining for Understanding Peer Reviews},
  author = {Xinyu Hua and Mitko Nikolov and Nikhil Badugu and Lu Wang},
  year = {2019},
  booktitle = {Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)},
  doi = {10.18653/v1/n19-1219},
  url = {https://aclanthology.org/N19-1219/},
}
```

</details>

#### Makiko Ida et al. (2019). *Can You Give Me a Reason?: Argument-Inducing Online Forum by Argument Mining*. The World Wide Web Conference.

- `doi:10.1145/3308558.3314127`
- doc_type: `conference` | tier: T2 | tags: dialogue, extraction | also in: dialogue
- [landing](https://doi.org/10.1145/3308558.3314127)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.2833 (cites 0.0, cocite 0.0, keyword 0.8333, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This demonstration paper presents an argument-inducing online forum that stimulates participants with lack of premises for their claim in online discussions." "The proposed forum provides its participants the following two subsystems: (1) Argument estimator for online discussions automatically generates a visualization of the argument structures in posts based on argument mining." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{ida2019canyougi,
  title = {Can You Give Me a Reason?: Argument-Inducing Online Forum by Argument Mining},
  author = {Makiko Ida and Gaku Morio and Kosui Iwasa and Tomoyuki Tatsumi and Takaki Yasui and Katsuhide Fujita},
  year = {2019},
  booktitle = {The World Wide Web Conference},
  doi = {10.1145/3308558.3314127},
  url = {https://doi.org/10.1145/3308558.3314127},
}
```

</details>

#### Manfred Stede, Jodi Schneider and Graeme Hirst (2018). *Argumentation mining*. Synthesis Lectures on Human Language Technologies.

- `doi:10.2200/s00883ed1v01y201811hlt040`
- doc_type: `journal` | tier: T2 | tags: extraction
- [landing](https://doi.org/10.2200/S00883ED1V01Y201811HLT040)
- verified against: bibcorpus:harisont/biboba, bibcorpus:ir-anthology/ir-anthology.github.io | note: bibcorpus:mystreamer/lt2326-final-project: venue mismatch ('Synthesis Lectures on Human Language Technologies' vs 'Springer')
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Synthesis Lectures on Human Language Technologies, 2018), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@article{stede2018argumentat,
  title = {Argumentation mining},
  author = {Manfred Stede and Jodi Schneider and Graeme Hirst},
  year = {2018},
  journal = {Synthesis Lectures on Human Language Technologies},
  doi = {10.2200/s00883ed1v01y201811hlt040},
  url = {https://doi.org/10.2200/S00883ED1V01Y201811HLT040},
}
```

</details>

#### Christian Stab et al. (2018). *Cross-topic Argument Mining from Heterogeneous Sources*. Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/d18-1402` | aliases: `acl:D18-1402`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/D18-1402/) | [OA PDF](https://aclanthology.org/D18-1402.pdf) (via acl)
- verified against: acl, bibcorpus:ljvmiranda921/ljvmiranda921.github.io
- score 0.3187 (cites 0.0, cocite 0.125, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we propose a new sentential annotation scheme that is reliably applicable by crowd workers to arbitrary Web texts." "We show that integrating topic information into bidirectional long short-term memory networks outperforms vanilla BiLSTMs by more than 3 percentage points in F1 in two- and three-label cross-topic settings." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{stab2018crosstopi,
  title = {Cross-topic Argument Mining from Heterogeneous Sources},
  author = {Christian Stab and Tristan Miller and Benjamin Schiller and Pranav Rai and Iryna Gurevych},
  year = {2018},
  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/d18-1402},
  url = {https://aclanthology.org/D18-1402/},
}
```

</details>

#### Teresa Botschen, Daniil Sorokin and Iryna Gurevych (2018). *Frame- and Entity-Based Knowledge for Common-Sense Argumentative Reasoning*. Proceedings of the 5th Workshop on Argument Mining.

- `doi:10.18653/v1/w18-5211` | aliases: `acl:W18-5211`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/W18-5211/) | [OA PDF](https://aclanthology.org/W18-5211.pdf) (via acl)
- verified against: acl, bibcorpus:IKMLab/arct2
- score 0.3521 (cites 0.0, cocite 0.25, keyword 0.4583, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Common-sense argumentative reasoning is a challenging task that requires holistic understanding of the argumentation where external knowledge about the world is hypothesized to play a key role." "We find that both resources can contribute to an improvement over the non-enriched approach and point out two persisting challenges: first, integration of many annotations of the same type, and second, fusion of complementary annotations." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{botschen2018frameand,
  title = {Frame- and Entity-Based Knowledge for Common-Sense Argumentative Reasoning},
  author = {Teresa Botschen and Daniil Sorokin and Iryna Gurevych},
  year = {2018},
  booktitle = {Proceedings of the 5th Workshop on Argument Mining},
  doi = {10.18653/v1/w18-5211},
  url = {https://aclanthology.org/W18-5211/},
}
```

</details>

#### Eyal Shnarch et al. (2018). *Will it Blend? Blending Weak and Strong Labeled Data in a Neural Network for Argumentation Mining*. Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics, ACL 2018, Melbourne, Australia, July 15-20, 2018, Volume 2: Short Papers.

- `doi:10.18653/v1/p18-2095` | aliases: `acl:P18-2095`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/P18-2095/) | [OA PDF](https://aclanthology.org/P18-2095.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications, bibcorpus:lihebi/biber-dist
- score 0.3187 (cites 0.0, cocite 0.125, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We propose a methodology to blend high quality but scarce strong labeled data with noisy but abundant weak labeled data during the training of neural networks." "In addition, we provide a manually annotated data set for the task of topic-dependent evidence detection." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{shnarch2018willitbl,
  title = {Will it Blend? Blending Weak and Strong Labeled Data in a Neural Network for Argumentation Mining},
  author = {Eyal Shnarch and Carlos Alzate and Lena Dankin and Martin Gleize and Yufang Hou and Leshem Choshen and Ranit Aharonov and Noam Slonim},
  year = {2018},
  booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics, ACL 2018, Melbourne, Australia, July 15-20, 2018, Volume 2: Short Papers},
  doi = {10.18653/v1/p18-2095},
  url = {https://aclanthology.org/P18-2095/},
}
```

</details>

#### Yufang Hou and Charles Jochim (2017). *Argument Relation Classification Using a Joint Inference Model*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5107` | aliases: `acl:W17-5107`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/W17-5107/) | [OA PDF](https://aclanthology.org/W17-5107.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook | note: venue not corroborated by both sources
- score 0.3063 (cites 0.0, cocite 0.0, keyword 0.625, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we address the problem of argument relation classification where argument units are from different texts." "We show that our joint model improves the results over several strong baselines." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{hou2017argumentr,
  title = {Argument Relation Classification Using a Joint Inference Model},
  author = {Yufang Hou and Charles Jochim},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5107},
  url = {https://aclanthology.org/W17-5107/},
}
```

</details>

#### Eyal Shnarch, Ran Levy, Vikas Raykar and Noam Slonim (2017). *GRASP: Rich Patterns for Argumentation Mining*. EMNLP.

- `title:f36bd2c70ff42e41d1283ef243b7b55af248697f` | aliases: `acl:D17-1140`, `doi:10.18653/v1/d17-1140`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/D17-1140/) | [OA PDF](https://aclanthology.org/D17-1140.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist | note: bibcorpus:jbingel/emnlp2017-handbook: venue mismatch ('Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing' vs 'TOBEFILLED-Proceedings of the Second Workshop on Bui…
- score 0.2958 (cites 0.0, cocite 0.0, keyword 0.5833, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "GRASP (GReedy Augmented Sequential Patterns) is an algorithm for automatically extracting patterns that characterize subtle linguistic phenomena." "We report highly promising experimental results in several challenging text analysis tasks within the field of Argumentation Mining." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{shnarch2017graspric,
  title = {GRASP: Rich Patterns for Argumentation Mining},
  author = {Eyal Shnarch and Ran Levy and Vikas Raykar and Noam Slonim},
  year = {2017},
  booktitle = {EMNLP},
  doi = {10.18653/v1/d17-1140},
  url = {https://aclanthology.org/D17-1140/},
}
```

</details>

####  (2017). *Manual Identification of Arguments with Implicit Conclusions Using Semantic Rules for Argument Mining*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5109` | aliases: `acl:W17-5109`
- doc_type: `conference` | tier: T2 | tags: extraction, schemes
- [landing](https://aclanthology.org/W17-5109/) | [OA PDF](https://aclanthology.org/W17-5109.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook | note: venue not corroborated by both sources
- score 0.3375 (cites 0.0, cocite 0.0, keyword 0.75, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This paper describes a pilot study to evaluate human analysts’ ability to identify the argumentation scheme and premises of an argument having an implicit conclusion." "In preparation for the study, argumentation scheme definitions were crafted for genetics research articles." For a debate-transcript argument database it supplies argumentation-scheme and critical-question structure, which is how stored inferences can be typed rather than left as untyped support links; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{green2017manualide,
  title = {Manual Identification of Arguments with Implicit Conclusions Using Semantic Rules for Argument Mining},
  author = {Nancy Green},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5109},
  url = {https://aclanthology.org/W17-5109/},
}
```

</details>

#### John Lawrence and Chris Reed (2017). *Mining Argumentative Structure from Natural Language text using Automatically Generated Premise-Conclusion Topic Models*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5105` | aliases: `acl:W17-5105`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/W17-5105/) | [OA PDF](https://aclanthology.org/W17-5105.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook | note: venue not corroborated by both sources
- score 0.3896 (cites 0.0, cocite 0.0, keyword 0.9583, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This paper presents a method of extracting argumentative structure from natural language text." "We leverage high-precision, low-recall techniques in order to automatically build a large corpus of inferential statements related to the text’s topic." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{lawrence2017miningarg,
  title = {Mining Argumentative Structure from Natural Language text using Automatically Generated Premise-Conclusion Topic Models},
  author = {John Lawrence and Chris Reed},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5105},
  url = {https://aclanthology.org/W17-5105/},
}
```

</details>

#### Steffen Eger, Johannes Daxenberger and Iryna Gurevych (2017). *Neural End-to-End Learning for Computational Argumentation Mining*. Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/p17-1002` | aliases: `acl:P17-1002`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/P17-1002/) | [OA PDF](https://aclanthology.org/P17-1002.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database
- score 0.3583 (cites 0.0, cocite 0.0, keyword 0.8333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We investigate neural techniques for end-to-end computational argumentation mining (AM)." "We frame AM both as a token-based dependency parsing and as a token-based sequence tagging problem, including a multi-task learning setup." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{eger2017neuralend,
  title = {Neural End-to-End Learning for Computational Argumentation Mining},
  author = {Steffen Eger and Johannes Daxenberger and Iryna Gurevych},
  year = {2017},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/p17-1002},
  url = {https://aclanthology.org/P17-1002/},
}
```

</details>

#### Yamen Ajjour et al. (2017). *Unit Segmentation of Argumentative Texts*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5115` | aliases: `acl:W17-5115`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/W17-5115/) | [OA PDF](https://aclanthology.org/W17-5115.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook, bibcorpus:m0re4u/paper-database | note: venue not corroborated by both sources
- score 0.2958 (cites 0.0, cocite 0.0, keyword 0.5833, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The segmentation of an argumentative text into argument units and their non-argumentative counterparts is the first step in identifying the argumentative structure of the text." "Each such context is reflected by one machine learning model that we evaluate within and across three domains of texts." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{ajjour2017unitsegme,
  title = {Unit Segmentation of Argumentative Texts},
  author = {Yamen Ajjour and Wei-Fan Chen and Johannes Kiesel and Henning Wachsmuth and Benno Stein},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5115},
  url = {https://aclanthology.org/W17-5115/},
}
```

</details>

#### Alfio Ferrara, Stefano Montanelli and Georgios Petasis (2017). *Unsupervised Detection of Argumentative Units though Topic Modeling Techniques*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5113` | aliases: `acl:W17-5113`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/W17-5113/) | [OA PDF](https://aclanthology.org/W17-5113.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook | note: venue not corroborated by both sources
- score 0.3792 (cites 0.0, cocite 0.0, keyword 0.9167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper we present a new unsupervised approach, “Attraction to Topics” – A2T , for the detection of argumentative units, a sub-task of argument mining." "Motivated by the importance of topic identification in manual annotation, we examine whether topic modeling can be used for performing unsupervised detection of argumentative sentences, and to what extend topic modeling can be used to classify sentences as claims and premises." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{ferrara2017unsupervis,
  title = {Unsupervised Detection of Argumentative Units though Topic Modeling Techniques},
  author = {Alfio Ferrara and Stefano Montanelli and Georgios Petasis},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5113},
  url = {https://aclanthology.org/W17-5113/},
}
```

</details>

#### John Lawrence and Chris Reed (2017). *Using Complex Argumentative Interactions to Reconstruct the Argumentative Structure of Large-Scale Debates*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5114` | aliases: `acl:W17-5114`
- doc_type: `workshop` | tier: T2 | tags: dialogue, extraction
- [landing](https://aclanthology.org/W17-5114/) | [OA PDF](https://aclanthology.org/W17-5114.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook | note: venue not corroborated by both sources
- score 0.2958 (cites 0.0, cocite 0.0, keyword 0.5833, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We investigate metrics for analysing properties of these networks, illustrating these using a corpus of arguments taken from the 2016 US Presidential Debates." "We present techniques for determining these features directly from natural language text and show that there is a strong correlation between these automatically identified features and the argumentative structure contained within the text." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{lawrence2017usingcomp,
  title = {Using Complex Argumentative Interactions to Reconstruct the Argumentative Structure of Large-Scale Debates},
  author = {John Lawrence and Chris Reed},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5114},
  url = {https://aclanthology.org/W17-5114/},
}
```

</details>

#### Ahmet Aker et al. (2017). *What works and what does not: Classifier and feature analysis for argument mining*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5112` | aliases: `acl:W17-5112`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/W17-5112/) | [OA PDF](https://aclanthology.org/W17-5112.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook | note: venue not corroborated by both sources
- score 0.3167 (cites 0.0, cocite 0.0, keyword 0.6667, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This paper offers a comparative analysis of the performance of different supervised machine learning methods and feature sets on argument mining tasks." "Specifically, we address the tasks of extracting argumentative segments from texts and predicting the structure between those segments." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{aker2017whatworks,
  title = {What works and what does not: Classifier and feature analysis for argument mining},
  author = {Ahmet Aker and Alfred Sliwa and Yuan Ma and Ruishen Lui and Niravkumar Borad and Seyedeh Ziyaei and Mina Ghobadi},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5112},
  url = {https://aclanthology.org/W17-5112/},
}
```

</details>

#### Isaac Persing and Vincent Ng (2016). *End-to-End Argumentation Mining in Student Essays*. Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.

- `doi:10.18653/v1/n16-1164` | aliases: `acl:N16-1164`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/N16-1164/) | [OA PDF](https://aclanthology.org/N16-1164.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist
- score 0.3583 (cites 0.0, cocite 0.0, keyword 0.8333, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, 2016), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{persing2016endtoend,
  title = {End-to-End Argumentation Mining in Student Essays},
  author = {Isaac Persing and Vincent Ng},
  year = {2016},
  booktitle = {Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  doi = {10.18653/v1/n16-1164},
  url = {https://aclanthology.org/N16-1164/},
}
```

</details>

#### Rory Duthie, John Lawrence, Katarzyna Budzynska and Chris Reed (2016). *The CASS Technique for Evaluating the Performance of Argument Mining*. Proceedings of the Third Workshop on Argument Mining (ArgMining2016).

- `doi:10.18653/v1/w16-2805` | aliases: `acl:W16-2805`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/W16-2805/) | [OA PDF](https://aclanthology.org/W16-2805.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.4062 (cites 0.0, cocite 0.375, keyword 0.5, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (workshop, Proceedings of the Third Workshop on Argument Mining (ArgMining2016), 2016), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{duthie2016thecasst,
  title = {The CASS Technique for Evaluating the Performance of Argument Mining},
  author = {Rory Duthie and John Lawrence and Katarzyna Budzynska and Chris Reed},
  year = {2016},
  booktitle = {Proceedings of the Third Workshop on Argument Mining (ArgMining2016)},
  doi = {10.18653/v1/w16-2805},
  url = {https://aclanthology.org/W16-2805/},
}
```

</details>

#### Marco Lippi and Paolo Torroni (2015). *Context-Independent Claim Detection for Argument Mining*. IJCAI.

- `title:301be2f14805fc8646b001ef9b132eb5f8bbd02b`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](http://ijcai.org/papers15/Abstracts/IJCAI15-033.html)
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:harisont/biboba, bibcorpus:lihebi/biber-dist
- score 0.4437 (cites 0.0, cocite 0.125, keyword 1.0, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, IJCAI, 2015), verified against 3 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{lippi2015contextin,
  title = {Context-Independent Claim Detection for Argument Mining},
  author = {Marco Lippi and Paolo Torroni},
  year = {2015},
  booktitle = {IJCAI},
  url = {http://ijcai.org/papers15/Abstracts/IJCAI15-033.html},
}
```

</details>

#### Ivan Habernal and Iryna Gurevych (2015). *Exploiting Debate Portals for Semi-Supervised Argumentation Mining in User-Generated Web Discourse*. Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/d15-1255` | aliases: `acl:D15-1255`
- doc_type: `conference` | tier: T2 | tags: dialogue, extraction
- [landing](https://aclanthology.org/D15-1255/) | [OA PDF](https://aclanthology.org/D15-1255.pdf) (via acl)
- verified against: acl, bibcorpus:davidar/dblp.yaml, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database
- score 0.3167 (cites 0.0, cocite 0.0, keyword 0.6667, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, 2015), verified against 4 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{habernal2015exploiting,
  title = {Exploiting Debate Portals for Semi-Supervised Argumentation Mining in User-Generated Web Discourse},
  author = {Ivan Habernal and Iryna Gurevych},
  year = {2015},
  booktitle = {Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/d15-1255},
  url = {https://aclanthology.org/D15-1255/},
}
```

</details>

#### Andreas Peldszus and Manfred Stede (2015). *Joint prediction in MST-style discourse parsing for argumentation mining*. Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/d15-1110` | aliases: `acl:D15-1110`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/D15-1110/) | [OA PDF](https://aclanthology.org/D15-1110.pdf) (via acl)
- verified against: acl, bibcorpus:davidar/dblp.yaml, bibcorpus:lihebi/biber-dist
- score 0.3167 (cites 0.0, cocite 0.0, keyword 0.6667, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, 2015), verified against 3 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{peldszus2015jointpred,
  title = {Joint prediction in MST-style discourse parsing for argumentation mining},
  author = {Andreas Peldszus and Manfred Stede},
  year = {2015},
  booktitle = {Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/d15-1110},
  url = {https://aclanthology.org/D15-1110/},
}
```

</details>

#### Ivan Habernal, Judith Eckle-Kohler and Iryna Gurevych (2014). *Argumentation Mining on the Web from Information Seeking Perspective*. ArgNLP.

- `title:e2dd0248ee2104b83fabae9e89b7c5d7e89a5690`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](http://ceur-ws.org/Vol-1341/paper4.pdf)
- verified against: bibcorpus:IKMLab/arct2, bibcorpus:davidar/dblp.yaml
- score 0.2875 (cites 0.0, cocite 0.25, keyword 0.5, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, ArgNLP, 2014), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{habernal2014argumentat,
  title = {Argumentation Mining on the Web from Information Seeking Perspective},
  author = {Ivan Habernal and Judith Eckle-Kohler and Iryna Gurevych},
  year = {2014},
  booktitle = {ArgNLP},
  url = {http://ceur-ws.org/Vol-1341/paper4.pdf},
}
```

</details>

#### Raquel Mochales and Marie-Francine Moens (2011). *Argumentation Mining*. Artif. Intell. Law.

- `doi:10.1007/s10506-010-9104-x`
- doc_type: `journal` | tier: T2 | tags: extraction
- [landing](http://dx.doi.org/10.1007/s10506-010-9104-x)
- verified against: bibcorpus:IKMLab/arct2, bibcorpus:davidar/dblp.yaml | note: author order differs (mochales / palau); bibcorpus:m0re4u/paper-database: venue mismatch ('Artif. Intell. Law' vs 'Artificial Intelligence and Law'); bibcorpus:nshkrdotcom/research_papers: venue mism…
- score 0.3312 (cites 0.0, cocite 0.375, keyword 0.5, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Artif. Intell. Law, 2011), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@article{mochales2011argumentat,
  title = {Argumentation Mining},
  author = {Raquel Mochales and Marie-Francine Moens},
  year = {2011},
  journal = {Artif. Intell. Law},
  doi = {10.1007/s10506-010-9104-x},
  url = {http://dx.doi.org/10.1007/s10506-010-9104-x},
}
```

</details>

#### Raquel Mochales Palau and Marie-Francine Moens (2009). *Argumentation Mining: The Detection, Classification and Structure of Arguments in Text*. ICAIL.

- `title:a5c50d63741d8b767183270f762294ea5fa75236`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](http://doi.acm.org/10.1145/1568234.1568246)
- verified against: bibcorpus:BarryMafu/LitLens, bibcorpus:davidar/dblp.yaml | note: bibcorpus:ljvmiranda921/ljvmiranda921.github.io: venue mismatch ('ICAIL' vs 'Proceedings of the 12th International Conference on Artificial Intelligence and Law')
- score 0.3312 (cites 0.0, cocite 0.375, keyword 0.5, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, ICAIL, 2009), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{palau2009argumentat,
  title = {Argumentation Mining: The Detection, Classification and Structure of Arguments in Text},
  author = {Raquel Mochales Palau and Marie-Francine Moens},
  year = {2009},
  booktitle = {ICAIL},
  url = {http://doi.acm.org/10.1145/1568234.1568246},
}
```

</details>

### T3 - Dataset / tool / annotation guideline, including the guideline documents themselves.

#### Marc Feger, Katarina Boland and Stefan Dietze (2025). *Limited Generalizability in Argument Mining: State-Of-The-Art Models Learn Datasets, Not Arguments*. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025, Vienna, Austria, July 27 - August 1, 2025.

- `title:ecc66f83f08f4809231d027e9ba9ccb1e4c3f5ba` | aliases: `acl:2025.acl-long.1164`, `doi:10.18653/v1/2025.acl-long.1164`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue, extraction | also in: resources
- [landing](https://aclanthology.org/2025.acl-long.1164/) | [OA PDF](https://aclanthology.org/2025.acl-long.1164.pdf) (via acl) | [repo](https://github.com/mit0110/argument_mining)
- verified against: acl, bibcorpus:CogSciPrag/project_ideas | note: repo linked on token overlap: ['argument', 'datasets', 'mining']
- score 0.4062 (cites 0.0, cocite 0.375, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We evaluate four transformers, three standard and one enhanced with contrastive pre-training for better generalization, on 17 English sentence-level datasets as most relevant to the task." "While the models achieve strong results on familiar benchmarks, their performance drops markedly when applied to unseen datasets." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{feger2025limitedge,
  title = {Limited Generalizability in Argument Mining: State-Of-The-Art Models Learn Datasets, Not Arguments},
  author = {Marc Feger and Katarina Boland and Stefan Dietze},
  year = {2025},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025, Vienna, Austria, July 27 - August 1, 2025},
  doi = {10.18653/v1/2025.acl-long.1164},
  url = {https://aclanthology.org/2025.acl-long.1164/},
}
```

</details>

#### Keshav Singh et al. (2021). *Exploring Methodologies for Collecting High-Quality Implicit Reasoning in Arguments*. Proceedings of the 8th Workshop on Argument Mining.

- `doi:10.18653/v1/2021.argmining-1.6` | aliases: `acl:2021.argmining-1.6`
- doc_type: `workshop` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/2021.argmining-1.6/) | [OA PDF](https://aclanthology.org/2021.argmining-1.6.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.2646 (cites 0.0, cocite 0.0, keyword 0.4583, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Therefore, in order to annotate warrants in a more interpretative and restrictive way, we propose two methodologies to annotate warrants in a semi-structured form." "To further facilitate research towards the task of explicating warrants in arguments, we release our materials publicly (i.e., crowdsourcing guidelines and collected warrants)." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{singh2021exploring,
  title = {Exploring Methodologies for Collecting High-Quality Implicit Reasoning in Arguments},
  author = {Keshav Singh and Farjana Sultana Mim and Naoya Inoue and Shoichi Naito and Kentaro Inui},
  year = {2021},
  booktitle = {Proceedings of the 8th Workshop on Argument Mining},
  doi = {10.18653/v1/2021.argmining-1.6},
  url = {https://aclanthology.org/2021.argmining-1.6/},
}
```

</details>

#### Nina Bauwelinck and Els Lefever (2020). *Annotating Topics, Stance, Argumentativeness and Claims in Dutch Social Media Comments: A Pilot Study*. Proceedings of the 7th Workshop on Argument Mining.

- `title:845517f340fa84f9278786e5e5f5cca686edfa5a` | aliases: `acl:2020.argmining-1.2`
- doc_type: `workshop` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/2020.argmining-1.2/) | [OA PDF](https://aclanthology.org/2020.argmining-1.2.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.3688 (cites 0.0, cocite 0.0, keyword 0.875, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The theoretical motivations underlying the annotation guidelines used to generate labelled corpora rarely include motivation for the use of a particular theoretical basis." "This pilot study reports on the annotation of a corpus of 100 Dutch user comments made in response to politically-themed news articles on Facebook." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{bauwelinck2020annotating,
  title = {Annotating Topics, Stance, Argumentativeness and Claims in Dutch Social Media Comments: A Pilot Study},
  author = {Nina Bauwelinck and Els Lefever},
  year = {2020},
  booktitle = {Proceedings of the 7th Workshop on Argument Mining},
  url = {https://aclanthology.org/2020.argmining-1.2/},
}
```

</details>

#### Benedetta Torsi and Roser Morante (2018). *Annotating Claims in the Vaccination Debate*. Proceedings of the 5th Workshop on Argument Mining.

- `doi:10.18653/v1/w18-5207` | aliases: `acl:W18-5207`
- doc_type: `workshop` | tier: T3 | tags: dataset, dialogue, extraction | also in: dialogue, resources
- [landing](https://aclanthology.org/W18-5207/) | [OA PDF](https://aclanthology.org/W18-5207.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.2854 (cites 0.0, cocite 0.0, keyword 0.5417, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper we present annotation experiments with three different annotation schemes for the identification of argument components in texts related to the vaccination debate." "Since most corpora that have been annotated with argumentation information contain texts that belong to a specific genre and have a well defined argumentation structure, we needed to adjust the annotation schemes to our corpus, which contains heterogeneous texts from the Web." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{torsi2018annotating,
  title = {Annotating Claims in the Vaccination Debate},
  author = {Benedetta Torsi and Roser Morante},
  year = {2018},
  booktitle = {Proceedings of the 5th Workshop on Argument Mining},
  doi = {10.18653/v1/w18-5207},
  url = {https://aclanthology.org/W18-5207/},
}
```

</details>

#### Claudia Schulz et al. (2018). *Multi-Task Learning for Argumentation Mining in Low-Resource Settings*. Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers).

- `doi:10.18653/v1/n18-2006` | aliases: `acl:N18-2006`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/N18-2006/) | [OA PDF](https://aclanthology.org/N18-2006.pdf) (via acl) | [repo](https://github.com/UKPLab/naacl18-multitask_argument_mining)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database | note: repo linked on token overlap: ['argumentation', 'learning', 'low', 'mining', 'multi', 'resource', 'settings', 'task']
- score 0.3375 (cites 0.0, cocite 0.0, keyword 0.75, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We investigate whether and where multi-task learning (MTL) can improve performance on NLP problems related to argumentation mining (AM), in particular argument component identification." "Our results show that MTL performs particularly well (and better than single-task learning) when little training data is available for the main task, a common scenario in AM." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{schulz2018multitask,
  title = {Multi-Task Learning for Argumentation Mining in Low-Resource Settings},
  author = {Claudia Schulz and Steffen Eger and Johannes Daxenberger and Tobias Kahse and Iryna Gurevych},
  year = {2018},
  booktitle = {Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)},
  doi = {10.18653/v1/n18-2006},
  url = {https://aclanthology.org/N18-2006/},
}
```

</details>

#### Ivan Habernal, Henning Wachsmuth, Iryna Gurevych and Benno Stein (2018). *SemEval-2018 Task 12: The Argument Reasoning Comprehension Task*. Proceedings of the 12th International Workshop on Semantic Evaluation.

- `doi:10.18653/v1/s18-1121` | aliases: `acl:S18-01121`
- doc_type: `workshop` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/S18-01121/) | [OA PDF](https://aclanthology.org/S18-01121.pdf) (via acl) | [repo](https://github.com/UKPLab/argument-reasoning-comprehension-task)
- verified against: acl, bibcorpus:IKMLab/arct2, bibcorpus:m0re4u/paper-database | note: repo linked on token overlap: ['argument', 'comprehension', 'reasoning', 'task']
- score 0.2667 (cites 0.0, cocite 0.25, keyword 0.4167, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "A natural language argument is composed of a claim as well as reasons given as premises for the claim." "We describe the dataset with 1970 instances that we built for the task, and we outline the 21 computational approaches that participated, most of which used neural networks." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{habernal2018semeval,
  title = {SemEval-2018 Task 12: The Argument Reasoning Comprehension Task},
  author = {Ivan Habernal and Henning Wachsmuth and Iryna Gurevych and Benno Stein},
  year = {2018},
  booktitle = {Proceedings of the 12th International Workshop on Semantic Evaluation},
  doi = {10.18653/v1/s18-1121},
  url = {https://aclanthology.org/S18-01121/},
}
```

</details>

#### Ivan Habernal, Henning Wachsmuth, Iryna Gurevych and Benno Stein (2018). *The Argument Reasoning Comprehension Task: Identification and Reconstruction of Implicit Warrants*. Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers).

- `doi:10.18653/v1/n18-1175` | aliases: `acl:N18-1175`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/N18-1175/) | [OA PDF](https://aclanthology.org/N18-1175.pdf) (via acl) | [repo](https://github.com/UKPLab/argument-reasoning-comprehension-task)
- verified against: acl, bibcorpus:IKMLab/arct2, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database | note: repo linked on token overlap: ['argument', 'comprehension', 'reasoning', 'task']
- score 0.3208 (cites 0.0, cocite 0.25, keyword 0.3333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper we develop a methodology for reconstructing warrants systematically." "On this basis, we present a new challenging task, the argument reasoning comprehension task." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{habernal2018theargume,
  title = {The Argument Reasoning Comprehension Task: Identification and Reconstruction of Implicit Warrants},
  author = {Ivan Habernal and Henning Wachsmuth and Iryna Gurevych and Benno Stein},
  year = {2018},
  booktitle = {Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)},
  doi = {10.18653/v1/n18-1175},
  url = {https://aclanthology.org/N18-1175/},
}
```

</details>

#### Christopher Hidey et al. (2017). *Analyzing the Semantic Types of Claims and Premises in an Online Persuasive Forum*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5102` | aliases: `acl:W17-5102`
- doc_type: `workshop` | tier: T3 | tags: dataset, dialogue, extraction | also in: dialogue, resources
- [landing](https://aclanthology.org/W17-5102/) | [OA PDF](https://aclanthology.org/W17-5102.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook | note: venue not corroborated by both sources
- score 0.4 (cites 0.0, cocite 0.0, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We propose a two-tiered annotation scheme to label claims and premises and their semantic types in an online persuasive forum, Change My View, with the long-term goal of understanding what makes a message persuasive." "Premises are annotated with the three types of persuasive modes: ethos, logos, pathos, while claims are labeled as interpretation, evaluation, agreement, or disagreement, the latter two designed to account for the dialogical nature of our corpus." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{hidey2017analyzing,
  title = {Analyzing the Semantic Types of Claims and Premises in an Online Persuasive Forum},
  author = {Christopher Hidey and Elena Musi and Alyssa Hwang and Smaranda Muresan and Kathy McKeown},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5102},
  url = {https://aclanthology.org/W17-5102/},
}
```

</details>

#### Vlad Niculae, Joonsuk Park and Claire Cardie (2017). *Argument Mining with Structured SVMs and RNNs*. Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/p17-1091` | aliases: `acl:P17-1091`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/P17-1091/) | [OA PDF](https://aclanthology.org/P17-1091.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist
- score 0.3167 (cites 0.0, cocite 0.0, keyword 0.6667, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We propose a novel factor graph model for argument mining, designed for settings in which the argumentative relations in a document do not necessarily form a tree structure." "(This is the case in over 20% of the web comments dataset we release.) Our model jointly learns elementary unit type classification and argumentative relation prediction." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{niculae2017argumentm,
  title = {Argument Mining with Structured SVMs and RNNs},
  author = {Vlad Niculae and Joonsuk Park and Claire Cardie},
  year = {2017},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/p17-1091},
  url = {https://aclanthology.org/P17-1091/},
}
```

</details>

#### Ivan Habernal and Iryna Gurevych (2017). *Argumentation Mining in User-Generated Web Discourse*. Computational Linguistics, Volume 43, Issue 1 - April 2017.

- `doi:10.1162/coli_a_00276` | aliases: `acl:J17-1004`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/J17-1004/) | [OA PDF](https://aclanthology.org/J17-1004.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database
- score 0.4229 (cites 0.0, cocite 0.125, keyword 0.9167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The goal of argumentation mining, an evolving research field in computational linguistics, is to design methods capable of analyzing people’s argumentation." "We offer the data, source codes, and annotation guidelines to the community under free licenses." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{habernal2017argumentat,
  title = {Argumentation Mining in User-Generated Web Discourse},
  author = {Ivan Habernal and Iryna Gurevych},
  year = {2017},
  booktitle = {Computational Linguistics, Volume 43, Issue 1 - April 2017},
  doi = {10.1162/coli_a_00276},
  url = {https://aclanthology.org/J17-1004/},
}
```

</details>

#### Christian Stab and Iryna Gurevych (2017). *Parsing Argumentation Structures in Persuasive Essays*. Computational Linguistics, Volume 43, Issue 3 - September 2017.

- `doi:10.1162/coli_a_00295` | aliases: `acl:J17-3005`
- doc_type: `journal` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/J17-3005/) | [OA PDF](https://aclanthology.org/J17-3005.pdf)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this article, we present a novel approach for parsing argumentation structures." "Moreover, we introduce a novel corpus of persuasive essays annotated with argumentation structures." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@article{stab2017parsingar,
  title = {Parsing Argumentation Structures in Persuasive Essays},
  author = {Christian Stab and Iryna Gurevych},
  year = {2017},
  journal = {Computational Linguistics, Volume 43, Issue 3 - September 2017},
  doi = {10.1162/coli_a_00295},
  url = {https://aclanthology.org/J17-3005/},
}
```

</details>

#### Ahmet Aker and Huangpan Zhang (2017). *Projection of Argumentative Corpora from Source to Target Languages*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5108` | aliases: `acl:W17-5108`
- doc_type: `workshop` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/W17-5108/) | [OA PDF](https://aclanthology.org/W17-5108.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook | note: venue not corroborated by both sources
- score 0.3479 (cites 0.0, cocite 0.0, keyword 0.7917, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper we release the first publicly available Mandarin argumentative corpus." "In this way we introduce a new task of multi-lingual argument mapping that can be evaluated using our English-Mandarin argumentative corpus." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{aker2017projection,
  title = {Projection of Argumentative Corpora from Source to Target Languages},
  author = {Ahmet Aker and Huangpan Zhang},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5108},
  url = {https://aclanthology.org/W17-5108/},
}
```

</details>

#### Christian Stab and Iryna Gurevych (2017). *Recognizing Insufficiently Supported Arguments in Argumentative Essays*. Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 1, Long Papers.

- `title:4548f0ff40575ec88d744f306fc5a7f696551502` | aliases: `acl:E17-1092`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/E17-1092/) | [OA PDF](https://aclanthology.org/E17-1092.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:npnkhoi/memefal-paper, bibcorpus:xinyannnnnnn/fact-driven-storytelling-with-llms
- score 0.4917 (cites 0.0, cocite 0.5, keyword 0.6667, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we propose a new task for assessing the quality of natural language arguments." "In this work, we show that human annotators substantially agree on the sufficiency criterion and introduce a novel annotated corpus." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{stab2017recognizin,
  title = {Recognizing Insufficiently Supported Arguments in Argumentative Essays},
  author = {Christian Stab and Iryna Gurevych},
  year = {2017},
  booktitle = {Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 1, Long Papers},
  url = {https://aclanthology.org/E17-1092/},
}
```

</details>

#### Ran Levy et al. (2017). *Unsupervised corpus–wide claim detection*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5110` | aliases: `acl:W17-5110`
- doc_type: `workshop` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/W17-5110/) | [OA PDF](https://aclanthology.org/W17-5110.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook, bibcorpus:m0re4u/paper-database | note: venue not corroborated by both sources
- score 0.4 (cites 0.0, cocite 0.0, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Here, we present a first corpus– wide claim detection framework, that can be directly applied to massive corpora." "Next, we employ simple heuristics to rank the sentences, leading to an unsupervised corpus–wide claim detection system, with precision that outperforms previously reported results on the task of claim detection given relevant documents and labeled data." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{levy2017unsupervis,
  title = {Unsupervised corpus–wide claim detection},
  author = {Ran Levy and Shai Gretz and Benjamin Sznajder and Shay Hummel and Ranit Aharonov and Noam Slonim},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5110},
  url = {https://aclanthology.org/W17-5110/},
}
```

</details>

### T4 - Recent (2023-2026). LLM-era work; lower durability confidence, high build relevance.

#### Zihao Zheng, Zhaowei Wang, Qing Zong and Yangqiu Song (2024). *KNOWCOMP POKEMON Team at DialAM-2024: A Two-Stage Pipeline for Detecting Relations in Dialogue Argument Mining*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.11` | aliases: `acl:2024.argmining-1.11`
- doc_type: `workshop` | tier: T4 | tags: dialogue, extraction | also in: dialogue
- [landing](https://aclanthology.org/2024.argmining-1.11/) | [OA PDF](https://aclanthology.org/2024.argmining-1.11.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.5016 (cites 0.0, cocite 0.4688, keyword 0.75, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Dialogue Argument Mining(DialAM) is an important branch of Argument Mining(AM)." "To accomplish this, we propose a two-stage pipeline, which includes the Two-Step S-Node Prediction Model in Stage 1 and the YA-Node Prediction Model in Stage 2." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{zheng2024knowcompp,
  title = {KNOWCOMP POKEMON Team at DialAM-2024: A Two-Stage Pipeline for Detecting Relations in Dialogue Argument Mining},
  author = {Zihao Zheng and Zhaowei Wang and Qing Zong and Yangqiu Song},
  year = {2024},
  booktitle = {Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024)},
  doi = {10.18653/v1/2024.argmining-1.11},
  url = {https://aclanthology.org/2024.argmining-1.11/},
}
```

</details>

#### Pierpaolo Goffredo, Mariana Chaves, Serena Villata and Elena Cabrio (2023). *Argument-based Detection and Classification of Fallacies in Political Debates*. Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2023.emnlp-main.684` | aliases: `acl:2023.emnlp-main.684`
- doc_type: `conference` | tier: T4 | tags: dialogue, extraction, fallacy, quality | also in: quality
- [landing](https://aclanthology.org/2023.emnlp-main.684/) | [OA PDF](https://aclanthology.org/2023.emnlp-main.684.pdf) (via acl)
- verified against: acl, bibcorpus:lefteriskat/Logical-Fallacy-Detection-Using-LLMs, bibcorpus:npnkhoi/memefal-paper
- score 0.3812 (cites 0.0, cocite 0.125, keyword 0.75, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "First, we extend the ElecDeb60To16 dataset of U.S. presidential debates annotated with fallacious arguments, by incorporating the most recent Trump-Biden presidential debate." "We include updated token-level annotations, incorporating argumentative components (i.e., claims and premises), the relations between these components (i.e., support and attack), and six categories of fallacious arguments (i.e., Ad Hominem, Appeal to Authority, Appeal to Emotion, False Cause, Slippery Slope, and Sloga…" For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it gives quality dimensions or a scoring target.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{goffredo2023argumentb,
  title = {Argument-based Detection and Classification of Fallacies in Political Debates},
  author = {Pierpaolo Goffredo and Mariana Chaves and Serena Villata and Elena Cabrio},
  year = {2023},
  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/2023.emnlp-main.684},
  url = {https://aclanthology.org/2023.emnlp-main.684/},
}
```

</details>

## 6.3 Argument quality and evaluation (26 entries, quota 40)

### T2 - Core method. Defines a task formulation, model, or evaluation still in use.

#### Christine De Kock, Tom Stafford and Andreas Vlachos (2022). *How to disagree well: Investigating the dispute tactics used on Wikipedia*. Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2022.emnlp-main.252` | aliases: `acl:2022.emnlp-main.252`
- doc_type: `conference` | tier: T2 | tags: dialogue, fallacy, quality
- [landing](https://aclanthology.org/2022.emnlp-main.252/) | [OA PDF](https://aclanthology.org/2022.emnlp-main.252.pdf) (via acl)
- verified against: acl, bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments
- score 0.4521 (cites 0.0, cocite 0.625, keyword 0.3333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We propose a framework of dispute tactics which unifies these two perspectives, as well as other dialogue acts which play a role in resolving disputes, such as asking questions and providing clarification." "Finally, we show that these annotations can be used to provide useful additional signals to improve performance on the task of predicting escalation." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it gives quality dimensions or a scoring target.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{kock2022howtodis,
  title = {How to disagree well: Investigating the dispute tactics used on Wikipedia},
  author = {Christine De Kock and Tom Stafford and Andreas Vlachos},
  year = {2022},
  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/2022.emnlp-main.252},
  url = {https://aclanthology.org/2022.emnlp-main.252/},
}
```

</details>

#### Zhijing Jin et al. (2022). *Logical Fallacy Detection*. Findings of the Association for Computational Linguistics: EMNLP 2022.

- `doi:10.18653/v1/2022.findings-emnlp.532` | aliases: `acl:2022.findings-emnlp.532`, `arxiv:2202.13758`
- doc_type: `conference` | tier: T2 | tags: extraction, fallacy, quality
- [landing](https://aclanthology.org/2022.findings-emnlp.532/) | [OA PDF](https://aclanthology.org/2022.findings-emnlp.532.pdf)
- verified against: acl, bibcorpus:danny-v-nguyen/thesis, bibcorpus:edgar-demeude/KEIGO-SYNC, bibcorpus:lefteriskat/Logical-Fallacy-Detection-Using-LLMs, bibcorpus:npnkhoi/memefal-paper | note: venue not corroborated by both sources
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we propose the task of logical fallacy detection, and provide a new dataset (Logic) of logical fallacies generally found in text, together with an additional challenge set for detecting logical fallacies in climate change claims (LogicClimate)." "In contrast, we show that a simple structure-aware classifier outperforms the best language model by 5.46% F1 scores on Logic and 4.51% on LogicClimate." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it types defective inference.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{jin2022logicalfa,
  title = {Logical Fallacy Detection},
  author = {Zhijing Jin and Abhinav Lalwani and Tejas Vaidhya and Xiaoyu Shen and Yiwen Ding and Zhiheng Lyu and Mrinmaya Sachan and Rada Mihalcea and Bernhard Schölkopf},
  year = {2022},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},
  doi = {10.18653/v1/2022.findings-emnlp.532},
  url = {https://aclanthology.org/2022.findings-emnlp.532/},
}
```

</details>

#### Tariq Alhindi, Tuhin Chakrabarty, Elena Musi and Smaranda Muresan (2022). *Multitask Instruction-based Prompting for Fallacy Recognition*. Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2022.emnlp-main.560` | aliases: `acl:2022.emnlp-main.560`
- doc_type: `conference` | tier: T2 | tags: dialogue, fallacy, quality | also in: llm
- [landing](https://aclanthology.org/2022.emnlp-main.560/) | [OA PDF](https://aclanthology.org/2022.emnlp-main.560.pdf) (via acl)
- verified against: acl, bibcorpus:lefteriskat/Logical-Fallacy-Detection-Using-LLMs
- score 0.3187 (cites 0.0, cocite 0.125, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Moreover, a big challenge for computational models lies in the fact that fallacies are formulated differently across the datasets with differences in the input format (e.g., question-answer pair, sentence with fallacy fragment), genre (e.g., social media, dialogue, news), as well as types and number of fallacies (from…" "We show the ability of this multitask prompting approach to recognize 28 unique fallacies across domains and genres and study the effect of model size and prompt choice by analyzing the per-class (i.e., fallacy type) results." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it gives quality dimensions or a scoring target.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{alhindi2022multitask,
  title = {Multitask Instruction-based Prompting for Fallacy Recognition},
  author = {Tariq Alhindi and Tuhin Chakrabarty and Elena Musi and Smaranda Muresan},
  year = {2022},
  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/2022.emnlp-main.560},
  url = {https://aclanthology.org/2022.emnlp-main.560/},
}
```

</details>

#### Neele Falk, Iman Jundi, Eva Maria Vecchi and Gabriella Lapesa (2021). *Predicting Moderation of Deliberative Arguments: Is Argument Quality the Key?*. Proceedings of the 8th Workshop on Argument Mining.

- `doi:10.18653/v1/2021.argmining-1.13` | aliases: `acl:2021.argmining-1.13`
- doc_type: `workshop` | tier: T2 | tags: dialogue, extraction, quality
- [landing](https://aclanthology.org/2021.argmining-1.13/) | [OA PDF](https://aclanthology.org/2021.argmining-1.13.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.4938 (cites 0.0, cocite 0.625, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Human moderation is commonly employed in deliberative contexts (argumentation and discussion targeting a shared decision on an issue relevant to a group, e.g., citizens arguing on how to employ a shared budget)." "As the scale of discussion enlarges in online settings, the overall discussion quality risks to drop and moderation becomes more important to assist participants in having a cooperative and productive interaction." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it gives quality dimensions or a scoring target.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{falk2021predicting,
  title = {Predicting Moderation of Deliberative Arguments: Is Argument Quality the Key?},
  author = {Neele Falk and Iman Jundi and Eva Maria Vecchi and Gabriella Lapesa},
  year = {2021},
  booktitle = {Proceedings of the 8th Workshop on Argument Mining},
  doi = {10.18653/v1/2021.argmining-1.13},
  url = {https://aclanthology.org/2021.argmining-1.13/},
}
```

</details>

#### Benjamin Schiller, Johannes Daxenberger and Iryna Gurevych (2021). *Stance Detection Benchmark: How Robust is Your Stance Detection?*. Kunstliche Intell..

- `doi:10.1007/s13218-021-00714-w`
- doc_type: `journal` | tier: T2 | tags: extraction, quality
- [landing](https://doi.org/10.1007/s13218-021-00714-w)
- verified against: bibcorpus:CogSciPrag/project_ideas, bibcorpus:danielhers/danielhers.github.io
- score 0.3729 (cites 0.0, cocite 0.375, keyword 0.6667, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Kunstliche Intell., 2021), verified against 2 sources. For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@article{schiller2021stancedet,
  title = {Stance Detection Benchmark: How Robust is Your Stance Detection?},
  author = {Benjamin Schiller and Johannes Daxenberger and Iryna Gurevych},
  year = {2021},
  journal = {Kunstliche Intell.},
  doi = {10.1007/s13218-021-00714-w},
  url = {https://doi.org/10.1007/s13218-021-00714-w},
}
```

</details>

#### Jonathan Kobbe, Ines Rehbein, Ioana Hulpuș and Heiner Stuckenschmidt (2020). *Exploring Morality in Argumentation*. Proceedings of the 7th Workshop on Argument Mining.

- `title:b2f4fa5e60b83569b494f246038316d498b8b4ec` | aliases: `acl:2020.argmining-1.4`
- doc_type: `workshop` | tier: T2 | tags: dialogue, extraction, quality | also in: mining
- [landing](https://aclanthology.org/2020.argmining-1.4/) | [OA PDF](https://aclanthology.org/2020.argmining-1.4.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.2542 (cites 0.0, cocite 0.0, keyword 0.4167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We propose to add another perspective to the analysis, namely moral sentiment." "In the paper, we present different models for automatically predicting moral sentiment in debates and evaluate them on a manually annotated testset." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it gives quality dimensions or a scoring target.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{kobbe2020exploring,
  title = {Exploring Morality in Argumentation},
  author = {Jonathan Kobbe and Ines Rehbein and Ioana Hulpuș and Heiner Stuckenschmidt},
  year = {2020},
  booktitle = {Proceedings of the 7th Workshop on Argument Mining},
  url = {https://aclanthology.org/2020.argmining-1.4/},
}
```

</details>

#### Martin Gleize et al. (2019). *Are You Convinced? Choosing the More Convincing Evidence with a Siamese Network*. Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics.

- `doi:10.18653/v1/p19-1093` | aliases: `acl:P19-1093`
- doc_type: `conference` | tier: T2 | tags: extraction, quality
- [landing](https://aclanthology.org/P19-1093/) | [OA PDF](https://aclanthology.org/P19-1093.pdf) (via acl)
- verified against: acl, bibcorpus:BarryMafu/LitLens, bibcorpus:borgr/publications | note: bibcorpus:xinyannnnnnn/fact-driven-storytelling-with-llms: venue mismatch ('Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics' vs 'arXiv preprint arXiv:1907.0897…
- score 0.4688 (cites 0.0, cocite 0.375, keyword 0.75, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "With the advancement in argument detection, we suggest to pay more attention to the challenging task of identifying the more convincing arguments." "In this paper, we present a new data set, IBM-EviConv, of pairs of evidence labeled for convincingness, designed to be more challenging than existing alternatives." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{gleize2019areyouco,
  title = {Are You Convinced? Choosing the More Convincing Evidence with a Siamese Network},
  author = {Martin Gleize and Eyal Shnarch and Leshem Choshen and Lena Dankin and Guy Moshkowich and Ranit Aharonov and Noam Slonim},
  year = {2019},
  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  doi = {10.18653/v1/p19-1093},
  url = {https://aclanthology.org/P19-1093/},
}
```

</details>

#### Ivan Habernal, Henning Wachsmuth, Iryna Gurevych and Benno Stein (2018). *Before Name-Calling: Dynamics and Triggers of Ad Hominem Fallacies in Web Argumentation*. Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers).

- `doi:10.18653/v1/n18-1036` | aliases: `acl:N18-1036`
- doc_type: `conference` | tier: T2 | tags: dialogue, fallacy, quality
- [landing](https://aclanthology.org/N18-1036/) | [OA PDF](https://aclanthology.org/N18-1036.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:npnkhoi/memefal-paper
- score 0.4437 (cites 0.0, cocite 0.125, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Arguing without committing a fallacy is one of the main requirements of an ideal debate." "But even when debating rules are strictly enforced and fallacious arguments punished, arguers often lapse into attacking the opponent by an ad hominem argument." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it gives quality dimensions or a scoring target.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{habernal2018beforenam,
  title = {Before Name-Calling: Dynamics and Triggers of Ad Hominem Fallacies in Web Argumentation},
  author = {Ivan Habernal and Henning Wachsmuth and Iryna Gurevych and Benno Stein},
  year = {2018},
  booktitle = {Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)},
  doi = {10.18653/v1/n18-1036},
  url = {https://aclanthology.org/N18-1036/},
}
```

</details>

#### Ivan Habernal et al. (2017). *Argotario: Computational Argumentation Meets Serious Games*. Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing: System Demonstrations.

- `doi:10.18653/v1/d17-2002` | aliases: `acl:D17-2002`
- doc_type: `conference` | tier: T2 | tags: fallacy, quality
- [landing](https://aclanthology.org/D17-2002/) | [OA PDF](https://aclanthology.org/D17-2002.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook, bibcorpus:lefteriskat/Logical-Fallacy-Detection-Using-LLMs, bibcorpus:lihebi/biber-dist, bibcorpus:npnkhoi/memefal-paper | note: venue not corroborated by both sources
- score 0.3187 (cites 0.0, cocite 0.125, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The nonexistence of resources dealing with fallacious argumentation calls for scalable approaches to data acquisition and annotation, for which the serious games methodology offers an appealing, yet unexplored, alternative." "We present Argotario, a serious game that deals with fallacies in everyday argumentation." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it types defective inference.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{habernal2017argotario,
  title = {Argotario: Computational Argumentation Meets Serious Games},
  author = {Ivan Habernal and Raffael Hannemann and Christian Pollak and Christopher Klamm and Patrick Pauli and Iryna Gurevych},
  year = {2017},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},
  doi = {10.18653/v1/d17-2002},
  url = {https://aclanthology.org/D17-2002/},
}
```

</details>

#### Henning Wachsmuth et al. (2017). *Argumentation Quality Assessment: Theory vs. Practice*. Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers).

- `doi:10.18653/v1/p17-2039` | aliases: `acl:P17-2039`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://aclanthology.org/P17-2039/) | [OA PDF](https://aclanthology.org/P17-2039.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist
- score 0.3583 (cites 0.0, cocite 0.0, keyword 0.8333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Argumentation quality is viewed differently in argumentation theory and in practical assessment approaches." "Our results clarify how the two views can learn from each other." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{wachsmuth2017argumentat,
  title = {Argumentation Quality Assessment: Theory vs. Practice},
  author = {Henning Wachsmuth and Nona Naderi and Ivan Habernal and Yufang Hou and Graeme Hirst and Iryna Gurevych and Benno Stein},
  year = {2017},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
  doi = {10.18653/v1/p17-2039},
  url = {https://aclanthology.org/P17-2039/},
}
```

</details>

#### Henning Wachsmuth et al. (2017). *Computational Argumentation Quality Assessment in Natural Language*. Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 1, Long Papers.

- `title:55893f7c5565660a055d8f689db3e97c66843203` | aliases: `acl:E17-1017`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://aclanthology.org/E17-1017/) | [OA PDF](https://aclanthology.org/E17-1017.pdf)
- verified against: acl, bibcorpus:allenai/ir_datasets, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database, bibcorpus:nexuspllc/responsiveness-bench
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This paper presents the first holistic work on computational argumentation quality in natural language." "In addition, we provide a corpus with 320 arguments, annotated for all 15 dimensions in the taxonomy." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{wachsmuth2017computatio,
  title = {Computational Argumentation Quality Assessment in Natural Language},
  author = {Henning Wachsmuth and Nona Naderi and Yufang Hou and Yonatan Bilu and Vinodkumar Prabhakaran and Tim Alberdingk Thijm and Graeme Hirst and Benno Stein},
  year = {2017},
  booktitle = {Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 1, Long Papers},
  url = {https://aclanthology.org/E17-1017/},
}
```

</details>

#### Roy Bar-Haim, Lilach Edelstein, Charles Jochim and Noam Slonim (2017). *Improving Claim Stance Classification with Lexical Knowledge Expansion and Context Utilization*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5104` | aliases: `acl:W17-5104`
- doc_type: `workshop` | tier: T2 | tags: extraction, quality | also in: mining
- [landing](https://aclanthology.org/W17-5104/) | [OA PDF](https://aclanthology.org/W17-5104.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook | note: venue not corroborated by both sources
- score 0.2333 (cites 0.0, cocite 0.0, keyword 0.3333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Stance classification is a core component in on-demand argument construction pipelines." "We show that both accuracy and coverage can be significantly improved through automatic expansion of the initial lexicon." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{barhaim2017improving,
  title = {Improving Claim Stance Classification with Lexical Knowledge Expansion and Context Utilization},
  author = {Roy Bar-Haim and Lilach Edelstein and Charles Jochim and Noam Slonim},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5104},
  url = {https://aclanthology.org/W17-5104/},
}
```

</details>

#### Alexey Borisov, Ilya Markov, Maarten de Rijke and Pavel Serdyukov (2016). *A Neural Click Model for Web Search*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2883033`
- doc_type: `conference` | tier: T2 | tags: dialogue, quality
- [landing](https://doi.org/10.1145/2872427.2883033)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.1396 (cites 0.0, cocite 0.125, keyword 0.0833, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "They are based on the probabilistic graphical model (PGM) framework, in which user behavior is represented as a sequence of observable and hidden events." "We propose an alternative based on the idea of distributed representations: to represent the user's information need and the information available to the user with a vector state." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it gives quality dimensions or a scoring target.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{borisov2016aneuralc,
  title = {A Neural Click Model for Web Search},
  author = {Alexey Borisov and Ilya Markov and Maarten de Rijke and Pavel Serdyukov},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2883033},
  url = {https://doi.org/10.1145/2872427.2883033},
}
```

</details>

#### Samuel Barbosa, Dan Cosley, Amit Sharma and Roberto M. Cesar (2016). *Averaging Gone Wrong: Using Time-Aware Analyses to Better Understand Behavior*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2883083`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://doi.org/10.1145/2872427.2883083)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.1604 (cites 0.0, cocite 0.125, keyword 0.1667, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Because both people and communities change over time, we argue that analyses of these communities that take time into account will lead to deeper and more accurate results." "Using Reddit as an example, we study the evolution of users based on comment and submission data from 2007 to 2014." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{barbosa2016averaging,
  title = {Averaging Gone Wrong: Using Time-Aware Analyses to Better Understand Behavior},
  author = {Samuel Barbosa and Dan Cosley and Amit Sharma and Roberto M. Cesar},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2883083},
  url = {https://doi.org/10.1145/2872427.2883083},
}
```

</details>

#### Yixuan Li et al. (2016). *In a World That Counts: Clustering and Detecting Fake Social Engagement at Scale*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2882972`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://doi.org/10.1145/2872427.2882972)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.1396 (cites 0.0, cocite 0.125, keyword 0.0833, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we focus on the social site of YouTube and the problem of identifying bad actors posting inorganic contents and inflating the count of social engagement metrics." "We propose an effective method, Leas (Local Expansion at Scale), and show how the fake engagement activities on YouTube can be tracked over time by analyzing the temporal graph based on the engagement behavior pattern between users and YouTube videos." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{li2016inaworld,
  title = {In a World That Counts: Clustering and Detecting Fake Social Engagement at Scale},
  author = {Yixuan Li and Oscar Martinez and Xing Chen and Yi Li and John E. Hopcroft},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2882972},
  url = {https://doi.org/10.1145/2872427.2882972},
}
```

</details>

#### Jiezhong Qiu et al. (2016). *The Lifecycle and Cascade of WeChat Social Messaging Groups*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2882979`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://doi.org/10.1145/2872427.2882979)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.1396 (cites 0.0, cocite 0.125, keyword 0.0833, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we analyze the daily usage logs from WeChat group messaging platform the largest standalone messaging communication service in China with the goal of understanding the processes by which social messaging groups come together, grow new members, and evolve over time." "In addition to modeling the growth and evolution from group-level perspective, we investigate the individual-level attributes of group members and study the diffusion process by which groups gain new members." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{qiu2016thelifecy,
  title = {The Lifecycle and Cascade of WeChat Social Messaging Groups},
  author = {Jiezhong Qiu and Yixuan Li and Jie Tang and Zheng Lu and Hao Ye and Bo Chen and Qiang Yang and John E. Hopcroft},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2882979},
  url = {https://doi.org/10.1145/2872427.2882979},
}
```

</details>

#### Alexey Borisov, Pavel Serdyukov and Maarten de Rijke (2016). *Using Metafeatures to Increase the Effectiveness of Latent Semantic Models in Web Search*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2882987`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://doi.org/10.1145/2872427.2882987)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.1604 (cites 0.0, cocite 0.125, keyword 0.1667, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We argue that this is not optimal, because a single value output by a latent semantic model may be insufficient to describe all aspects of the model's prediction, and thus some information captured by the model is not used effectively by the search engine." "To increase the effectiveness of latent semantic models in web search, we propose to create metafeatures-feature vectors that describe the structure of the model's prediction for a given query-document pair and pass them to the global ranker along with the models? scores." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{borisov2016usingmeta,
  title = {Using Metafeatures to Increase the Effectiveness of Latent Semantic Models in Web Search},
  author = {Alexey Borisov and Pavel Serdyukov and Maarten de Rijke},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2882987},
  url = {https://doi.org/10.1145/2872427.2882987},
}
```

</details>

#### Jiongqian Liang et al. (2016). *What Links Alice and Bob? Matching and Ranking Semantic Patterns in Heterogeneous Networks*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2883007`
- doc_type: `conference` | tier: T2 | tags: dialogue, quality
- [landing](https://doi.org/10.1145/2872427.2883007)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.1604 (cites 0.0, cocite 0.125, keyword 0.1667, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "An increasing number of applications are modeled and analyzed in network form, where nodes represent entities of interest and edges represent interactions or relationships between entities." "Commonly, such relationship analysis tools assume homogeneity in both node type and edge type." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it gives quality dimensions or a scoring target.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{liang2016whatlinks,
  title = {What Links Alice and Bob? Matching and Ranking Semantic Patterns in Heterogeneous Networks},
  author = {Jiongqian Liang and Deepak Ajwani and Patrick K. Nicholson and Alessandra Sala and Srinivasan Parthasarathy},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2883007},
  url = {https://doi.org/10.1145/2872427.2883007},
}
```

</details>

#### Sandro Bauer, Filip Radlinski and Ryen W. White (2016). *Where Can I Buy a Boulder? Searching for Offline Retail Locations*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2882998`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://doi.org/10.1145/2872427.2882998)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.1812 (cites 0.0, cocite 0.125, keyword 0.25, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we investigate "where can I buy"-style queries related to in-person purchases of products and services." "Our final contribution is a new evaluation framework that combines distance with store relevance in measuring the effectiveness of such a search system." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{bauer2016wherecan,
  title = {Where Can I Buy a Boulder? Searching for Offline Retail Locations},
  author = {Sandro Bauer and Filip Radlinski and Ryen W. White},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2882998},
  url = {https://doi.org/10.1145/2872427.2882998},
}
```

</details>

#### Ivan Habernal and Iryna Gurevych (2016). *Which argument is more convincing? Analyzing and predicting convincingness of Web arguments using bidirectional LSTM*. Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/p16-1150` | aliases: `acl:P16-1150`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://aclanthology.org/P16-1150/) | [OA PDF](https://aclanthology.org/P16-1150.pdf)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:xinyannnnnnn/fact-driven-storytelling-with-llms
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2016), verified against 3 sources. For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{habernal2016whichargu,
  title = {Which argument is more convincing? Analyzing and predicting convincingness of Web arguments using bidirectional LSTM},
  author = {Ivan Habernal and Iryna Gurevych},
  year = {2016},
  booktitle = {Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/p16-1150},
  url = {https://aclanthology.org/P16-1150/},
}
```

</details>

### T3 - Dataset / tool / annotation guideline, including the guideline documents themselves.

#### Min-Hsuan Yeh, Ruyuan Wan and Ting-Hao Kenneth Huang (2024). *CoCoLoFa: A Dataset of News Comments with Common Logical Fallacies Written by LLM-Assisted Crowds*. Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2024.emnlp-main.39` | aliases: `acl:2024.emnlp-main.39`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction, fallacy, quality | also in: llm, resources
- [landing](https://aclanthology.org/2024.emnlp-main.39/) | [OA PDF](https://aclanthology.org/2024.emnlp-main.39.pdf) (via acl)
- verified against: acl, bibcorpus:npnkhoi/memefal-paper
- score 0.3187 (cites 0.0, cocite 0.125, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Manually annotating fallacies in large-scale, real-world text data to create datasets for developing and validating detection models is costly." "This paper introduces CoCoLoFa, the largest known logical fallacy dataset, containing 7,706 comments for 648 news articles, with each comment labeled for fallacy presence and type." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it types defective inference.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{yeh2024cocolofa,
  title = {CoCoLoFa: A Dataset of News Comments with Common Logical Fallacies Written by LLM-Assisted Crowds},
  author = {Min-Hsuan Yeh and Ruyuan Wan and Ting-Hao Kenneth Huang},
  year = {2024},
  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/2024.emnlp-main.39},
  url = {https://aclanthology.org/2024.emnlp-main.39/},
}
```

</details>

#### Saumya Sahai, Oana Balalau and Roxana Horincar (2021). *Breaking Down the Invisible Wall of Informal Fallacies in Online Discussions*. Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers).

- `doi:10.18653/v1/2021.acl-long.53` | aliases: `acl:2021.acl-long.53`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue, fallacy, quality | also in: dialogue, resources
- [landing](https://aclanthology.org/2021.acl-long.53/) | [OA PDF](https://aclanthology.org/2021.acl-long.53.pdf) (via acl)
- verified against: acl, bibcorpus:lefteriskat/Logical-Fallacy-Detection-Using-LLMs, bibcorpus:npnkhoi/memefal-paper
- score 0.2672 (cites 0.0, cocite 0.1562, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we study the most frequent fallacies on Reddit, and we present them using the pragma-dialectical theory of argumentation." "We construct a new annotated dataset of fallacies, using user comments containing fallacy mentions as noisy labels, and cleaning the data via crowdsourcing." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it gives quality dimensions or a scoring target.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{sahai2021breakingd,
  title = {Breaking Down the Invisible Wall of Informal Fallacies in Online Discussions},
  author = {Saumya Sahai and Oana Balalau and Roxana Horincar},
  year = {2021},
  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},
  doi = {10.18653/v1/2021.acl-long.53},
  url = {https://aclanthology.org/2021.acl-long.53/},
}
```

</details>

#### Shai Gretz et al. (2020). *A large-scale dataset for argument quality ranking: Construction and analysis*. AAAI.

- `title:a9d9191746f644eca733d0b0d7b6a25bd4853ba2`
- doc_type: `conference` | tier: T3 | tags: dataset, quality | also in: resources
- [landing](https://api.semanticscholar.org/CorpusID:208291067) | [repo](https://github.com/Hellisotherpeople/DebateSum)
- verified against: bibcorpus:BarryMafu/LitLens, bibcorpus:xinyannnnnnn/fact-driven-storytelling-with-llms | note: bibcorpus:dimits-ts/llm_moderation_research: venue mismatch ('AAAI' vs 'ArXiv'); bibcorpus:dimits-ts/synthetic_moderation_experiments: venue mismatch ('AAAI' vs 'ArXiv') repo linked on token overlap:…
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, AAAI, 2020), verified against 2 sources. For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{gretz2020alargesc,
  title = {A large-scale dataset for argument quality ranking: Construction and analysis},
  author = {Shai Gretz and Roni Friedman and Edo Cohen-Karlik and Assaf Toledo and Dan Lahav and Ranit Aharonov and Noam Slonim},
  year = {2020},
  booktitle = {AAAI},
  url = {https://api.semanticscholar.org/CorpusID:208291067},
}
```

</details>

#### Lily Ng, Anne Lauscher, Joel Tetreault and Courtney Napoles (2020). *Creating a Domain-diverse Corpus for Theory-based Argument Quality Assessment*. Proceedings of the 7th Workshop on Argument Mining.

- `title:8973c9782426ec9080181ce8b676df529016c076` | aliases: `acl:2020.argmining-1.13`
- doc_type: `workshop` | tier: T3 | tags: dataset, extraction, quality | also in: resources
- [landing](https://aclanthology.org/2020.argmining-1.13/) | [OA PDF](https://aclanthology.org/2020.argmining-1.13.pdf) (via acl) | [repo](https://github.com/jayliqinzhang/A-Dutch-essay-corpus-with-argument-structures-and-quality-indicators)
- verified against: acl, bibcorpus:m0re4u/paper-database | note: repo linked on token overlap: ['argument', 'corpus', 'quality']
- score 0.4 (cites 0.0, cocite 0.0, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this work, we describe GAQCorpus, the first large, domain-diverse annotated corpus of theory-based AQ." "We discuss how we designed the annotation task to reliably collect a large number of judgments with crowdsourcing, formulating theory-based guidelines that helped make subjective judgments of AQ more objective." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{ng2020creatinga,
  title = {Creating a Domain-diverse Corpus for Theory-based Argument Quality Assessment},
  author = {Lily Ng and Anne Lauscher and Joel Tetreault and Courtney Napoles},
  year = {2020},
  booktitle = {Proceedings of the 7th Workshop on Argument Mining},
  url = {https://aclanthology.org/2020.argmining-1.13/},
}
```

</details>

### T4 - Recent (2023-2026). LLM-era work; lower durability confidence, high build relevance.

#### Abhinav Lalwani et al. (2025). *Autoformalizing Natural Language to First-Order Logic: A Case Study in Logical Fallacy Detection*. Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics.

- `doi:10.18653/v1/2025.findings-ijcnlp.8` | aliases: `acl:2025.findings-ijcnlp.8`, `arxiv:2405.02318`
- doc_type: `conference` | tier: T4 | tags: extraction, fallacy, quality | also in: llm
- [landing](https://aclanthology.org/2025.findings-ijcnlp.8/) | [OA PDF](https://arxiv.org/pdf/2405.02318) (via arxiv)
- verified against: acl, bibcorpus:danny-v-nguyen/thesis | note: venue not corroborated by both sources
- score 0.4437 (cites 0.0, cocite 0.125, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we introduce Natural Language to First-Order Logic (NL2FOL), a framework to autoformalize natural language to FOL step-by-step using Large Language Models (LLMs)." "We present logical fallacy detection as a case study to evaluate the efficacy of NL2FOL." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it types defective inference.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{lalwani2025autoformal,
  title = {Autoformalizing Natural Language to First-Order Logic: A Case Study in Logical Fallacy Detection},
  author = {Abhinav Lalwani and Tasha Kim and Lovish Chopra and Christopher Hahn and Zhijing Jin and Mrinmaya Sachan},
  year = {2025},
  booktitle = {Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics},
  doi = {10.18653/v1/2025.findings-ijcnlp.8},
  url = {https://aclanthology.org/2025.findings-ijcnlp.8/},
}
```

</details>

#### Rositsa V Ivanova and Reto Gubelmann (2025). *The Shift from Logic to Dialectic in Argumentation Theory: Implications for Computational Argument Quality Assessment*. Proceedings of the 31st International Conference on Computational Linguistics.

- `title:3081c2f49d86b933976822d3e21e4f8fdc9410a6` | aliases: `acl:2025.coling-main.321`
- doc_type: `conference` | tier: T4 | tags: quality
- [landing](https://aclanthology.org/2025.coling-main.321/) | [OA PDF](https://aclanthology.org/2025.coling-main.321.pdf) (via acl)
- verified against: acl, bibcorpus:nexuspllc/responsiveness-bench
- score 0.4437 (cites 0.0, cocite 0.125, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We show how, in the course of this development, dialectical considerations have taken center stage, at the cost of the logical perspective." "We propose an even clearer separation between the two quality dimensions not only in regards to their definitions, but also in regards to the granularity at which the argumentative text is being annotated and assessed." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{ivanova2025theshift,
  title = {The Shift from Logic to Dialectic in Argumentation Theory: Implications for Computational Argument Quality Assessment},
  author = {Rositsa V Ivanova and Reto Gubelmann},
  year = {2025},
  booktitle = {Proceedings of the 31st International Conference on Computational Linguistics},
  url = {https://aclanthology.org/2025.coling-main.321/},
}
```

</details>

## 6.4 Dialogue and debate (17 entries, quota 40)

### T1 - Foundational / survey. Read in full: theory anchors, major surveys, canonical papers.

#### Ramon Ruiz-Dolz, John Lawrence, Ella Schad and Chris Reed (2024). *Overview of DialAM-2024: Argument Mining in Natural Language Dialogues*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.8` | aliases: `acl:2024.argmining-1.8`
- doc_type: `workshop` | tier: T1 | tags: dialogue, extraction | also in: mining
- [landing](https://aclanthology.org/2024.argmining-1.8/) | [OA PDF](https://aclanthology.org/2024.argmining-1.8.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.5432 (cites 0.0, cocite 0.4688, keyword 0.9167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Argumentation is the process by which humans rationally elaborate their thoughts and opinions in written (e.g., essays) or spoken (e.g., debates) contexts." "In this paper, we present an overview of DialAM-2024, the first shared task in dialogical argument mining, where argumentative relations and speech illocutions are modelled together in a unified framework." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{ruizdolz2024overviewo,
  title = {Overview of DialAM-2024: Argument Mining in Natural Language Dialogues},
  author = {Ramon Ruiz-Dolz and John Lawrence and Ella Schad and Chris Reed},
  year = {2024},
  booktitle = {Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024)},
  doi = {10.18653/v1/2024.argmining-1.8},
  url = {https://aclanthology.org/2024.argmining-1.8/},
}
```

</details>

### T2 - Core method. Defines a task formulation, model, or evaluation still in use.

#### Noam Slonim et al. (2021). *An autonomous debating system*. Nat..

- `doi:10.1038/s41586-021-03215-w`
- doc_type: `journal` | tier: T2 | tags: dialogue | also in: llm
- [landing](https://doi.org/10.1038/s41586-021-03215-w)
- verified against: bibcorpus:CogSciPrag/project_ideas, bibcorpus:borgr/publications | note: bibcorpus:danielhers/danielhers.github.io: venue mismatch ('Nat.' vs 'Nature')
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Artificial intelligence (AI) is defined as the ability of machines to perform tasks that are usually associated with intelligent beings." "Here we present Project Debater, an autonomous debating system that can engage in a competitive debate with humans." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@article{slonim2021anautonom,
  title = {An autonomous debating system},
  author = {Noam Slonim and Yonatan Bilu and Carlos Alzate and Roy Bar-Haim and Ben Bogin and Francesca Bonin and Leshem Choshen and Edo Cohen-Karlik and Lena Dankin and Lilach Edelstein and Liat Ein-Dor and Roni Friedman-Melamed and Assaf Gavron and Ariel Gera and Martin Gleize and Shai Gretz and Dan Gutfreund and Alon Halfon and Daniel Hershcovich and Ron Hoory and Yufang Hou and Shay Hummel and Michal Jacovi and Charles Jochim and Yoav Kantor and Yoav Katz and David Konopnicki and Zvi Kons and Lili Kotlerman and Dalia Krieger and Dan Lahav and Tamar Lavee and Ran Levy and Naftali Liberman and Yosi Mass and Amir Menczel and Shachar Mirkin and Guy Moshkowich and Shila Ofek-Koifman and Matan Orbach and Ella Rabinovich and Ruty Rinott and Slava Shechtman and Dafna Sheinwald and Eyal Shnarch and Ilya Shnayderman and Aya Soffer and Artem Spector and Benjamin Sznajder and Assaf Toledo and Orith Toledo-Ronen and Elad Venezian and Ranit Aharonov},
  year = {2021},
  journal = {Nat.},
  doi = {10.1038/s41586-021-03215-w},
  url = {https://doi.org/10.1038/s41586-021-03215-w},
}
```

</details>

#### Christopher T. Small et al. (2021). *Polis: Scaling Deliberation by Mapping High Dimensional Opinion Spaces*. Recerca: Revista de pensament i analisi.

- `doi:10.6035/recerca.5516`
- doc_type: `conference` | tier: T2 | tags: dialogue
- no URL recorded
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments, bibcorpus:ochyai/open-japan-politech-platform
- score 0.4865 (cites 0.0, cocite 0.9375, keyword 0.3333, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Recerca: Revista de pensament i analisi, 2021), verified against 3 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{small2021polissca,
  title = {Polis: Scaling Deliberation by Mapping High Dimensional Opinion Spaces},
  author = {Christopher T. Small and Michael Bjorkegren and Timo Erkkilä and Lynette Shaw and Colin Megill},
  year = {2021},
  booktitle = {Recerca: Revista de pensament i analisi},
  doi = {10.6035/recerca.5516},
}
```

</details>

#### Justine Zhang et al. (2018). *Conversations Gone Awry: Detecting Early Signs of Conversational Failure*. Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/p18-1125` | aliases: `acl:P18-1125`
- doc_type: `conference` | tier: T2 | tags: dialogue
- [landing](https://aclanthology.org/P18-1125/) | [OA PDF](https://aclanthology.org/P18-1125.pdf) (via acl)
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments | note: acl: venue mismatch ('CoRR' vs 'Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)')
- score 0.4651 (cites 0.0, cocite 0.7812, keyword 0.1667, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this work, we introduce the task of predicting from the very start of a conversation whether it will get out of hand." "To this end, we develop a framework for capturing pragmatic devices—such as politeness strategies and rhetorical prompts—used to start a conversation, and analyze their relation to its future trajectory." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{zhang2018conversati,
  title = {Conversations Gone Awry: Detecting Early Signs of Conversational Failure},
  author = {Justine Zhang and Jonathan Chang and Cristian Danescu-Niculescu-Mizil and Lucas Dixon and Yiqing Hua and Dario Taraborelli and Nithum Thain},
  year = {2018},
  booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/p18-1125},
  url = {https://aclanthology.org/P18-1125/},
}
```

</details>

#### Justine Zhang, Ravi Kumar, Sujith Ravi and Cristian Danescu-Niculescu-Mizil (2016). *Conversational Flow in Oxford-style Debates*. Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.

- `doi:10.18653/v1/n16-1017` | aliases: `acl:N16-1017`
- doc_type: `conference` | tier: T2 | tags: dialogue
- [landing](https://aclanthology.org/N16-1017/) | [OA PDF](https://aclanthology.org/N16-1017.pdf) (via acl)
- verified against: acl, bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments, bibcorpus:lihebi/biber-dist | note: venue not corroborated by both sources
- score 0.5484 (cites 0.0, cocite 0.7812, keyword 0.5, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, 2016), verified against 4 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{zhang2016conversati,
  title = {Conversational Flow in Oxford-style Debates},
  author = {Justine Zhang and Ravi Kumar and Sujith Ravi and Cristian Danescu-Niculescu-Mizil},
  year = {2016},
  booktitle = {Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  doi = {10.18653/v1/n16-1017},
  url = {https://aclanthology.org/N16-1017/},
}
```

</details>

#### Filip Boltužić and Jan Šnajder (2016). *Fill the Gap! Analyzing Implicit Premises between Claims from Online Debates*. Proceedings of the Third Workshop on Argument Mining (ArgMining2016).

- `doi:10.18653/v1/w16-2815` | aliases: `acl:W16-2815`
- doc_type: `workshop` | tier: T2 | tags: dialogue, extraction | also in: mining
- [landing](https://aclanthology.org/W16-2815/) | [OA PDF](https://aclanthology.org/W16-2815.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.413 (cites 0.0, cocite 0.1562, keyword 0.8333, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (workshop, Proceedings of the Third Workshop on Argument Mining (ArgMining2016), 2016), verified against 2 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{boltui2016filltheg,
  title = {Fill the Gap! Analyzing Implicit Premises between Claims from Online Debates},
  author = {Filip Boltužić and Jan Šnajder},
  year = {2016},
  booktitle = {Proceedings of the Third Workshop on Argument Mining (ArgMining2016)},
  doi = {10.18653/v1/w16-2815},
  url = {https://aclanthology.org/W16-2815/},
}
```

</details>

#### Amit K. Chopra and Munindar P. Singh (2016). *From Social Machines to Social Protocols: Software Engineering Foundations for Sociotechnical Systems*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2883018`
- doc_type: `conference` | tier: T2 | tags: dialogue
- [landing](https://doi.org/10.1145/2872427.2883018)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.1505 (cites 0.0, cocite 0.1562, keyword 0.0833, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The overarching vision of social machines is to facilitate social processes by having computers provide administrative support." "We introduce Interaction-Oriented Software Engineering (IOSE) as a paradigm expressly suited to capturing the social basis of STSs." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{chopra2016fromsocia,
  title = {From Social Machines to Social Protocols: Software Engineering Foundations for Sociotechnical Systems},
  author = {Amit K. Chopra and Munindar P. Singh},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2883018},
  url = {https://doi.org/10.1145/2872427.2883018},
}
```

</details>

#### Yoram Bachrach et al. (2016). *Mechanism Design for Mixed Bidders*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2882983`
- doc_type: `conference` | tier: T2 | tags: dialogue
- [landing](https://doi.org/10.1145/2872427.2882983)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.1505 (cites 0.0, cocite 0.1562, keyword 0.0833, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We introduce a transitional mechanism which encourages advertisers to update their bids to their valuations, while mitigating revenue loss." "In this setting, it is easier to propose first a payment function rather than an allocation function, so we give a general framework which guarantees incentive compatibility by requiring that the payment functions satisfy two specific properties." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{bachrach2016mechanism,
  title = {Mechanism Design for Mixed Bidders},
  author = {Yoram Bachrach and Sofia Ceppi and Ian A. Kash and Peter Key and Mohammad Reza Khani},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2882983},
  url = {https://doi.org/10.1145/2872427.2882983},
}
```

</details>

#### Chantal van Son et al. (2016). *Unshared Task at the 3rd Workshop on Argument Mining: Perspective Based Local Agreement and Disagreement in Online Debate*. Proceedings of the Third Workshop on Argument Mining (ArgMining2016).

- `doi:10.18653/v1/w16-2819` | aliases: `acl:W16-2819`
- doc_type: `workshop` | tier: T2 | tags: dialogue, extraction | also in: mining
- [landing](https://aclanthology.org/W16-2819/) | [OA PDF](https://aclanthology.org/W16-2819.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.4 (cites 0.0, cocite 0.0, keyword 1.0, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (workshop, Proceedings of the Third Workshop on Argument Mining (ArgMining2016), 2016), verified against 2 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{son2016unsharedt,
  title = {Unshared Task at the 3rd Workshop on Argument Mining: Perspective Based Local Agreement and Disagreement in Online Debate},
  author = {Chantal van Son and Tommaso Caselli and Antske Fokkens and Isa Maks and Roser Morante and Lora Aroyo and Piek Vossen},
  year = {2016},
  booktitle = {Proceedings of the Third Workshop on Argument Mining (ArgMining2016)},
  doi = {10.18653/v1/w16-2819},
  url = {https://aclanthology.org/W16-2819/},
}
```

</details>

#### Chenhao Tan, Vlad Niculae, Cristian Danescu-Niculescu-Mizil and Lillian Lee (2016). *Winning Arguments: Interaction Dynamics and Persuasion Strategies in Good-Faith Online Discussions*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2883081`
- doc_type: `conference` | tier: T2 | tags: dataset, dialogue | also in: resources
- [landing](https://doi.org/10.1145/2872427.2883081)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io, bibcorpus:m0re4u/paper-database
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this work, we study these interactions to understand the mechanisms behind persuasion.We find that persuasive arguments are characterized by interesting patterns of interaction dynamics, such as participant entry-order and degree of back-and-forth exchange." "Furthermore, by comparing similar counterarguments to the same opinion, we show that language factors play an essential role." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{tan2016winningar,
  title = {Winning Arguments: Interaction Dynamics and Persuasion Strategies in Good-Faith Online Discussions},
  author = {Chenhao Tan and Vlad Niculae and Cristian Danescu-Niculescu-Mizil and Lillian Lee},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2883081},
  url = {https://doi.org/10.1145/2872427.2883081},
}
```

</details>

#### Scott Wright and John Street (2007). *Democracy, deliberation and design: the case of online discussion forums*. New Media & Society.

- `doi:10.1177/1461444807081230`
- doc_type: `journal` | tier: T2 | tags: dialogue
- [landing](https://doi.org/10.1177/1461444807081230)
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments
- score 0.4318 (cites 0.0, cocite 0.7812, keyword 0.3333, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Within democratic theory, the deliberative variant has assumed pre-eminence." "It represents for many the ideal of democracy, and in pursuit of this ideal, online discussion forums have been proposed as solutions to the practical limits to mass deliberation." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@article{wright2007democracy,
  title = {Democracy, deliberation and design: the case of online discussion forums},
  author = {Scott Wright and John Street},
  year = {2007},
  journal = {New Media & Society},
  doi = {10.1177/1461444807081230},
  url = {https://doi.org/10.1177/1461444807081230},
}
```

</details>

### T3 - Dataset / tool / annotation guideline, including the guideline documents themselves.

#### Annette Hautli-Janisz et al. (2022). *QT30: A Corpus of Argument and Conflict in Broadcast Debate*. Proceedings of the Thirteenth Language Resources and Evaluation Conference.

- `title:e4827cf79a5103f624f48b2e7d4a4ccc7ab6c0ea` | aliases: `acl:2022.lrec-1.352`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue, extraction | also in: resources
- [landing](https://aclanthology.org/2022.lrec-1.352/) | [OA PDF](https://aclanthology.org/2022.lrec-1.352.pdf)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "With QT30, we present the largest corpus of analysed dialogical argumentation ever created (19,842 utterances, 280,000 words) and also the largest corpus of analysed broadcast political debate to date, using 30 episodes of BBC’s ‘Question Time’ from 2020 and 2021." "QT30 is annotated with Inference Anchoring Theory, a framework well-known in argument mining, which encodes the way arguments and conflicts are created and reacted to in dialogical settings." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{hautlijanisz2022qtaco,
  title = {QT30: A Corpus of Argument and Conflict in Broadcast Debate},
  author = {Annette Hautli-Janisz and Zlata Kikteva and Wassiliki Siskou and Kamila Gorska and Ray Becker and Chris Reed},
  year = {2022},
  booktitle = {Proceedings of the Thirteenth Language Resources and Evaluation Conference},
  url = {https://aclanthology.org/2022.lrec-1.352/},
}
```

</details>

#### Kasia Budzynska et al. (2014). *A Model for Processing Illocutionary Structures and Argumentation in Debates*. Proceedings of the Ninth International Conference on Language Resources and Evaluation (LREC'14).

- `title:5c30e54b1303736b308e1674274f1a1132b052df` | aliases: `acl:L14-1599`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue, extraction | also in: resources
- [landing](https://aclanthology.org/L14-1599/) | [OA PDF](https://aclanthology.org/L14-1599.pdf) (via acl)
- verified against: acl, bibcorpus:davidar/dblp.yaml
- score 0.4 (cites 0.0, cocite 0.0, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we briefly present the objectives of Inference Anchoring Theory (IAT) and the formal structure which is proposed for dialogues." "Then, we introduce our development corpus, and a computational model designed for the identification of discourse minimal units in the context of argumentation and the illocutionary force associated with each unit." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{budzynska2014amodelfo,
  title = {A Model for Processing Illocutionary Structures and Argumentation in Debates},
  author = {Kasia Budzynska and Mathilde Janier and Chris Reed and Patrick Saint-Dizier and Manfred Stede and Olena Yakorska},
  year = {2014},
  booktitle = {Proceedings of the Ninth International Conference on Language Resources and Evaluation (LREC'14)},
  url = {https://aclanthology.org/L14-1599/},
}
```

</details>

#### Marilyn Walker et al. (2012). *A Corpus for Research on Deliberation and Debate*. Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12).

- `title:ae7588dc60be7ab8f03855ae779ec0f0519a8728` | aliases: `acl:L12-1643`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue | also in: resources
- [landing](https://aclanthology.org/L12-1643/) | [OA PDF](https://aclanthology.org/L12-1643.pdf)
- verified against: acl, bibcorpus:davidar/dblp.yaml | note: Internet Argument Corpus; exact title must be verified.
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This paper presents the Internet Argument Corpus (IAC), a set of 390,704 posts in 11,800 discussions extracted from the online debate site 4forums.com." "A 2866 thread/130,206 post extract of the corpus has been manually sided for topic of discussion, and subsets of this topic-labeled extract have been annotated for several dialogic and argumentative markers: degrees of agreement with a previous post, cordiality, audience-direction, combativeness, assertiveness, emotio…" For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{walker2012acorpusf,
  title = {A Corpus for Research on Deliberation and Debate},
  author = {Marilyn Walker and Jean Fox Tree and Pranav Anand and Rob Abbott and Joseph King},
  year = {2012},
  booktitle = {Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12)},
  url = {https://aclanthology.org/L12-1643/},
}
```

</details>

### T4 - Recent (2023-2026). LLM-era work; lower durability confidence, high build relevance.

#### Arne Binder, Tatiana Anikina, Leonhard Hennig and Simon Ostermann (2024). *DFKI-MLST at DialAM-2024 Shared Task: System Description*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.9` | aliases: `acl:2024.argmining-1.9`
- doc_type: `workshop` | tier: T4 | tags: dialogue, extraction | also in: mining
- [landing](https://aclanthology.org/2024.argmining-1.9/) | [OA PDF](https://aclanthology.org/2024.argmining-1.9.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.4391 (cites 0.0, cocite 0.4688, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This paper presents the dfki-mlst submission for the DialAM shared task (Ruiz-Dolz et al., 2024) on identification of argumentative and illocutionary relations in dialogue." "We describe our implementation of the data pre-processing, relation encoding and classification, evaluating 11 different base models and performing experiments with, e.g., node text combination and data augmentation." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{binder2024dfkimlst,
  title = {DFKI-MLST at DialAM-2024 Shared Task: System Description},
  author = {Arne Binder and Tatiana Anikina and Leonhard Hennig and Simon Ostermann},
  year = {2024},
  booktitle = {Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024)},
  doi = {10.18653/v1/2024.argmining-1.9},
  url = {https://aclanthology.org/2024.argmining-1.9/},
}
```

</details>

#### Yuetong Wu et al. (2024). *KnowComp at DialAM-2024: Fine-tuning Pre-trained Language Models for Dialogical Argument Mining with Inference Anchoring Theory*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.10` | aliases: `acl:2024.argmining-1.10`
- doc_type: `workshop` | tier: T4 | tags: dialogue, extraction, formal | also in: formal, mining
- [landing](https://aclanthology.org/2024.argmining-1.10/) | [OA PDF](https://aclanthology.org/2024.argmining-1.10.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.5641 (cites 0.0, cocite 0.4688, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we present our framework for DialAM-2024 TaskA: Identification of Propositional Relations and TaskB: Identification of Illocutionary Relations." "Noticing the definition of the relations are strict and professional under the context of IAT framework, we meticulously curate prompts which not only incorporate formal definition of the relations, but also exhibit the subtle differences between them." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it supplies the formal semantics for deciding what stands once arguments and attacks are stored.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{wu2024knowcompa,
  title = {KnowComp at DialAM-2024: Fine-tuning Pre-trained Language Models for Dialogical Argument Mining with Inference Anchoring Theory},
  author = {Yuetong Wu and Yukai Zhou and Baixuan Xu and Weiqi Wang and Yangqiu Song},
  year = {2024},
  booktitle = {Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024)},
  doi = {10.18653/v1/2024.argmining-1.10},
  url = {https://aclanthology.org/2024.argmining-1.10/},
}
```

</details>

#### Sirawut Chaixanien, Eugene Choi, Shaden Shaar and Claire Cardie (2024). *Pungene at DialAM-2024: Identification of Propositional and Illocutionary Relations*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.12` | aliases: `acl:2024.argmining-1.12`
- doc_type: `workshop` | tier: T4 | tags: dialogue, extraction
- [landing](https://aclanthology.org/2024.argmining-1.12/) | [OA PDF](https://aclanthology.org/2024.argmining-1.12.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.5641 (cites 0.0, cocite 0.4688, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper we tackle the shared task DialAM-2024 aiming to annotate dialogue based on the inference anchoring theory (IAT)." "We propose a pipelined system made up of three parts: (1) locutionary-propositions relation detection, (2) propositional relations detection, and (3) illocutionary relations identification." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{chaixanien2024pungeneat,
  title = {Pungene at DialAM-2024: Identification of Propositional and Illocutionary Relations},
  author = {Sirawut Chaixanien and Eugene Choi and Shaden Shaar and Claire Cardie},
  year = {2024},
  booktitle = {Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024)},
  doi = {10.18653/v1/2024.argmining-1.12},
  url = {https://aclanthology.org/2024.argmining-1.12/},
}
```

</details>

## 6.5 LLM era, 2023-2026 (14 entries, quota 40)

### T1 - Foundational / survey. Read in full: theory anchors, major surveys, canonical papers.

#### Lixing Zhu, Runcong Zhao, Lin Gui and Yulan He (2023). *Are NLP Models Good at Tracing Thoughts: An Overview of Narrative Understanding*. Findings of the Association for Computational Linguistics: EMNLP 2023.

- `doi:10.18653/v1/2023.findings-emnlp.677` | aliases: `acl:2023.findings-emnlp.677`
- doc_type: `conference` | tier: T1 | tags: extraction
- [landing](https://aclanthology.org/2023.findings-emnlp.677/) | [OA PDF](https://aclanthology.org/2023.findings-emnlp.677.pdf) (via acl)
- verified against: acl, bibcorpus:xinyannnnnnn/fact-driven-storytelling-with-llms
- score 0.425 (cites 0.0, cocite 0.25, keyword 0.75, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Narrative understanding involves capturing the author’s cognitive processes, providing insights into their knowledge, intentions, beliefs, and desires." "In this paper, we conduct a comprehensive survey of narrative understanding tasks, thoroughly examining their key features, definitions, taxonomy, associated datasets, training objectives, evaluation metrics, and limitations." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{zhu2023arenlpmo,
  title = {Are NLP Models Good at Tracing Thoughts: An Overview of Narrative Understanding},
  author = {Lixing Zhu and Runcong Zhao and Lin Gui and Yulan He},
  year = {2023},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2023},
  doi = {10.18653/v1/2023.findings-emnlp.677},
  url = {https://aclanthology.org/2023.findings-emnlp.677/},
}
```

</details>

### T2 - Core method. Defines a task formulation, model, or evaluation still in use.

#### Joon Sung Park et al. (2022). *Social Simulacra: Creating Populated Prototypes for Social Computing Systems*. Proceedings of the 35th Annual ACM Symposium on User Interface Software and Technology.

- `doi:10.1145/3526113.3545616`
- doc_type: `conference` | tier: T2 | tags: dialogue
- [landing](https://doi.org/10.1145/3526113.3545616)
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments | note: venue not corroborated by both sources
- score 0.4604 (cites 0.0, cocite 0.625, keyword 0.6667, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We introduce social simulacra, a prototyping technique that generates a breadth of realistic social interactions that may emerge when a social computing system is populated." "In evaluations, we show that participants are often unable to distinguish social simulacra from actual community behavior and that social computing designers successfully refine their social computing designs when using social simulacra." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{park2022socialsim,
  title = {Social Simulacra: Creating Populated Prototypes for Social Computing Systems},
  author = {Joon Sung Park and Lindsay Popowski and Carrie Cai and Meredith Ringel Morris and Percy Liang and Michael S. Bernstein},
  year = {2022},
  booktitle = {Proceedings of the 35th Annual ACM Symposium on User Interface Software and Technology},
  doi = {10.1145/3526113.3545616},
  url = {https://doi.org/10.1145/3526113.3545616},
}
```

</details>

#### Michiel van der Meer et al. (2022). *Will It Blend? Mixing Training Paradigms & Prompting for Argument Quality Prediction*. Proceedings of the 9th Workshop on Argument Mining.

- `title:c0c3d6e17f097affb03b136b1c855103a0564d72` | aliases: `acl:2022.argmining-1.8`
- doc_type: `workshop` | tier: T2 | tags: extraction, quality | also in: quality
- [landing](https://aclanthology.org/2022.argmining-1.8/) | [OA PDF](https://aclanthology.org/2022.argmining-1.8.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.4 (cites 0.0, cocite 0.0, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This paper describes our contributions to the Shared Task of the 9th Workshop on Argument Mining (2022)." "Our approach uses Large Language Models for the task of Argument Quality Prediction." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{meer2022willitbl,
  title = {Will It Blend? Mixing Training Paradigms & Prompting for Argument Quality Prediction},
  author = {Michiel van der Meer and Myrthe Reuver and Urja Khurana and Lea Krause and Selene Baez Santamaria},
  year = {2022},
  booktitle = {Proceedings of the 9th Workshop on Argument Mining},
  url = {https://aclanthology.org/2022.argmining-1.8/},
}
```

</details>

### T3 - Dataset / tool / annotation guideline, including the guideline documents themselves.

#### Fengjun Pan, Xiaobao Wu, Zongrui Li and Anh Tuan Luu (2024). *Are LLMs Good Zero-Shot Fallacy Classifiers?*. Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2024.emnlp-main.794` | aliases: `acl:2024.emnlp-main.794`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction, fallacy, quality | also in: quality, resources
- [landing](https://aclanthology.org/2024.emnlp-main.794/) | [OA PDF](https://aclanthology.org/2024.emnlp-main.794.pdf) (via acl)
- verified against: acl, bibcorpus:lefteriskat/Logical-Fallacy-Detection-Using-LLMs
- score 0.4437 (cites 0.0, cocite 0.125, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "To elicit fallacy-related knowledge and reasoning abilities of LLMs, we propose diverse single-round and multi-round prompting schemes, applying different taskspecific instructions such as extraction, summarization, and Chain-of-Thought reasoning." "With comprehensive experiments on benchmark datasets, we suggest that LLMs could be potential zero-shot fallacy classifiers." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it types defective inference.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{pan2024arellmsg,
  title = {Are LLMs Good Zero-Shot Fallacy Classifiers?},
  author = {Fengjun Pan and Xiaobao Wu and Zongrui Li and Anh Tuan Luu},
  year = {2024},
  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/2024.emnlp-main.794},
  url = {https://aclanthology.org/2024.emnlp-main.794/},
}
```

</details>

#### Felipe Maia Polo et al. (2024). *tinyBenchmarks: evaluating LLMs with fewer examples*. Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024.

- `title:edb3d8bd1cbd986fc1430e09234833845d0bfe69`
- doc_type: `conference` | tier: T3 | tags: dataset | also in: resources
- [landing](https://openreview.net/forum?id=qAml3FpfhG)
- verified against: bibcorpus:CogSciPrag/project_ideas, bibcorpus:borgr/publications
- score 0.3312 (cites 0.0, cocite 0.375, keyword 0.5, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024, 2024), verified against 2 sources. For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{polo2024tinybenchm,
  title = {tinyBenchmarks: evaluating LLMs with fewer examples},
  author = {Felipe Maia Polo and Lucas Weber and Leshem Choshen and Yuekai Sun and Gongjun Xu and Mikhail Yurochkin},
  year = {2024},
  booktitle = {Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024},
  url = {https://openreview.net/forum?id=qAml3FpfhG},
}
```

</details>

### T4 - Recent (2023-2026). LLM-era work; lower durability confidence, high build relevance.

#### Xiaohou Shi, Jiahao Liu and Yaqi Song (2024). *BERT and LLM-Based Multivariate Hate Speech Detection on Twitter: Comparative Analysis and Superior Performance*. Artificial Intelligence and Machine Learning.

- `title:32e7cb8118fde12ed5a9b2dd19d20e94c9cf25b3`
- doc_type: `conference` | tier: T4 | tags: extraction
- no URL recorded
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments
- score 0.5979 (cites 0.0, cocite 0.625, keyword 0.9167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The analysis will be conducted using the Twitter hate speech dataset." "Experiments were performed on the same dataset using 1-layer BERT, 2-layers BERT, and logistic regression models for both training and prediction purposes." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{shi2024bertandl,
  title = {BERT and LLM-Based Multivariate Hate Speech Detection on Twitter: Comparative Analysis and Superior Performance},
  author = {Xiaohou Shi and Jiahao Liu and Yaqi Song},
  year = {2024},
  booktitle = {Artificial Intelligence and Machine Learning},
}
```

</details>

#### Dennis Ulmer et al. (2024). *Bootstrapping LLM-based Task-Oriented Dialogue Agents via Self-Talk*. Findings of the Association for Computational Linguistics: ACL 2024.

- `doi:10.18653/v1/2024.findings-acl.566` | aliases: `acl:2024.findings-acl.566`
- doc_type: `conference` | tier: T4 | tags: dialogue
- [landing](https://aclanthology.org/2024.findings-acl.566/) | [OA PDF](https://aclanthology.org/2024.findings-acl.566.pdf) (via acl)
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments | note: acl: venue mismatch ('ArXiv' vs 'Findings of the Association for Computational Linguistics: ACL 2024')
- score 0.6188 (cites 0.0, cocite 0.625, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Inspired by the self-play technique in reinforcement learning and the use of LLMs to simulate human agents, we propose a more effective method for data collection through LLMs engaging in a conversation in various roles." "We introduce an automated way to measure the (partial) success of a dialogue." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{ulmer2024bootstrapp,
  title = {Bootstrapping LLM-based Task-Oriented Dialogue Agents via Self-Talk},
  author = {Dennis Ulmer and Elman Mansimov and Kaixiang Lin and Lijia Sun and Xibin Gao and Yi Zhang},
  year = {2024},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},
  doi = {10.18653/v1/2024.findings-acl.566},
  url = {https://aclanthology.org/2024.findings-acl.566/},
}
```

</details>

#### Yanda Li et al. (2024). *Reason from Fallacy: Enhancing Large Language Models’ Logical Reasoning through Logical Fallacy Understanding*. Findings of the Association for Computational Linguistics: NAACL 2024.

- `doi:10.18653/v1/2024.findings-naacl.192` | aliases: `acl:2024.findings-naacl.192`
- doc_type: `conference` | tier: T4 | tags: fallacy, quality | also in: quality
- [landing](https://aclanthology.org/2024.findings-naacl.192/) | [OA PDF](https://aclanthology.org/2024.findings-naacl.192.pdf) (via acl)
- verified against: acl, bibcorpus:npnkhoi/memefal-paper
- score 0.4437 (cites 0.0, cocite 0.125, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "To evaluate LLMs’ capability of logical fallacy understanding (LFU), we propose five concrete tasks from three cognitive dimensions of WHAT, WHY, and HOW in this paper." "Towards these LFU tasks, we have successfully constructed a new dataset LFUD based on GPT-4 accompanied by a little human effort." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it types defective inference.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{li2024reasonfro,
  title = {Reason from Fallacy: Enhancing Large Language Models’ Logical Reasoning through Logical Fallacy Understanding},
  author = {Yanda Li and Dixuan Wang and Jiaqing Liang and Guochao Jiang and Qianyu He and Yanghua Xiao and Deqing Yang},
  year = {2024},
  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},
  doi = {10.18653/v1/2024.findings-naacl.192},
  url = {https://aclanthology.org/2024.findings-naacl.192/},
}
```

</details>

#### Amir Taubenfeld, Yaniv Dover, Roi Reichart and Ariel Goldstein (2024). *Systematic Biases in LLM Simulations of Debates*. Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2024.emnlp-main.16` | aliases: `acl:2024.emnlp-main.16`
- doc_type: `conference` | tier: T4 | tags: dialogue
- [landing](https://aclanthology.org/2024.emnlp-main.16/) | [OA PDF](https://aclanthology.org/2024.emnlp-main.16.pdf) (via acl)
- verified against: acl, bibcorpus:dimits-ts/synthetic_moderation_experiments | note: bibcorpus:dimits-ts/llm_moderation_research: venue mismatch ('Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing' vs 'ArXiv')
- score 0.6188 (cites 0.0, cocite 0.625, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The emergence of Large Language Models (LLMs), has opened exciting possibilities for constructing computational simulations designed to replicate human behavior accurately." "Current research suggests that LLM-based agents become increasingly human-like in their performance, sparking interest in using these AI agents as substitutes for human participants in behavioral studies." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{taubenfeld2024systematic,
  title = {Systematic Biases in LLM Simulations of Debates},
  author = {Amir Taubenfeld and Yaniv Dover and Roi Reichart and Ariel Goldstein},
  year = {2024},
  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/2024.emnlp-main.16},
  url = {https://aclanthology.org/2024.emnlp-main.16/},
}
```

</details>

#### Ayushi Nirmal, Amrita Bhattacharjee, Paras Sheth and Huan Liu (2024). *Towards Interpretable Hate Speech Detection using Large Language Model-extracted Rationales*. Proceedings of the 8th Workshop on Online Abuse and Harms (WOAH 2024).

- `doi:10.18653/v1/2024.woah-1.17` | aliases: `acl:2024.woah-1.17`
- doc_type: `workshop` | tier: T4 | tags: extraction
- [landing](https://aclanthology.org/2024.woah-1.17/) | [OA PDF](https://aclanthology.org/2024.woah-1.17.pdf) (via acl)
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments | note: acl: venue mismatch ('ArXiv' vs 'Proceedings of the 8th Workshop on Online Abuse and Harms (WOAH 2024)')
- score 0.5437 (cites 0.0, cocite 0.625, keyword 1.0, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "To address the lack of interpretability, in this paper, we propose to use state-of-the-art Large Language Models (LLMs) to extract features in the form of rationales from the input text, to train a base hate speech classifier, thereby enabling faithful interpretability by design." "Our framework effectively combines the textual understanding capabilities of LLMs and the discriminative power of state-of-the-art hate speech classifiers to make these classifiers faithfully interpretable." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{nirmal2024towardsin,
  title = {Towards Interpretable Hate Speech Detection using Large Language Model-extracted Rationales},
  author = {Ayushi Nirmal and Amrita Bhattacharjee and Paras Sheth and Huan Liu},
  year = {2024},
  booktitle = {Proceedings of the 8th Workshop on Online Abuse and Harms (WOAH 2024)},
  doi = {10.18653/v1/2024.woah-1.17},
  url = {https://aclanthology.org/2024.woah-1.17/},
}
```

</details>

#### Sougata Saha and Rohini Srihari (2024). *Turiya at DialAM-2024: Inference Anchoring Theory Based LLM Parsers*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.13` | aliases: `acl:2024.argmining-1.13`
- doc_type: `workshop` | tier: T4 | tags: dialogue, extraction, formal | also in: dialogue, formal
- [landing](https://aclanthology.org/2024.argmining-1.13/) | [OA PDF](https://aclanthology.org/2024.argmining-1.13.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.5224 (cites 0.0, cocite 0.4688, keyword 0.8333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Although computational frameworks for constructing graphs from monologues exist, there is a lack of frameworks for parsing dialogue." "Here, we introduce computational models for implementing the IAT framework for parsing dialogues." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it supplies the formal semantics for deciding what stands once arguments and attacks are stored.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{saha2024turiyaat,
  title = {Turiya at DialAM-2024: Inference Anchoring Theory Based LLM Parsers},
  author = {Sougata Saha and Rohini Srihari},
  year = {2024},
  booktitle = {Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024)},
  doi = {10.18653/v1/2024.argmining-1.13},
  url = {https://aclanthology.org/2024.argmining-1.13/},
}
```

</details>

#### Zhun Yang, Adam Ishay and Joohyung Lee (2023). *Coupling Large Language Models with Logic Programming for Robust and General Reasoning from Text*. Findings of the Association for Computational Linguistics: ACL 2023.

- `doi:10.18653/v1/2023.findings-acl.321` | aliases: `acl:2023.findings-acl.321`, `arxiv:2307.07696`
- doc_type: `conference` | tier: T4 | tags: extraction
- [landing](https://aclanthology.org/2023.findings-acl.321/) | [OA PDF](https://arxiv.org/pdf/2307.07696) (via arxiv)
- verified against: acl, bibcorpus:danny-v-nguyen/thesis | note: venue not corroborated by both sources
- score 0.4437 (cites 0.0, cocite 0.125, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "While large language models (LLMs), such as GPT-3, appear to be robust and general, their reasoning ability is not at a level to compete with the best models trained for specific natural language reasoning problems." "We demonstrate that this method achieves state-of-the-art performance on several NLP benchmarks, including bAbI, StepGame, CLUTRR, and gSCAN." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{yang2023couplingl,
  title = {Coupling Large Language Models with Logic Programming for Robust and General Reasoning from Text},
  author = {Zhun Yang and Adam Ishay and Joohyung Lee},
  year = {2023},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
  doi = {10.18653/v1/2023.findings-acl.321},
  url = {https://aclanthology.org/2023.findings-acl.321/},
}
```

</details>

#### Maria Valentini et al. (2023). *On the Automatic Generation and Simplification of Children’s Stories*. Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2023.emnlp-main.218` | aliases: `acl:2023.emnlp-main.218`
- doc_type: `conference` | tier: T4 | tags: extraction
- [landing](https://aclanthology.org/2023.emnlp-main.218/) | [OA PDF](https://aclanthology.org/2023.emnlp-main.218.pdf) (via acl)
- verified against: acl, bibcorpus:xinyannnnnnn/fact-driven-storytelling-with-llms
- score 0.425 (cites 0.0, cocite 0.25, keyword 0.75, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "With recent advances in large language models (LLMs), the concept of automatically generating children’s educational materials has become increasingly realistic." "In order to test these models, we develop a dataset of child-directed lexical simplification instances, with examples taken from the LLM-generated stories in our first experiment." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{valentini2023ontheaut,
  title = {On the Automatic Generation and Simplification of Children’s Stories},
  author = {Maria Valentini and Jennifer Weber and Jesus Salcido and Téa Wright and Eliana Colunga and Katharina von der Wense},
  year = {2023},
  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/2023.emnlp-main.218},
  url = {https://aclanthology.org/2023.emnlp-main.218/},
}
```

</details>

#### Cheng Jiayang et al. (2023). *StoryAnalogy: Deriving Story-level Analogies from Large Language Models to Unlock Analogical Understanding*. Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2023.emnlp-main.706` | aliases: `acl:2023.emnlp-main.706`
- doc_type: `conference` | tier: T4 | tags: extraction
- [landing](https://aclanthology.org/2023.emnlp-main.706/) | [OA PDF](https://aclanthology.org/2023.emnlp-main.706.pdf) (via acl)
- verified against: acl, bibcorpus:xinyannnnnnn/fact-driven-storytelling-with-llms
- score 0.4875 (cites 0.0, cocite 0.25, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Analogy-making between narratives is crucial for human reasoning." "In this paper, we evaluate the ability to identify and generate analogies by constructing a first-of-its-kind large-scale story-level analogy corpus, StoryAnalogy, which contains 24K story pairs from diverse domains with human annotations on two similarities from the extended Structure-Mapping Theory." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{jiayang2023storyanalo,
  title = {StoryAnalogy: Deriving Story-level Analogies from Large Language Models to Unlock Analogical Understanding},
  author = {Cheng Jiayang and Lin Qiu and Tsz Chan and Tianqing Fang and Weiqi Wang and Chunkit Chan and Dongyu Ru and Qipeng Guo and Hongming Zhang and Yangqiu Song and Yue Zhang and Zheng Zhang},
  year = {2023},
  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/2023.emnlp-main.706},
  url = {https://aclanthology.org/2023.emnlp-main.706/},
}
```

</details>

## 6.6 Datasets, tools, annotation guidelines (27 entries, quota 30)

### T1 - Foundational / survey. Read in full: theory anchors, major surveys, canonical papers.

#### Dimitrios Tsirmpas, Ioannis Gkionis, Georgios Th. Papadopoulos and Ioannis Mademlis (2024). *Neural natural language processing for long texts: A survey on classification and summarization*. Engineering Applications of Artificial Intelligence.

- `doi:10.1016/j.engappai.2024.108231`
- doc_type: `journal` | tier: T1 | tags: dataset
- [landing](https://www.sciencedirect.com/science/article/pii/S0952197624003890)
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments
- score 0.4521 (cites 0.0, cocite 0.625, keyword 0.3333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The adoption of Deep Neural Networks (DNNs) has greatly benefited Natural Language Processing (NLP) during the past decade." "Finally, it offers a concise definition of “long text/document”, presents an original overarching taxonomy of common deep neural methods for long document analysis and lists publicly available annotated datasets that can facilitate further research in this area." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@article{tsirmpas2024neuralnat,
  title = {Neural natural language processing for long texts: A survey on classification and summarization},
  author = {Dimitrios Tsirmpas and Ioannis Gkionis and Georgios Th. Papadopoulos and Ioannis Mademlis},
  year = {2024},
  journal = {Engineering Applications of Artificial Intelligence},
  doi = {10.1016/j.engappai.2024.108231},
  url = {https://www.sciencedirect.com/science/article/pii/S0952197624003890},
}
```

</details>

### T3 - Dataset / tool / annotation guideline, including the guideline documents themselves.

#### Alan Ramponi, Agnese Daffara and Sara Tonelli (2025). *Fine-grained Fallacy Detection with Human Label Variation*. Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers).

- `doi:10.18653/v1/2025.naacl-long.34` | aliases: `acl:2025.naacl-long.34`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction, fallacy, quality | also in: quality
- [landing](https://aclanthology.org/2025.naacl-long.34/) | [OA PDF](https://aclanthology.org/2025.naacl-long.34.pdf) (via acl)
- verified against: acl, bibcorpus:npnkhoi/memefal-paper
- score 0.4229 (cites 0.0, cocite 0.125, keyword 0.9167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We introduce FAINA, the first dataset for fallacy detection that embraces multiple plausible answers and natural disagreement." "We release our data, code, and annotation guidelines to foster research on fallacy detection and human label variation more broadly." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it types defective inference.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{ramponi2025finegrain,
  title = {Fine-grained Fallacy Detection with Human Label Variation},
  author = {Alan Ramponi and Agnese Daffara and Sara Tonelli},
  year = {2025},
  booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
  doi = {10.18653/v1/2025.naacl-long.34},
  url = {https://aclanthology.org/2025.naacl-long.34/},
}
```

</details>

#### Chadi Helwe et al. (2024). *MAFALDA: A Benchmark and Comprehensive Study of Fallacy Detection and Classification*. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers).

- `doi:10.18653/v1/2024.naacl-long.270` | aliases: `acl:2024.naacl-long.270`, `arxiv:2311.09761`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction, fallacy, quality | also in: quality, llm
- [landing](https://aclanthology.org/2024.naacl-long.270/) | [OA PDF](https://arxiv.org/pdf/2311.09761) (via arxiv)
- verified against: acl, bibcorpus:npnkhoi/memefal-paper | note: bibcorpus:lefteriskat/Logical-Fallacy-Detection-Using-LLMs: venue mismatch ('Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human L…
- score 0.4021 (cites 0.0, cocite 0.125, keyword 0.8333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We introduce MAFALDA, a benchmark for fallacy classification that merges and unites previous fallacy datasets." "We propose a new annotation scheme tailored for subjective NLP tasks, and a new evaluation method designed to handle subjectivity." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it types defective inference.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{helwe2024mafaldaa,
  title = {MAFALDA: A Benchmark and Comprehensive Study of Fallacy Detection and Classification},
  author = {Chadi Helwe and Tom Calamai and Pierre-Henri Paris and Chloé Clavel and Fabian Suchanek},
  year = {2024},
  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
  doi = {10.18653/v1/2024.naacl-long.270},
  url = {https://aclanthology.org/2024.naacl-long.270/},
}
```

</details>

#### Ethan Perez et al. (2023). *Discovering Language Model Behaviors with Model-Written Evaluations*. Findings of the Association for Computational Linguistics: ACL 2023.

- `doi:10.18653/v1/2023.findings-acl.847` | aliases: `acl:2023.findings-acl.847`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/2023.findings-acl.847/) | [OA PDF](https://aclanthology.org/2023.findings-acl.847.pdf) (via acl)
- verified against: bibcorpus:BarryMafu/LitLens, bibcorpus:edgar-demeude/KEIGO-SYNC | note: acl: venue mismatch ('arXiv preprint arXiv:2212.09251' vs 'Findings of the Association for Computational Linguistics: ACL 2023')
- score 0.3854 (cites 0.0, cocite 0.375, keyword 0.4167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Crowdworkers rate the examples as highly relevant and agree with 90-100% of labels, sometimes more so than corresponding human-written datasets." "We generate 154 datasets and discover new cases of inverse scaling where LMs get worse with size." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{perez2023discoverin,
  title = {Discovering Language Model Behaviors with Model-Written Evaluations},
  author = {Ethan Perez and Sam Ringer and Kamile Lukosiute and Karina Nguyen and Edwin Chen and Scott Heiner and Craig Pettit and Catherine Olsson and Sandipan Kundu and Saurav Kadavath and Andy Jones and Anna Chen and Benjamin Mann and Brian Israel and Bryan Seethor and Cameron McKinnon and Christopher Olah and Da Yan and Daniela Amodei and Dario Amodei and Dawn Drain and Dustin Li and Eli Tran-Johnson and Guro Khundadze and Jackson Kernion and James Landis and Jamie Kerr and Jared Mueller and Jeeyoon Hyun and Joshua Landau and Kamal Ndousse and Landon Goldberg and Liane Lovitt and Martin Lucas and Michael Sellitto and Miranda Zhang and Neerav Kingsland and Nelson Elhage and Nicholas Joseph and Noemi Mercado and Nova DasSarma and Oliver Rausch and Robin Larson and Sam McCandlish and Scott Johnston and Shauna Kravec and Sheer El Showk and Tamera Lanham and Timothy Telleen-Lawton and Tom Brown and Tom Henighan and Tristan Hume and Yuntao Bai and Zac Hatfield-Dodds and Jack Clark and Samuel R. Bowman and Amanda Askell and Roger Grosse and Danny Hernandez and Deep Ganguli and Evan Hubinger and Nicholas Schiefer and Jared Kaplan},
  year = {2023},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
  doi = {10.18653/v1/2023.findings-acl.847},
  url = {https://aclanthology.org/2023.findings-acl.847/},
}
```

</details>

#### Sewon Min et al. (2023). *Nonparametric Masked Language Modeling*. Findings of the Association for Computational Linguistics: ACL 2023.

- `doi:10.18653/v1/2023.findings-acl.132` | aliases: `acl:2023.findings-acl.132`
- doc_type: `conference` | tier: T3 | tags: dataset | also in: llm
- [landing](https://aclanthology.org/2023.findings-acl.132/) | [OA PDF](https://aclanthology.org/2023.findings-acl.132.pdf) (via acl)
- verified against: acl, bibcorpus:BarryMafu/LitLens
- score 0.3417 (cites 0.0, cocite 0.25, keyword 0.4167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We introduce NPM, the first nonparametric masked language model that replaces this softmax with a nonparametric distribution over every phrase in a reference corpus." "We show that NPM can be efficiently trained with a contrastive objective and an in-batch approximation to full corpus retrieval." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{min2023nonparamet,
  title = {Nonparametric Masked Language Modeling},
  author = {Sewon Min and Weijia Shi and Mike Lewis and Xilun Chen and Wen-tau Yih and Hannaneh Hajishirzi and Luke Zettlemoyer},
  year = {2023},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
  doi = {10.18653/v1/2023.findings-acl.132},
  url = {https://aclanthology.org/2023.findings-acl.132/},
}
```

</details>

#### Shibani Santurkar et al. (2023). *Whose opinions do language models reflect?*. ICML.

- `title:872e5a0c162b4d6617c9678c9ff8c029356967a8` | aliases: `arxiv:2303.17548`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://arxiv.org/abs/2303.17548) | [OA PDF](https://arxiv.org/pdf/2303.17548) (via arxiv)
- verified against: bibcorpus:BarryMafu/LitLens, bibcorpus:CogSciPrag/project_ideas, bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments | note: venue not corroborated by both sources
- score 0.4875 (cites 0.0, cocite 1.0, keyword 0.25, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We put forth a quantitative framework to investigate the opinions reflected by LMs – by leveraging high-quality public opinion polls." "Using this framework, we create OpinionQA, a dataset for evaluating the alignment of LM opinions with those of 60 US demographic groups over topics ranging from abortion to automation." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{santurkar2023whoseopin,
  title = {Whose opinions do language models reflect?},
  author = {Shibani Santurkar and Esin Durmus and Faisal Ladhak and Cinoo Lee and Percy Liang and Tatsunori Hashimoto},
  year = {2023},
  booktitle = {ICML},
  url = {https://arxiv.org/abs/2303.17548},
}
```

</details>

#### Abelardo Carlos Martínez Lorenzo, Marco Maru and Roberto Navigli (2022). *Fully-Semantic Parsing and Generation: the BabelNet Meaning Representation*. Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/2022.acl-long.121` | aliases: `acl:2022.acl-long.121`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction
- [landing](https://aclanthology.org/2022.acl-long.121/) | [OA PDF](https://aclanthology.org/2022.acl-long.121.pdf) (via acl)
- verified against: acl, bibcorpus:Danysan1/ai-unibo-nlp-project
- score 0.3396 (cites 0.0, cocite 0.125, keyword 0.5833, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we present the BabelNet Meaning Representation (BMR), an interlingual formalism that abstracts away from language-specific constraints by taking advantage of the multilingual semantic resources of BabelNet and VerbAtlas." "We describe the rationale behind the creation of BMR and put forward BMR 1.0, a dataset labeled entirely according to the new formalism." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{lorenzo2022fullysema,
  title = {Fully-Semantic Parsing and Generation: the BabelNet Meaning Representation},
  author = {Abelardo Carlos Martínez Lorenzo and Marco Maru and Roberto Navigli},
  year = {2022},
  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/2022.acl-long.121},
  url = {https://aclanthology.org/2022.acl-long.121/},
}
```

</details>

#### Paul Röttger, Bertie Vidgen, Dirk Hovy and Janet Pierrehumbert (2022). *Two Contrasting Data Annotation Paradigms for Subjective NLP Tasks*. Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.

- `doi:10.18653/v1/2022.naacl-main.13` | aliases: `acl:2022.naacl-main.13`, `arxiv:2112.07475`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/2022.naacl-main.13/) | [OA PDF](https://arxiv.org/pdf/2112.07475) (via arxiv)
- verified against: acl, bibcorpus:Danysan1/ai-unibo-nlp-project, bibcorpus:ljvmiranda921/ljvmiranda921.github.io | note: venue not corroborated by both sources
- score 0.2562 (cites 0.0, cocite 0.125, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "So far, dataset creators have acknowledged annotator subjectivity, but rarely actively managed it in the annotation process." "To address this issue, we propose two contrasting paradigms for data annotation." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{rttger2022twocontra,
  title = {Two Contrasting Data Annotation Paradigms for Subjective NLP Tasks},
  author = {Paul Röttger and Bertie Vidgen and Dirk Hovy and Janet Pierrehumbert},
  year = {2022},
  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  doi = {10.18653/v1/2022.naacl-main.13},
  url = {https://aclanthology.org/2022.naacl-main.13/},
}
```

</details>

#### Georgi Karadzhov, Tom Stafford and Andreas Vlachos (2021). *DeliData: A Dataset for Deliberation in Multi-party Problem Solving*. Proceedings of the ACM on Human-Computer Interaction.

- `title:a53d191087c04c6d49d9d46488abffa0090e89de`
- doc_type: `journal` | tier: T3 | tags: dataset, dialogue | also in: dialogue
- [landing](https://api.semanticscholar.org/CorpusID:236975941)
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments
- score 0.4734 (cites 0.0, cocite 0.7812, keyword 0.5, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Proceedings of the ACM on Human-Computer Interaction, 2021), verified against 2 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@article{karadzhov2021delidata,
  title = {DeliData: A Dataset for Deliberation in Multi-party Problem Solving},
  author = {Georgi Karadzhov and Tom Stafford and Andreas Vlachos},
  year = {2021},
  journal = {Proceedings of the ACM on Human-Computer Interaction},
  url = {https://api.semanticscholar.org/CorpusID:236975941},
}
```

</details>

#### Dimitar Dimitrov et al. (2021). *SemEval-2021 Task 6: Detection of Persuasion Techniques in Texts and Images*. Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021).

- `doi:10.18653/v1/2021.semeval-1.7` | aliases: `acl:2021.semeval-1.7`
- doc_type: `workshop` | tier: T3 | tags: dataset, dialogue, extraction
- [landing](https://aclanthology.org/2021.semeval-1.7/) | [OA PDF](https://aclanthology.org/2021.semeval-1.7.pdf) (via acl)
- verified against: acl, bibcorpus:allenai/ir_datasets, bibcorpus:npnkhoi/memefal-paper
- score 0.225 (cites 0.0, cocite 0.25, keyword 0.25, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We describe SemEval-2021 task 6 on Detection of Persuasion Techniques in Texts and Images: the data, the annotation guidelines, the evaluation setup, the results, and the participating systems." "The task focused on memes and had three subtasks: (i) detecting the techniques in the text, (ii) detecting the text spans where the techniques are used, and (iii) detecting techniques in the entire meme, i.e., both in the text and in the image." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{dimitrov2021semeval,
  title = {SemEval-2021 Task 6: Detection of Persuasion Techniques in Texts and Images},
  author = {Dimitar Dimitrov and Bishr Bin Ali and Shaden Shaar and Firoj Alam and Fabrizio Silvestri and Hamed Firooz and Preslav Nakov and Giovanni Da San Martino},
  year = {2021},
  booktitle = {Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021)},
  doi = {10.18653/v1/2021.semeval-1.7},
  url = {https://aclanthology.org/2021.semeval-1.7/},
}
```

</details>

#### Francesco Antici et al. (2021). *SubjectivITA: An Italian Corpus for Subjectivity Detection in Newspapers*. Experimental IR Meets Multilinguality, Multimodality, and Interaction - 12th International Conference of the CLEF Association, CLEF 2021, Virtual Event, September 21-24, 2021, Proceedings.

- `doi:10.1007/978-3-030-85251-1_4`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue, extraction
- [landing](https://doi.org/10.1007/978-3-030-85251-1_4)
- verified against: bibcorpus:Danysan1/ai-unibo-nlp-project, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.2438 (cites 0.0, cocite 0.125, keyword 0.5, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Experimental IR Meets Multilinguality, Multimodality, and Interaction - 12th International Conference of the CLEF Association, CLEF 2021, Virtual Event, September 21-24, 2021, Proceedings, 2021), verified against 2 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{antici2021subjectivi,
  title = {SubjectivITA: An Italian Corpus for Subjectivity Detection in Newspapers},
  author = {Francesco Antici and Luca Bolognini and Matteo Antonio Inajetovic and Bogdan Ivasiuk and Andrea Galassi and Federico Ruggeri},
  year = {2021},
  booktitle = {Experimental IR Meets Multilinguality, Multimodality, and Interaction - 12th International Conference of the CLEF Association, CLEF 2021, Virtual Event, September 21-24, 2021, Proceedings},
  doi = {10.1007/978-3-030-85251-1_4},
  url = {https://doi.org/10.1007/978-3-030-85251-1_4},
}
```

</details>

#### Liat Ein-Dor et al. (2020). *Corpus Wide Argument Mining - A Working Solution*. The Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, The Thirty-Second Innovative Applications of Artificial Intelligence Conference, IAAI 2020, The Tenth AAAI Symposium on Educational Advances in Artificial Intelligence, EAAI 2020, New York, NY, USA, February 7-12, 2020.

- `doi:10.1609/aaai.v34i05.6270`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction | also in: mining
- [landing](https://doi.org/10.1609/aaai.v34i05.6270)
- verified against: bibcorpus:borgr/publications, bibcorpus:m0re4u/paper-database | note: bibcorpus:lihebi/biber-dist: venue mismatch ('The Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, The Thirty-Second Innovative Applications of Artificial Intelligence Conference,…
- score 0.3396 (cites 0.0, cocite 0.125, keyword 0.5833, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, The Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, The Thirty-Second Innovative Applications of Artificial Intelligence Conference, IAAI 2020, The Tenth AAAI Symposium on Educational Advances in Artificial Intelligence, EAAI 2020, New York, NY, USA, February 7-12, 2020, 2020), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{eindor2020corpuswid,
  title = {Corpus Wide Argument Mining - A Working Solution},
  author = {Liat Ein-Dor and Eyal Shnarch and Lena Dankin and Alon Halfon and Benjamin Sznajder and Ariel Gera and Carlos Alzate and Martin Gleize and Leshem Choshen and Yufang Hou and Yonatan Bilu and Ranit Aharonov and Noam Slonim},
  year = {2020},
  booktitle = {The Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, The Thirty-Second Innovative Applications of Artificial Intelligence Conference, IAAI 2020, The Tenth AAAI Symposium on Educational Advances in Artificial Intelligence, EAAI 2020, New York, NY, USA, February 7-12, 2020},
  doi = {10.1609/aaai.v34i05.6270},
  url = {https://doi.org/10.1609/aaai.v34i05.6270},
}
```

</details>

#### Nils Reimers et al. (2019). *Classification and Clustering of Arguments with Contextualized Word Embeddings*. Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics.

- `doi:10.18653/v1/p19-1054` | aliases: `acl:P19-1054`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue, extraction
- [landing](https://aclanthology.org/P19-1054/) | [OA PDF](https://aclanthology.org/P19-1054.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.3792 (cites 0.0, cocite 0.0, keyword 0.9167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "For the first time, we show how to leverage the power of contextualized word embeddings to classify and cluster topic-dependent arguments, achieving impressive results on both tasks and across multiple datasets." "For the understudied task of argument clustering, we propose a pre-training step which improves by 7.8 percentage points over strong baselines on a novel dataset, and by 12.3 percentage points for the Argument Facet Similarity (AFS) Corpus." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{reimers2019classifica,
  title = {Classification and Clustering of Arguments with Contextualized Word Embeddings},
  author = {Nils Reimers and Benjamin Schiller and Tilman Beck and Johannes Daxenberger and Christian Stab and Iryna Gurevych},
  year = {2019},
  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  doi = {10.18653/v1/p19-1054},
  url = {https://aclanthology.org/P19-1054/},
}
```

</details>

#### Yamen Ajjour et al. (2019). *Data Acquisition for Argument Search: The args.me corpus*. 42nd German Conference on Artificial Intelligence (KI 2019).

- `doi:10.1007/978-3-030-30179-8_4`
- doc_type: `conference` | tier: T3 | tags: dataset
- no URL recorded
- verified against: bibcorpus:CogSciPrag/project_ideas, bibcorpus:allenai/ir_datasets
- score 0.575 (cites 0.0, cocite 0.5, keyword 1.0, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, 42nd German Conference on Artificial Intelligence (KI 2019), 2019), verified against 2 sources. For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{ajjour2019dataacqui,
  title = {Data Acquisition for Argument Search: The args.me corpus},
  author = {Yamen Ajjour and Henning Wachsmuth and Johannes Kiesel and Martin Potthast and Matthias Hagen and Benno Stein},
  year = {2019},
  booktitle = {42nd German Conference on Artificial Intelligence (KI 2019)},
  doi = {10.1007/978-3-030-30179-8_4},
}
```

</details>

#### Eric Wallace et al. (2019). *Universal Adversarial Triggers for Attacking and Analyzing NLP*. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP).

- `doi:10.18653/v1/d19-1221` | aliases: `acl:D19-1221`
- doc_type: `conference` | tier: T3 | tags: dataset, quality | also in: quality
- [landing](https://aclanthology.org/D19-1221/) | [OA PDF](https://aclanthology.org/D19-1221.pdf) (via acl)
- verified against: acl, bibcorpus:BarryMafu/LitLens
- score 0.3 (cites 0.0, cocite 0.25, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We define universal adversarial triggers: input-agnostic sequences of tokens that trigger a model to produce a specific prediction when concatenated to any input from a dataset." "We propose a gradient-guided search over tokens which finds short trigger sequences (e.g., one word for classification and four words for language modeling) that successfully trigger the target prediction." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{wallace2019universal,
  title = {Universal Adversarial Triggers for Attacking and Analyzing NLP},
  author = {Eric Wallace and Shi Feng and Nikhil Kandpal and Matt Gardner and Sameer Singh},
  year = {2019},
  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
  doi = {10.18653/v1/d19-1221},
  url = {https://aclanthology.org/D19-1221/},
}
```

</details>

#### Joonsuk Park and Claire Cardie (2018). *A Corpus of eRulemaking User Comments for Measuring Evaluability of Arguments*. Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018).

- `title:fb5f11e278c8bd8c14ae4a205093409670e5bba3` | aliases: `acl:L18-1257`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/L18-1257/) | [OA PDF](https://aclanthology.org/L18-1257.pdf) (via acl)
- verified against: acl, bibcorpus:harisont/biboba
- score 0.3396 (cites 0.0, cocite 0.125, keyword 0.5833, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018), 2018), verified against 2 sources. For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{park2018acorpuso,
  title = {A Corpus of eRulemaking User Comments for Measuring Evaluability of Arguments},
  author = {Joonsuk Park and Claire Cardie},
  year = {2018},
  booktitle = {Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
  url = {https://aclanthology.org/L18-1257/},
}
```

</details>

#### Ivan Sanchez, Jeff Mitchell and Sebastian Riedel (2018). *Behavior Analysis of NLI Models: Uncovering the Influence of Three Factors on Robustness*. Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers).

- `doi:10.18653/v1/n18-1179` | aliases: `acl:N18-1179`
- doc_type: `conference` | tier: T3 | tags: dataset, quality | also in: quality
- [landing](https://aclanthology.org/N18-1179/) | [OA PDF](https://aclanthology.org/N18-1179.pdf) (via acl)
- verified against: acl, bibcorpus:IKMLab/arct2
- score 0.3 (cites 0.0, cocite 0.25, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Our results demonstrate a number of strengths and weaknesses in the models’ ability to generalise to new in-domain instances." "Overall, we show that evaluations of NLI models can benefit from studying the influence of factors intrinsic to the models or found in the dataset used." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{sanchez2018behaviora,
  title = {Behavior Analysis of NLI Models: Uncovering the Influence of Three Factors on Robustness},
  author = {Ivan Sanchez and Jeff Mitchell and Sebastian Riedel},
  year = {2018},
  booktitle = {Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)},
  doi = {10.18653/v1/n18-1179},
  url = {https://aclanthology.org/N18-1179/},
}
```

</details>

#### HongSeok Choi and Hyunju Lee (2018). *GIST at SemEval-2018 Task 12: A network transferring inference knowledge to Argument Reasoning Comprehension task*. Proceedings of the 12th International Workshop on Semantic Evaluation.

- `doi:10.18653/v1/s18-1122` | aliases: `acl:S18-01122`
- doc_type: `workshop` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/S18-01122/) | [OA PDF](https://aclanthology.org/S18-01122.pdf) (via acl) | [repo](https://github.com/UKPLab/argument-reasoning-comprehension-task)
- verified against: acl, bibcorpus:IKMLab/arct2 | note: repo linked on token overlap: ['argument', 'comprehension', 'reasoning', 'task']
- score 0.225 (cites 0.0, cocite 0.25, keyword 0.25, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We describe how to use ESIM for transfer learning to choose correct warrant through a proposed system." "We show comparable results through ablation experiments." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{choi2018gistatse,
  title = {GIST at SemEval-2018 Task 12: A network transferring inference knowledge to Argument Reasoning Comprehension task},
  author = {HongSeok Choi and Hyunju Lee},
  year = {2018},
  booktitle = {Proceedings of the 12th International Workshop on Semantic Evaluation},
  doi = {10.18653/v1/s18-1122},
  url = {https://aclanthology.org/S18-01122/},
}
```

</details>

#### Timothy Niven and Hung-Yu Kao (2018). *NLITrans at SemEval-2018 Task 12: Transfer of Semantic Knowledge for Argument Comprehension*. Proceedings of the 12th International Workshop on Semantic Evaluation.

- `doi:10.18653/v1/s18-1185` | aliases: `acl:S18-01185`
- doc_type: `workshop` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/S18-01185/) | [OA PDF](https://aclanthology.org/S18-01185.pdf) (via acl) | [repo](https://github.com/UKPLab/argument-reasoning-comprehension-task)
- verified against: acl, bibcorpus:IKMLab/arct2 | note: repo linked on token overlap: ['argument', 'comprehension', 'task']
- score 0.225 (cites 0.0, cocite 0.25, keyword 0.25, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We focus on transfer of a sentence encoder to bootstrap more complicated architectures given the small size of the dataset." "Sharing parameters for independent warrant evaluation provides regularization and effectively doubles the size of the dataset." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{niven2018nlitransa,
  title = {NLITrans at SemEval-2018 Task 12: Transfer of Semantic Knowledge for Argument Comprehension},
  author = {Timothy Niven and Hung-Yu Kao},
  year = {2018},
  booktitle = {Proceedings of the 12th International Workshop on Semantic Evaluation},
  doi = {10.18653/v1/s18-1185},
  url = {https://aclanthology.org/S18-01185/},
}
```

</details>

#### Yiqing Hua et al. (2018). *WikiConv: A Corpus of the Complete Conversational History of a Large Online Collaborative Community*. Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/d18-1305` | aliases: `acl:D18-1305`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue
- [landing](https://aclanthology.org/D18-1305/) | [OA PDF](https://aclanthology.org/D18-1305.pdf) (via acl)
- verified against: acl, bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments
- score 0.4938 (cites 0.0, cocite 0.625, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We present a corpus that encompasses the complete history of conversations between contributors to Wikipedia, one of the largest online collaborative communities." "Our framework is designed to be language agnostic, and we show that it extracts high quality data in both Chinese and English." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{hua2018wikiconv,
  title = {WikiConv: A Corpus of the Complete Conversational History of a Large Online Collaborative Community},
  author = {Yiqing Hua and Cristian Danescu-Niculescu-Mizil and Dario Taraborelli and Nithum Thain and Jeffery Sorensen and Lucas Dixon},
  year = {2018},
  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/d18-1305},
  url = {https://aclanthology.org/D18-1305/},
}
```

</details>

#### Robin Jia and Percy Liang (2017). *Adversarial Examples for Evaluating Reading Comprehension Systems*. Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/d17-1215` | aliases: `acl:D17-1215`, `arxiv:1707.07328`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/D17-1215/) | [OA PDF](https://arxiv.org/pdf/1707.07328) (via arxiv)
- verified against: acl, bibcorpus:BarryMafu/LitLens | note: bibcorpus:IKMLab/arct2: venue mismatch ('Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing' vs 'CoRR'); bibcorpus:jbingel/emnlp2017-handbook: venue mismatch ('Pro…
- score 0.3875 (cites 0.0, cocite 0.5, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Standard accuracy metrics indicate that reading comprehension systems are making rapid progress, but the extent to which these systems truly understand language remains unclear." "To reward systems with real language understanding abilities, we propose an adversarial evaluation scheme for the Stanford Question Answering Dataset (SQuAD)." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{jia2017adversaria,
  title = {Adversarial Examples for Evaluating Reading Comprehension Systems},
  author = {Robin Jia and Percy Liang},
  year = {2017},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/d17-1215},
  url = {https://aclanthology.org/D17-1215/},
}
```

</details>

#### Henning Wachsmuth et al. (2017). *Building an Argument Search Engine for the Web*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5106` | aliases: `acl:W17-5106`
- doc_type: `workshop` | tier: T3 | tags: dataset, extraction | also in: mining
- [landing](https://aclanthology.org/W17-5106/) | [OA PDF](https://aclanthology.org/W17-5106.pdf) (via acl)
- verified against: acl, bibcorpus:allenai/ir_datasets, bibcorpus:jbingel/emnlp2017-handbook, bibcorpus:m0re4u/paper-database | note: venue not corroborated by both sources
- score 0.2354 (cites 0.0, cocite 0.125, keyword 0.1667, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we develop an argument search framework for studying these and further questions." "Based on the framework, we build a prototype search engine, called args, that relies on an initial, freely accessible index of nearly 300k arguments crawled from reliable web resources." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{wachsmuth2017buildinga,
  title = {Building an Argument Search Engine for the Web},
  author = {Henning Wachsmuth and Martin Potthast and Khalid Al-Khatib and Yamen Ajjour and Jana Puschmann and Jiani Qu and Jonas Dorsch and Viorel Morari and Janek Bevendorff and Benno Stein},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5106},
  url = {https://aclanthology.org/W17-5106/},
}
```

</details>

#### Yeye He, Kaushik Chakrabarti, Tao Cheng and Tomasz Tylenda (2016). *Automatic Discovery of Attribute Synonyms Using Query Logs and Table Corpora*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2874816`
- doc_type: `conference` | tier: T3 | tags: dataset, quality | also in: quality
- [landing](https://doi.org/10.1145/2872427.2874816)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.1812 (cites 0.0, cocite 0.125, keyword 0.25, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "To address that problem, we propose to automatically discover all the alternate ways of referring to the attributes of a given class of entities (referred to as attribute synonyms) in order to improve search quality." "We develop a linear programming based algorithm to solve the problem that has bi-criteria approximation guarantees." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{he2016automatic,
  title = {Automatic Discovery of Attribute Synonyms Using Query Logs and Table Corpora},
  author = {Yeye He and Kaushik Chakrabarti and Tao Cheng and Tomasz Tylenda},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2874816},
  url = {https://doi.org/10.1145/2872427.2874816},
}
```

</details>

#### Rob Abbott, Brian Ecker, Pranav Anand and Marilyn Walker (2016). *Internet Argument Corpus 2.0: An SQL schema for Dialogic Social Media and the Corpora to go with it*. Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC'16).

- `title:5fdf28d47fecc818952baba478a8bd9d1b71a516` | aliases: `acl:L16-1704`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue | also in: dialogue
- [landing](https://aclanthology.org/L16-1704/) | [OA PDF](https://aclanthology.org/L16-1704.pdf) (via acl)
- verified against: acl, bibcorpus:IKMLab/argalign1, bibcorpus:m0re4u/paper-database
- score 0.3583 (cites 0.0, cocite 0.0, keyword 0.8333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Now, with the emergence of large scale social media websites incorporating a threaded dialogue structure, content feedback, and self-annotation (such as stance labeling), there are valuable new corpora available to researchers." "In previous work, we released the INTERNET ARGUMENT CORPUS, one of the first larger scale resources available for opinion sharing dialogue." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{abbott2016interneta,
  title = {Internet Argument Corpus 2.0: An SQL schema for Dialogic Social Media and the Corpora to go with it},
  author = {Rob Abbott and Brian Ecker and Pranav Anand and Marilyn Walker},
  year = {2016},
  booktitle = {Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC'16)},
  url = {https://aclanthology.org/L16-1704/},
}
```

</details>

#### Ruining He and Julian McAuley (2016). *Ups and Downs: Modeling the Visual Evolution of Fashion Trends with One-Class Collaborative Filtering*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2883037`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://doi.org/10.1145/2872427.2883037)
- verified against: bibcorpus:BarryMafu/LitLens, bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.2687 (cites 0.0, cocite 0.375, keyword 0.25, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper we build novel models for the One-Class Collaborative Filtering setting, where our goal is to estimate users' fashion-aware personalized ranking functions based on their past feedback." "Experimentally we evaluate our method on two large real-world datasets from Amazon.com, where we show it to outperform state-of-the-art personalized ranking measures, and also use it to visualize the high-level fashion trends across the 11-year span of our dataset." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{he2016upsanddo,
  title = {Ups and Downs: Modeling the Visual Evolution of Fashion Trends with One-Class Collaborative Filtering},
  author = {Ruining He and Julian McAuley},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2883037},
  url = {https://doi.org/10.1145/2872427.2883037},
}
```

</details>

#### Samuel R. Bowman, Gabor Angeli, Christopher Potts and Christopher D. Manning (2015). *A large annotated corpus for learning natural language inference*. Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/d15-1075` | aliases: `acl:D15-1075`, `arxiv:1508.05326`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/D15-1075/) | [OA PDF](https://arxiv.org/pdf/1508.05326) (via arxiv)
- verified against: acl, bibcorpus:danny-v-nguyen/thesis | note: bibcorpus:IKMLab/arct2: venue mismatch ('Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing' vs 'CoRR')
- score 0.5312 (cites 0.0, cocite 0.375, keyword 1.0, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, 2015), verified against 2 sources. For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{bowman2015alargean,
  title = {A large annotated corpus for learning natural language inference},
  author = {Samuel R. Bowman and Gabor Angeli and Christopher Potts and Christopher D. Manning},
  year = {2015},
  booktitle = {Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/d15-1075},
  url = {https://aclanthology.org/D15-1075/},
}
```

</details>

#### Lynn Carlson, Daniel Marcu and Mary Ellen Okurovsky (2001). *Building a Discourse-Tagged Corpus in the Framework of Rhetorical Structure Theory*. Proceedings of the Second SIGdial Workshop on Discourse and Dialogue.

- `title:c0c1c1a16c75ec3d49c0545c7c923b0a6e8af900` | aliases: `acl:W01-1605`
- doc_type: `workshop` | tier: T3 | tags: dataset, dialogue
- [landing](https://aclanthology.org/W01-1605/) | [OA PDF](https://aclanthology.org/W01-1605.pdf) (via acl)
- verified against: acl, bibcorpus:CogSciPrag/project_ideas
- score 0.3312 (cites 0.0, cocite 0.375, keyword 0.5, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (workshop, Proceedings of the Second SIGdial Workshop on Discourse and Dialogue, 2001), verified against 2 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{carlson2001buildinga,
  title = {Building a Discourse-Tagged Corpus in the Framework of Rhetorical Structure Theory},
  author = {Lynn Carlson and Daniel Marcu and Mary Ellen Okurovsky},
  year = {2001},
  booktitle = {Proceedings of the Second SIGdial Workshop on Discourse and Dialogue},
  url = {https://aclanthology.org/W01-1605/},
}
```

</details>
