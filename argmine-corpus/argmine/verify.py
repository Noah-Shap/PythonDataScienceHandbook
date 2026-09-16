"""Phase 3 - verify.

A record is ``verified`` only when at least two independent sources agree on title,
first author, year and venue. Anything else is ``unverified`` with a note saying exactly
what disagreed, and unverified records never reach the main bibliography - they go to
``99-unverified-and-rejected.md``.

Independence: each API counts once; the BibTeX corroboration corpus counts once per
*distinct repository* whose bibliography is not simply a copy of the ACL Anthology's own
BibTeX export, since two unrelated research groups listing the same work with the same
metadata is genuine corroboration.
"""
from __future__ import annotations

from rapidfuzz import fuzz

from .cache import advance
from .util import iso_now, norm_text, norm_title, surname

TITLE_AGREE = 95.0
SOURCE_PRIORITY = ["acl", "crossref", "openalex", "semanticscholar", "arxiv", "bibcorpus"]

VENUE_ALIASES = {
    "computational linguistics": ["cl", "coli", "mit press"],
    "annual meeting of the association for computational linguistics": ["acl"],
    "empirical methods in natural language processing": ["emnlp"],
    "north american chapter of the association for computational linguistics": ["naacl"],
    "european chapter of the association for computational linguistics": ["eacl"],
    "international conference on computational linguistics": ["coling"],
    "language resources and evaluation": ["lrec"],
    "workshop on argument mining": ["argmining", "argmin", "arg-mining"],
    "artificial intelligence": ["aij", "artif intell"],
    "knowledge engineering review": ["ker"],
    "argument & computation": ["argument and computation", "argcom"],
    "transactions of the association for computational linguistics": ["tacl"],
    "association for the advancement of artificial intelligence": ["aaai"],
    "international joint conference on artificial intelligence": ["ijcai"],
}


# -- comparison -----------------------------------------------------------
def venue_compatible(a: str, b: str) -> tuple[bool, str]:
    va, vb = norm_text(a), norm_text(b)
    if not va or not vb:
        return True, "venue not corroborated by both sources"
    if va in vb or vb in va:
        return True, ""
    if fuzz.token_set_ratio(va, vb) >= 80:
        return True, ""
    for canon, aliases in VENUE_ALIASES.items():
        forms = [canon] + aliases
        if any(f in va for f in forms) and any(f in vb for f in forms):
            return True, ""
    return False, f"venue mismatch ({a!r} vs {b!r})"


def views_match(a: dict, b: dict) -> tuple[bool, list[str]]:
    notes = []
    if fuzz.ratio(norm_title(a["title"]), norm_title(b["title"])) < TITLE_AGREE:
        return False, [f"title mismatch ({a['source']} vs {b['source']})"]
    fa = surname(a["authors"][0]) if a.get("authors") else ""
    fb = surname(b["authors"][0]) if b.get("authors") else ""
    if fa and fb and fa != fb:
        # Author order differs between sources often enough to check membership too.
        others = {surname(x) for x in (a.get("authors") or [])} | {surname(x) for x in (b.get("authors") or [])}
        if not (fa in others and fb in others):
            return False, [f"first author mismatch ({fa!r} vs {fb!r})"]
        notes.append(f"author order differs ({fa} / {fb})")
    elif not fa or not fb:
        notes.append("author list missing from one source")
    if a.get("year") and b.get("year") and abs(int(a["year"]) - int(b["year"])) > 1:
        return False, [f"year mismatch ({a['year']} vs {b['year']})"]
    ok, note = venue_compatible(a.get("venue", ""), b.get("venue", ""))
    if not ok:
        return False, [note]
    if note:
        notes.append(note)
    return True, notes


def _source_label(view: dict) -> str:
    if view["source"] == "bibcorpus":
        return f"bibcorpus:{view['extra'].get('repo', '?')}"
    return view["source"]


