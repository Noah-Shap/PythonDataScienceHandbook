"""A BibTeX corroboration corpus mined from GitHub repositories.

Why this exists: the citation graph APIs (Semantic Scholar, OpenAlex, Crossref) are the
pipeline's first-choice sources, but they are not reachable from every environment. The
bibliographies that argumentation researchers ship with their code are: each ``.bib``
file in a cloned repository is an independently curated reference list, which gives

* a second, independent metadata record for a work (title / authors / year / venue), and
* a co-citation signal - two works listed in the same curated bibliography were judged
  relevant to the same piece of work, which is exactly what the ``cocite`` component of
  the scoring function is trying to measure.

Repositories are pinned by commit in ``corpus/bib_repos.json`` so the corpus is
reproducible, and clones are never re-fetched once present.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

from rapidfuzz import fuzz, process

from ..util import iso_now, norm_title
from . import bibtex
from .base import candidate

MARKER = ".argmine_clone.json"
ENTRY_START_RE = re.compile(r"^[ \t]*@[A-Za-z]+[ \t]*[{(]", re.MULTILINE)
SMALL_FILE_BYTES = 200_000
# Cheap substring gate for the large multi-venue dumps: an entry that mentions none of
# these is not argumentation literature and is not worth parsing. Small bibliographies
# are always parsed in full, because their co-occurrence structure is the point.
RELEVANCE_TERMS = (
    "argumentation", "argumentative", "argument min", "argument quality", "argument graph",
    "argument interchange", "argument structure", "counterargument", "counter-argument",
    "fallac", "toulmin", "defeasible", "persuasi", "dialectic", "rhetoric", "debate",
    "enthymeme", "phan minh dung", "acceptability of arguments", "changemyview",
    "argument retrieval", "argument search", "claim detection", "stance",
)
ANTHOLOGY_KEY_RE = re.compile(r"^[a-z\-]+-(etal-)?(19|20)\d{2}-[a-z\-]+$")
SCHEMA = 4


class BibCorpus:
    name = "bibcorpus"

    def __init__(self, cfg, http=None):
        self.cfg, self.http = cfg, http
        spec = cfg["sources"]["bibcorpus"]
        self.clone_root = cfg.path(spec["clone_root"])
        self.max_bib_bytes = int(spec.get("max_bib_bytes", 8_000_000))
        self.max_repos = int(spec.get("max_repos", 60))
        self.curated_max = int(spec.get("curated_max_entries", 300))
        self.exclude = set(spec.get("exclude_repos", []))
        self.prune = bool(spec.get("prune_after_clone", True))
        self.include = list(spec.get("include_repos", []))
        self.repos_path = cfg.corpus / "bib_repos.json"
        self.index_path = cfg.corpus / "bib_index.json"
        self.entries: list[dict] = []
        self.by_title: dict[str, list[int]] = {}
        self.title_files: dict[str, set[str]] = {}
        self.files: dict[str, dict] = {}
        self._ntitles: list[str] = []
        self._acl_bibkeys: set[str] | None = None
        self._match_cache: dict[tuple[str, float], str] = {}

    def set_anthology_bibkeys(self, keys) -> None:
        """Teach the corpus which bibkeys the ACL Anthology itself issues.

        Without this the test is a guess from the key's shape, which wrongly flags other
        anthologies (the IR Anthology uses the same ``author-year-word`` convention) as
        re-exports and throws away real corroboration.
        """
        self._acl_bibkeys = {k.lower() for k in keys if k}

    def _anthology_derived(self, key: str) -> bool:
        k = (key or "").lower()
        if self._acl_bibkeys is not None:
            return k in self._acl_bibkeys
        return bool(ANTHOLOGY_KEY_RE.match(k))

    # -- repo list ---------------------------------------------------------
    def load_repos(self) -> list[dict]:
        if not self.repos_path.exists():
            return []
        return json.loads(self.repos_path.read_text()).get("repos", [])

    def save_repos(self, repos: list[dict]) -> None:
        self.repos_path.parent.mkdir(parents=True, exist_ok=True)
        self.repos_path.write_text(
            json.dumps({"repos": sorted(repos, key=lambda r: r["full_name"])}, indent=2) + "\n")

    def add_repo(self, full_name: str, why: str, discovered_via: str) -> dict:
        repos = self.load_repos()
        existing = next((r for r in repos if r["full_name"] == full_name), None)
        if existing:
            return existing
        entry = {"full_name": full_name, "url": f"https://github.com/{full_name}.git",
                 "why": why, "discovered_via": discovered_via, "sha": "", "bib_files": 0,
                 "bib_entries": 0, "cloned": False}
        repos.append(entry)
        self.save_repos(repos)
        return entry

    def discover_from_search_cache(self, gh, log=print) -> list[str]:
        """Turn cached GitHub code-search hits (``*.bib`` files) into repos to mine.

        Idempotent: repositories already listed in corpus/bib_repos.json are left alone,
        and excluded repositories (verbatim ACL Anthology re-exports) are never added.
        """
        added = []
        for query, payload in sorted(gh.cache.get("code_queries", {}).items()):
            for item in payload.get("items", []):
                full = item.get("repository", "")
                if not full or full in self.exclude:
                    continue
                if any(r["full_name"] == full for r in self.load_repos()):
                    continue
                self.add_repo(full, why=f"carries {item.get('path', '*.bib')}",
                              discovered_via=f"github-code-search:{query}")
                added.append(full)
        for spec in self.include:
            if spec["full_name"] in self.exclude:
                continue
            if not any(r["full_name"] == spec["full_name"] for r in self.load_repos()):
                self.add_repo(spec["full_name"], why=spec.get("why", "curated addition"),
                              discovered_via="config:sources.bibcorpus.include_repos")
                added.append(spec["full_name"])
        if added:
            log(f"  bib corpus: {len(added)} new repositories queued for cloning")
        return added

    def clone_dir(self, full_name: str) -> Path:
        return self.clone_root / full_name.replace("/", "__")

    def ensure_clones(self, log=print) -> list[dict]:
        """Shallow-clone every configured repo once. Existing clones are never re-fetched."""
        all_repos = self.load_repos()
        repos, rest = all_repos[: self.max_repos], all_repos[self.max_repos:]
        for entry in repos:
            path = self.clone_dir(entry["full_name"])
            marker = path / MARKER
            if marker.exists():
                entry["cloned"] = True
                entry.setdefault("sha", json.loads(marker.read_text()).get("sha", ""))
                continue
            if not (path / ".git").exists():
                path.parent.mkdir(parents=True, exist_ok=True)
                try:
                    subprocess.run(["git", "clone", "--depth", "1", entry["url"], str(path)],
                                   capture_output=True, text=True, check=True, timeout=600)
                except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError) as exc:
                    entry["cloned"] = False
                    entry["error"] = str(exc)[:200]
                    log(f"  clone failed: {entry['full_name']}")
                    continue
            entry["cloned"] = True
            entry.pop("error", None)
            try:
                entry["sha"] = subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"],
                                              capture_output=True, text=True, check=True).stdout.strip()
            except subprocess.CalledProcessError:
                entry["sha"] = ""
            if self.prune:
                kept = self._prune_clone(path, entry["sha"])
                entry["pruned_to_bibtex"] = True
                entry["kept_files"] = kept
                log(f"  pruned {entry['full_name']} to {kept} bibliography files")
        self.save_repos(repos + rest)
        return repos

    def _prune_clone(self, path: Path, sha: str) -> int:
        """Keep only the BibTeX (and README/LICENCE); record the commit in a marker file.

        The bibliography evidence is what this source is for; the rest of a repository can
        be gigabytes. The marker means the clone is never re-fetched.
        """
        keep_suffixes = {".bib"}
        keep_names = {"README.md", "README.rst", "README.txt", "README", "LICENSE",
                      "LICENSE.md", "LICENCE", "COPYING"}
        kept = 0
        for f in list(path.rglob("*")):
            if f.is_symlink():
                f.unlink(missing_ok=True)
                continue
            if not f.is_file():
                continue
            if f.suffix.lower() in keep_suffixes or f.name in keep_names:
                kept += 1
                continue
            try:
                f.unlink()
            except OSError:
                pass
        shutil.rmtree(path / ".git", ignore_errors=True)
        for d in sorted((d for d in path.rglob("*") if d.is_dir()), key=lambda x: -len(x.parts)):
            try:
                d.rmdir()
            except OSError:
                pass
        (path / MARKER).write_text(json.dumps(
            {"sha": sha, "pruned_at": iso_now(), "kept_files": kept,
             "note": "clone pruned to BibTeX by argmine; delete this file to re-clone"},
            indent=2) + "\n")
        return kept

    # -- index -------------------------------------------------------------
    def _fingerprint(self) -> str:
        repos = self.load_repos()
        return json.dumps(sorted((r["full_name"], r.get("sha", "")) for r in repos)) + f"|v{SCHEMA}"

    def build_index(self, force: bool = False, log=print) -> int:
        if not force and self.index_path.exists():
            data = json.loads(self.index_path.read_text())
            if data.get("fingerprint") == self._fingerprint():
                self._install(data)
                return len(self.entries)
        entries, files = [], {}
        repos = self.load_repos()
        for repo in repos:
            path = self.clone_dir(repo["full_name"])
            if not path.exists():
                continue
            n_files = n_entries = 0
            for bib in sorted(path.rglob("*.bib")):
                parsed, curated = self._parse_bib_file(bib)
                if not parsed:
                    continue
                rel = str(bib.relative_to(path))
                file_id = f"{repo['full_name']}:{rel}"
                titles, anth_keys = [], 0
                for e in parsed:
                    f = e["fields"]
                    title = f.get("title", "")
                    if len(title) < 8:
                        continue
                    nt = norm_title(title)
                    if ANTHOLOGY_KEY_RE.match(e["key"].lower()):
                        anth_keys += 1
                    entries.append({
                        "ntitle": nt, "title": title, "authors": bibtex.authors(f.get("author", "")),
                        "year": bibtex.year(f), "venue": bibtex.venue(f),
                        "doc_type": bibtex.doc_type(e["entrytype"], f),
                        "doi": f.get("doi", ""), "url": f.get("url", ""),
                        "eprint": f.get("eprint", "") if f.get("archiveprefix", "").lower() == "arxiv" else "",
                        "key": e["key"], "repo": repo["full_name"], "file": rel, "file_id": file_id,
                    })
                    titles.append(nt)
                if titles:
                    ratio = round(anth_keys / max(len(titles), 1), 3)
                    files[file_id] = {
                        "repo": repo["full_name"], "path": rel, "n": len(titles),
                        "anthology_ratio": ratio,
                        # Only a real reference list is evidence that two works belong
                        # together; a whole-venue or whole-anthology dump is not.
                        "curated": bool(curated and ratio <= 0.8),
                        "titles": sorted(set(titles)),
                    }
                    n_files += 1
                    n_entries += len(titles)
            repo["bib_files"], repo["bib_entries"] = n_files, n_entries
        self.save_repos(repos)
        data = {"fingerprint": self._fingerprint(), "entries": entries, "files": files}
        self.index_path.write_text(json.dumps(data))
        self._install(data)
        log(f"  bib corpus: {len(entries)} entries in {len(files)} bibliographies "
            f"from {len({e['repo'] for e in entries})} repositories")
        return len(entries)

    def _parse_bib_file(self, bib: Path) -> tuple[list[dict], bool]:
        """Parse one .bib file. Returns (entries, curated?).

        Small bibliographies are parsed whole and count as curated reference lists.
        Large dumps (whole venues, whole anthologies) are scanned entry by entry and only
        the argumentation-relevant entries are parsed, which keeps a multi-gigabyte DBLP
        mirror usable as a corroboration source without paying to parse all of it.
        """
        try:
            if bib.stat().st_size > self.max_bib_bytes:
                return [], False
            text = bib.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return [], False
        starts = [m.start() for m in ENTRY_START_RE.finditer(text)]
        if not starts:
            return [], False
        if len(starts) <= self.curated_max:
            return bibtex.parse(text), True
        low = text.lower()
        if not any(term in low for term in RELEVANCE_TERMS):
            return [], False
        bounds = starts + [len(text)]
        out = []
        for i, begin in enumerate(starts):
            chunk = text[begin:bounds[i + 1]]
            if not any(term in chunk.lower() for term in RELEVANCE_TERMS):
                continue
            out.extend(bibtex.parse(chunk))
        return out, False

    def _install(self, data: dict) -> None:
        self._match_cache = {}
        self.entries = data["entries"]
        self.files = {k: {**v, "titles": set(v["titles"])} for k, v in data["files"].items()}
        self.by_title, self.title_files = {}, {}
        for idx, e in enumerate(self.entries):
            self.by_title.setdefault(e["ntitle"], []).append(idx)
            self.title_files.setdefault(e["ntitle"], set()).add(e["file_id"])
        self._ntitles = list(self.by_title)

    # -- queries -----------------------------------------------------------
    def _to_candidate(self, e: dict) -> dict:
        return candidate(
            self.name,
            title=e["title"], authors=e["authors"], year=e["year"], venue=e["venue"],
            doc_type=e["doc_type"], doi=e.get("doi", ""), arxiv=e.get("eprint", ""),
            urls={"landing": e.get("url", "")},
            extra={"repo": e["repo"], "file": e["file"], "file_id": e["file_id"],
                   "bibkey": e["key"],
                   "anthology_derived": self._anthology_derived(e["key"])},
        )

    def match_title(self, title: str, cutoff: float = 95.0) -> str | None:
        """Exact normalised match, else a fuzzy match over every indexed title.

        Memoised: a record is looked up several times per phase (metadata, independence,
        co-citation), and the fuzzy scan is the most expensive thing the local sources do.
        """
        nt = norm_title(title)
        if nt in self.by_title:
            return nt
        if not self._ntitles:
            return None
        cached = self._match_cache.get((nt, cutoff))
        if cached is not None:
            return cached or None
        hit = process.extractOne(nt, self._ntitles, scorer=fuzz.ratio, score_cutoff=cutoff)
        result = hit[0] if hit else ""
        self._match_cache[(nt, cutoff)] = result
        return result or None

    def lookup(self, title: str, year=None) -> list[dict]:
        nt = self.match_title(title)
        if not nt:
            return []
        out = [self._to_candidate(self.entries[i]) for i in self.by_title[nt]]
        if year:
            out = [c for c in out if not c["year"] or abs(c["year"] - int(year)) <= 2] or out
        return out

    def independent_repos(self, title: str) -> list[str]:
        """Distinct repositories carrying this work in a bibliography that is not simply a
        copy of the ACL Anthology's own BibTeX export."""
        repos = set()
        for c in self.lookup(title):
            if c["extra"].get("anthology_derived"):
                continue
            repos.add(c["extra"]["repo"])
        return sorted(repos)

    def search(self, query: str, limit: int = 40) -> list[dict]:
        """Keyword search over bibliography titles: every query token must appear.

        Ranked by how many distinct bibliographies list the work, which is a reasonable
        stand-in for prominence when no citation counts are available.
        """
        tokens = [t for t in norm_title(query).split() if len(t) > 2]
        if not tokens:
            return []
        hits = []
        for nt in self._ntitles:
            if all(t in nt for t in tokens):
                hits.append((len(self.title_files.get(nt, ())), nt))
        hits.sort(key=lambda kv: -kv[0])
        out = []
        for _n, nt in hits[:limit]:
            rec = self.best_record(nt)
            if rec:
                out.append(rec)
        return out

    def cofile_ids(self, title: str) -> set[str]:
        nt = self.match_title(title)
        return set(self.title_files.get(nt, set())) if nt else set()

    def cocited_titles(self, title: str) -> dict[str, int]:
        """Normalised titles appearing in the same *curated* bibliographies, with counts."""
        out: dict[str, int] = {}
        for fid in self.cofile_ids(title):
            if not self.files.get(fid, {}).get("curated"):
                continue
            for other in self.files.get(fid, {}).get("titles", ()):
                out[other] = out.get(other, 0) + 1
        out.pop(norm_title(title), None)
        return out

    def candidates_for_titles(self, ntitles) -> list[dict]:
        out = []
        for nt in ntitles:
            idxs = self.by_title.get(nt, [])
            if idxs:
                out.append(self._to_candidate(self.entries[idxs[0]]))
        return out

    def best_record(self, ntitle: str) -> dict | None:
        """The most complete bib record for a normalised title across all repos."""
        idxs = self.by_title.get(ntitle, [])
        if not idxs:
            return None
        best = max((self.entries[i] for i in idxs),
                   key=lambda e: (bool(e.get("doi")), bool(e.get("venue")), len(e.get("authors", [])),
                                  bool(e.get("year"))))
        return self._to_candidate(best)
