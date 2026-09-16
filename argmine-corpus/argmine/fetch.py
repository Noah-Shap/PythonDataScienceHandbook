"""Phase 5a - fetch.

Downloads open-access PDFs (T1-T3 first, then T4), shallow-clones the dataset and tool
repositories behind T3 entries, copies their READMEs and any annotation guideline into
``corpus/text/guidelines/``, and writes ``deliverables/05-fetch-manifest.csv`` covering
*every* entry - including the ones this environment could not fetch - so they can be
fetched elsewhere.

Politeness: only hosts on the open-access allowlist (or URLs Unpaywall / OpenAlex
resolved as open access) are ever requested. No publisher paywall is touched.
"""
from __future__ import annotations

import csv
import hashlib
import re
import shutil
from pathlib import Path
from urllib.parse import urlsplit

from .cache import advance
from .util import iso_now, norm_text, safe_id

STOP = {"the", "a", "an", "of", "for", "and", "in", "on", "to", "with", "from", "using",
        "via", "by", "at", "is", "are", "new", "towards", "toward", "into", "its", "their"}
# Words every second repository in this field uses: matching on these alone is a
# coincidence, not evidence that this repo belongs to this paper.
GENERIC = {"argument", "arguments", "argumentation", "argumentative", "mining", "corpus",
           "corpora", "dataset", "datasets", "data", "task", "tasks", "classification",
           "detection", "identification", "analysis", "text", "neural", "model", "models",
           "learning", "annotation", "annotated", "quality", "code", "paper", "nlp",
           "language", "based", "large", "study", "approach"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def _tokens(text: str) -> set[str]:
    return {t for t in re.split(r"[^a-z0-9]+", norm_text(text)) if len(t) > 2 and t not in STOP}


# -- repositories ---------------------------------------------------------
def link_repos(ctx) -> dict:
    """Attach a GitHub repository to resource records, on token-overlap evidence."""
    reg = ctx.registry
    items = []
    for payload in ctx.gh.cache.get("repo_queries", {}).values():
        items.extend(payload.get("items", []))
    seen = {}
    for it in items:
        seen[it["full_name"]] = it
    linked = {}
    for rec in reg.records.values():
        if rec.get("urls", {}).get("repo"):
            continue
        if rec.get("tier") != 3 and "resources" not in rec.get("area", []):
            continue
        title_tokens = _tokens(rec.get("title", ""))
        best, best_key = None, None
        for full_name, it in seen.items():
            repo_tokens = _tokens(full_name.split("/")[-1].replace("-", " ").replace("_", " "))
            repo_tokens |= _tokens(it.get("description", ""))
            overlap = title_tokens & repo_tokens
            distinctive = overlap - GENERIC
            key = (len(distinctive), len(overlap))
            if best_key is None or key > best_key:
                best, best_key = (full_name, overlap, distinctive), key
        # Either two words that are specific to this work, or a broad overlap that includes
        # at least one specific word.
        if best and (best_key[0] >= 2 or (best_key[0] >= 1 and best_key[1] >= 4)):
            full_name, overlap, distinctive = best
            rec.setdefault("urls", {})["repo"] = f"https://github.com/{full_name}"
            rec["discovered_from"].append({"id": f"github:{full_name}", "via": f"github:{full_name}"})
            rec["verification"]["notes"] = (
                rec["verification"].get("notes", "") +
                f" repo linked on distinctive title/description overlap: "
                f"{sorted(distinctive)} (all shared words: {sorted(overlap)})").strip()
            linked[rec["id"]] = full_name
    return linked


def copy_guidelines(ctx, rec: dict, repo_path: Path) -> list[str]:
    """README plus anything that looks like an annotation manual, kept as its own document."""
    cfg = ctx.cfg
    out_dir = cfg.corpus / "text" / "guidelines"
    out_dir.mkdir(parents=True, exist_ok=True)
    copied = []
    name, text = ctx.gh.readme(repo_path)
    if text:
        dest = out_dir / f"{safe_id(rec['id'])}__README.md"
        dest.write_text(text, encoding="utf-8")
        copied.append(str(dest.relative_to(cfg.root)))
    for f in ctx.gh.guideline_files(repo_path, cfg["fetch"]["guideline_patterns"]):
        dest = out_dir / f"{safe_id(rec['id'])}__{f.name}"
        try:
            shutil.copyfile(f, dest)
            copied.append(str(dest.relative_to(cfg.root)))
        except OSError:
            continue
    return copied


# -- pdfs -----------------------------------------------------------------
def oa_allowed(cfg, rec: dict, url: str) -> bool:
    if not url:
        return False
    if rec.get("urls", {}).get("pdf_oa_source") in ("unpaywall", "openalex"):
        return True
    host = urlsplit(url).netloc.lower()
    return any(host == h or host.endswith("." + h) or h in url
               for h in cfg["fetch"].get("oa_hosts", []))


def fetch_pdf(ctx, rec: dict) -> tuple[bool, str]:
    cfg = ctx.cfg
    url = rec.get("urls", {}).get("pdf_oa", "")
    if not url:
        return False, "no open-access PDF url resolved"
    if not oa_allowed(cfg, rec, url):
        return False, f"host not on the open-access allowlist ({urlsplit(url).netloc})"
    source = ("arxiv" if "arxiv.org" in url
              else "acl_web" if "aclanthology.org" in url
              else rec.get("urls", {}).get("pdf_oa_source") or "oa_host")
    if ctx.http.unreachable(source):
        reason = ctx.http.status.get(source, {}).get("reason", "")
        return False, f"{source} unreachable from this environment ({reason[:60]})"
    dest = cfg.corpus / "pdfs" / f"{safe_id(rec['id'])}.pdf"
    ok = ctx.http.download(source, url, dest)
    if not ok:
        return False, "download failed or response was not a PDF"
    digest = sha256_file(dest)
    if dest.stat().st_size > int(cfg["fetch"].get("max_pdf_mb", 40)) * 1024 * 1024:
        dest.unlink(missing_ok=True)
        return False, "PDF exceeded the size limit"
    rec.setdefault("files", {})["pdf"] = str(dest.relative_to(cfg.root))
    rec["files"]["pdf_sha256"] = digest
    return True, "fetched"


# -- manifest -------------------------------------------------------------
def write_manifest(ctx) -> Path:
    cfg, reg = ctx.cfg, ctx.registry
    path = cfg.deliverables / "05-fetch-manifest.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for rec in sorted(reg.records.values(), key=lambda r: (r.get("tier") or 9, r.get("id", ""))):
        files = rec.get("files", {})
        rows.append({
            "id": rec["id"],
            "title": rec.get("title", ""),
            "authors": "; ".join(rec.get("authors", [])[:4]),
            "year": rec.get("year") or "",
            "tier": rec.get("tier") or "",
            "area": "|".join(rec.get("area", [])),
            "doc_type": rec.get("doc_type", ""),
            "url": rec.get("urls", {}).get("pdf_oa") or rec.get("urls", {}).get("landing", ""),
            "landing": rec.get("urls", {}).get("landing", ""),
            "repo": rec.get("urls", {}).get("repo", ""),
            "source": rec.get("urls", {}).get("pdf_oa_source", ""),
            "fetched": bool(files.get("pdf")),
            "sha256": files.get("pdf_sha256", ""),
            "reason_not_fetched": files.get("pdf_status", "") if not files.get("pdf") else "",
        })
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else
                                ["id", "title", "authors", "year", "tier", "area", "doc_type",
                                 "url", "landing", "repo", "source", "fetched", "sha256",
                                 "reason_not_fetched"])
        writer.writeheader()
        writer.writerows(rows)
    return path


