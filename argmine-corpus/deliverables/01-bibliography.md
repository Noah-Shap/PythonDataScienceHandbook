# 01 - Annotated bibliography

140 verified entries, grouped by area and then by tier. Every entry here agreed across at least two independent metadata sources; anything that did not is in `99-unverified-and-rejected.md`. Each annotation says which retrieved text it was written from (`grounded_on`), and quotes that text rather than paraphrasing it from outside knowledge.

Generated 2026-09-16T03:24:36+00:00 | criteria_version 1 | cap 250

**Added in the latest run (250):** `doi:10.1007/978-0-387-98197-0_19`, `doi:10.1007/978-3-642-23963-2_10`, `doi:10.1007/s10458-009-9116-7`, `doi:10.1007/s10506-010-9104-x`, `doi:10.1007/s10579-019-09446-8`, `doi:10.1007/s13222-020-00347-7`, `doi:10.1016/0004-3702(94)00041-x`, `doi:10.1016/j.artint.2007.04.010`, `doi:10.1016/j.artint.2015.12.004`, `doi:10.1017/cbo9780511802034`, `doi:10.1017/s0269888906001044`, `doi:10.1017/s0269888911000166`, `doi:10.1038/s41586-021-03215-w`, `doi:10.1057/palgrave.ap.5500115`, `doi:10.1080/19462160903564592`, `doi:10.1080/19462166.2010.486479`, `doi:10.1080/19462166.2012.661766`, `doi:10.1080/19462166.2013.862303`, `doi:10.1080/19462166.2013.869764`, `doi:10.1080/19462166.2013.869766`, `doi:10.1080/19462166.2013.869767`, `doi:10.1080/19462166.2013.869878`, `doi:10.1080/19462166.2014.1001790`, `doi:10.1093/logcom/14.5.675`, `doi:10.1093/oso/9780198862536.003.0005`, `doi:10.1111/coin.12111`, `doi:10.1145/2850417`, `doi:10.1145/2872427.2883081`, `doi:10.1145/3308558.3314127`, `doi:10.1145/3331184.3331327`, `doi:10.1162/coli_a_00276`, `doi:10.1162/coli_a_00295`, `doi:10.1162/coli_a_00364`, `doi:10.1162/coli_a_00502`, `doi:10.1162/coli_a_00553`, `doi:10.1162/tacl_a_00481`, `doi:10.1177/1461444807081230`, `doi:10.1609/aaai.v34i05.6270`, `doi:10.1609/aaai.v34i05.6285`, `doi:10.18653/v1/2020.acl-main.298` ...

## 6.1 Formal foundations (27 entries, quota 30)

### T1 - Foundational / survey. Read in full: theory anchors, major surveys, canonical papers.

