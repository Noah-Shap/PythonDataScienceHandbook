# 01 - Annotated bibliography

137 verified entries, grouped by area and then by tier. Every entry here agreed across at least two independent metadata sources; anything that did not is in `99-unverified-and-rejected.md`. Each annotation says which retrieved text it was written from (`grounded_on`), and quotes that text rather than paraphrasing it from outside knowledge.

Generated 2026-09-16T01:33:48+00:00 | criteria_version 1 | cap 250

**Added in the latest run (250):** `doi:10.1007/978-0-387-98197-0_19`, `doi:10.1007/978-3-030-30179-8_4`, `doi:10.1007/978-3-030-85251-1_4`, `doi:10.1007/978-3-642-23963-2_10`, `doi:10.1007/s10458-009-9116-7`, `doi:10.1007/s10506-010-9104-x`, `doi:10.1016/0004-3702(94)00041-x`, `doi:10.1016/j.artint.2007.04.009`, `doi:10.1016/j.ipm.2019.102055`, `doi:10.1017/cbo9780511802034`, `doi:10.1017/s0269888906001044`, `doi:10.1017/s0269888911000166`, `doi:10.1038/s41586-021-03215-w`, `doi:10.1080/19462166.2010.485698`, `doi:10.1080/19462166.2010.486479`, `doi:10.1080/19462166.2012.661766`, `doi:10.1080/19462166.2012.708670`, `doi:10.1080/19462166.2012.729861`, `doi:10.1080/19462166.2013.862303`, `doi:10.1080/19462166.2013.869764`, `doi:10.1080/19462166.2013.869766`, `doi:10.1080/19462166.2013.869767`, `doi:10.1080/19462166.2013.869878`, `doi:10.1080/19462166.2014.1001790`, `doi:10.1080/19462166.2014.1002535`, `doi:10.1080/19462166.2015.1107134`, `doi:10.1093/logcom/14.5.675`, `doi:10.1093/logcom/exp064`, `doi:10.1093/oso/9780198862536.003.0005`, `doi:10.1145/2701336.2701635`, `doi:10.1145/2850417`, `doi:10.1145/2872427.2883039`, `doi:10.1145/2872427.2883081`, `doi:10.1145/2872427.2883091`, `doi:10.1145/3308558.3314127`, `doi:10.1145/3350546.3352506`, `doi:10.1162/coli_a_00295`, `doi:10.1162/coli_a_00364`, `doi:10.1162/coli_a_00502`, `doi:10.1162/tacl.a.38` ...

## 6.1 Formal foundations (16 entries, quota 30)

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
- score 0.34 (cites 0.0, cocite 0.4, keyword 0.5, venue 0.5)
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
- score 0.485 (cites 0.0, cocite 0.6, keyword 0.5, venue 1.0)
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
- score 0.345 (cites 0.0, cocite 0.2, keyword 0.5, venue 1.0)
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
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Argument & Computation, 2014), verified against 4 sources. For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

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
- doc_type: `journal` | tier: T1 | tags: formal
- no URL recorded
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:p4s3r0/argumentation-framework-clustering, bibcorpus:ttmassa/ter
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Knowledge Eng. Review, 2011), verified against 3 sources. For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

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
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Artificial Intelligence, 1995), verified against 8 sources. For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

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
- score 0.2358 (cites 0.0, cocite 0.4, keyword 0.0833, venue 0.5)
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

#### Alejandro J. García and Guillermo R. Simari (2014). *Defeasible logic programming: DeLP-servers, contextual queries, and explanations for answers*. Argument & Computation.

- `doi:10.1080/19462166.2013.869767`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:KWARC/bibs, bibcorpus:davidar/dblp.yaml, bibcorpus:slatex/sTeX
- score 0.4283 (cites 0.0, cocite 0.2, keyword 0.8333, venue 1.0)
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
- score 0.2983 (cites 0.0, cocite 0.4, keyword 0.3333, venue 0.5)
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
- score 0.34 (cites 0.0, cocite 0.4, keyword 0.5, venue 0.5)
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
- score 0.415 (cites 0.0, cocite 0.4, keyword 0.5, venue 1.0)
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

#### Uwe Egly, Sarah Alice Gaggl and Stefan Woltran (2010). *Answer-set programming encodings for argumentation frameworks*. Argument & Computation.

- `doi:10.1080/19462166.2010.486479`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:p4s3r0/argumentation-framework-clustering
- score 0.485 (cites 0.0, cocite 0.6, keyword 0.5, venue 1.0)
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

## 6.2 Argument mining (NLP) (45 entries, quota 60)

### T1 - Foundational / survey. Read in full: theory anchors, major surveys, canonical papers.

#### Eva Maria Vecchi, Neele Falk, Iman Jundi and Gabriella Lapesa (2021). *Towards Argument Mining for Social Good: A Survey*. Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers).

- `doi:10.18653/v1/2021.acl-long.107` | aliases: `acl:2021.acl-long.107`
- doc_type: `conference` | tier: T1 | tags: dialogue, extraction
- [landing](https://aclanthology.org/2021.acl-long.107/) | [OA PDF](https://aclanthology.org/2021.acl-long.107.pdf) (via acl)
- verified against: acl, bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments, bibcorpus:m0re4u/paper-database
- score 0.6458 (cites 0.0, cocite 1.0, keyword 0.5833, venue 1.0)
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
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, ACM Trans. Internet Technol., 2016), verified against 3 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

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
- score 0.41 (cites 0.0, cocite 0.6, keyword 0.5, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Int. J. Cogn. Informatics Nat. Intell., 2013), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

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

### T2 - Core method. Defines a task formulation, model, or evaluation still in use.

#### Terne Sasha Thorn Jakobsen, Maria Barrett, Anders Sogaard and David Lassen (2022). *The Sensitivity of Annotator Bias to Task Definitions in Argument Mining*. Proceedings of the 16th Linguistic Annotation Workshop (LAW-XVI) within LREC2022.

- `title:61fadcac208eb3f58c0f9834cf909c5aaa5c7972` | aliases: `acl:2022.law-1.6`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/2022.law-1.6/) | [OA PDF](https://aclanthology.org/2022.law-1.6.pdf) (via acl)
- verified against: acl, bibcorpus:ljvmiranda921/ljvmiranda921.github.io
- score 0.345 (cites 0.0, cocite 0.2, keyword 0.5, venue 1.0)
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

#### Yuxiao Ye and Simone Teufel (2021). *End-to-End Argument Mining as Biaffine Dependency Parsing*. Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume.

- `doi:10.18653/v1/2021.eacl-main.55` | aliases: `acl:2021.eacl-main.55`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/2021.eacl-main.55/) | [OA PDF](https://aclanthology.org/2021.eacl-main.55.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.5683 (cites 0.0, cocite 0.6, keyword 0.8333, venue 1.0)
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

#### Tariq Alhindi, Smaranda Muresan and Daniel Preotiuc-Pietro (2020). *Fact vs. Opinion: the Role of Argumentation Features in News Classification*. Proceedings of the 28th International Conference on Computational Linguistics.

- `doi:10.18653/v1/2020.coling-main.540` | aliases: `acl:2020.coling-main.540`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/2020.coling-main.540/) | [OA PDF](https://aclanthology.org/2020.coling-main.540.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.2825 (cites 0.0, cocite 0.2, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We present an approach to classify news articles into newsstories (i.e., reporting of factual information) and opinion pieces using models that aim to sup-plement the article content representation with argumentation features." "We show that argumentation features outperform linguistic features used previ-ously and improve on fine-tuned transformer-based models when tested on data from publishersunseen in training." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{alhindi2020factvso,
  title = {Fact vs. Opinion: the Role of Argumentation Features in News Classification},
  author = {Tariq Alhindi and Smaranda Muresan and Daniel Preotiuc-Pietro},
  year = {2020},
  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics},
  doi = {10.18653/v1/2020.coling-main.540},
  url = {https://aclanthology.org/2020.coling-main.540/},
}
```

</details>

#### Tuhin Chakrabarty et al. (2019). *AMPERSAND: Argument Mining for PERSuAsive oNline Discussions*. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP).

- `doi:10.18653/v1/d19-1291` | aliases: `acl:D19-1291`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/D19-1291/) | [OA PDF](https://aclanthology.org/D19-1291.pdf) (via acl)
- verified against: bibcorpus:harisont/biboba, bibcorpus:m0re4u/paper-database | note: acl: venue mismatch ('arXiv preprint arXiv:2004.14677' vs 'Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural…
- score 0.3867 (cites 0.0, cocite 0.2, keyword 0.6667, venue 1.0)
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

#### Makiko Ida et al. (2019). *Can You Give Me a Reason?: Argument-Inducing Online Forum by Argument Mining*. The World Wide Web Conference.

- `doi:10.1145/3308558.3314127`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://doi.org/10.1145/3308558.3314127)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.2 (cites 0.0, cocite 0.0, keyword 0.5, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, The World Wide Web Conference, 2019), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

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

#### Daniel Hershcovich et al. (2019). *SemEval-2019 Task 1: Cross-lingual Semantic Parsing with UCCA*. Proceedings of the 13th International Workshop on Semantic Evaluation.

- `doi:10.18653/v1/s19-2001` | aliases: `acl:S19-0201`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/S19-0201/) | [OA PDF](https://aclanthology.org/S19-0201.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications | note: bibcorpus:danielhers/danielhers.github.io: venue mismatch ('Proceedings of the 13th International Workshop on Semantic Evaluation' vs 'Proc. of SemEval')
- score 0.1658 (cites 0.0, cocite 0.2, keyword 0.0833, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We present the SemEval 2019 shared task on Universal Conceptual Cognitive Annotation (UCCA) parsing in English, German and French, and discuss the participating systems and results." "UCCA is a cross-linguistically applicable framework for semantic representation, which builds on extensive typological work and supports rapid annotation." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{hershcovich2019semeval,
  title = {SemEval-2019 Task 1: Cross-lingual Semantic Parsing with UCCA},
  author = {Daniel Hershcovich and Zohar Aizenbud and Leshem Choshen and Elior Sulem and Ari Rappoport and Omri Abend},
  year = {2019},
  booktitle = {Proceedings of the 13th International Workshop on Semantic Evaluation},
  doi = {10.18653/v1/s19-2001},
  url = {https://aclanthology.org/S19-0201/},
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
- score 0.345 (cites 0.0, cocite 0.2, keyword 0.5, venue 1.0)
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
- score 0.4046 (cites 0.0, cocite 0.4, keyword 0.4583, venue 1.0)
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

#### Leshem Choshen and Omri Abend (2018). *Inherent Biases in Reference-based Evaluation for Grammatical Error Correction*. Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/p18-1059` | aliases: `acl:P18-1059`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/P18-1059/) | [OA PDF](https://aclanthology.org/P18-1059.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.2408 (cites 0.0, cocite 0.2, keyword 0.0833, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The prevalent use of too few references for evaluating text-to-text generation is known to bias estimates of their quality (henceforth, low coverage bias or LCB)." "Concretely, we show that LCB incentivizes GEC systems to avoid correcting even when they can generate a valid correction." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{choshen2018inherentb,
  title = {Inherent Biases in Reference-based Evaluation for Grammatical Error Correction},
  author = {Leshem Choshen and Omri Abend},
  year = {2018},
  booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/p18-1059},
  url = {https://aclanthology.org/P18-1059/},
}
```

</details>

#### Eyal Shnarch et al. (2018). *Will it Blend? Blending Weak and Strong Labeled Data in a Neural Network for Argumentation Mining*. Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics, ACL 2018, Melbourne, Australia, July 15-20, 2018, Volume 2: Short Papers.

- `doi:10.18653/v1/p18-2095` | aliases: `acl:P18-2095`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/P18-2095/) | [OA PDF](https://aclanthology.org/P18-2095.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications, bibcorpus:lihebi/biber-dist
- score 0.345 (cites 0.0, cocite 0.2, keyword 0.5, venue 1.0)
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

#### Mihai Dusmanu, Elena Cabrio and Serena Villata (2017). *Argument Mining on Twitter: Arguments, Facts and Sources*. EMNLP.

- `title:3b6e82826f260ecbbce1a01398ed3ab9749f3820` | aliases: `acl:D17-1245`, `doi:10.18653/v1/d17-1245`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/D17-1245/) | [OA PDF](https://aclanthology.org/D17-1245.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database | note: bibcorpus:jbingel/emnlp2017-handbook: venue mismatch ('Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing' vs 'TOBEFILLED-Proceedings of the Second Workshop on Bui…
- score 0.275 (cites 0.0, cocite 0.0, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we apply supervised classification to identify arguments on Twitter, and we present two new tasks for argument mining, namely facts recognition and source identification." "We study the feasibility of the approaches proposed to address these tasks on a set of tweets related to the Grexit and Brexit news topics." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{dusmanu2017argumentm,
  title = {Argument Mining on Twitter: Arguments, Facts and Sources},
  author = {Mihai Dusmanu and Elena Cabrio and Serena Villata},
  year = {2017},
  booktitle = {EMNLP},
  doi = {10.18653/v1/d17-1245},
  url = {https://aclanthology.org/D17-1245/},
}
```