# -- phase ----------------------------------------------------------------
def run(ctx) -> dict:
    cfg, reg = ctx.cfg, ctx.registry
    ctx.prepare_local_sources()
    linked = link_repos(ctx)
    summary = {"repos_linked": len(linked), "pdfs_fetched": 0, "pdfs_cached": 0,
               "pdfs_unavailable": 0, "repos_cloned": 0, "guidelines": 0, "reasons": {}}

    todo = [r for r in reg.records.values() if r.get("status") in ("tiered", "fetched")]
    todo.sort(key=lambda r: (cfg["fetch"]["tier_priority"].index(r["tier"])
                             if r.get("tier") in cfg["fetch"]["tier_priority"] else 9))
    for rec in todo:
        files = rec.setdefault("files", {})
        pdf_path = cfg.path(files["pdf"]) if files.get("pdf") else None
        if pdf_path and pdf_path.exists() and files.get("pdf_sha256") == sha256_file(pdf_path):
            summary["pdfs_cached"] += 1          # layer 2: already fetched, hash unchanged
        else:
            ok, reason = fetch_pdf(ctx, rec)
            if ok:
                summary["pdfs_fetched"] += 1
                files.pop("pdf_status", None)
            else:
                summary["pdfs_unavailable"] += 1
                files["pdf_status"] = reason
                summary["reasons"][reason] = summary["reasons"].get(reason, 0) + 1

        repo_url = rec.get("urls", {}).get("repo", "")
        if repo_url and rec.get("tier") == 3:
            full_name = repo_url.rstrip("/").split("github.com/")[-1]
            path = ctx.gh.clone(full_name, depth=int(cfg["fetch"].get("repo_clone_depth", 1)),
                                log=ctx.log)
            if path:
                summary["repos_cloned"] += 1
                copied = copy_guidelines(ctx, rec, path)
                files.setdefault("guidelines", []).extend(
                    c for c in copied if c not in files.get("guidelines", []))
                files["repo_dir"] = str(path.relative_to(cfg.root))
                files["repo_licence"] = ctx.gh.licence(path)
                files["repo_commit"] = ctx.gh.head(full_name)
                summary["guidelines"] += len(copied)
        rec["updated_at"] = iso_now()
        advance(rec, "fetched")

    summary["manifest"] = str(write_manifest(ctx).relative_to(cfg.root))
    summary["manifest_rows"] = len(reg.records)
    return summary


def paragraph(summary: dict) -> str:
    reasons = "; ".join(f"{k} ({v})" for k, v in sorted(summary.get("reasons", {}).items(),
                                                        key=lambda kv: -kv[1])[:3])
    return (f"Phase fetch: linked {summary.get('repos_linked', 0)} GitHub repositories to "
            f"resource records, downloaded {summary.get('pdfs_fetched', 0)} open-access PDFs "
            f"({summary.get('pdfs_cached', 0)} already present with a matching hash, "
            f"{summary.get('pdfs_unavailable', 0)} unavailable), cloned "
            f"{summary.get('repos_cloned', 0)} dataset/tool repositories and copied "
            f"{summary.get('guidelines', 0)} README/guideline documents. "
            f"Wrote {summary.get('manifest')} covering all {summary.get('manifest_rows', 0)} "
            f"entries. Main reasons a PDF was not fetched: {reasons or 'none'}.")