def views_agree(views: list[dict]) -> tuple[str, list[str], str]:
    """Returns (status, corroborating source labels, notes)."""
    if not views:
        return "unverified", [], "no source returned a record"
    primary = _consensus_view(views)
    labels, notes, conflicts = {_source_label(primary)}, [], []
    for other in views:
        if other is primary:
            continue
        ok, why = views_match(primary, other)
        if ok:
            labels.add(_source_label(other))
            notes.extend(why)
        else:
            conflicts.extend(f"{_source_label(other)}: {w}" for w in why)
    independent = {l.split(":")[0] if not l.startswith("bibcorpus") else l for l in labels}
    status = "verified" if len(independent) >= 2 else "unverified"
    note = "; ".join(dict.fromkeys(notes + conflicts))[:600]
    if status == "unverified" and not conflicts:
        note = (note + "; only one independent source could be reached").strip("; ")
    return status, sorted(labels), note


def _consensus_view(views: list[dict]) -> dict:
    """The view the most other views agree with, breaking ties by source priority.

    Comparing everything against an arbitrary first view would let one outlier - a
    bibliography listing a later edition of a classic, say - decide that a work no source
    actually disputes is unverified.
    """
    def priority(v):
        return SOURCE_PRIORITY.index(v["source"]) if v["source"] in SOURCE_PRIORITY else 99

    best, best_key = views[0], None
    for view in views:
        agree = sum(1 for other in views if other is not view and views_match(view, other)[0])
        key = (agree, -priority(view), len(view.get("abstract") or ""))
        if best_key is None or key > best_key:
            best, best_key = view, key
    return best


def merge_views(views: list[dict]) -> dict:
    """Fold several source views into the fields of one registry record."""
    ordered = sorted(views, key=lambda v: (SOURCE_PRIORITY.index(v["source"])
                                           if v["source"] in SOURCE_PRIORITY else 99))
    best = ordered[0]
    aliases, urls = set(), {}
    authors, abstract, venue, doc_type, year, title = [], "", "", "", None, ""
    for v in ordered:
        aliases |= set(v.get("aliases", []))
        for k, val in (v.get("urls") or {}).items():
            if val and not urls.get(k):
                urls[k] = val
        if len(v.get("authors") or []) > len(authors):
            authors = v["authors"]
        if len(v.get("abstract") or "") > len(abstract):
            abstract = v["abstract"]
        venue = venue or v.get("venue", "")
        doc_type = doc_type or v.get("doc_type", "")
        year = year if year is not None else v.get("year")
        title = title or v.get("title", "")
    return {
        "title": best.get("title") or title,
        "authors": authors or best.get("authors", []),
        "year": best.get("year") or year,
        "venue": best.get("venue") or venue,
        "doc_type": best.get("doc_type") or doc_type,
        "abstract": abstract,
        "aliases": sorted(a for a in aliases if a),
        "urls": urls,
    }


# -- resolution -----------------------------------------------------------
def _best(views: list[dict], title: str, year=None) -> dict | None:
    scored = []
    for v in views:
        if not v.get("title"):
            continue
        s = fuzz.ratio(norm_title(v["title"]), norm_title(title))
        if year and v.get("year"):
            s -= min(abs(int(v["year"]) - int(year)), 5) * 2
        scored.append((s, v))
    if not scored:
        return None
    scored.sort(key=lambda x: -x[0])
    return scored[0][1] if scored[0][0] >= TITLE_AGREE - 8 else None


def resolve_views(ctx, title: str, year=None, authors=None, doi: str = "",
                  aliases=None) -> list[dict]:
    """Ask every reachable source about one work; returns one best view per source
    (plus one per independent bibliography repository)."""
    out: list[dict] = []
    aliases = list(aliases or [])
    acl_id = next((a.split(":", 1)[1] for a in aliases if a.startswith("acl:")), "")

    if ctx.live("acl"):
        view = ctx.acl.get(acl_id) if acl_id else None
        view = view or _best(ctx.acl.lookup_title(title, year), title, year)
        if view:
            out.append(view)
            doi = doi or next((a.split(":", 1)[1] for a in view["aliases"] if a.startswith("doi:")), "")

    if ctx.live("crossref"):
        view = ctx.crossref.by_doi(doi) if doi else None
        view = view or _best(ctx.crossref.search_bibliographic(
            title, (authors or [""])[0] if authors else "", year), title, year)
        if view:
            out.append(view)

    if ctx.live("openalex"):
        view = ctx.openalex.by_doi(doi) if doi else None
        view = view or _best(ctx.openalex.search_title(title, year), title, year)
        if view:
            out.append(view)

    if ctx.live("semanticscholar"):
        view = ctx.s2.by_doi(doi) if doi else None
        view = view or _best(ctx.s2.search(title, limit=10), title, year)
        if view:
            out.append(view)

    if ctx.live("arxiv"):
        view = _best(ctx.arxiv.search(title, limit=5, title_only=True), title, year)
        if view:
            out.append(view)

    if ctx.live("bibcorpus"):
        per_repo: dict[str, dict] = {}
        for v in ctx.bib.lookup(title, year):
            if v["extra"].get("anthology_derived"):
                continue
            repo = v["extra"].get("repo", "?")
            prev = per_repo.get(repo)
            if prev is None or _rank(v, year) > _rank(prev, year):
                per_repo[repo] = v
        out.extend(per_repo.values())
    return out