#### John Lawrence and Chris Reed (2019). *Argument Mining: A Survey*. Computational Linguistics.

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
  journal = {Computational Linguistics},
  doi = {10.1162/coli_a_00364},
  url = {https://aclanthology.org/J19-4006/},
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

#### Pietro Baroni, Martin Caminada and Massimiliano Giacomin (2011). *An introduction to argumentation semantics*. The Knowledge Engineering Review.

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
  journal = {The Knowledge Engineering Review},
  doi = {10.1017/s0269888911000166},
}
```

</details>

#### Douglas Walton, Christopher Reed and Fabrizio Macagno (2008). *Argumentation Schemes*. Cambridge University Press.

- `doi:10.1017/cbo9780511802034`
- doc_type: `book` | tier: T1 | tags: formal, schemes
- [landing](https://www.cambridge.org/core/product/identifier/9780511802034/type/book)
- verified against: bibcorpus:KWARC/bibs, bibcorpus:RicoStaedeli/NLP2025_CQG, bibcorpus:carneades/carneades-3, bibcorpus:davidar/dblp.yaml, bibcorpus:slatex/sTeX
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This book provides a systematic analysis of many common argumentation schemes and a compendium of 96 schemes." "The study of these schemes, or forms of argument that capture stereotypical patterns of human reasoning, is at the core of argumentation research." For a debate-transcript argument database it supplies argumentation-scheme and critical-question structure, which is how stored inferences can be typed rather than left as untyped support links; and it supplies the formal semantics for deciding what stands once arguments and attacks are stored.

<details><summary>BibTeX</summary>

```bibtex
@book{walton2008argumentat,
  title = {Argumentation Schemes},
  author = {Douglas Walton and Christopher Reed and Fabrizio Macagno},
  year = {2008},
  publisher = {Cambridge University Press},
  doi = {10.1017/cbo9780511802034},
  url = {https://www.cambridge.org/core/product/identifier/9780511802034/type/book},
}
```

</details>

#### Carlos Chesñevar et al. (2006). *Towards an Argument Interchange Format*. The Knowledge Engineering Review.

- `doi:10.1017/s0269888906001044`
- doc_type: `journal` | tier: T1 | tags: formal
- [landing](http://dx.doi.org/10.1017/s0269888906001044)
- verified against: bibcorpus:KWARC/bibs, bibcorpus:davidar/dblp.yaml, bibcorpus:slatex/sTeX
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### P.M. Dung (1995). *On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Logic Programming and n-Person Games*. Artificial Intelligence.

- `doi:10.1016/0004-3702(94)00041-x`
- doc_type: `journal` | tier: T1 | tags: formal
- [landing](https://www.sciencedirect.com/science/article/pii/000437029400041X)
- verified against: bibcorpus:KWARC/bibs, bibcorpus:aig-hagen/aig-templates, bibcorpus:davidar/dblp.yaml, bibcorpus:lmlearning/AFGraphLib, bibcorpus:ochyai/open-japan-politech-platform, bibcorpus:p4s3r0/argumentation-framework-clustering, bibcorpus:slatex/sTeX, bibcorpus:smucclaw/complaw, bibcorpus:ttmassa/ter
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

#### Stephen E. Toulmin (1960). *The uses of argument*. Cambridge University Press.

- `title:df299e3284c272f02cac357fba80718526676f2a`
- doc_type: `conference` | tier: T1 | tags: formal
- [landing](https://api.semanticscholar.org/CorpusID:120694372)
- verified against: bibcorpus:IKMLab/arct2, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive | note: bibcorpus:CogSciPrag/project_ideas: year mismatch (1958 vs 1960)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{toulmin1960theuseso,
  title = {The uses of argument},
  author = {Stephen E. Toulmin},
  year = {1960},
  booktitle = {Cambridge University Press},
  url = {https://api.semanticscholar.org/CorpusID:120694372},
}
```

</details>

### T2 - Core method. Defines a task formulation, model, or evaluation still in use.

#### Pietro Baroni, Dov Gabbay, Massimiliano Giacomin and Leendert van der Torre (2018). *Handbook of Formal Argumentation*. College Publications.

- `title:c01257ffd78768bab2a908ba8509b177ebd2f015`
- doc_type: `book` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:KWARC/bibs, bibcorpus:lmlearning/AFGraphLib, bibcorpus:p4s3r0/argumentation-framework-clustering, bibcorpus:slatex/sTeX | note: author list missing from one source; venue not corroborated by both sources
- score 0.35 (cites 0.0, cocite 0.4286, keyword 0.5, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Fabrizio Macagno, Douglas Walton and Chris Reed (2017). *Argumentation Schemes. History, Classifications, and Computational Applications*. IFCoLog Journal of Logics and Their Applications.

- `title:156478672e00c4f4e6cb6079e97120915f66c518`
- doc_type: `journal` | tier: T2 | tags: formal, schemes
- [landing](http://dougwalton.ca/papers in pdf/17IFColog SCHEMES.pdf)
- verified against: bibcorpus:KWARC/bibs, bibcorpus:slatex/sTeX
- score 0.2 (cites 0.0, cocite 0.0, keyword 0.5, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Toshiko Wakaki (2017). *Assumption-Based Argumentation Equipped with Preferences and its Application to Decision Making, Practical Reasoning, and Epistemic Reasoning*. Computational Intelligence.

- `doi:10.1111/coin.12111`
- doc_type: `journal` | tier: T2 | tags: formal
- [landing](https://onlinelibrary.wiley.com/doi/abs/10.1111/coin.12111)
- verified against: bibcorpus:KWARC/bibs, bibcorpus:slatex/sTeX
- score 0.2 (cites 0.0, cocite 0.0, keyword 0.5, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@article{wakaki2017assumption,
  title = {Assumption-Based Argumentation Equipped with Preferences and its Application to Decision Making, Practical Reasoning, and Epistemic Reasoning},
  author = {Toshiko Wakaki},
  year = {2017},
  journal = {Computational Intelligence},
  doi = {10.1111/coin.12111},
  url = {https://onlinelibrary.wiley.com/doi/abs/10.1111/coin.12111},
}
```

</details>

#### Kristijonas Cyras, Xiuyi Fan, Claudia Schulz and Francesca Toni (2017). *Assumption-based argumentation: Disputes, explanations, preferences*. IFCoLog Journal of Logics and Their Applications.

- `title:b2c0b65c9c0b6c67d10d97e391b6302f31b66c93`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:KWARC/bibs, bibcorpus:slatex/sTeX
- score 0.2 (cites 0.0, cocite 0.0, keyword 0.5, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@article{cyras2017assumption,
  title = {Assumption-based argumentation: Disputes, explanations, preferences},
  author = {Kristijonas Cyras and Xiuyi Fan and Claudia Schulz and Francesca Toni},
  year = {2017},
  journal = {IFCoLog Journal of Logics and Their Applications},
}
```

</details>

#### Elise Bonzon, Jérôme Delobelle, Sébastien Konieczny and Nicolas Maudet (2016). *A Comparative Study of Ranking-Based Semantics for Abstract Argumentation*. AAAI.

- `title:177275e11cfa165d7647e57e9c0a2506d322d7b8`
- doc_type: `conference` | tier: T2 | tags: formal
- [landing](https://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/viewPaper/12465)
- verified against: bibcorpus:lihebi/biber-dist, bibcorpus:lmlearning/AFGraphLib
- score 0.275 (cites 0.0, cocite 0.0, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Argumentation is a process of evaluating and comparing a set of arguments." "This is what we propose in this work." For a debate-transcript argument database it supplies the formal semantics for deciding what stands once arguments and attacks are stored, so strength is computed rather than asserted.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{bonzon2016acomparat,
  title = {A Comparative Study of Ranking-Based Semantics for Abstract Argumentation},
  author = {Elise Bonzon and Jérôme Delobelle and Sébastien Konieczny and Nicolas Maudet},
  year = {2016},
  booktitle = {AAAI},
  url = {https://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/viewPaper/12465},
}
```

</details>

#### Robert Craven and Francesca Toni (2016). *Argument Graphs and Assumption-based Argumentation*. Artif. Intell..

- `doi:10.1016/j.artint.2015.12.004`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:KWARC/bibs, bibcorpus:slatex/sTeX
- score 0.2833 (cites 0.0, cocite 0.0, keyword 0.8333, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@article{craven2016argumentg,
  title = {Argument Graphs and Assumption-based Argumentation},
  author = {Robert Craven and Francesca Toni},
  year = {2016},
  journal = {Artif. Intell.},
  doi = {10.1016/j.artint.2015.12.004},
}
```

</details>

#### Pavithra Rajendran, Danushka Bollegala and Simon Parsons (2016). *Contextual stance classification of opinions: A step towards enthymeme reconstruction in online reviews*. Proceedings of the Third Workshop on Argument Mining (ArgMining2016).

- `doi:10.18653/v1/w16-2804` | aliases: `acl:W16-2804`
- doc_type: `workshop` | tier: T2 | tags: extraction, formal, quality | also in: quality
- [landing](https://aclanthology.org/W16-2804/) | [OA PDF](https://aclanthology.org/W16-2804.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.2333 (cites 0.0, cocite 0.0, keyword 0.3333, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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
- score 0.3875 (cites 0.0, cocite 0.1429, keyword 0.75, venue 1.0)
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

#### Claudia Schulz 0001 (2015). *Graphical Representation of Assumption-Based Argumentation*. AAAI.

- `title:68b73e54770197cc7438c73cef166bb69e8041e5`
- doc_type: `conference` | tier: T2 | tags: formal
- [landing](http://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/view/9825)
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:lihebi/biber-dist | note: author order differs (0001 / schulz)
- score 0.275 (cites 0.0, cocite 0.0, keyword 0.5, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{anon2015graphical,
  title = {Graphical Representation of Assumption-Based Argumentation},
  author = {Claudia Schulz 0001},
  year = {2015},
  booktitle = {AAAI},
  url = {http://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/view/9825},
}
```

</details>

#### Claudia Schulz 0001 and Francesca Toni (2015). *Logic Programming in Assumption-Based Argumentation Revisited - Semantics and Graphical Representation*. AAAI.

- `title:853f7d761baa66348c962ef162f1c92ee39f9ed0`
- doc_type: `conference` | tier: T2 | tags: formal
- [landing](http://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/view/9827)
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:lihebi/biber-dist | note: author order differs (0001 / schulz)
- score 0.275 (cites 0.0, cocite 0.0, keyword 0.5, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{anon2015logicprog,
  title = {Logic Programming in Assumption-Based Argumentation Revisited - Semantics and Graphical Representation},
  author = {Claudia Schulz 0001 and Francesca Toni},
  year = {2015},
  booktitle = {AAAI},
  url = {http://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/view/9827},
}
```

</details>

#### Francesca Toni (2014). *A tutorial on assumption-based argumentation*. Argument & Computation.

- `doi:10.1080/19462166.2013.869878`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:p4s3r0/argumentation-framework-clustering
- score 0.475 (cites 0.0, cocite 0.5714, keyword 0.5, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Alejandro J. García and Guillermo R. Simari (2014). *Defeasible logic programming: DeLP-servers, contextual queries, and explanations for answers*. Argument & Computation.

- `doi:10.1080/19462166.2013.869767`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:KWARC/bibs, bibcorpus:davidar/dblp.yaml, bibcorpus:slatex/sTeX
- score 0.4083 (cites 0.0, cocite 0.1429, keyword 0.8333, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Philippe Besnard et al. (2014). *Introduction to structured argumentation*. Argument & Computation.

- `doi:10.1080/19462166.2013.869764`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:KWARC/bibs, bibcorpus:davidar/dblp.yaml, bibcorpus:slatex/sTeX
- score 0.325 (cites 0.0, cocite 0.1429, keyword 0.5, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Xiuyi Fan and Francesca Toni (2011). *Assumption-Based Argumentation Dialogues*. IJCAI.

- `title:7acff355fd26bb28fda645b20618cd58d743b7ae`
- doc_type: `conference` | tier: T2 | tags: dialogue, formal
- [landing](http://ijcai.org/papers11/Papers/IJCAI11-044.pdf)
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:lihebi/biber-dist
- score 0.275 (cites 0.0, cocite 0.0, keyword 0.5, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{fan2011assumption,
  title = {Assumption-Based Argumentation Dialogues},
  author = {Xiuyi Fan and Francesca Toni},
  year = {2011},
  booktitle = {IJCAI},
  url = {http://ijcai.org/papers11/Papers/IJCAI11-044.pdf},
}
```

</details>

#### Serena Villata, Guido Boella and Leendert W. N. van der Torre (2011). *Attack Semantics for Abstract Argumentation*. IJCAI.

- `title:220b9b7c2eaa45b1fcb78e944014f83ce9be3f5d`
- doc_type: `conference` | tier: T2 | tags: formal
- [landing](http://ijcai.org/papers11/Papers/IJCAI11-076.pdf)
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:lihebi/biber-dist
- score 0.275 (cites 0.0, cocite 0.0, keyword 0.5, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{villata2011attacksem,
  title = {Attack Semantics for Abstract Argumentation},
  author = {Serena Villata and Guido Boella and Leendert W. N. van der Torre},
  year = {2011},
  booktitle = {IJCAI},
  url = {http://ijcai.org/papers11/Papers/IJCAI11-076.pdf},
}
```

</details>

#### Martin Caminada and Gabriella Pigozzi (2011). *On judgment aggregation in abstract argumentation*. Autonomous Agents and Multi-Agent Systems.

- `doi:10.1007/s10458-009-9116-7`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:ttmassa/ter
- score 0.3 (cites 0.0, cocite 0.2857, keyword 0.5, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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
- score 0.375 (cites 0.0, cocite 0.2857, keyword 0.5, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Henry Prakken (2010). *An abstract framework for argumentation with structured arguments*. Argument & Computation.

- `doi:10.1080/19462160903564592`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:carneades/carneades-3, bibcorpus:davidar/dblp.yaml
- score 0.4375 (cites 0.0, cocite 0.2857, keyword 0.75, venue 1.0)
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
- score 0.475 (cites 0.0, cocite 0.5714, keyword 0.5, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Guido Governatori, Michael J. Maher, Grigoris Antoniou and David Billington (2004). *Argumentation Semantics for Defeasible Logic*. J. Log. Comput..

- `doi:10.1093/logcom/14.5.675`
- doc_type: `journal` | tier: T2 | tags: formal
- no URL recorded
- verified against: bibcorpus:davidar/dblp.yaml, bibcorpus:p4s3r0/argumentation-framework-clustering
- score 0.35 (cites 0.0, cocite 0.4286, keyword 0.5, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@article{governatori2004argumentat,
  title = {Argumentation Semantics for Defeasible Logic},
  author = {Guido Governatori and Michael J. Maher and Grigoris Antoniou and David Billington},
  year = {2004},
  journal = {J. Log. Comput.},
  doi = {10.1093/logcom/14.5.675},
}
```

</details>

## 6.2 Argument mining (NLP) (54 entries, quota 60)

### T1 - Foundational / survey. Read in full: theory anchors, major surveys, canonical papers.

#### Eva Maria Vecchi, Neele Falk, Iman Jundi and Gabriella Lapesa (2021). *Towards Argument Mining for Social Good: A Survey*. Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers).

- `doi:10.18653/v1/2021.acl-long.107` | aliases: `acl:2021.acl-long.107`
- doc_type: `conference` | tier: T1 | tags: dialogue, extraction
- [landing](https://aclanthology.org/2021.acl-long.107/) | [OA PDF](https://aclanthology.org/2021.acl-long.107.pdf) (via acl)
- verified against: acl, bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments, bibcorpus:m0re4u/paper-database
- score 0.5458 (cites 0.0, cocite 0.7143, keyword 0.5833, venue 1.0)
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
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Marco Lippi and Paolo Torroni (2016). *Argumentation Mining: State of the Art and Emerging Trends*. ACM Transactions on Internet Technology (TOIT).

- `doi:10.1145/2850417` | aliases: `doi:10.1145/2897213`
- doc_type: `journal` | tier: T1 | tags: extraction
- [landing](https://doi.org/10.1145/2850417)
- verified against: bibcorpus:CogSciPrag/project_ideas, bibcorpus:Danysan1/ai-unibo-nlp-project, bibcorpus:IKMLab/arct2, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive, bibcorpus:m0re4u/paper-database, bibcorpus:nshkrdotcom/research_papers
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Argumentation mining aims at automatically extracting structured arguments from unstructured textual documents." "In this survey article, we introduce argumentation models and methods, review existing systems and applications, and discuss challenges and perspectives of this exciting new research area." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@article{lippi2016argumentat,
  title = {Argumentation Mining: State of the Art and Emerging Trends},
  author = {Marco Lippi and Paolo Torroni},
  year = {2016},
  journal = {ACM Transactions on Internet Technology (TOIT)},
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
- score 0.5042 (cites 0.0, cocite 0.5714, keyword 0.9167, venue 0.5)
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

### T2 - Core method. Defines a task formulation, model, or evaluation still in use.

#### Eleonora Mancini, Federico Ruggeri, Andrea Galassi and Paolo Torroni (2022). *Multimodal Argument Mining: A Case Study in Political Debates*. Proceedings of the 9th Workshop on Argument Mining.

- `title:4981c968e6b2dde7090be6cc1cd312d1d74031a3` | aliases: `acl:2022.argmining-1.15`
- doc_type: `workshop` | tier: T2 | tags: dialogue, extraction | also in: dialogue
- [landing](https://aclanthology.org/2022.argmining-1.15/) | [OA PDF](https://aclanthology.org/2022.argmining-1.15.pdf) (via acl)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive
- score 0.525 (cites 0.0, cocite 0.7143, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We propose a study on multimodal argument mining in the domain of political debates." "Our results provide interesting indications about future directions in this important domain." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{mancini2022multimodal,
  title = {Multimodal Argument Mining: A Case Study in Political Debates},
  author = {Eleonora Mancini and Federico Ruggeri and Andrea Galassi and Paolo Torroni},
  year = {2022},
  booktitle = {Proceedings of the 9th Workshop on Argument Mining},
  url = {https://aclanthology.org/2022.argmining-1.15/},
}
```

</details>

#### Terne Sasha Thorn Jakobsen, Maria Barrett, Anders Sogaard and David Lassen (2022). *The Sensitivity of Annotator Bias to Task Definitions in Argument Mining*. Proceedings of the 16th Linguistic Annotation Workshop (LAW-XVI) within LREC2022.

- `title:61fadcac208eb3f58c0f9834cf909c5aaa5c7972` | aliases: `acl:2022.law-1.6`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/2022.law-1.6/) | [OA PDF](https://aclanthology.org/2022.law-1.6.pdf) (via acl)
- verified against: acl, bibcorpus:ljvmiranda921/ljvmiranda921.github.io
- score 0.325 (cites 0.0, cocite 0.1429, keyword 0.5, venue 1.0)
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
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive, bibcorpus:mystreamer/lt2326-final-project
- score 0.7083 (cites 0.0, cocite 1.0, keyword 0.8333, venue 1.0)
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

#### Johannes Kiesel, Nico Reichenbach, Benno Stein and Martin Potthast (2021). *Image Retrieval for Arguments Using Stance-Aware Query Expansion*. Proceedings of the 8th Workshop on Argument Mining.

- `doi:10.18653/v1/2021.argmining-1.4` | aliases: `acl:2021.argmining-1.4`
- doc_type: `workshop` | tier: T2 | tags: extraction, quality | also in: quality
- [landing](https://aclanthology.org/2021.argmining-1.4/) | [OA PDF](https://aclanthology.org/2021.argmining-1.4.pdf) (via acl)
- verified against: acl, bibcorpus:allenai/ir_datasets, bibcorpus:corite/ir-documentation
- score 0.3042 (cites 0.0, cocite 0.1429, keyword 0.4167, venue 1.0)
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

#### Milad Alshomary et al. (2021). *Key Point Analysis via Contrastive Learning and Extractive Argument Summarization*. Proceedings of the 8th Workshop on Argument Mining.

- `doi:10.18653/v1/2021.argmining-1.19` | aliases: `acl:2021.argmining-1.19`
- doc_type: `workshop` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/2021.argmining-1.19/) | [OA PDF](https://aclanthology.org/2021.argmining-1.19.pdf) (via acl)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive
- score 0.4333 (cites 0.0, cocite 0.5714, keyword 0.3333, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Key point analysis is the task of extracting a set of concise and high-level statements from a given collection of arguments, representing the gist of these arguments." "This paper presents our proposed approach to the Key Point Analysis Shared Task, colocated with the 8th Workshop on Argument Mining." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{alshomary2021keypoint,
  title = {Key Point Analysis via Contrastive Learning and Extractive Argument Summarization},
  author = {Milad Alshomary and Timon Gurcke and Shahbaz Syed and Philipp Heinisch and Maximilian Spliethöver and Philipp Cimiano and Martin Potthast and Henning Wachsmuth},
  year = {2021},
  booktitle = {Proceedings of the 8th Workshop on Argument Mining},
  doi = {10.18653/v1/2021.argmining-1.19},
  url = {https://aclanthology.org/2021.argmining-1.19/},
}
```

</details>

#### Luca Lugini and Diane Litman (2020). *Contextual Argument Component Classification for Class Discussions*. Proceedings of the 28th International Conference on Computational Linguistics.

- `doi:10.18653/v1/2020.coling-main.128` | aliases: `acl:2020.coling-main.128`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/2020.coling-main.128/) | [OA PDF](https://aclanthology.org/2020.coling-main.128.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.4 (cites 0.0, cocite 0.0, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Argument mining systems often consider contextual information, i.e. information outside of an argumentative discourse unit, when trained to accomplish tasks such as argument component identification, classification, and relation extraction." "In this work, we show how two different types of contextual information, local discourse context and speaker context, can be incorporated into a computational model for classifying argument components in multi-party classroom discussions." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{lugini2020contextual,
  title = {Contextual Argument Component Classification for Class Discussions},
  author = {Luca Lugini and Diane Litman},
  year = {2020},
  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics},
  doi = {10.18653/v1/2020.coling-main.128},
  url = {https://aclanthology.org/2020.coling-main.128/},
}
```

</details>

#### Gaku Morio et al. (2020). *Towards Better Non-Tree Argument Mining: Proposition-Level Biaffine Parsing with Task-Specific Parameterization*. Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics.

- `doi:10.18653/v1/2020.acl-main.298` | aliases: `acl:2020.acl-main.298`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/2020.acl-main.298/) | [OA PDF](https://aclanthology.org/2020.acl-main.298.pdf) (via acl)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive
- score 0.475 (cites 0.0, cocite 0.5714, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "State-of-the-art argument mining studies have advanced the techniques for predicting argument structures." "In this paper, we focus on non-tree argument mining with a neural model." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{morio2020towardsbe,
  title = {Towards Better Non-Tree Argument Mining: Proposition-Level Biaffine Parsing with Task-Specific Parameterization},
  author = {Gaku Morio and Hiroaki Ozaki and Terufumi Morishita and Yuta Koreeda and Kohsuke Yanai},
  year = {2020},
  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
  doi = {10.18653/v1/2020.acl-main.298},
  url = {https://aclanthology.org/2020.acl-main.298/},
}
```

</details>

#### Tobias Mayer, Elena Cabrio and Serena Villata (2020). *Transformer-Based Argument Mining for Healthcare Applications*. Proceedings of the 24th European Conference on Artificial Intelligence ECAI Including 10th Conference on Prestigious Applications of Artificial Intelligence (PAIS 2020).

- `doi:10.3233/faia200334`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://doi.org/10.3233/FAIA200334)
- verified against: bibcorpus:NeWildeSache/argument-mining-in-the-web-archive, bibcorpus:m0re4u/paper-database
- score 0.475 (cites 0.0, cocite 0.5714, keyword 0.5, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{mayer2020transforme,
  title = {Transformer-Based Argument Mining for Healthcare Applications},
  author = {Tobias Mayer and Elena Cabrio and Serena Villata},
  year = {2020},
  booktitle = {Proceedings of the 24th European Conference on Artificial Intelligence ECAI Including 10th Conference on Prestigious Applications of Artificial Intelligence (PAIS 2020)},
  doi = {10.3233/faia200334},
  url = {https://doi.org/10.3233/FAIA200334},
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
- score 0.3667 (cites 0.0, cocite 0.1429, keyword 0.6667, venue 1.0)
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
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive, bibcorpus:ljvmiranda921/ljvmiranda921.github.io
- score 0.525 (cites 0.0, cocite 0.7143, keyword 0.5, venue 1.0)
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
- score 0.4146 (cites 0.0, cocite 0.4286, keyword 0.4583, venue 1.0)
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

#### Eyal Shnarch et al. (2018). *Will it Blend? Blending Weak and Strong Labeled Data in a Neural Network for Argumentation Mining*. Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers).

- `doi:10.18653/v1/p18-2095` | aliases: `acl:P18-2095`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/P18-2095/) | [OA PDF](https://aclanthology.org/P18-2095.pdf) (via acl)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive, bibcorpus:borgr/publications, bibcorpus:lihebi/biber-dist
- score 0.5667 (cites 0.0, cocite 0.7143, keyword 0.6667, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We propose a methodology to blend high quality but scarce strong labeled data with noisy but abundant weak labeled data during the training of neural networks." "In addition, we provide a manually annotated data set for the task of topic-dependent evidence detection." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{shnarch2018willitbl,
  title = {Will it Blend? Blending Weak and Strong Labeled Data in a Neural Network for Argumentation Mining},
  author = {Eyal Shnarch and Carlos Alzate and Lena Dankin and Martin Gleize and Yufang Hou and Leshem Choshen and Ranit Aharonov and Noam Slonim},
  year = {2018},
  booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
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

#### Nancy L. Green (2017). *Manual Identification of Arguments with Implicit Conclusions Using Semantic Rules for Argument Mining*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5109` | aliases: `acl:W17-5109`
- doc_type: `workshop` | tier: T2 | tags: extraction, schemes
- [landing](https://aclanthology.org/W17-5109/) | [OA PDF](https://aclanthology.org/W17-5109.pdf) (via acl)
- verified against: acl, bibcorpus:jbingel/emnlp2017-handbook | note: venue not corroborated by both sources
- score 0.3375 (cites 0.0, cocite 0.0, keyword 0.75, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This paper describes a pilot study to evaluate human analysts’ ability to identify the argumentation scheme and premises of an argument having an implicit conclusion." "In preparation for the study, argumentation scheme definitions were crafted for genetics research articles." For a debate-transcript argument database it supplies argumentation-scheme and critical-question structure, which is how stored inferences can be typed rather than left as untyped support links; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{green2017manualide,
  title = {Manual Identification of Arguments with Implicit Conclusions Using Semantic Rules for Argument Mining},
  author = {Nancy L. Green},
  year = {2017},
  booktitle = {Proceedings of the 4th Workshop on Argument Mining},
  doi = {10.18653/v1/w17-5109},
  url = {https://aclanthology.org/W17-5109/},
}
```

</details>

#### John Lawrence and Chris Reed (2017). *Mining Argumentative Structure from Natural Language text using Automatically Generated Premise-Conclusion Topic Models*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5105` | aliases: `acl:W17-5105`
- doc_type: `workshop` | tier: T2 | tags: extraction
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
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database
- score 0.5583 (cites 0.0, cocite 0.5714, keyword 0.8333, venue 1.0)
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

#### Isaac Persing and Vincent Ng (2016). *End-to-End Argumentation Mining in Student Essays*. Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.

- `doi:10.18653/v1/n16-1164` | aliases: `acl:N16-1164`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](https://aclanthology.org/N16-1164/) | [OA PDF](https://aclanthology.org/N16-1164.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist
- score 0.3583 (cites 0.0, cocite 0.0, keyword 0.8333, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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
- score 0.425 (cites 0.0, cocite 0.4286, keyword 0.5, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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
- score 0.45 (cites 0.0, cocite 0.1429, keyword 1.0, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Christian Stab and Iryna Gurevych (2014). *Annotating Argument Components and Relations in Persuasive Essays*. Proceedings of COLING 2014, the 25th International Conference on Computational Linguistics: Technical Papers.

- `title:97249276aac1f18259184dfbfac19f869827fdaa` | aliases: `acl:C14-1142`
- doc_type: `conference` | tier: T2 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/C14-1142/) | [OA PDF](https://aclanthology.org/C14-1142.pdf) (via acl) | [repo](https://github.com/thiemowa/-argumentative_business_model_pitches)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive, bibcorpus:davidar/dblp.yaml, bibcorpus:m0re4u/paper-database | note: repo linked on distinctive title/description overlap: ['components', 'persuasive', 'relations'] (all shared words: ['components', 'persuasive', 'relations'])
- score 0.475 (cites 0.0, cocite 0.5714, keyword 0.5, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{stab2014annotating,
  title = {Annotating Argument Components and Relations in Persuasive Essays},
  author = {Christian Stab and Iryna Gurevych},
  year = {2014},
  booktitle = {Proceedings of COLING 2014, the 25th International Conference on Computational Linguistics: Technical Papers},
  url = {https://aclanthology.org/C14-1142/},
}
```

</details>

#### Ivan Habernal, Judith Eckle-Kohler and Iryna Gurevych (2014). *Argumentation Mining on the Web from Information Seeking Perspective*. ArgNLP.

- `title:e2dd0248ee2104b83fabae9e89b7c5d7e89a5690`
- doc_type: `conference` | tier: T2 | tags: extraction
- [landing](http://ceur-ws.org/Vol-1341/paper4.pdf)
- verified against: bibcorpus:IKMLab/arct2, bibcorpus:davidar/dblp.yaml
- score 0.35 (cites 0.0, cocite 0.4286, keyword 0.5, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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
- score 0.3062 (cites 0.0, cocite 0.5714, keyword 0.125, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Raquel Mochales and Marie-Francine Moens (2011). *Argumentation Mining*. Artif. Intell. Law.

- `doi:10.1007/s10506-010-9104-x`
- doc_type: `journal` | tier: T2 | tags: extraction
- [landing](http://dx.doi.org/10.1007/s10506-010-9104-x)
- verified against: bibcorpus:IKMLab/arct2, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive, bibcorpus:davidar/dblp.yaml, bibcorpus:m0re4u/paper-database, bibcorpus:nshkrdotcom/research_papers | note: author order differs (mochales / palau)
- score 0.45 (cites 0.0, cocite 0.7143, keyword 0.5, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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
- score 0.35 (cites 0.0, cocite 0.4286, keyword 0.5, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Maria Poiaganova and Manfred Stede (2025). *From Debates to Diplomacy: Argument Mining Across Political Registers*. Proceedings of the 12th Argument mining Workshop.

- `doi:10.18653/v1/2025.argmining-1.20` | aliases: `acl:2025.argmining-1.20`
- doc_type: `workshop` | tier: T3 | tags: dataset, dialogue, extraction | also in: resources
- [landing](https://aclanthology.org/2025.argmining-1.20/) | [OA PDF](https://aclanthology.org/2025.argmining-1.20.pdf) (via acl) | [repo](https://github.com/AzkaQadir/multimodal-fallacy-detection)
- verified against: acl, bibcorpus:mpoiaganova/poiaganova | note: repo linked on distinctive title/description overlap: ['debates', 'political'] (all shared words: ['debates', 'political'])
- score 0.4 (cites 0.0, cocite 0.0, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This paper addresses the problem of cross-register generalization in argument mining within political discourse." "As part of this work, we introduce ArgUNSC, a new corpus of 144 UNSC speeches manually annotated with claims, premises, and their argumentative links." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{poiaganova2025fromdebat,
  title = {From Debates to Diplomacy: Argument Mining Across Political Registers},
  author = {Maria Poiaganova and Manfred Stede},
  year = {2025},
  booktitle = {Proceedings of the 12th Argument mining Workshop},
  doi = {10.18653/v1/2025.argmining-1.20},
  url = {https://aclanthology.org/2025.argmining-1.20/},
}
```

</details>

#### Marc Feger, Katarina Boland and Stefan Dietze (2025). *Limited Generalizability in Argument Mining: State-Of-The-Art Models Learn Datasets, Not Arguments*. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025, Vienna, Austria, July 27 - August 1, 2025.

- `title:ecc66f83f08f4809231d027e9ba9ccb1e4c3f5ba` | aliases: `acl:2025.acl-long.1164`, `doi:10.18653/v1/2025.acl-long.1164`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue, extraction | also in: resources
- [landing](https://aclanthology.org/2025.acl-long.1164/) | [OA PDF](https://aclanthology.org/2025.acl-long.1164.pdf) (via acl)
- verified against: acl, bibcorpus:CogSciPrag/project_ideas
- score 0.475 (cites 0.0, cocite 0.5714, keyword 0.5, venue 1.0)
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

#### Masayuki Kawarada, Tsutomu Hirao, Wataru Uchida and Masaaki Nagata (2024). *Argument Mining as a Text-to-Text Generation Task*. Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/2024.eacl-long.121` | aliases: `acl:2024.eacl-long.121`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/2024.eacl-long.121/) | [OA PDF](https://aclanthology.org/2024.eacl-long.121.pdf) (via acl)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive
- score 0.5167 (cites 0.0, cocite 0.5714, keyword 0.6667, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "To address this difficulty, we propose a simple yet strong method based on a text-to-text generation approach using a pretrained encoder-decoder language model." "Furthermore, because it is a straightforward text-to-text generation method, we can easily adapt our approach to various types of argumentative structures.Experimental results demonstrate the effectiveness of our method, as it achieves state-of-the-art performance on three different types of benchmark datasets: the Ar…" For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{kawarada2024argumentm,
  title = {Argument Mining as a Text-to-Text Generation Task},
  author = {Masayuki Kawarada and Tsutomu Hirao and Wataru Uchida and Masaaki Nagata},
  year = {2024},
  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/2024.eacl-long.121},
  url = {https://aclanthology.org/2024.eacl-long.121/},
}
```

</details>

#### Roni Friedman et al. (2021). *Overview of the 2021 Key Point Analysis Shared Task*. Proceedings of the 8th Workshop on Argument Mining.

- `doi:10.18653/v1/2021.argmining-1.16` | aliases: `acl:2021.argmining-1.16`
- doc_type: `workshop` | tier: T3 | tags: dataset, extraction
- [landing](https://aclanthology.org/2021.argmining-1.16/) | [OA PDF](https://aclanthology.org/2021.argmining-1.16.pdf) (via acl)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive
- score 0.4542 (cites 0.0, cocite 0.5714, keyword 0.4167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We describe the 2021 Key Point Analysis (KPA-2021) shared task on key point analysis that we organized as a part of the 8th Workshop on Argument Mining (ArgMining 2021) at EMNLP 2021." "We expect the task and the findings reported in this paper to be relevant for researchers working on text summarization and argument mining." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{friedman2021overviewo,
  title = {Overview of the 2021 Key Point Analysis Shared Task},
  author = {Roni Friedman and Lena Dankin and Yufang Hou and Ranit Aharonov and Yoav Katz and Noam Slonim},
  year = {2021},
  booktitle = {Proceedings of the 8th Workshop on Argument Mining},
  doi = {10.18653/v1/2021.argmining-1.16},
  url = {https://aclanthology.org/2021.argmining-1.16/},
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
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database | note: repo linked on distinctive title/description overlap: ['low', 'multi', 'resource', 'settings'] (all shared words: ['argumentation', 'learning', 'low', 'mining', 'multi', 'resource', 'settings', 'task…
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

#### Ivan Habernal and Iryna Gurevych (2017). *Argumentation Mining in User-Generated Web Discourse*. Computational Linguistics.

- `doi:10.1162/coli_a_00276` | aliases: `acl:J17-1004`
- doc_type: `journal` | tier: T3 | tags: dataset, extraction | also in: resources
- [landing](https://aclanthology.org/J17-1004/) | [OA PDF](https://aclanthology.org/J17-1004.pdf) (via acl)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive, bibcorpus:lihebi/biber-dist, bibcorpus:m0re4u/paper-database
- score 0.5792 (cites 0.0, cocite 0.5714, keyword 0.9167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The goal of argumentation mining, an evolving research field in computational linguistics, is to design methods capable of analyzing people’s argumentation." "We offer the data, source codes, and annotation guidelines to the community under free licenses." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@article{habernal2017argumentat,
  title = {Argumentation Mining in User-Generated Web Discourse},
  author = {Ivan Habernal and Iryna Gurevych},
  year = {2017},
  journal = {Computational Linguistics},
  doi = {10.1162/coli_a_00276},
  url = {https://aclanthology.org/J17-1004/},
}
```

</details>

#### Christian Stab and Iryna Gurevych (2017). *Parsing Argumentation Structures in Persuasive Essays*. Computational Linguistics.

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
  journal = {Computational Linguistics},
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
- score 0.4667 (cites 0.0, cocite 0.4286, keyword 0.6667, venue 1.0)
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

#### Deborah Dore, Stefano Faralli and Serena Villata (2025). *Leveraging Graph Structural Knowledge to Improve Argument Relation Prediction in Political Debates*. Proceedings of the 12th Argument mining Workshop.

- `doi:10.18653/v1/2025.argmining-1.7` | aliases: `acl:2025.argmining-1.7`
- doc_type: `workshop` | tier: T4 | tags: dialogue, extraction, fallacy
- [landing](https://aclanthology.org/2025.argmining-1.7/) | [OA PDF](https://aclanthology.org/2025.argmining-1.7.pdf) (via acl)
- verified against: acl, bibcorpus:deborahdore/deborahdore.github.io
- score 0.4 (cites 0.0, cocite 0.0, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Despite the few approaches proposed in the literature to apply AM to political debates, this application scenario is still challenging, and, more precisely, concerning the task of predicting the relation holding between two argument components." "In this paper, we propose to address the relation prediction task in AM by combining the structural knowledge provided by a Knowledge Graph Embedding Model with the contextual knowledge provided by a fine-tuned Large Language Model." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it types defective inference.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{dore2025leveraging,
  title = {Leveraging Graph Structural Knowledge to Improve Argument Relation Prediction in Political Debates},
  author = {Deborah Dore and Stefano Faralli and Serena Villata},
  year = {2025},
  booktitle = {Proceedings of the 12th Argument mining Workshop},
  doi = {10.18653/v1/2025.argmining-1.7},
  url = {https://aclanthology.org/2025.argmining-1.7/},
}
```

</details>

#### Zihao Zheng, Zhaowei Wang, Qing Zong and Yangqiu Song (2024). *KNOWCOMP POKEMON Team at DialAM-2024: A Two-Stage Pipeline for Detecting Relations in Dialogue Argument Mining*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.11` | aliases: `acl:2024.argmining-1.11`
- doc_type: `workshop` | tier: T4 | tags: dialogue, extraction | also in: dialogue
- [landing](https://aclanthology.org/2024.argmining-1.11/) | [OA PDF](https://aclanthology.org/2024.argmining-1.11.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.525 (cites 0.0, cocite 0.5357, keyword 0.75, venue 1.0)
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
- score 0.3875 (cites 0.0, cocite 0.1429, keyword 0.75, venue 1.0)
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

#### Neele Falk, Iman Jundi, Eva Maria Vecchi and Gabriella Lapesa (2021). *Predicting Moderation of Deliberative Arguments: Is Argument Quality the Key?*. Proceedings of the 8th Workshop on Argument Mining.

- `doi:10.18653/v1/2021.argmining-1.13` | aliases: `acl:2021.argmining-1.13`
- doc_type: `workshop` | tier: T2 | tags: dialogue, extraction, quality
- [landing](https://aclanthology.org/2021.argmining-1.13/) | [OA PDF](https://aclanthology.org/2021.argmining-1.13.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.525 (cites 0.0, cocite 0.7143, keyword 0.5, venue 1.0)
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
- score 0.4875 (cites 0.0, cocite 0.4286, keyword 0.75, venue 1.0)
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

#### Martin Potthast et al. (2019). *Argument Search: Assessing Argument Relevance*. Proceedings of the 42nd International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR 2019, Paris, France, July 21-25, 2019.

- `doi:10.1145/3331184.3331327`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://doi.org/10.1145/3331184.3331327)
- verified against: bibcorpus:CogSciPrag/project_ideas, bibcorpus:boudinfl/acm-cr, bibcorpus:ir-anthology/ir-anthology.github.io
- score 0.3167 (cites 0.0, cocite 0.5714, keyword 0.1667, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We report on the first user study on assessing argument relevance." "Based on a search among more than 300,000 arguments, four standard retrieval models are compared on 40 topics for 20 controversial issues: every issue has one topic with a biased stance and another neutral one." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{potthast2019arguments,
  title = {Argument Search: Assessing Argument Relevance},
  author = {Martin Potthast and Lukas Gienapp and Florian Euchner and Nick Heilenkotter and Nico Weidmann and Henning Wachsmuth and Benno Stein and Matthias Hagen},
  year = {2019},
  booktitle = {Proceedings of the 42nd International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR 2019, Paris, France, July 21-25, 2019},
  doi = {10.1145/3331184.3331327},
  url = {https://doi.org/10.1145/3331184.3331327},
}
```

</details>

#### Ivan Habernal, Henning Wachsmuth, Iryna Gurevych and Benno Stein (2018). *Before Name-Calling: Dynamics and Triggers of Ad Hominem Fallacies in Web Argumentation*. Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers).

- `doi:10.18653/v1/n18-1036` | aliases: `acl:N18-1036`
- doc_type: `conference` | tier: T2 | tags: dialogue, fallacy, quality
- [landing](https://aclanthology.org/N18-1036/) | [OA PDF](https://aclanthology.org/N18-1036.pdf) (via acl)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:npnkhoi/memefal-paper
- score 0.45 (cites 0.0, cocite 0.1429, keyword 1.0, venue 1.0)
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
- score 0.325 (cites 0.0, cocite 0.1429, keyword 0.5, venue 1.0)
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

#### Orith Toledo-Ronen, Roy Bar-Haim and Noam Slonim (2016). *Expert Stance Graphs for Computational Argumentation*. Proceedings of the Third Workshop on Argument Mining (ArgMining2016).

- `doi:10.18653/v1/w16-2814` | aliases: `acl:W16-2814`
- doc_type: `workshop` | tier: T2 | tags: extraction, quality
- [landing](https://aclanthology.org/W16-2814/) | [OA PDF](https://aclanthology.org/W16-2814.pdf) (via acl)
- verified against: acl, bibcorpus:julia-zhou/Argmining
- score 0.2333 (cites 0.0, cocite 0.0, keyword 0.3333, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{toledoronen2016expertsta,
  title = {Expert Stance Graphs for Computational Argumentation},
  author = {Orith Toledo-Ronen and Roy Bar-Haim and Noam Slonim},
  year = {2016},
  booktitle = {Proceedings of the Third Workshop on Argument Mining (ArgMining2016)},
  doi = {10.18653/v1/w16-2814},
  url = {https://aclanthology.org/W16-2814/},
}
```

</details>

#### Ivan Habernal and Iryna Gurevych (2016). *Which argument is more convincing? Analyzing and predicting convincingness of Web arguments using bidirectional LSTM*. Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

- `doi:10.18653/v1/p16-1150` | aliases: `acl:P16-1150`
- doc_type: `conference` | tier: T2 | tags: quality
- [landing](https://aclanthology.org/P16-1150/) | [OA PDF](https://aclanthology.org/P16-1150.pdf)
- verified against: acl, bibcorpus:lihebi/biber-dist, bibcorpus:xinyannnnnnn/fact-driven-storytelling-with-llms
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Neele Falk and Gabriella Lapesa (2023). *Bridging Argument Quality and Deliberative Quality Annotations with Adapters*. Findings of the Association for Computational Linguistics: EACL 2023.

- `doi:10.18653/v1/2023.findings-eacl.187` | aliases: `acl:2023.findings-eacl.187`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction, quality | also in: resources
- [landing](https://aclanthology.org/2023.findings-eacl.187/) | [OA PDF](https://aclanthology.org/2023.findings-eacl.187.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.3375 (cites 0.0, cocite 0.0, keyword 0.75, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We employ adapter-fusion (Pfeiffer et al., 2021) as a multi-task learning framework which a) can improve the prediction of individual quality dimensions by injecting knowledge about related dimensions b) is efficient and modular and c) can serve as an analysis tool to investigate relations between different dimensions." "Last, we show the benefits of this approach by improving the performance in an extrinsic, out-of-domain task: prediction of moderator interventions in a deliberative forum." For a debate-transcript argument database it gives quality dimensions or a scoring target, which is what an argument-strength field in the database would be measured against; and it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{falk2023bridginga,
  title = {Bridging Argument Quality and Deliberative Quality Annotations with Adapters},
  author = {Neele Falk and Gabriella Lapesa},
  year = {2023},
  booktitle = {Findings of the Association for Computational Linguistics: EACL 2023},
  doi = {10.18653/v1/2023.findings-eacl.187},
  url = {https://aclanthology.org/2023.findings-eacl.187/},
}
```

</details>

#### Shai Gretz et al. (2020). *A large-scale dataset for argument quality ranking: Construction and analysis*. Proceedings of the Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, The Thirty-Second Innovative Applications of Artificial Intelligence Conference, IAAI 2020, The Tenth AAAI Symposium on Educational Advances in Artificial Intelligence, EAAI 2020.

- `doi:10.1609/aaai.v34i05.6285`
- doc_type: `conference` | tier: T3 | tags: dataset, quality | also in: resources
- [landing](https://doi.org/10.1609/aaai.v34i05.6285) | [repo](https://github.com/Hellisotherpeople/DebateSum)
- verified against: bibcorpus:BarryMafu/LitLens, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive, bibcorpus:xinyannnnnnn/fact-driven-storytelling-with-llms | note: bibcorpus:dimits-ts/llm_moderation_research: venue mismatch ('AAAI' vs 'ArXiv'); bibcorpus:dimits-ts/synthetic_moderation_experiments: venue mismatch ('AAAI' vs 'ArXiv') repo linked on distinctive ti…
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{gretz2020alargesc,
  title = {A large-scale dataset for argument quality ranking: Construction and analysis},
  author = {Shai Gretz and Roni Friedman and Edo Cohen-Karlik and Assaf Toledo and Dan Lahav and Ranit Aharonov and Noam Slonim},
  year = {2020},
  booktitle = {Proceedings of the Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, The Thirty-Second Innovative Applications of Artificial Intelligence Conference, IAAI 2020, The Tenth AAAI Symposium on Educational Advances in Artificial Intelligence, EAAI 2020},
  doi = {10.1609/aaai.v34i05.6285},
  url = {https://doi.org/10.1609/aaai.v34i05.6285},
}
```

</details>

#### Lily Ng, Anne Lauscher, Joel Tetreault and Courtney Napoles (2020). *Creating a Domain-diverse Corpus for Theory-based Argument Quality Assessment*. Proceedings of the 7th Workshop on Argument Mining.

- `title:8973c9782426ec9080181ce8b676df529016c076` | aliases: `acl:2020.argmining-1.13`
- doc_type: `workshop` | tier: T3 | tags: dataset, extraction, quality | also in: resources
- [landing](https://aclanthology.org/2020.argmining-1.13/) | [OA PDF](https://aclanthology.org/2020.argmining-1.13.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
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
- score 0.45 (cites 0.0, cocite 0.1429, keyword 1.0, venue 1.0)
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

#### Pierpaolo Goffredo, Deborah Dore, Elena Cabrio and Serena Villata (2025). *DISPUTool 3.0: Fallacy Detection and Repairing in Argumentative Political Debates*. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations), ACL 2025, Vienna, Austria, July 27 - August 1, 2025.

- `doi:10.18653/v1/2025.acl-demo.45` | aliases: `acl:2025.acl-demo.45`
- doc_type: `conference` | tier: T4 | tags: dialogue, extraction, fallacy, quality | also in: mining
- [landing](https://aclanthology.org/2025.acl-demo.45/) | [OA PDF](https://aclanthology.org/2025.acl-demo.45.pdf) (via acl)
- verified against: acl, bibcorpus:deborahdore/deborahdore.github.io
- score 0.3375 (cites 0.0, cocite 0.0, keyword 0.75, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This paper introduces and evaluates a novel web-based application designed to identify and repair fallacious arguments in political debates." "In this paper, we introduce a novel task which is integrated as a new module in DISPUTool, i.e., the automatic detection and classification of fallacious arguments, and the automatic \textit{repairing} of such misleading arguments." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it gives quality dimensions or a scoring target.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{goffredo2025disputool,
  title = {DISPUTool 3.0: Fallacy Detection and Repairing in Argumentative Political Debates},
  author = {Pierpaolo Goffredo and Deborah Dore and Elena Cabrio and Serena Villata},
  year = {2025},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations), ACL 2025, Vienna, Austria, July 27 - August 1, 2025},
  doi = {10.18653/v1/2025.acl-demo.45},
  url = {https://aclanthology.org/2025.acl-demo.45/},
}
```

</details>

#### Alessio Pittiglio (2025). *Leveraging Context for Multimodal Fallacy Classification in Political Debates*. Proceedings of the 12th Argument mining Workshop.

- `doi:10.18653/v1/2025.argmining-1.39` | aliases: `acl:2025.argmining-1.39`
- doc_type: `workshop` | tier: T4 | tags: dialogue, extraction, fallacy, quality | also in: dialogue, mining
- [landing](https://aclanthology.org/2025.argmining-1.39/) | [OA PDF](https://aclanthology.org/2025.argmining-1.39.pdf) (via acl)
- verified against: acl, bibcorpus:alessiopittiglio/alessiopittiglio.github.io
- score 0.275 (cites 0.0, cocite 0.0, keyword 0.5, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we present our submission to the MM-ArgFallacy2025 shared task, which aims to advance research in multimodal argument mining, focusing on logical fallacies in political debates." "Our approach uses pretrained Transformer-based models and proposes several ways to leverage context." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it gives quality dimensions or a scoring target.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{pittiglio2025leveraging,
  title = {Leveraging Context for Multimodal Fallacy Classification in Political Debates},
  author = {Alessio Pittiglio},
  year = {2025},
  booktitle = {Proceedings of the 12th Argument mining Workshop},
  doi = {10.18653/v1/2025.argmining-1.39},
  url = {https://aclanthology.org/2025.argmining-1.39/},
}
```

</details>

#### Rositsa V Ivanova and Reto Gubelmann (2025). *The Shift from Logic to Dialectic in Argumentation Theory: Implications for Computational Argument Quality Assessment*. Proceedings of the 31st International Conference on Computational Linguistics.

- `title:3081c2f49d86b933976822d3e21e4f8fdc9410a6` | aliases: `acl:2025.coling-main.321`
- doc_type: `conference` | tier: T4 | tags: quality
- [landing](https://aclanthology.org/2025.coling-main.321/) | [OA PDF](https://aclanthology.org/2025.coling-main.321.pdf) (via acl)
- verified against: acl, bibcorpus:nexuspllc/responsiveness-bench
- score 0.45 (cites 0.0, cocite 0.1429, keyword 1.0, venue 1.0)
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

## 6.4 Dialogue and debate (19 entries, quota 40)

### T1 - Foundational / survey. Read in full: theory anchors, major surveys, canonical papers.

#### Ramon Ruiz-Dolz, John Lawrence, Ella Schad and Chris Reed (2024). *Overview of DialAM-2024: Argument Mining in Natural Language Dialogues*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.8` | aliases: `acl:2024.argmining-1.8`
- doc_type: `workshop` | tier: T1 | tags: dialogue, extraction | also in: mining
- [landing](https://aclanthology.org/2024.argmining-1.8/) | [OA PDF](https://aclanthology.org/2024.argmining-1.8.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.5667 (cites 0.0, cocite 0.5357, keyword 0.9167, venue 1.0)
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

#### Noam Slonim et al. (2021). *An autonomous debating system*. Nature.

- `doi:10.1038/s41586-021-03215-w`
- doc_type: `journal` | tier: T2 | tags: dialogue | also in: llm
- [landing](https://doi.org/10.1038/s41586-021-03215-w)
- verified against: bibcorpus:CogSciPrag/project_ideas, bibcorpus:borgr/publications, bibcorpus:danielhers/danielhers.github.io
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Artificial intelligence (AI) is defined as the ability of machines to perform tasks that are usually associated with intelligent beings." "Here we present Project Debater, an autonomous debating system that can engage in a competitive debate with humans." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@article{slonim2021anautonom,
  title = {An autonomous debating system},
  author = {Noam Slonim and Yonatan Bilu and Carlos Alzate and Roy Bar-Haim and Ben Bogin and Francesca Bonin and Leshem Choshen and Edo Cohen-Karlik and Lena Dankin and Lilach Edelstein and Liat Ein-Dor and Roni Friedman-Melamed and Assaf Gavron and Ariel Gera and Martin Gleize and Shai Gretz and Dan Gutfreund and Alon Halfon and Daniel Hershcovich and Ron Hoory and Yufang Hou and Shay Hummel and Michal Jacovi and Charles Jochim and Yoav Kantor and Yoav Katz and David Konopnicki and Zvi Kons and Lili Kotlerman and Dalia Krieger and Dan Lahav and Tamar Lavee and Ran Levy and Naftali Liberman and Yosi Mass and Amir Menczel and Shachar Mirkin and Guy Moshkowich and Shila Ofek-Koifman and Matan Orbach and Ella Rabinovich and Ruty Rinott and Slava Shechtman and Dafna Sheinwald and Eyal Shnarch and Ilya Shnayderman and Aya Soffer and Artem Spector and Benjamin Sznajder and Assaf Toledo and Orith Toledo-Ronen and Elad Venezian and Ranit Aharonov},
  year = {2021},
  journal = {Nature},
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
- score 0.5083 (cites 0.0, cocite 1.0, keyword 0.3333, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Jacky Visser et al. (2019). *Argumentation in the 2016 US presidential elections: annotated corpora of television debates and social media reaction*. Language Resources and Evaluation.

- `doi:10.1007/s10579-019-09446-8`
- doc_type: `journal` | tier: T2 | tags: dialogue
- [landing](https://doi.org/10.1007/s10579-019-09446-8)
- verified against: bibcorpus:IKMLab/argalign1, bibcorpus:RicoStaedeli/NLP2025_CQG, bibcorpus:m0re4u/paper-database
- score 0.2958 (cites 0.0, cocite 0.1786, keyword 0.3333, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@article{visser2019argumentat,
  title = {Argumentation in the 2016 US presidential elections: annotated corpora of television debates and social media reaction},
  author = {Jacky Visser and Barbara Konat and Rory Duthie and Marcin Koszowy and Katarzyna Budzynska and Chris Reed},
  year = {2019},
  journal = {Language Resources and Evaluation},
  doi = {10.1007/s10579-019-09446-8},
  url = {https://doi.org/10.1007/s10579-019-09446-8},
}
```

</details>

#### Justine Zhang, Ravi Kumar, Sujith Ravi and Cristian Danescu-Niculescu-Mizil (2016). *Conversational Flow in Oxford-style Debates*. Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.

- `doi:10.18653/v1/n16-1017` | aliases: `acl:N16-1017`
- doc_type: `conference` | tier: T2 | tags: dialogue
- [landing](https://aclanthology.org/N16-1017/) | [OA PDF](https://aclanthology.org/N16-1017.pdf) (via acl)
- verified against: acl, bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments, bibcorpus:lihebi/biber-dist | note: venue not corroborated by both sources
- score 0.5875 (cites 0.0, cocite 0.8929, keyword 0.5, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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
- score 0.4208 (cites 0.0, cocite 0.1786, keyword 0.8333, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Chenhao Tan, Vlad Niculae, Cristian Danescu-Niculescu-Mizil and Lillian Lee (2016). *Winning Arguments: Interaction Dynamics and Persuasion Strategies in Good-Faith Online Discussions*. Proceedings of the 25th International Conference on World Wide Web, WWW 2016, Montreal, Canada, April 11 - 15, 2016.

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
  booktitle = {Proceedings of the 25th International Conference on World Wide Web, WWW 2016, Montreal, Canada, April 11 - 15, 2016},
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
- score 0.4708 (cites 0.0, cocite 0.8929, keyword 0.3333, venue 0.5)
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

#### Thomas F. Gordon, Henry Prakken and Douglas Walton (2007). *The Carneades model of argument and burden of proof*. Artif. Intell..

- `doi:10.1016/j.artint.2007.04.010`
- doc_type: `journal` | tier: T2 | tags: dialogue
- no URL recorded
- verified against: bibcorpus:carneades/carneades-3, bibcorpus:davidar/dblp.yaml
- score 0.2625 (cites 0.0, cocite 0.1786, keyword 0.5, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@article{gordon2007thecarnea,
  title = {The Carneades model of argument and burden of proof},
  author = {Thomas F. Gordon and Henry Prakken and Douglas Walton},
  year = {2007},
  journal = {Artif. Intell.},
  doi = {10.1016/j.artint.2007.04.010},
}
```

</details>

#### Davy Janssen and Raphaël Kies (2005). *Online Forums and Deliberative Democracy*. Acta Politica.

- `doi:10.1057/palgrave.ap.5500115`
- doc_type: `journal` | tier: T2 | tags: dialogue
- [landing](https://doi.org/10.1057/palgrave.ap.5500115)
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments
- score 0.45 (cites 0.0, cocite 0.8929, keyword 0.25, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this article, we present an overview of some of the empirical research that evaluates the quality of political conversations in online forums." "In the conclusion, we present some objections to the previous research and offer some ideas for a more comprehensive approach to online forum analysis." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@article{janssen2005onlinefor,
  title = {Online Forums and Deliberative Democracy},
  author = {Davy Janssen and Raphaël Kies},
  year = {2005},
  journal = {Acta Politica},
  doi = {10.1057/palgrave.ap.5500115},
  url = {https://doi.org/10.1057/palgrave.ap.5500115},
}
```

</details>

### T3 - Dataset / tool / annotation guideline, including the guideline documents themselves.

#### Arne Binder, Tatiana Anikina, Leonhard Hennig and Simon Ostermann (2024). *DFKI-MLST at DialAM-2024 Shared Task: System Description*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.9` | aliases: `acl:2024.argmining-1.9`
- doc_type: `workshop` | tier: T3 | tags: dataset, dialogue, extraction | also in: mining
- [landing](https://aclanthology.org/2024.argmining-1.9/) | [OA PDF](https://aclanthology.org/2024.argmining-1.9.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.4625 (cites 0.0, cocite 0.5357, keyword 0.5, venue 1.0)
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

#### Saumya Sahai, Oana Balalau and Roxana Horincar (2021). *Breaking Down the Invisible Wall of Informal Fallacies in Online Discussions*. Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers).

- `doi:10.18653/v1/2021.acl-long.53` | aliases: `acl:2021.acl-long.53`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue, fallacy, quality | also in: quality, resources
- [landing](https://aclanthology.org/2021.acl-long.53/) | [OA PDF](https://aclanthology.org/2021.acl-long.53.pdf) (via acl)
- verified against: acl, bibcorpus:lefteriskat/Logical-Fallacy-Detection-Using-LLMs, bibcorpus:npnkhoi/memefal-paper
- score 0.275 (cites 0.0, cocite 0.1786, keyword 0.25, venue 1.0)
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

#### Chantal van Son et al. (2016). *Unshared Task at the 3rd Workshop on Argument Mining: Perspective Based Local Agreement and Disagreement in Online Debate*. Proceedings of the Third Workshop on Argument Mining (ArgMining2016).

- `doi:10.18653/v1/w16-2819` | aliases: `acl:W16-2819`
- doc_type: `workshop` | tier: T3 | tags: dataset, dialogue, extraction | also in: mining
- [landing](https://aclanthology.org/W16-2819/) | [OA PDF](https://aclanthology.org/W16-2819.pdf) (via acl)
- verified against: acl, bibcorpus:m0re4u/paper-database
- score 0.4 (cites 0.0, cocite 0.0, keyword 1.0, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Mohammad Khosravani, Chenyang Huang and Amine Trabelsi (2024). *Enhancing Argument Summarization: Prioritizing Exhaustiveness in Key Point Generation and Introducing an Automatic Coverage Evaluation Metric*. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers).

- `doi:10.18653/v1/2024.naacl-long.454` | aliases: `acl:2024.naacl-long.454`
- doc_type: `conference` | tier: T4 | tags: dialogue
- [landing](https://aclanthology.org/2024.naacl-long.454/) | [OA PDF](https://aclanthology.org/2024.naacl-long.454.pdf) (via acl)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive
- score 0.5042 (cites 0.0, cocite 0.7143, keyword 0.4167, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This paper introduces a novel extractive approach for key point generation, that outperforms previous state-of-the-art methods for the task." "To this end, we propose a new evaluation metric for assessing the generated key points by their coverage." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{khosravani2024enhancing,
  title = {Enhancing Argument Summarization: Prioritizing Exhaustiveness in Key Point Generation and Introducing an Automatic Coverage Evaluation Metric},
  author = {Mohammad Khosravani and Chenyang Huang and Amine Trabelsi},
  year = {2024},
  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
  doi = {10.18653/v1/2024.naacl-long.454},
  url = {https://aclanthology.org/2024.naacl-long.454/},
}
```

</details>

#### Yuetong Wu et al. (2024). *KnowComp at DialAM-2024: Fine-tuning Pre-trained Language Models for Dialogical Argument Mining with Inference Anchoring Theory*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.10` | aliases: `acl:2024.argmining-1.10`
- doc_type: `workshop` | tier: T4 | tags: dialogue, extraction, formal | also in: formal, mining
- [landing](https://aclanthology.org/2024.argmining-1.10/) | [OA PDF](https://aclanthology.org/2024.argmining-1.10.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.5875 (cites 0.0, cocite 0.5357, keyword 1.0, venue 1.0)
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
- score 0.5875 (cites 0.0, cocite 0.5357, keyword 1.0, venue 1.0)
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

## 6.5 LLM era, 2023-2026 (11 entries, quota 40)

### T2 - Core method. Defines a task formulation, model, or evaluation still in use.

#### Tariq Alhindi, Tuhin Chakrabarty, Elena Musi and Smaranda Muresan (2022). *Multitask Instruction-based Prompting for Fallacy Recognition*. Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2022.emnlp-main.560` | aliases: `acl:2022.emnlp-main.560`
- doc_type: `conference` | tier: T2 | tags: dialogue, fallacy, quality | also in: quality
- [landing](https://aclanthology.org/2022.emnlp-main.560/) | [OA PDF](https://aclanthology.org/2022.emnlp-main.560.pdf) (via acl)
- verified against: acl, bibcorpus:lefteriskat/Logical-Fallacy-Detection-Using-LLMs
- score 0.325 (cites 0.0, cocite 0.1429, keyword 0.5, venue 1.0)
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

#### Jeremie Cabessa, Hugo Hernault and Umer Mushtaq (2025). *Argument Mining with Fine-Tuned Large Language Models*. Proceedings of the 31st International Conference on Computational Linguistics.

- `title:b3f2fb478758d0b73038947a352f801896c15505` | aliases: `acl:2025.coling-main.442`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction | also in: mining, resources
- [landing](https://aclanthology.org/2025.coling-main.442/) | [OA PDF](https://aclanthology.org/2025.coling-main.442.pdf) (via acl)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive
- score 0.6 (cites 0.0, cocite 0.5714, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We fine-tune eight popular quantized and non-quantized LLMs -- LLaMA-3, LLaMA-3.1, Gemma-2, Mistral, Phi-3, Qwen-2 -- which are among the most capable open-weight models, on the benchmark PE, AbstRCT, and CDCP datasets that represent diverse data sources." "Our approach achieves state-of-the-art results across all AM sub-tasks and datasets, showing significant improvements over previous benchmarks." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{cabessa2025argumentm,
  title = {Argument Mining with Fine-Tuned Large Language Models},
  author = {Jeremie Cabessa and Hugo Hernault and Umer Mushtaq},
  year = {2025},
  booktitle = {Proceedings of the 31st International Conference on Computational Linguistics},
  url = {https://aclanthology.org/2025.coling-main.442/},
}
```

</details>

#### Fengjun Pan, Xiaobao Wu, Zongrui Li and Anh Tuan Luu (2024). *Are LLMs Good Zero-Shot Fallacy Classifiers?*. Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2024.emnlp-main.794` | aliases: `acl:2024.emnlp-main.794`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction, fallacy, quality | also in: quality, resources
- [landing](https://aclanthology.org/2024.emnlp-main.794/) | [OA PDF](https://aclanthology.org/2024.emnlp-main.794.pdf) (via acl)
- verified against: acl, bibcorpus:lefteriskat/Logical-Fallacy-Detection-Using-LLMs
- score 0.45 (cites 0.0, cocite 0.1429, keyword 1.0, venue 1.0)
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

#### Min-Hsuan Yeh, Ruyuan Wan and Ting-Hao Kenneth Huang (2024). *CoCoLoFa: A Dataset of News Comments with Common Logical Fallacies Written by LLM-Assisted Crowds*. Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing.

- `doi:10.18653/v1/2024.emnlp-main.39` | aliases: `acl:2024.emnlp-main.39`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction, fallacy, quality | also in: quality, resources
- [landing](https://aclanthology.org/2024.emnlp-main.39/) | [OA PDF](https://aclanthology.org/2024.emnlp-main.39.pdf) (via acl)
- verified against: acl, bibcorpus:npnkhoi/memefal-paper
- score 0.325 (cites 0.0, cocite 0.1429, keyword 0.5, venue 1.0)
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

#### Blanca Calvo Figueras and Rodrigo Agerri (2024). *Critical Questions Generation: Motivation and Challenges*. Proceedings of the 28th Conference on Computational Natural Language Learning.

- `doi:10.18653/v1/2024.conll-1.9` | aliases: `acl:2024.conll-1.9`
- doc_type: `conference` | tier: T3 | tags: dataset, formal, schemes | also in: formal, resources
- [landing](https://aclanthology.org/2024.conll-1.9/) | [OA PDF](https://aclanthology.org/2024.conll-1.9.pdf) (via acl)
- verified against: acl, bibcorpus:RicoStaedeli/NLP2025_CQG
- score 0.375 (cites 0.0, cocite 0.1429, keyword 1.0, venue 0.5)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "The development of Large Language Models (LLMs) has brought impressive performances on mitigation strategies against misinformation, such as counterargument generation." "Thus, in this work we investigate two complementary methods to create such a resource: (i) instantiating CQs templates as defined by Walton’s argumentation theory and (ii), using LLMs as CQs generators." For a debate-transcript argument database it supplies argumentation-scheme and critical-question structure, which is how stored inferences can be typed rather than left as untyped support links; and it supplies the formal semantics for deciding what stands once arguments and attacks are stored.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{figueras2024criticalq,
  title = {Critical Questions Generation: Motivation and Challenges},
  author = {Blanca Calvo Figueras and Rodrigo Agerri},
  year = {2024},
  booktitle = {Proceedings of the 28th Conference on Computational Natural Language Learning},
  doi = {10.18653/v1/2024.conll-1.9},
  url = {https://aclanthology.org/2024.conll-1.9/},
}
```

</details>

### T4 - Recent (2023-2026). LLM-era work; lower durability confidence, high build relevance.

#### Caleb Ziems et al. (2024). *Can Large Language Models Transform Computational Social Science?*. Computational Linguistics.

- `doi:10.1162/coli_a_00502` | aliases: `acl:2024.cl-1.8`
- doc_type: `journal` | tier: T4 | tags: extraction
- [landing](https://aclanthology.org/2024.cl-1.8/) | [OA PDF](https://aclanthology.org/2024.cl-1.8.pdf) (via acl)
- verified against: acl, bibcorpus:CogSciPrag/project_ideas
- score 0.6 (cites 0.0, cocite 0.5714, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "Towards this end, we contribute a set of prompting best practices and an extensive evaluation pipeline to measure the zero-shot performance of 13 language models on 25 representative English CSS benchmarks." "We conclude that the performance of today’s LLMs can augment the CSS research pipeline in two ways: (1) serving as zero-shot data annotators on human annotation teams, and (2) bootstrapping challenging creative generation tasks (e.g., explaining the underlying attributes of a text)." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations.

<details><summary>BibTeX</summary>

```bibtex
@article{ziems2024canlarge,
  title = {Can Large Language Models Transform Computational Social Science?},
  author = {Caleb Ziems and William Held and Omar Shaikh and Jiaao Chen and Zhehao Zhang and Diyi Yang},
  year = {2024},
  journal = {Computational Linguistics},
  doi = {10.1162/coli_a_00502},
  url = {https://aclanthology.org/2024.cl-1.8/},
}
```

</details>

#### Yanda Li et al. (2024). *Reason from Fallacy: Enhancing Large Language Models’ Logical Reasoning through Logical Fallacy Understanding*. Findings of the Association for Computational Linguistics: NAACL 2024.

- `doi:10.18653/v1/2024.findings-naacl.192` | aliases: `acl:2024.findings-naacl.192`
- doc_type: `conference` | tier: T4 | tags: fallacy, quality | also in: quality
- [landing](https://aclanthology.org/2024.findings-naacl.192/) | [OA PDF](https://aclanthology.org/2024.findings-naacl.192.pdf) (via acl)
- verified against: acl, bibcorpus:npnkhoi/memefal-paper
- score 0.45 (cites 0.0, cocite 0.1429, keyword 1.0, venue 1.0)
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

#### Sougata Saha and Rohini Srihari (2024). *Turiya at DialAM-2024: Inference Anchoring Theory Based LLM Parsers*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.13` | aliases: `acl:2024.argmining-1.13`
- doc_type: `workshop` | tier: T4 | tags: dialogue, extraction, formal | also in: dialogue, formal
- [landing](https://aclanthology.org/2024.argmining-1.13/) | [OA PDF](https://aclanthology.org/2024.argmining-1.13.pdf) (via acl)
- verified against: acl, bibcorpus:mystreamer/lt2326-final-project
- score 0.5458 (cites 0.0, cocite 0.5357, keyword 0.8333, venue 1.0)
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

#### Ramon Ruiz-Dolz and John Lawrence (2023). *Detecting Argumentative Fallacies in the Wild: Problems and Limitations of Large Language Models*. Proceedings of the 10th Workshop on Argument Mining.

- `doi:10.18653/v1/2023.argmining-1.1` | aliases: `acl:2023.argmining-1.1`
- doc_type: `workshop` | tier: T4 | tags: extraction, fallacy, schemes | also in: mining
- [landing](https://aclanthology.org/2023.argmining-1.1/) | [OA PDF](https://aclanthology.org/2023.argmining-1.1.pdf) (via acl)
- verified against: acl, bibcorpus:RicoStaedeli/NLP2025_CQG
- score 0.45 (cites 0.0, cocite 0.1429, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "In this paper, we present the first analysis of the limitations that these data-driven approaches could show in real situations." "For that purpose, we first create a validation corpus consisting of natural language argumentation schemes." For a debate-transcript argument database it supplies argumentation-scheme and critical-question structure, which is how stored inferences can be typed rather than left as untyped support links; and it types defective inference.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{ruizdolz2023detecting,
  title = {Detecting Argumentative Fallacies in the Wild: Problems and Limitations of Large Language Models},
  author = {Ramon Ruiz-Dolz and John Lawrence},
  year = {2023},
  booktitle = {Proceedings of the 10th Workshop on Argument Mining},
  doi = {10.18653/v1/2023.argmining-1.1},
  url = {https://aclanthology.org/2023.argmining-1.1/},
}
```

</details>

#### Christopher T. Small et al. (2023). *Opportunities and Risks of LLMs for Scalable Deliberation with Polis*. ArXiv.

- `title:8b3f61648db920b2a250f881b93c556a099c2a21`
- doc_type: `preprint` | tier: T4 | tags: dialogue | also in: dialogue
- [landing](https://api.semanticscholar.org/CorpusID:259211996)
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments
- score 0.4675 (cites 0.0, cocite 0.8929, keyword 0.5, venue 0.2)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

## 6.6 Datasets, tools, annotation guidelines (10 entries, quota 30)

### T3 - Dataset / tool / annotation guideline, including the guideline documents themselves.

#### Alan Ramponi, Agnese Daffara and Sara Tonelli (2025). *Fine-grained Fallacy Detection with Human Label Variation*. Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers).

- `doi:10.18653/v1/2025.naacl-long.34` | aliases: `acl:2025.naacl-long.34`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction, fallacy, quality | also in: quality
- [landing](https://aclanthology.org/2025.naacl-long.34/) | [OA PDF](https://aclanthology.org/2025.naacl-long.34.pdf) (via acl)
- verified against: acl, bibcorpus:npnkhoi/memefal-paper
- score 0.4292 (cites 0.0, cocite 0.1429, keyword 0.9167, venue 1.0)
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
- score 0.4083 (cites 0.0, cocite 0.1429, keyword 0.8333, venue 1.0)
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

#### Eleonora Mancini et al. (2024). *MAMKit: A Comprehensive Multimodal Argument Mining Toolkit*. Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024).

- `doi:10.18653/v1/2024.argmining-1.7` | aliases: `acl:2024.argmining-1.7`
- doc_type: `workshop` | tier: T3 | tags: dataset, extraction | also in: mining
- [landing](https://aclanthology.org/2024.argmining-1.7) | [OA PDF](https://aclanthology.org/2024.argmining-1.7.pdf) (via acl)
- verified against: acl, bibcorpus:StefanoColamonaco/StefanoColamonaco.github.io
- score 0.4 (cites 0.0, cocite 0.0, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "However, the research community still lacks a comprehensive platform where results can be easily reproduced, and methods and models can be stored, compared, and tested against a variety of benchmarks." "To address these challenges, we propose MAMKit, an open, publicly available, PyTorch toolkit that consolidates datasets and models, providing a standardized platform for experimentation." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{mancini2024mamkita,
  title = {MAMKit: A Comprehensive Multimodal Argument Mining Toolkit},
  author = {Eleonora Mancini and Federico Ruggeri and Stefano Colamonaco and Andrea Zecca and Samuele Marro and Paolo Torroni},
  year = {2024},
  booktitle = {Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024)},
  doi = {10.18653/v1/2024.argmining-1.7},
  url = {https://aclanthology.org/2024.argmining-1.7},
}
```

</details>

#### Georgi Karadzhov, Tom Stafford and Andreas Vlachos (2021). *DeliData: A Dataset for Deliberation in Multi-party Problem Solving*. Proceedings of the ACM on Human-Computer Interaction.

- `title:a53d191087c04c6d49d9d46488abffa0090e89de`
- doc_type: `journal` | tier: T3 | tags: dataset, dialogue | also in: dialogue
- [landing](https://api.semanticscholar.org/CorpusID:236975941)
- verified against: bibcorpus:dimits-ts/llm_moderation_research, bibcorpus:dimits-ts/synthetic_moderation_experiments
- score 0.5125 (cites 0.0, cocite 0.8929, keyword 0.5, venue 0.5)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

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

#### Liat Ein-Dor et al. (2020). *Corpus Wide Argument Mining - A Working Solution*. Proceedings of the Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, The Thirty-Second Innovative Applications of Artificial Intelligence Conference, IAAI 2020, The Tenth AAAI Symposium on Educational Advances in Artificial Intelligence, EAAI 2020.

- `doi:10.1609/aaai.v34i05.6270`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction | also in: mining
- [landing](https://doi.org/10.1609/aaai.v34i05.6270)
- verified against: bibcorpus:NeWildeSache/argument-mining-in-the-web-archive, bibcorpus:borgr/publications, bibcorpus:m0re4u/paper-database | note: bibcorpus:lihebi/biber-dist: venue mismatch ('Proceedings of the Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, The Thirty-Second Innovative Applications of Artificial Intellige…
- score 0.5458 (cites 0.0, cocite 0.7143, keyword 0.5833, venue 1.0)
- annotation: none. No abstract or full text was retrieved for this entry (`grounded_on: none`), so nothing is written about its content.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{eindor2020corpuswid,
  title = {Corpus Wide Argument Mining - A Working Solution},
  author = {Liat Ein-Dor and Eyal Shnarch and Lena Dankin and Alon Halfon and Benjamin Sznajder and Ariel Gera and Carlos Alzate and Martin Gleize and Leshem Choshen and Yufang Hou and Yonatan Bilu and Ranit Aharonov and Noam Slonim},
  year = {2020},
  booktitle = {Proceedings of the Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, The Thirty-Second Innovative Applications of Artificial Intelligence Conference, IAAI 2020, The Tenth AAAI Symposium on Educational Advances in Artificial Intelligence, EAAI 2020},
  doi = {10.1609/aaai.v34i05.6270},
  url = {https://doi.org/10.1609/aaai.v34i05.6270},
}
```

</details>

#### Nils Reimers et al. (2019). *Classification and Clustering of Arguments with Contextualized Word Embeddings*. Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics.

- `doi:10.18653/v1/p19-1054` | aliases: `acl:P19-1054`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue, extraction
- [landing](https://aclanthology.org/P19-1054/) | [OA PDF](https://aclanthology.org/P19-1054.pdf) (via acl)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive, bibcorpus:m0re4u/paper-database
- score 0.5792 (cites 0.0, cocite 0.5714, keyword 0.9167, venue 1.0)
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

#### Yamen Ajjour, Milad Alshomary, Henning Wachsmuth and Benno Stein (2019). *Modeling Frames in Argumentation*. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP).

- `doi:10.18653/v1/d19-1290` | aliases: `acl:D19-1290`
- doc_type: `conference` | tier: T3 | tags: dataset, dialogue, extraction, quality | also in: dialogue, mining, quality
- [landing](https://aclanthology.org/D19-1290/) | [OA PDF](https://aclanthology.org/D19-1290.pdf) (via acl)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive
- score 0.4625 (cites 0.0, cocite 0.7143, keyword 0.25, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "This paper introduces frame identification, which is the task of splitting a set of arguments into non-overlapping frames." "We present a fully unsupervised approach to this task, which first removes topical information and then identifies frames using clustering." For a debate-transcript argument database it supplies dialogue-level structure - who said what, in reply to what - which is exactly the relation layer a debate-transcript database has to store; and it gives quality dimensions or a scoring target.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{ajjour2019modelingf,
  title = {Modeling Frames in Argumentation},
  author = {Yamen Ajjour and Milad Alshomary and Henning Wachsmuth and Benno Stein},
  year = {2019},
  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
  doi = {10.18653/v1/d19-1290},
  url = {https://aclanthology.org/D19-1290/},
}
```

</details>

#### Artem Chernodub et al. (2019). *TARGER: Neural Argument Mining at Your Fingertips*. Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics: System Demonstrations.

- `doi:10.18653/v1/p19-3031` | aliases: `acl:P19-3031`
- doc_type: `conference` | tier: T3 | tags: dataset, extraction | also in: mining
- [landing](https://aclanthology.org/P19-3031/) | [OA PDF](https://aclanthology.org/P19-3031.pdf) (via acl)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive
- score 0.6 (cites 0.0, cocite 0.5714, keyword 1.0, venue 1.0)
- annotation (`grounded_on: abstract`): Contribution, in the work's own words from its abstract: "We present TARGER, an open source neural argument mining framework for tagging arguments in free input texts and for keyword-based retrieval of arguments from an argument-tagged web-scale corpus." "The currently available models are pre-trained on three recent argument mining datasets and enable the use of neural argument mining without any reproducibility effort on the user’s side." For a debate-transcript argument database it defines the extraction step that turns raw transcript text into stored components and relations; and it is a reusable resource whose annotation structure a transcript schema can copy rather than reinvent.

<details><summary>BibTeX</summary>

```bibtex
@inproceedings{chernodub2019targerne,
  title = {TARGER: Neural Argument Mining at Your Fingertips},
  author = {Artem Chernodub and Oleksiy Oliynyk and Philipp Heidenreich and Alexander Bondarenko and Matthias Hagen and Chris Biemann and Alexander Panchenko},
  year = {2019},
  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
  doi = {10.18653/v1/p19-3031},
  url = {https://aclanthology.org/P19-3031/},
}
```

</details>

#### Henning Wachsmuth et al. (2017). *Building an Argument Search Engine for the Web*. Proceedings of the 4th Workshop on Argument Mining.

- `doi:10.18653/v1/w17-5106` | aliases: `acl:W17-5106`
- doc_type: `workshop` | tier: T3 | tags: dataset, extraction | also in: mining
- [landing](https://aclanthology.org/W17-5106/) | [OA PDF](https://aclanthology.org/W17-5106.pdf) (via acl)
- verified against: acl, bibcorpus:NeWildeSache/argument-mining-in-the-web-archive, bibcorpus:allenai/ir_datasets, bibcorpus:jbingel/emnlp2017-handbook, bibcorpus:m0re4u/paper-database | note: venue not corroborated by both sources
- score 0.4417 (cites 0.0, cocite 0.7143, keyword 0.1667, venue 1.0)
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