</details>

#### Ivan Habernal and Iryna Gurevych (2017). *Argumentation Mining in User-Generated Web Discourse*. CL.

- `title:ca6f9e03a1dcd4266f5306de7e9977daf3fcad22` | aliases: `acl:J17-1004`, `doi:10.1162/coli_a_00276`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/J17-1004/) | [OA PDF](https://aclanthology.org/J17-1004.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database
- score 0.3117 (cites 0.0, cocite 0.2, keyword 0.6667, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The goal of argumentation mining, an evolving research field in computational linguistics, is to design methods capable of analyzing people’s argumentation." "We offer the data, source codes, and annotation guidelines to the community under free licenses." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{habernal2017argumentat,
  title = {Argumentation Mining in User-Generated Web Discourse},
  author = {Ivan Habernal and Iryna Gurevych},
  year = {2017},
  booktitle = {CL},
  doi = {10.1162/coli_a_00276},
  url = {https://aclanthology.org/J17-1004/},
}
```

</details>

#### Eyal Shnarch, Ran Levy, Vikas Raykar and Noam Slonim (2017). *GRASP: Rich Patterns for Argumentation Mining*. EMNLP.

- `title:f36bd2c70ff42e41d1283ef243b7b55af248697f` | aliases: `acl:D17-1140`, `doi:10.18653/v1/d17-1140`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/D17-1140/) | [OA PDF](https://aclanthology.org/D17-1140.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist | note: bibcorpus:jbingel/emnlp2017-handbook: venue mismatch ('Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing' vs 'TOBEFILLED-Proceedings of the Second Workshop on Bui…
- score 0.275 (cites 0.0, cocite 0.0, keyword 0.5, venue 1.0)
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

#### Steffen Eger, Johannes Daxenberger and Iryna Gurevych (2017). *Neural End-to-End Learning for Computational Argumentation Mining*. ACL.

- `title:fc0205dac13ac46c067f284b16656e1b179d8904` | aliases: `acl:P17-1002`, `doi:10.18653/v1/p17-1002`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/P17-1002/) | [OA PDF](https://aclanthology.org/P17-1002.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database
- score 0.275 (cites 0.0, cocite 0.0, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We investigate neural techniques for end-to-end computational argumentation mining (AM)." "We frame AM both as a token-based dependency parsing and as a token-based sequence tagging problem, including a multi-task learning setup." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{eger2017neuralend,
  title = {Neural End-to-End Learning for Computational Argumentation Mining},
  author = {Steffen Eger and Johannes Daxenberger and Iryna Gurevych},
  year = {2017},
  booktitle = {ACL},
  doi = {10.18653/v1/p17-1002},
  url = {https://aclanthology.org/P17-1002/},
}
```

</details>

####  (2017). *Using Question-Answering Techniques to Implement a Knowledge-Driven Argument Mining Approach*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5111` | aliases: `acl:W17-5111`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/W17-5111/) | [OA PDF](https://aclanthology.org/W17-5111.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook | note: venue not corroborated by both sources
- score 0.275 (cites 0.0, cocite 0.0, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This short paper presents a first implementation of a knowledge-driven argument mining approach." "The major processing steps and language resources of the system are surveyed." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{saintdizier2017usingques,
  title = {Using Question-Answering Techniques to Implement a Knowledge-Driven Argument Mining Approach},
  author = {Patrick Saint-Dizier},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5111},
  url = {https://aclanthology.org/W17-5111/},
}
```

</details>

#### Ahmet Aker et al. (2017). *What works and what does not: Classifier and feature analysis for argument mining*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5112` | aliases: `acl:W17-5112`
- doc_type: `workshop` | tier: T2 | tags: extraction
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

#### Khalid Al-Khatib et al. (2016). *Cross-Domain Mining of Argumentative Text through Distant Supervision*. NAACL.

- `title:c60c719a9320f01f8ebf567305e6334f8c7a0202` | aliases: `acl:N16-1165`, `doi:10.18653/v1/n16-1165`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/N16-1165/) | [OA PDF](https://aclanthology.org/N16-1165.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database | note: author order differs (al-khatib / khatib)
- score 0.2333 (cites 0.0, cocite 0.0, keyword 0.3333, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, NAACL, 2016), verified against 3 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{alkhatib2016crossdoma,
  title = {Cross-Domain Mining of Argumentative Text through Distant Supervision},
  author = {Khalid Al-Khatib and Henning Wachsmuth and Matthias Hagen and Jonas Köhler and Benno Stein},
  year = {2016},
  booktitle = {NAACL},
  doi = {10.18653/v1/n16-1165},
  url = {https://aclanthology.org/N16-1165/},
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

#### Peter Potash, Alexey Romanov and Anna Rumshisky (2016). *Here's my point: Joint pointer architecture for argument mining*. arXiv preprint arXiv:1612.08994.

- `doi:10.18653/v1/d17-1143` | aliases: `acl:D17-1143`
- doc_type: `preprint` | tier: T2 | tags: extraction
- [landing](:https://www.aclweb.org/anthology/D17-1143.pdf:URL) | [OA PDF](https://aclanthology.org/D17-1143.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist | note: bibcorpus:jbingel/emnlp2017-handbook: venue mismatch ('Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing' vs 'TOBEFILLED-Proceedings of the Second Workshop on Bui…
- score 0.155 (cites 0.0, cocite 0.0, keyword 0.5, venue 0.2)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Specifically, we propose a novel architecture that applies Pointer Network sequence-to-sequence attention modeling to structural prediction in discourse parsing tasks." "The proposed joint model achieves state-of-the-art results on two separate evaluation corpora, showing far superior performance than the previously proposed corpus-specific and heavily feature-engineered models." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@misc{potash2016heresmy,
  title = {Here's my point: Joint pointer architecture for argument mining},
  author = {Peter Potash and Alexey Romanov and Anna Rumshisky},
  year = {2016},
  publisher = {arXiv preprint arXiv:1612.08994},
  doi = {10.18653/v1/d17-1143},
  url = {:https://www.aclweb.org/anthology/D17-1143.pdf:URL},
}
```

</details>

#### Rory Duthie, John Lawrence, Katarzyna Budzynska and Chris Reed (2016). *The CASS Technique for Evaluating the Performance of Argument Mining*. Proceedings of the Third Workshop on Argument Mining (ArgMining2016).

- `doi:10.18653/v1/w16-2805` | aliases: `acl:W16-2805`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/W16-2805/) | [OA PDF](https://aclanthology.org/W16-2805.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.485 (cites 0.0, cocite 0.6, keyword 0.5, venue 1.0)
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

#### Reid Swanson, Brian Ecker and Marilyn Walker (2015). *Argument Mining: Extracting Arguments from Online Dialogue*. Proceedings of the 16th Annual Meeting of the Special Interest Group on Discourse and Dialogue.

- `doi:10.18653/v1/w15-4631` | aliases: `acl:W15-4631`
- doc_type: `conference` | tier: T2 | tags: dialogue, extraction
- [landing](https://aclanthology.org/W15-4631/) | [OA PDF](https://aclanthology.org/W15-4631.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.2104 (cites 0.0, cocite 0.0, keyword 0.5417, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Proceedings of the 16th Annual Meeting of the Special Interest Group on Discourse and Dialogue, 2015), verified against 2 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{swanson2015argumentm,
  title = {Argument Mining: Extracting Arguments from Online Dialogue},
  author = {Reid Swanson and Brian Ecker and Marilyn Walker},
  year = {2015},
  booktitle = {Proceedings of the 16th Annual Meeting of the Special Interest Group on Discourse and Dialogue},
  doi = {10.18653/v1/w15-4631},
  url = {https://aclanthology.org/W15-4631/},
}
```

</details>

#### John Lawrence and Chris Reed (2015). *Combining Argument Mining Techniques*. Proceedings of the 2nd Workshop on Argumentation Mining.

- `doi:10.3115/v1/w15-0516` | aliases: `acl:W15-0516`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/W15-0516/) | [OA PDF](https://aclanthology.org/W15-0516.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.2313 (cites 0.0, cocite 0.0, keyword 0.625, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (workshop, Proceedings of the 2nd Workshop on Argumentation Mining, 2015), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{lawrence2015combining,
  title = {Combining Argument Mining Techniques},
  author = {John Lawrence and Chris Reed},
  year = {2015},
  booktitle = {Proceedings of the 2nd Workshop on Argumentation Mining},
  doi = {10.3115/v1/w15-0516},
  url = {https://aclanthology.org/W15-0516/},
}
```

</details>

#### Marco Lippi and Paolo Torroni (2015). *Context-Independent Claim Detection for Argument Mining*. IJCAI.

- `title:301be2f14805fc8646b001ef9b132eb5f8bbd02b`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](http://ijcai.org/papers15/Abstracts/IJCAI15-033.html)
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:harisont/biboba, bibcorpus:lihebi/biber-dist
- score 0.47 (cites 0.0, cocite 0.2, keyword 1.0, venue 1.0)
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

#### Peter Novák 0001 and Cees Witteveen (2015). *Context-aware reconfiguration of large-scale surveillance systems: argumentative approach*. Argument & Computation.

- `doi:10.1080/19462166.2014.1001790`
- doc_type: `journal` | tier: T2 | tags: extraction
- [landing](http://content.iospress.com/doi/10.1080/19462166.2014.1001790)
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:lmlearning/AFGraphLib | note: author order differs (0001 / novak)
- score 0.3033 (cites 0.0, cocite 0.2, keyword 0.3333, venue 1.0)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Argument & Computation, 2015), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

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
- score 0.34 (cites 0.0, cocite 0.4, keyword 0.5, venue 0.5)
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

#### Joonsuk Park and Claire Cardie (2014). *Identifying Appropriate Support for Propositions in Online User Comments*. Proceedings of the First Workshop on Argumentation Mining.

- `doi:10.3115/v1/w14-2105` | aliases: `acl:W14-2105`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/W14-2105/) | [OA PDF](https://aclanthology.org/W14-2105.pdf) (via acl)
- verified against: acl, bibcorpus:harisont/biboba
- score 0.1762 (cites 0.0, cocite 0.2, keyword 0.125, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (workshop, Proceedings of the First Workshop on Argumentation Mining, 2014), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{park2014identifyin,
  title = {Identifying Appropriate Support for Propositions in Online User Comments},
  author = {Joonsuk Park and Claire Cardie},
  year = {2014},
  booktitle = {Proceedings of the First Workshop on Argumentation Mining},
  doi = {10.3115/v1/w14-2105},
  url = {https://aclanthology.org/W14-2105/},
}
```

</details>

####  (2013). *Argumentation Mining: Where Are We Now, Where Do We Want to Be and How Do We Get There?*. Post-Proceedings of the 4th and 5th Workshops of the Forum for Information Retrieval Evaluation.

- `doi:10.1145/2701336.2701635`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://doi.org/10.1145/2701336.2701635)
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:ir-anthology/ir-anthology.github.io | note: bibcorpus:boudinfl/acm-cr: venue mismatch ('FIRE' vs 'Post-Proceedings of the 4th and 5th Workshops of the Forum for Information Retrieval Evaluation')
- score 0.2 (cites 0.0, cocite 0.0, keyword 0.5, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (workshop, Post-Proceedings of the 4th and 5th Workshops of the Forum for Information Retrieval Evaluation, 2013), verified against 2 sources. For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{moens2013argumentat,
  title = {Argumentation Mining: Where Are We Now, Where Do We Want to Be and How Do We Get There?},
  author = {Marie-Francine Moens},
  year = {2013},
  booktitle = {Post-Proceedings of the 4th and 5th Workshops of the Forum for Information Retrieval Evaluation},
  doi = {10.1145/2701336.2701635},
  url = {https://doi.org/10.1145/2701336.2701635},
}
```

</details>

#### Raquel Mochales and Marie-Francine Moens (2011). *Argumentation Mining*. Artif. Intell. Law.

- `doi:10.1007/s10506-010-9104-x`
- doc_type: `journal` | tier: T2 | tags: extraction
- [landing](http://dx.doi.org/10.1007/s10506-010-9104-x)
- verified against: bibcorpus:IKMLab/arct2, bibcorpus:davidar/dblp.yaml | note: author order differs (mochales / palau); bibcorpus:m0re4u/paper-database: venue mismatch ('Artif. Intell. Law' vs 'Artificial Intelligence and Law'); bibcorpus:nshkrdotcom/research_papers: venue mism…
- score 0.41 (cites 0.0, cocite 0.6, keyword 0.5, venue 0.5)
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
- score 0.41 (cites 0.0, cocite 0.6, keyword 0.5, venue 0.5)
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
- score 0.485 (cites 0.0, cocite 0.6, keyword 0.5, venue 1.0)
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

#### Khalid Al-Khatib et al. (2018). *Modeling Deliberative Argumentation Strategies on Wikipedia*. Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/p18-1237` | aliases: `acl:P18-1237`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/P18-1237/) | [OA PDF](https://aclanthology.org/P18-1237.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database | note: author order differs (al-khatib / khatib)
- score 0.5625 (cites 0.0, cocite 1.0, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we present a model for deliberative discussions and we illustrate its operationalization." "On this basis, we automatically generate a corpus with about 200,000 turns, labeled for the 13 categories." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{alkhatib2018modelingd,
  title = {Modeling Deliberative Argumentation Strategies on Wikipedia},
  author = {Khalid Al-Khatib and Henning Wachsmuth and Kevin Lang and Jakob Herpel and Matthias Hagen and Benno Stein},
  year = {2018},
  booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/p18-1237},
  url = {https://aclanthology.org/P18-1237/},
}
```

</details>

#### Claudia Schulz et al. (2018). *Multi-Task Learning for Argumentation Mining in Low-Resource Settings*. NAACL.

- `title:e9c7f56b7cb5ad8351386161cee2a74b4cb0aa7f` | aliases: `acl:N18-2006`, `doi:10.18653/v1/n18-2006`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/N18-2006/) | [OA PDF](https://aclanthology.org/N18-2006.pdf) (via acl) | [repo](https://github.com/UKPLab/naacl18-multitask_argument_mining)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database | note: repo linked on token overlap: ['argumentation', 'learning', 'low', 'mining', 'multi', 'resource', 'settings', 'task']
- score 0.275 (cites 0.0, cocite 0.0, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We investigate whether and where multi-task learning (MTL) can improve performance on NLP problems related to argumentation mining (AM), in particular argument component identification." "Our results show that MTL performs particularly well (and better than single-task learning) when little training data is available for the main task, a common scenario in AM." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{schulz2018multitask,
  title = {Multi-Task Learning for Argumentation Mining in Low-Resource Settings},
  author = {Claudia Schulz and Steffen Eger and Johannes Daxenberger and Tobias Kahse and Iryna Gurevych},
  year = {2018},
  booktitle = {NAACL},
  doi = {10.18653/v1/n18-2006},
  url = {https://aclanthology.org/N18-2006/},
}
```

</details>

#### Ivan Habernal, Henning Wachsmuth, Iryna Gurevych and Benno Stein (2018). *SemEval-2018 Task 12: The Argument Reasoning Comprehension Task*. Proceedings of the 12th International Workshop on Semantic Evaluation.

- `doi:10.18653/v1/s18-1121` | aliases: `acl:S18-01121`
- doc_type: `workshop` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/S18-01121/) | [OA PDF](https://aclanthology.org/S18-01121.pdf) (via acl) | [repo](https://github.com/UKPLab/argument-reasoning-comprehension-task)
- verified against: acl, bibcorpus:IKMLab/arct2 | note: repo linked on token overlap: ['argument', 'comprehension', 'reasoning', 'task']
- score 0.3192 (cites 0.0, cocite 0.4, keyword 0.4167, venue 0.5)
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
- verified against: acl, bibcorpus:IKMLab/arct2 | note: bibcorpus:lihebi/biber-dist: venue mismatch ('Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1…
- score 0.3733 (cites 0.0, cocite 0.4, keyword 0.3333, venue 1.0)
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

#### Christian Stab and Iryna Gurevych (2017). *Recognizing Insufficiently Supported Arguments in Argumentative Essays*. Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 1, Long Papers.

- `title:4548f0ff40575ec88d744f306fc5a7f696551502` | aliases: `acl:E17-1092`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/E17-1092/) | [OA PDF](https://aclanthology.org/E17-1092.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:npnkhoi/memefal-paper, bibcorpus:xinyannnnnnn/fact-driven-storytelling-with-llms
- score 0.5967 (cites 0.0, cocite 0.8, keyword 0.6667, venue 1.0)
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

### T4 - Recent (2023-2026). LLM-era work; lower durability confidence, high build relevance.

#### Zihao Zheng, Zhaowei Wang, Qing Zong and Yangqiu Song (2024). *KNOWCOMP POKEMON Team at DialAM-2024: A Two-Stage Pipeline for Detecting Relations in Dialogue Argument Mining*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.11` | aliases: `acl:2024.argmining-1.11`
- doc_type: `workshop` | tier: T4 | tags: dialogue, extraction | also in: dialogue
- [landing](https://aclanthology.org/2024.argmining-1.11/) | [OA PDF](https://aclanthology.org/2024.argmining-1.11.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.6 (cites 0.0, cocite 0.75, keyword 0.75, venue 1.0)
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
- score 0.4075 (cites 0.0, cocite 0.2, keyword 0.75, venue 1.0)
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

## 6.3 Argument quality and evaluation (19 entries, quota 40)

### T2 - Core method. Defines a task formulation, model, or evaluation still in use.

#### Eyal Shnarch et al. (2022). *Cluster & Tune: Boost Cold Start Performance in Text Classification*. Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/2022.acl-long.526` | aliases: `acl:2022.acl-long.526`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://aclanthology.org/2022.acl-long.526/) | [OA PDF](https://aclanthology.org/2022.acl-long.526.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.2617 (cites 0.0, cocite 0.2, keyword 0.1667, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In real-world scenarios, a text classification task often begins with a cold start, when labeled data is scarce." "In such cases, the common practice of fine-tuning pre-trained models, such as BERT, for a target classification task, is prone to produce poor performance." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{shnarch2022cluster,
  title = {Cluster & Tune: Boost Cold Start Performance in Text Classification},
  author = {Eyal Shnarch and Ariel Gera and Alon Halfon and Lena Dankin and Leshem Choshen and Ranit Aharonov and Noam Slonim},
  year = {2022},
  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/2022.acl-long.526},
  url = {https://aclanthology.org/2022.acl-long.526/},
}
```

</details>

#### Christine De Kock, Tom Stafford and Andreas Vlachos (2022). *How to disagree well: Investigating the dispute tactics used on Wikipedia*. Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2022.emnlp-main.252` | aliases: `acl:2022.emnlp-main.252`
- doc_type: `conference` | tier: T2 | tags: dialogue, fallacy, quality
- [landing](https://aclanthology.org/2022.emnlp-main.252/) | [OA PDF](https://aclanthology.org/2022.emnlp-main.252.pdf) (via acl)
- verified against: acl, bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments
- score 0.5833 (cites 0.0, cocite 1.0, keyword 0.3333, venue 1.0)
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
- score 0.345 (cites 0.0, cocite 0.2, keyword 0.5, venue 1.0)
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

#### Martin Gleize et al. (2019). *Are You Convinced? Choosing the More Convincing Evidence with a Siamese Network*. Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics.

- `doi:10.18653/v1/p19-1093` | aliases: `acl:P19-1093`
- doc_type: `conference` | tier: T2 | tags: extraction, quality
- [landing](https://aclanthology.org/P19-1093/) | [OA PDF](https://aclanthology.org/P19-1093.pdf) (via acl)
- verified against: acl, bibcorpus:BarryMafu/LitLens, bibcorpus:borgr/publications | note: bibcorpus:xinyannnnnnn/fact-driven-storytelling-with-llms: venue mismatch ('Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics' vs 'arXiv preprint arXiv:1907.0897…
- score 0.5475 (cites 0.0, cocite 0.6, keyword 0.75, venue 1.0)
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

#### Leshem Choshen and Omri Abend (2019). *Automatically Extracting Challenge Sets for Non-Local Phenomena in Neural Machine Translation*. Proceedings of the 23rd Conference on Computational Natural Language Learning (CoNLL).

- `doi:10.18653/v1/k19-1028` | aliases: `acl:K19-1028`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://aclanthology.org/K19-1028/) | [OA PDF](https://aclanthology.org/K19-1028.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.1867 (cites 0.0, cocite 0.2, keyword 0.1667, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We show that the state-of-the-art Transformer MT model is not biased towards monotonic reordering (unlike previous recurrent neural network models), but that nevertheless, long-distance dependencies remain a challenge for the model." "Since most dependencies are short-distance, common evaluation metrics will be little influenced by how well systems perform on them." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{choshen2019automatica,
  title = {Automatically Extracting Challenge Sets for Non-Local Phenomena in Neural Machine Translation},
  author = {Leshem Choshen and Omri Abend},
  year = {2019},
  booktitle = {Proceedings of the 23rd Conference on Computational Natural Language Learning (CoNLL)},
  doi = {10.18653/v1/k19-1028},
  url = {https://aclanthology.org/K19-1028/},
}
```

</details>

#### Ivan Habernal, Henning Wachsmuth, Iryna Gurevych and Benno Stein (2018). *Before Name-Calling: Dynamics and Triggers of Ad Hominem Fallacies in Web Argumentation*. Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers).

- `doi:10.18653/v1/n18-1036` | aliases: `acl:N18-1036`
- doc_type: `conference` | tier: T2 | tags: dialogue, fallacy, quality
- [landing](https://aclanthology.org/N18-1036/) | [OA PDF](https://aclanthology.org/N18-1036.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:npnkhoi/memefal-paper
- score 0.47 (cites 0.0, cocite 0.2, keyword 1.0, venue 1.0)
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
- score 0.345 (cites 0.0, cocite 0.2, keyword 0.5, venue 1.0)
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

#### Frank Li et al. (2016). *Remedying Web Hijacking: Notification Effectiveness and Webmaster Comprehension*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2883039`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://doi.org/10.1145/2872427.2883039)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.1867 (cites 0.0, cocite 0.2, keyword 0.1667, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Proceedings of the 25th International Conference on World Wide Web, 2016), verified against 2 sources. For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{li2016remedying,
  title = {Remedying Web Hijacking: Notification Effectiveness and Webmaster Comprehension},
  author = {Frank Li and Grant Ho and Eric Kuan and Yuan Niu and Lucas Ballard and Kurt Thomas and Elie Bursztein and Vern Paxson},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2883039},
  url = {https://doi.org/10.1145/2872427.2883039},
}
```

</details>

#### Ivan Habernal and Iryna Gurevych (2016). *Which argument is more convincing? Analyzing and predicting convincingness of Web arguments using bidirectional LSTM*. Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/p16-1150` | aliases: `acl:P16-1150`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://aclanthology.org/P16-1150/) | [OA PDF](https://aclanthology.org/P16-1150.pdf)
- verified against: acl, bibcorpus:xinyannnnnnn/fact-driven-storytelling-with-llms
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2016), verified against 2 sources. For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

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
- score 0.345 (cites 0.0, cocite 0.2, keyword 0.5, venue 1.0)
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
- score 0.3 (cites 0.0, cocite 0.25, keyword 0.25, venue 1.0)
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

#### Adir Rahamim et al. (2026). *Will it Merge? On The Causes of Model Mergeability*. Findings of the Association for Computational Linguistics: ACL 2026.

- `doi:10.18653/v1/2026.findings-acl.1322` | aliases: `acl:2026.findings-acl.1322`
- doc_type: `conference` | tier: T4 | tags: quality
- [landing](https://aclanthology.org/2026.findings-acl.1322/) | [OA PDF](https://aclanthology.org/2026.findings-acl.1322.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.2617 (cites 0.0, cocite 0.2, keyword 0.1667, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this work, we investigate why specific models are merged better than others." "To do so, we propose a concrete, measurable definition of mergeability." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{rahamim2026willitme,
  title = {Will it Merge? On The Causes of Model Mergeability},
  author = {Adir Rahamim and Asaf Yehudai and Boaz Carmeli and Leshem Choshen and Yosi Mass and Yonatan Belinkov},
  year = {2026},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2026},
  doi = {10.18653/v1/2026.findings-acl.1322},
  url = {https://aclanthology.org/2026.findings-acl.1322/},
}
```

</details>

#### Abhinav Lalwani et al. (2025). *Autoformalizing Natural Language to First-Order Logic: A Case Study in Logical Fallacy Detection*. Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics.

- `doi:10.18653/v1/2025.findings-ijcnlp.8` | aliases: `acl:2025.findings-ijcnlp.8`, `arxiv:2405.02318`
- doc_type: `conference` | tier: T4 | tags: extraction, fallacy, quality | also in: llm
- [landing](https://aclanthology.org/2025.findings-ijcnlp.8/) | [OA PDF](https://arxiv.org/pdf/2405.02318) (via arxiv)
- verified against: acl, bibcorpus:danny-v-nguyen/thesis | note: venue not corroborated by both sources
- score 0.47 (cites 0.0, cocite 0.2, keyword 1.0, venue 1.0)
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
- score 0.47 (cites 0.0, cocite 0.2, keyword 1.0, venue 1.0)
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

## 6.4 Dialogue and debate (14 entries, quota 40)

### T1 - Foundational / survey. Read in full: theory anchors, major surveys, canonical papers.

#### Ramon Ruiz-Dolz, John Lawrence, Ella Schad and Chris Reed (2024). *Overview of DialAM-2024: Argument Mining in Natural Language Dialogues*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.8` | aliases: `acl:2024.argmining-1.8`
- doc_type: `workshop` | tier: T1 | tags: dialogue, extraction | also in: mining
- [landing](https://aclanthology.org/2024.argmining-1.8/) | [OA PDF](https://aclanthology.org/2024.argmining-1.8.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.6417 (cites 0.0, cocite 0.75, keyword 0.9167, venue 1.0)
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
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, Nat., 2021), verified against 2 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

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

#### Gabriel Doyle, Dan Yurovsky and Michael C. Frank (2016). *A Robust Framework for Estimating Linguistic Alignment in Twitter Conversations*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2883091`
- doc_type: `conference` | tier: T2 | tags: dialogue
- [landing](https://doi.org/10.1145/2872427.2883091)
- verified against: bibcorpus:IKMLab/argalign1, bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.2042 (cites 0.0, cocite 0.25, keyword 0.1667, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Proceedings of the 25th International Conference on World Wide Web, 2016), verified against 3 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{doyle2016arobustf,
  title = {A Robust Framework for Estimating Linguistic Alignment in Twitter Conversations},
  author = {Gabriel Doyle and Dan Yurovsky and Michael C. Frank},
  year = {2016},
  booktitle = {Proceedings of the 25th International Conference on World Wide Web},
  doi = {10.1145/2872427.2883091},
  url = {https://doi.org/10.1145/2872427.2883091},
}
```

</details>

#### Justine Zhang, Ravi Kumar, Sujith Ravi and Cristian Danescu-Niculescu-Mizil (2016). *Conversational Flow in Oxford-style Debates*. Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.

- `doi:10.18653/v1/n16-1017` | aliases: `acl:N16-1017`
- doc_type: `conference` | tier: T2 | tags: dialogue
- [landing](https://aclanthology.org/N16-1017/) | [OA PDF](https://aclanthology.org/N16-1017.pdf) (via acl)
- verified against: acl, bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments, bibcorpus:lihebi/biber-dist | note: venue not corroborated by both sources
- score 0.625 (cites 0.0, cocite 1.0, keyword 0.5, venue 1.0)
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
- score 0.4458 (cites 0.0, cocite 0.25, keyword 0.8333, venue 1.0)
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

#### Chenhao Tan, Vlad Niculae, Cristian Danescu-Niculescu-Mizil and Lillian Lee (2016). *Winning Arguments: Interaction Dynamics and Persuasion Strategies in Good-Faith Online Discussions*. Proceedings of the 25th International Conference on World Wide Web.

- `doi:10.1145/2872427.2883081`
- doc_type: `conference` | tier: T2 | tags: dataset, dialogue | also in: resources
- [landing](https://doi.org/10.1145/2872427.2883081)
- verified against: bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io, bibcorpus:m0re4u/paper-database
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (conference, Proceedings of the 25th International Conference on World Wide Web, 2016), verified against 3 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

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
- score 0.5083 (cites 0.0, cocite 1.0, keyword 0.3333, venue 0.5)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (journal, New Media & Society, 2007), verified against 2 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

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

#### Leshem Choshen and Omri Abend (2022). *Enhancing the Transformer Decoder with Transition-based Syntax*. Proceedings of the 26th Conference on Computational Natural Language Learning (CoNLL).

- `doi:10.18653/v1/2022.conll-1.27` | aliases: `acl:2022.conll-1.27`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue | also in: resources
- [landing](https://aclanthology.org/2022.conll-1.27/) | [OA PDF](https://aclanthology.org/2022.conll-1.27.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.2042 (cites 0.0, cocite 0.25, keyword 0.1667, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We propose a general approach for tree decoding using a transition-based approach." "Examining the challenging test case of incorporating Universal Dependencies syntax into machine translation, we present substantial improvements on test sets that focus on syntactic generalization, while presenting improved or comparable performance on standard MT benchmarks." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{choshen2022enhancing,
  title = {Enhancing the Transformer Decoder with Transition-based Syntax},
  author = {Leshem Choshen and Omri Abend},
  year = {2022},
  booktitle = {Proceedings of the 26th Conference on Computational Natural Language Learning (CoNLL)},
  doi = {10.18653/v1/2022.conll-1.27},
  url = {https://aclanthology.org/2022.conll-1.27/},
}
```

</details>

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
- score 0.5375 (cites 0.0, cocite 0.75, keyword 0.5, venue 1.0)
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
- score 0.6625 (cites 0.0, cocite 0.75, keyword 1.0, venue 1.0)
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
- score 0.6625 (cites 0.0, cocite 0.75, keyword 1.0, venue 1.0)
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

## 6.5 LLM era, 2023-2026 (15 entries, quota 40)

### T3 - Dataset / tool / annotation guideline, including the guideline documents themselves.

#### Shachar Don-Yehiya, Asaf Yehudai, Leshem Choshen and Omri Abend (2026). *Mediocrity is the key for LLM as a Judge Anchor Selection*. Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/2026.acl-long.706` | aliases: `acl:2026.acl-long.706`
- doc_type: `conference` | tier: T3 | tags: dataset | also in: resources
- [landing](https://aclanthology.org/2026.acl-long.706/) | [OA PDF](https://aclanthology.org/2026.acl-long.706.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.47 (cites 0.0, cocite 0.2, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "To address the quadratic scalability costs of pairwise comparisons, popular benchmarks like Arena-Hard and AlpacaEval compare all models against a single anchor." "In this work, we systematically investigate the effect of anchor selection by evaluating 22 different anchors on the Arena-Hard-v2.0 dataset." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{donyehiya2026mediocrity,
  title = {Mediocrity is the key for LLM as a Judge Anchor Selection},
  author = {Shachar Don-Yehiya and Asaf Yehudai and Leshem Choshen and Omri Abend},
  year = {2026},
  booktitle = {Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/2026.acl-long.706},
  url = {https://aclanthology.org/2026.acl-long.706/},
}
```

</details>

#### Fengjun Pan, Xiaobao Wu, Zongrui Li and Anh Tuan Luu (2024). *Are LLMs Good Zero-Shot Fallacy Classifiers?*. Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2024.emnlp-main.794` | aliases: `acl:2024.emnlp-main.794`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction, fallacy, quality | also in: quality, resources
- [landing](https://aclanthology.org/2024.emnlp-main.794/) | [OA PDF](https://aclanthology.org/2024.emnlp-main.794.pdf) (via acl)
- verified against: acl, bibcorpus:lefteriskat/Logical-Fallacy-Detection-Using-LLMs
- score 0.47 (cites 0.0, cocite 0.2, keyword 1.0, venue 1.0)
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

#### Leshem Choshen et al. (2024). *Navigating the Modern Evaluation Landscape: Considerations in Benchmarks and Frameworks for Large Language Models (LLMs)*. Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024): Tutorial Summaries.

- `title:6430e3971735a1240942ff8809e124281b95267b` | aliases: `acl:2024.lrec-tutorials.4`
- doc_type: `conference` | tier: T3 | tags: dataset | also in: resources
- [landing](https://aclanthology.org/2024.lrec-tutorials.4/) | [OA PDF](https://aclanthology.org/2024.lrec-tutorials.4.pdf) (via acl) | [repo](https://github.com/DAMO-NLP-SG/LLM-argumentation)
- verified against: acl, bibcorpus:borgr/publications | note: repo linked on token overlap: ['language', 'large', 'models']
- score 0.47 (cites 0.0, cocite 0.2, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The tutorial welcomes people from diverse backgrounds and assumes little familiarity with metrics, datasets, prompts and benchmarks." "We will contrast new to old approaches, from evaluating on many-task benchmarks rather than on dedicated datasets to efficiency constraints, and from testing stability and prompts on in-context learning to using the models themselves as evaluation metrics." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{choshen2024navigating,
  title = {Navigating the Modern Evaluation Landscape: Considerations in Benchmarks and Frameworks for Large Language Models (LLMs)},
  author = {Leshem Choshen and Ariel Gera and Yotam Perlitz and Michal Shmueli-Scheuer and Gabriel Stanovsky},
  year = {2024},
  booktitle = {Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024): Tutorial Summaries},
  url = {https://aclanthology.org/2024.lrec-tutorials.4/},
}
```

</details>

#### Felipe Maia Polo et al. (2024). *tinyBenchmarks: evaluating LLMs with fewer examples*. Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024.

- `title:edb3d8bd1cbd986fc1430e09234833845d0bfe69`
- doc_type: `conference` | tier: T3 | tags: dataset | also in: resources
- [landing](https://openreview.net/forum?id=qAml3FpfhG)
- verified against: bibcorpus:CogSciPrag/project_ideas, bibcorpus:borgr/publications
- score 0.41 (cites 0.0, cocite 0.6, keyword 0.5, venue 0.5)
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

#### Gautier Izacard and Edouard Grave (2021). *Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering*. Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume.

- `doi:10.18653/v1/2021.eacl-main.74` | aliases: `acl:2021.eacl-main.74`
- doc_type: `conference` | tier: T3 | tags: dataset | also in: resources
- [landing](https://aclanthology.org/2021.eacl-main.74/) | [OA PDF](https://aclanthology.org/2021.eacl-main.74.pdf) (via acl)
- verified against: acl, bibcorpus:BarryMafu/LitLens
- score 0.3317 (cites 0.0, cocite 0.4, keyword 0.1667, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we investigate how much these models can benefit from retrieving text passages, potentially containing evidence." "We obtain state-of-the-art results on the Natural Questions and TriviaQA open benchmarks." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{izacard2021leveraging,
  title = {Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering},
  author = {Gautier Izacard and Edouard Grave},
  year = {2021},
  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},
  doi = {10.18653/v1/2021.eacl-main.74},
  url = {https://aclanthology.org/2021.eacl-main.74/},
}
```

</details>

### T4 - Recent (2023-2026). LLM-era work; lower durability confidence, high build relevance.

#### Maxim Ifergan et al. (2025). *Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs*. Findings of the Association for Computational Linguistics: NAACL 2025.

- `title:78f1e57af8f02b9283a4449a8e757f4f62a0ae0a` | aliases: `acl:2025.findings-naacl.475`
- doc_type: `conference` | tier: T4 | tags: extraction
- [landing](https://aclanthology.org/2025.findings-naacl.475/) | [OA PDF](https://aclanthology.org/2025.findings-naacl.475.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.345 (cites 0.0, cocite 0.2, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We propose a methodology to measure the extent of representation sharing across languages by repurposing knowledge editing methods." "We examine LLMs with various multilingual configurations using a new multilingual dataset." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{ifergan2025beneathth,
  title = {Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs},
  author = {Maxim Ifergan and Leshem Choshen and Roee Aharoni and Idan Szpektor and Omri Abend},
  year = {2025},
  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
  url = {https://aclanthology.org/2025.findings-naacl.475/},
}
```

</details>

#### Dennis Ulmer et al. (2024). *Bootstrapping LLM-based Task-Oriented Dialogue Agents via Self-Talk*. Findings of the Association for Computational Linguistics: ACL 2024.

- `doi:10.18653/v1/2024.findings-acl.566` | aliases: `acl:2024.findings-acl.566`
- doc_type: `conference` | tier: T4 | tags: dialogue
- [landing](https://aclanthology.org/2024.findings-acl.566/) | [OA PDF](https://aclanthology.org/2024.findings-acl.566.pdf) (via acl)
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments | note: acl: venue mismatch ('ArXiv' vs 'Findings of the Association for Computational Linguistics: ACL 2024')
- score 0.75 (cites 0.0, cocite 1.0, keyword 1.0, venue 1.0)
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

#### Peiyi Wang et al. (2024). *Large Language Models are not Fair Evaluators*. Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/2024.acl-long.511` | aliases: `acl:2024.acl-long.511`, `arxiv:2305.17926`
- doc_type: `conference` | tier: T4 | tags: extraction
- [landing](https://aclanthology.org/2024.acl-long.511/) | [OA PDF](https://arxiv.org/pdf/2305.17926) (via arxiv)
- verified against: acl, bibcorpus:BarryMafu/LitLens, bibcorpus:ljvmiranda921/ljvmiranda921.github.io | note: venue not corroborated by both sources
- score 0.54 (cites 0.0, cocite 0.4, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we uncover a positional bias in the evaluation paradigm of adopting large language models (LLMs), e.g., GPT-4, as a referee to score and compare the quality of responses generated by candidate models." "We propose a simple yet effective calibration framework to address our discovered positional bias.To evaluate the effectiveness of our framework, we manually annotate the “win/tie/lose” outcomes of responses from ChatGPT and Vicuna-13B in the Vicuna Benchmark’s question prompt." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{wang2024largelang,
  title = {Large Language Models are not Fair Evaluators},
  author = {Peiyi Wang and Lei Li and Liang Chen and Zefan Cai and Dawei Zhu and Binghuai Lin and Yunbo Cao and Lingpeng Kong and Qi Liu and Tianyu Liu and Zhifang Sui},
  year = {2024},
  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/2024.acl-long.511},
  url = {https://aclanthology.org/2024.acl-long.511/},
}
```

</details>

#### Eli Schwartz et al. (2024). *NumeroLogic: Number Encoding for Enhanced LLMs’ Numerical Reasoning*. Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2024.emnlp-main.12` | aliases: `acl:2024.emnlp-main.12`
- doc_type: `conference` | tier: T4 | tags: extraction
- [landing](https://aclanthology.org/2024.emnlp-main.12/) | [OA PDF](https://aclanthology.org/2024.emnlp-main.12.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.345 (cites 0.0, cocite 0.2, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "To address this issue, we propose a simple adjustment to how numbers are represented by including the count of digits before each number." "We further demonstrate NumeroLogic applicability to general natural language modeling, improving language understanding performance in the MMLU benchmark." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{schwartz2024numerologi,
  title = {NumeroLogic: Number Encoding for Enhanced LLMs’ Numerical Reasoning},
  author = {Eli Schwartz and Leshem Choshen and Joseph Shtok and Sivan Doveh and Leonid Karlinsky and Assaf Arbelle},
  year = {2024},
  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/2024.emnlp-main.12},
  url = {https://aclanthology.org/2024.emnlp-main.12/},
}
```

</details>

#### Yanda Li et al. (2024). *Reason from Fallacy: Enhancing Large Language Models’ Logical Reasoning through Logical Fallacy Understanding*. Findings of the Association for Computational Linguistics: NAACL 2024.

- `doi:10.18653/v1/2024.findings-naacl.192` | aliases: `acl:2024.findings-naacl.192`
- doc_type: `conference` | tier: T4 | tags: fallacy, quality | also in: quality
- [landing](https://aclanthology.org/2024.findings-naacl.192/) | [OA PDF](https://aclanthology.org/2024.findings-naacl.192.pdf) (via acl)
- verified against: acl, bibcorpus:npnkhoi/memefal-paper
- score 0.47 (cites 0.0, cocite 0.2, keyword 1.0, venue 1.0)
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
- score 0.75 (cites 0.0, cocite 1.0, keyword 1.0, venue 1.0)
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

#### Sougata Saha and Rohini Srihari (2024). *Turiya at DialAM-2024: Inference Anchoring Theory Based LLM Parsers*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.13` | aliases: `acl:2024.argmining-1.13`
- doc_type: `workshop` | tier: T4 | tags: dialogue, extraction, formal | also in: dialogue, formal
- [landing](https://aclanthology.org/2024.argmining-1.13/) | [OA PDF](https://aclanthology.org/2024.argmining-1.13.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.6208 (cites 0.0, cocite 0.75, keyword 0.8333, venue 1.0)
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
- score 0.47 (cites 0.0, cocite 0.2, keyword 1.0, venue 1.0)
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

#### Christopher T. Small et al. (2023). *Opportunities and Risks of LLMs for Scalable Deliberation with Polis*. ArXiv.

- `title:8b3f61648db920b2a250f881b93c556a099c2a21`
- doc_type: `preprint` | tier: T4 | tags: dialogue | also in: dialogue
- [landing](https://api.semanticscholar.org/CorpusID:259211996)
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments
- score 0.505 (cites 0.0, cocite 1.0, keyword 0.5, venue 0.2)
- annotation (`grounded_on: none`): No abstract or full text was retrieved for this entry, so nothing about its content is asserted here. It is recorded from bibliographic metadata only (preprint, ArXiv, 2023), verified against 2 sources. For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@misc{small2023opportunit,
  title = {Opportunities and Risks of LLMs for Scalable Deliberation with Polis},
  author = {Christopher T. Small and Ivan Vendrov and Esin Durmus and Hadjar Homaei and Elizabeth Barry and Julien Cornebise and Ted Suzman and Deep Ganguli and Colin Megill},
  year = {2023},
  publisher = {ArXiv},
  url = {https://api.semanticscholar.org/CorpusID:259211996},
}
```

</details>

#### Xiaochuang Han et al. (2023). *Understanding In-Context Learning via Supportive Pretraining Data*. Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/2023.acl-long.708` | aliases: `acl:2023.acl-long.708`
- doc_type: `conference` | tier: T4 | tags: extraction
- [landing](https://aclanthology.org/2023.acl-long.708/) | [OA PDF](https://aclanthology.org/2023.acl-long.708.pdf) (via acl)
- verified against: acl, bibcorpus:BarryMafu/LitLens
- score 0.3733 (cites 0.0, cocite 0.4, keyword 0.3333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In-context learning (ICL) improves language models’ performance on a variety of NLP tasks by simply demonstrating a handful of examples at inference time." "Unlike prior work that explores implicit mechanisms behind ICL, we study ICL via investigating the pretraining data." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{han2023understand,
  title = {Understanding In-Context Learning via Supportive Pretraining Data},
  author = {Xiaochuang Han and Daniel Simig and Todor Mihaylov and Yulia Tsvetkov and Asli Celikyilmaz and Tianlu Wang},
  year = {2023},
  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/2023.acl-long.708},
  url = {https://aclanthology.org/2023.acl-long.708/},
}
```

</details>

## 6.6 Datasets, tools, annotation guidelines (28 entries, quota 30)

### T3 - Dataset / tool / annotation guideline, including the guideline documents themselves.

#### Pedro Ortiz Suarez et al. (2026). *CommonLID: Re-evaluating State-of-the-Art Language Identification Performance on Web Data*. Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/2026.acl-long.1527` | aliases: `acl:2026.acl-long.1527`, `arxiv:2601.18026`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction
- [landing](https://aclanthology.org/2026.acl-long.1527/) | [OA PDF](https://arxiv.org/pdf/2601.18026) (via arxiv)
- verified against: acl, bibcorpus:borgr/publications
- score 0.3033 (cites 0.0, cocite 0.2, keyword 0.3333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we introduce CommonLID, a community-driven, human-annotated LID benchmark for the web domain, covering 109 languages." "We show CommonLID’s value by using it, alongside five other common evaluation sets, to test eight popular LID models." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{suarez2026commonlid,
  title = {CommonLID: Re-evaluating State-of-the-Art Language Identification Performance on Web Data},
  author = {Pedro Ortiz Suarez and Laurie Burchell and Catherine Arnett and Rafael Mosquera and Sara Hincapié Monsalve and Thom Vaughan and Damian Stewart and Malte Ostendorff and Idris Abdulmumin and Vukosi Marivate and Shamsuddeen Hassan Muhammad and Atnafu Lambebo Tonja and Hend Al-Khalifa and Nadia Ghezaiel Hammouda and Verrah Akinyi Otiende and Tack Hwa Wong and Jakhongir Saydaliev and Melika Nobakhtian and Muhammad Ravi Shulthan Habibi and Chalamalasetti Kranti and Carol Muchemi and Khang Nguyen and Faisal Muhammad Adam and Luis Frentzen Salim and Reem Alqifari and Cynthia Jayne Amol and Joseph Marvin Imperial and Ilker Kesen and Ahmad Mustafid and Pavel Stepachev and Leshem Choshen and David Anugraha and Hamada Nayel and Seid Muhie Yimam and Vallerie Alexandra Putra and My Chiffon Nguyen and Azmine Toushik Wasi and Gouthami Vadithya and Rob van der Goot and Lanwenn ar C’horr and Karan Dua and Andrew Yates and Mithil Bangera and Yeshil Bangera and Hitesh Laxmichand Patel and Shu Okabe and Fenal Ashokbhai Ilasariya and Dmitry Gaynullin and Genta Indra Winata and Yiyuan Li and Juan Pablo Martínez and Amit Agarwal and Ikhlasul Akmal Hanif and Raia Abu Ahmad and Esther Adenuga and Filbert Aurelian Tjiaranata and Weerayut Buaphet and Michael Anugraha and Sowmya Vajjala and Benjamin L Rice and Azril Hafizi Amirudin and Jesujoba Oluwadara Alabi and Srikant Panda and Yassine Toughrai and Bruhan Kyomuhendo and Daniel Ruffinelli and Akshata and Manuel Goulão and Ej Zhou and Ingrid Gabriela Franco Ramirez and Cristina Aggazzotti and Konstantin Dobler and Jun Kevin and Quentin Pagès and Nicholas Andrews and Nuhu Ibrahim and Mattes Ruckdeschel and Amr Keleg and Mike Zhang and Casper Rufaro Muziri and Saron Samuel and Sotaro Takeshita and Kun Kerdthaisong and Luca Foppiano and Rasul Dent and Tommaso Green and Ahmad Mustapha Wali and Kamohelo Makaaka and Vicky Feliren and Inshirah Idris and Hande Celikkanat and Abdulhamid Abubakar and Jean Maillard and Benoît Sagot and Thibault Clérice and Kenton Murray and Sarah K. K. Luger},
  year = {2026},
  booktitle = {Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/2026.acl-long.1527},
  url = {https://aclanthology.org/2026.acl-long.1527/},
}
```

</details>

#### Ofir Arviv et al. (2026). *Stop Guessing When to Stop Testing: Efficient Model Evaluation with Just Enough Data*. Findings of the Association for Computational Linguistics: ACL 2026.

- `doi:10.18653/v1/2026.findings-acl.43` | aliases: `acl:2026.findings-acl.43`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction
- [landing](https://aclanthology.org/2026.findings-acl.43/) | [OA PDF](https://aclanthology.org/2026.findings-acl.43.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.2617 (cites 0.0, cocite 0.2, keyword 0.1667, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The inherent rigidity of fixed-size benchmarks makes them an inefficient tool for model evaluation." "We provide an adaptive evaluation framework, that provides a principled way to navigate the trade-off between efficiency and reliability in model evaluation." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{arviv2026stopguess,
  title = {Stop Guessing When to Stop Testing: Efficient Model Evaluation with Just Enough Data},
  author = {Ofir Arviv and Kristjan Greenewald and Yotam Perlitz and Hadar Mulian and Michal Shmueli-Scheuer and Leshem Choshen},
  year = {2026},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2026},
  doi = {10.18653/v1/2026.findings-acl.43},
  url = {https://aclanthology.org/2026.findings-acl.43/},
}
```

</details>

#### Alan Ramponi, Agnese Daffara and Sara Tonelli (2025). *Fine-grained Fallacy Detection with Human Label Variation*. Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers).

- `doi:10.18653/v1/2025.naacl-long.34` | aliases: `acl:2025.naacl-long.34`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction, fallacy, quality | also in: quality
- [landing](https://aclanthology.org/2025.naacl-long.34/) | [OA PDF](https://aclanthology.org/2025.naacl-long.34.pdf) (via acl)
- verified against: acl, bibcorpus:npnkhoi/memefal-paper
- score 0.4492 (cites 0.0, cocite 0.2, keyword 0.9167, venue 1.0)
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

#### Shivalika Singh et al. (2025). *Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation*. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/2025.acl-long.919` | aliases: `acl:2025.acl-long.919`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/2025.acl-long.919/) | [OA PDF](https://aclanthology.org/2025.acl-long.919.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.3033 (cites 0.0, cocite 0.2, keyword 0.3333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Reliable multilingual evaluation is difficult, and culturally appropriate evaluation is even harder to achieve.A common practice to fill this gap is to machine-translate English evaluation sets." "In this work, we highlight the extent and impact of these biases and present a multilingual evaluation framework that aims to mitigate them through improved translations and annotation practices.Through a large-scale study involving professional and community translators and annotators, we show that state-of-the-art m…" For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{singh2025globalmml,
  title = {Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation},
  author = {Shivalika Singh and Angelika Romanou and Clémentine Fourrier and David Ifeoluwa Adelani and Jian Gang Ngui and Daniel Vila-Suero and Peerat Limkonchotiwat and Kelly Marchisio and Wei Qi Leong and Yosephine Susanto and Raymond Ng and Shayne Longpre and Sebastian Ruder and Wei-Yin Ko and Antoine Bosselut and Alice Oh and Andre Martins and Leshem Choshen and Daphne Ippolito and Enzo Ferrante and Marzieh Fadaee and Beyza Ermis and Sara Hooker},
  year = {2025},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/2025.acl-long.919},
  url = {https://aclanthology.org/2025.acl-long.919/},
}
```

</details>

#### Afra Feyza Akyürek et al. (2024). *Deductive Closure Training of Language Models for Coherence, Accuracy, and Updatability*. Findings of the Association for Computational Linguistics: ACL 2024.

- `doi:10.18653/v1/2024.findings-acl.584` | aliases: `acl:2024.findings-acl.584`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/2024.findings-acl.584/) | [OA PDF](https://aclanthology.org/2024.findings-acl.584.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.2825 (cites 0.0, cocite 0.2, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We present a method called Deductive Closure Training (DCT) that uses LMs themselves to identify implications of (and contradictions within) the text that they generate, yielding an efficient self-supervised procedure for improving LM factuality." "Across the CREAK, MQuAKE, and Reversal Curse datasets, supervised DCT improves LM fact verification and text generation accuracy by 3-26%; on CREAK, fully unsupervised DCT improves verification accuracy by 12%." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{akyrek2024deductive,
  title = {Deductive Closure Training of Language Models for Coherence, Accuracy, and Updatability},
  author = {Afra Feyza Akyürek and Ekin Akyürek and Leshem Choshen and Derry Wijaya and Jacob Andreas},
  year = {2024},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},
  doi = {10.18653/v1/2024.findings-acl.584},
  url = {https://aclanthology.org/2024.findings-acl.584/},
}
```

</details>

#### Chadi Helwe et al. (2024). *MAFALDA: A Benchmark and Comprehensive Study of Fallacy Detection and Classification*. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers).

- `doi:10.18653/v1/2024.naacl-long.270` | aliases: `acl:2024.naacl-long.270`, `arxiv:2311.09761`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction, fallacy, quality | also in: quality, llm
- [landing](https://aclanthology.org/2024.naacl-long.270/) | [OA PDF](https://arxiv.org/pdf/2311.09761) (via arxiv)
- verified against: acl, bibcorpus:npnkhoi/memefal-paper | note: bibcorpus:lefteriskat/Logical-Fallacy-Detection-Using-LLMs: venue mismatch ('Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human L…
- score 0.4283 (cites 0.0, cocite 0.2, keyword 0.8333, venue 1.0)
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

#### Elron Bandel et al. (2024). *Unitxt: Flexible, Shareable and Reusable Data Preparation and Evaluation for Generative AI*. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 3: System Demonstrations).

- `doi:10.18653/v1/2024.naacl-demo.21` | aliases: `acl:2024.naacl-demo.21`
- doc_type: `conference` | tier: T3 | tags: dataset | also in: llm
- [landing](https://aclanthology.org/2024.naacl-demo.21/) | [OA PDF](https://aclanthology.org/2024.naacl-demo.21.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.3242 (cites 0.0, cocite 0.2, keyword 0.4167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In the dynamic landscape of generative NLP, traditional text processing pipelines limit research flexibility and reproducibility, as they are tailored to specific dataset, task, and model combinations." "The escalating complexity, involving system prompts, model-specific formats, instructions, and more, calls for a shift to a structured, modular, and customizable solution.Addressing this need, we present Unitxt, an innovative library for customizable textual data preparation and evaluation tailored to generative langu…" For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{bandel2024unitxtfl,
  title = {Unitxt: Flexible, Shareable and Reusable Data Preparation and Evaluation for Generative AI},
  author = {Elron Bandel and Yotam Perlitz and Elad Venezian and Roni Friedman and Ofir Arviv and Matan Orbach and Shachar Don-Yehiya and Dafna Sheinwald and Ariel Gera and Leshem Choshen and Michal Shmueli-Scheuer and Yoav Katz},
  year = {2024},
  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 3: System Demonstrations)},
  doi = {10.18653/v1/2024.naacl-demo.21},
  url = {https://aclanthology.org/2024.naacl-demo.21/},
}
```

</details>

#### Shachar Don-Yehiya et al. (2023). *ColD Fusion: Collaborative Descent for Distributed Multitask Finetuning*. Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/2023.acl-long.46` | aliases: `acl:2023.acl-long.46`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/2023.acl-long.46/) | [OA PDF](https://aclanthology.org/2023.acl-long.46.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.3242 (cites 0.0, cocite 0.2, keyword 0.4167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we propose ColD Fusion, a method that provides the benefits of multitask learning but leverages distributed computation and requires limited communication and no sharing of data." "We show that ColD Fusion yields comparable benefits to multitask training by producing a model that (a) attains strong performance on all of the datasets it was multitask trained on and (b) is a better starting point for finetuning on unseen datasets." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{donyehiya2023coldfusio,
  title = {ColD Fusion: Collaborative Descent for Distributed Multitask Finetuning},
  author = {Shachar Don-Yehiya and Elad Venezian and Colin Raffel and Noam Slonim and Leshem Choshen},
  year = {2023},
  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/2023.acl-long.46},
  url = {https://aclanthology.org/2023.acl-long.46/},
}
```

</details>

#### Ella Neeman et al. (2023). *DisentQA: Disentangling Parametric and Contextual Knowledge with Counterfactual Question Answering*. Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/2023.acl-long.559` | aliases: `acl:2023.acl-long.559`
- doc_type: `conference` | tier: T3 | tags: dataset | also in: llm
- [landing](https://aclanthology.org/2023.acl-long.559/) | [OA PDF](https://aclanthology.org/2023.acl-long.559.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.2825 (cites 0.0, cocite 0.2, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this work, we propose a new paradigm in which QA models are trained to disentangle the two sources of knowledge." "Using counterfactual data augmentation, we introduce a model that predicts two answers for a given question: one based on given contextual knowledge and one based on parametric knowledge." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{neeman2023disentqa,
  title = {DisentQA: Disentangling Parametric and Contextual Knowledge with Counterfactual Question Answering},
  author = {Ella Neeman and Roee Aharoni and Or Honovich and Leshem Choshen and Idan Szpektor and Omri Abend},
  year = {2023},
  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/2023.acl-long.559},
  url = {https://aclanthology.org/2023.acl-long.559/},
}
```

</details>

#### Abelardo Carlos Martínez Lorenzo, Marco Maru and Roberto Navigli (2022). *Fully-Semantic Parsing and Generation: the BabelNet Meaning Representation*. Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/2022.acl-long.121` | aliases: `acl:2022.acl-long.121`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction
- [landing](https://aclanthology.org/2022.acl-long.121/) | [OA PDF](https://aclanthology.org/2022.acl-long.121.pdf) (via acl)
- verified against: acl, bibcorpus:Danysan1/ai-unibo-nlp-project
- score 0.3658 (cites 0.0, cocite 0.2, keyword 0.5833, venue 1.0)
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
- score 0.2825 (cites 0.0, cocite 0.2, keyword 0.25, venue 1.0)
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
- score 0.55 (cites 0.0, cocite 1.0, keyword 0.5, venue 0.5)
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

#### Aviv Slobodkin, Leshem Choshen and Omri Abend (2021). *Mediators in Determining what Processing BERT Performs First*. Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.

- `doi:10.18653/v1/2021.naacl-main.8` | aliases: `acl:2021.naacl-main.8`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/2021.naacl-main.8/) | [OA PDF](https://aclanthology.org/2021.naacl-main.8.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.2825 (cites 0.0, cocite 0.2, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We show that not controlling for context length may lead to contradictory conclusions as to the localization patterns of the network, depending on the distribution of the probing dataset." "Indeed, when probing BERT with seven tasks, we find that it is possible to get 196 different rankings between them when manipulating the distribution of context lengths in the probing dataset." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{slobodkin2021mediators,
  title = {Mediators in Determining what Processing BERT Performs First},
  author = {Aviv Slobodkin and Leshem Choshen and Omri Abend},
  year = {2021},
  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  doi = {10.18653/v1/2021.naacl-main.8},
  url = {https://aclanthology.org/2021.naacl-main.8/},
}
```

</details>

#### Or Honovich et al. (2021). *Q^{2}: Evaluating Factual Consistency in Knowledge-Grounded Dialogues via Question Generation and Question Answering*. Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2021.emnlp-main.619` | aliases: `acl:2021.emnlp-main.619`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue
- [landing](https://aclanthology.org/2021.emnlp-main.619/) | [OA PDF](https://aclanthology.org/2021.emnlp-main.619.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications
- score 0.2825 (cites 0.0, cocite 0.2, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Inspired by recent work on evaluating factual consistency in abstractive summarization, we propose an automatic evaluation metric for factual consistency in knowledge-grounded dialogue using automatic question generation and question answering." "To foster proper evaluation, we curate a novel dataset of dialogue system outputs for the Wizard-of-Wikipedia dataset, manually annotated for factual consistency." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{honovich2021qeva,
  title = {Q^{2}: Evaluating Factual Consistency in Knowledge-Grounded Dialogues via Question Generation and Question Answering},
  author = {Or Honovich and Leshem Choshen and Roee Aharoni and Ella Neeman and Idan Szpektor and Omri Abend},
  year = {2021},
  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
  doi = {10.18653/v1/2021.emnlp-main.619},
  url = {https://aclanthology.org/2021.emnlp-main.619/},
}
```

</details>

#### Dimitar Dimitrov et al. (2021). *SemEval-2021 Task 6: Detection of Persuasion Techniques in Texts and Images*. Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021).

- `doi:10.18653/v1/2021.semeval-1.7` | aliases: `acl:2021.semeval-1.7`
- doc_type: `workshop` | tier: T3 | tags: dataset, dialogue, extraction
- [landing](https://aclanthology.org/2021.semeval-1.7/) | [OA PDF](https://aclanthology.org/2021.semeval-1.7.pdf) (via acl)
- verified against: acl, bibcorpus:allenai/ir_datasets, bibcorpus:npnkhoi/memefal-paper
- score 0.2775 (cites 0.0, cocite 0.4, keyword 0.25, venue 0.5)
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
- score 0.27 (cites 0.0, cocite 0.2, keyword 0.5, venue 0.5)
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
- score 0.3658 (cites 0.0, cocite 0.2, keyword 0.5833, venue 1.0)
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

#### Eyal Shnarch et al. (2020). *Unsupervised Expressive Rules Provide Explainability and Assist Human Experts Grasping New Domains*. Findings of the Association for Computational Linguistics: EMNLP 2020.

- `doi:10.18653/v1/2020.findings-emnlp.243` | aliases: `acl:2020.findings-emnlp.243`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/2020.findings-emnlp.243/) | [OA PDF](https://aclanthology.org/2020.findings-emnlp.243.pdf) (via acl)
- verified against: acl, bibcorpus:borgr/publications, bibcorpus:ljvmiranda921/ljvmiranda921.github.io
- score 0.2825 (cites 0.0, cocite 0.2, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Aiming to assist domain experts in their first steps into a new task over a new corpus, we present an unsupervised approach to reveal complex rules which cluster the unexplored corpus by its prominent categories (or facets)." "We present an extensive evaluation of the usefulness of these rules in identifying target categories, as well as a user study which assesses their interpretability." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{shnarch2020unsupervis,
  title = {Unsupervised Expressive Rules Provide Explainability and Assist Human Experts Grasping New Domains},
  author = {Eyal Shnarch and Leshem Choshen and Guy Moshkowich and Ranit Aharonov and Noam Slonim},
  year = {2020},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2020},
  doi = {10.18653/v1/2020.findings-emnlp.243},
  url = {https://aclanthology.org/2020.findings-emnlp.243/},
}
```

</details>

#### Yamen Ajjour et al. (2019). *Data Acquisition for Argument Search: The args.me corpus*. 42nd German Conference on Artificial Intelligence (KI 2019).

- `doi:10.1007/978-3-030-30179-8_4`
- doc_type: `conference` | tier: T3 | tags: dataset
- no URL recorded
- verified against: bibcorpus:CogSciPrag/project_ideas, bibcorpus:allenai/ir_datasets
- score 0.68 (cites 0.0, cocite 0.8, keyword 1.0, venue 1.0)
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

#### Joonsuk Park and Claire Cardie (2018). *A Corpus of eRulemaking User Comments for Measuring Evaluability of Arguments*. Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018).

- `title:fb5f11e278c8bd8c14ae4a205093409670e5bba3` | aliases: `acl:L18-1257`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/L18-1257/) | [OA PDF](https://aclanthology.org/L18-1257.pdf) (via acl)
- verified against: acl, bibcorpus:harisont/biboba
- score 0.3658 (cites 0.0, cocite 0.2, keyword 0.5833, venue 1.0)
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
- score 0.3525 (cites 0.0, cocite 0.4, keyword 0.25, venue 1.0)
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
- score 0.2775 (cites 0.0, cocite 0.4, keyword 0.25, venue 0.5)
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
- score 0.2775 (cites 0.0, cocite 0.4, keyword 0.25, venue 0.5)
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
- score 0.625 (cites 0.0, cocite 1.0, keyword 0.5, venue 1.0)
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
- score 0.4925 (cites 0.0, cocite 0.8, keyword 0.25, venue 1.0)
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

#### Danqi Chen, Adam Fisch, Jason Weston and Antoine Bordes (2017). *Reading Wikipedia to Answer Open-Domain Questions*. Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/p17-1171` | aliases: `acl:P17-1171`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/P17-1171/) | [OA PDF](https://aclanthology.org/P17-1171.pdf) (via acl)
- verified against: acl, bibcorpus:BarryMafu/LitLens
- score 0.3525 (cites 0.0, cocite 0.4, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This task of machine reading at scale combines the challenges of document retrieval (finding the relevant articles) with that of machine comprehension of text (identifying the answer spans from those articles)." "Our experiments on multiple existing QA datasets indicate that (1) both modules are highly competitive with respect to existing counterparts and (2) multitask learning using distant supervision on their combination is an effective complete system on this challenging task." For a debate-transcript argument database it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{chen2017readingwi,
  title = {Reading Wikipedia to Answer Open-Domain Questions},
  author = {Danqi Chen and Adam Fisch and Jason Weston and Antoine Bordes},
  year = {2017},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/p17-1171},
  url = {https://aclanthology.org/P17-1171/},
}
```

</details>

#### Rob Abbott, Brian Ecker, Pranav Anand and Marilyn Walker (2016). *Internet Argument Corpus 2.0: An SQL schema for Dialogic Social Media and the Corpora to go with it*. Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC'16).

- `title:5fdf28d47fecc818952baba478a8bd9d1b71a516` | aliases: `acl:L16-1704`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue | also in: dialogue
- [landing](https://aclanthology.org/L16-1704/) | [OA PDF](https://aclanthology.org/L16-1704.pdf) (via acl)
- verified against: acl, bibcorpus:IKMLab/argalign1
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

#### Samuel R. Bowman, Gabor Angeli, Christopher Potts and Christopher D. Manning (2015). *A large annotated corpus for learning natural language inference*. Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/d15-1075` | aliases: `acl:D15-1075`, `arxiv:1508.05326`
- doc_type: `conference` | tier: T3 | tags: dataset
- [landing](https://aclanthology.org/D15-1075/) | [OA PDF](https://arxiv.org/pdf/1508.05326) (via arxiv)
- verified against: acl, bibcorpus:danny-v-nguyen/thesis | note: bibcorpus:IKMLab/arct2: venue mismatch ('Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing' vs 'CoRR')
- score 0.61 (cites 0.0, cocite 0.6, keyword 1.0, venue 1.0)
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