def _rank(v: dict, year=None) -> tuple:
    """Prefer the edition the caller asked about, then the most complete record.

    Classics are re-issued (Toulmin 1958 / 2003), so a bibliography's year is only
    evidence about the edition it lists; picking the closest one keeps the comparison
    honest instead of manufacturing a year conflict.
    """
    proximity = 0
    if year and v.get("year"):
        proximity = -min(abs(int(v["year"]) - int(year)), 50)
    return (proximity, _richness(v))


def _richness(v: dict) -> int:
    return (2 * bool(v.get("doi")) + bool(v.get("venue")) + bool(v.get("year"))
            + min(len(v.get("authors") or []), 5))


def resolve_oa_pdf(ctx, rec: dict) -> tuple[str, str]:
    """OA PDF resolution order: OpenAlex best_oa_location, Unpaywall, arXiv, ACL Anthology."""
    doi = next((a.split(":", 1)[1] for a in [rec["id"]] + rec.get("aliases", [])
                if a.startswith("doi:")), "")
    if ctx.live("openalex") and doi:
        view = ctx.openalex.by_doi(doi)
        if view and view["urls"].get("pdf_oa"):
            return view["urls"]["pdf_oa"], "openalex"
    if ctx.live("unpaywall") and doi:
        hit = ctx.unpaywall.oa_pdf(doi)
        if hit:
            return hit["pdf"], "unpaywall"
    arx = next((a.split(":", 1)[1] for a in [rec["id"]] + rec.get("aliases", [])
                if a.startswith("arxiv:")), "")
    if arx:
        return f"https://arxiv.org/pdf/{arx}", "arxiv"
    acl_id = next((a.split(":", 1)[1] for a in [rec["id"]] + rec.get("aliases", [])
                   if a.startswith("acl:")), "")
    if acl_id:
        return f"https://aclanthology.org/{acl_id}.pdf", "acl"
    return "", ""


# -- phase ----------------------------------------------------------------
def run(ctx) -> dict:
    reg = ctx.registry
    ctx.prepare_local_sources()
    todo = reg.with_status("candidate")
    summary = {"considered": len(todo), "verified": 0, "unverified": 0, "oa_resolved": 0}
    for rec in todo:
        views = resolve_views(ctx, rec["title"], rec.get("year"), rec.get("authors"),
                              aliases=rec.get("aliases", []) + [rec["id"]])
        status, sources, notes = views_agree(views)
        merged = merge_views(views) if views else {}
        for field in ("title", "authors", "year", "venue", "doc_type", "abstract"):
            if merged.get(field) and not rec.get(field):
                rec[field] = merged[field]
        if merged.get("abstract") and len(merged["abstract"]) > len(rec.get("abstract") or ""):
            rec["abstract"] = merged["abstract"]
        for alias in merged.get("aliases", []):
            if alias not in rec["aliases"] and alias != rec["id"]:
                rec["aliases"].append(alias)
        rec["urls"] = {**merged.get("urls", {}), **{k: v for k, v in rec["urls"].items() if v}}
        rec["verification"] = {"status": status, "sources": sources, "checked_at": iso_now(),
                               "notes": notes}
        pdf, via = resolve_oa_pdf(ctx, rec)
        if pdf:
            rec["urls"]["pdf_oa"] = pdf
            rec["urls"]["pdf_oa_source"] = via
            summary["oa_resolved"] += 1
        if status == "verified":
            advance(rec, "verified")
            reg.frontier_add(rec["id"], rec["title"])
            summary["verified"] += 1
        else:
            summary["unverified"] += 1
        rec["updated_at"] = iso_now()
    return summary
