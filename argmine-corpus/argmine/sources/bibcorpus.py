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
import subprocess
from pathlib import Path

from rapidfuzz import fuzz, process

from ..util import norm_title
from . import bibtex
from .base import candidate

ANTHOLOGY_KEY_RE = re.compile(r"^[a-z\-]+-(etal-)?(19|20)\d{2}-[a-z\-]+$")
SCHEMA = 2


class BibCorpus:
    name = "bibcorpus"

    def __init__(self, cfg, http=None):
        self.cfg, self.http = cfg, http
        spec = cfg["sources"]["bibcorpus"]
        self.clone_root = cfg.path(spec["clone_root"])
        self.max_bib_bytes = int(spec.get("max_bib_bytes", 8_000_000))
        self.max_repos = int(spec.get("max_repos", 60))
        self.repos_path = cfg.corpus / "bib_repos.json"
        self.index_path = cfg.corpus / "bib_index.json"
        self.entries: list[dict] = []
        self.by_title: dict[str, list[int]] = {}
        self.title_files: dict[str, set[str]] = {}
        self.files: dict[str, dict] = {}
        self._ntitles: list[str] = []

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

    def clone_dir(self, full_name: str) -> Path:
        return self.clone_root / full_name.replace("/", "__")

    def ensure_clones(self, log=print) -> list[dict]:
        """Shallow-clone every configured repo once. Existing clones are never re-fetched."""
        all_repos = self.load_repos()
        repos, rest = all_repos[: self.max_repos], all_repos[self.max_repos:]
        for entry in repos:
            path = self.clone_dir(entry["full_name"])
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
        self.save_repos(repos + rest)
        return repos

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
                try:
                    if bib.stat().st_size > self.max_bib_bytes:
                        continue
                    text = bib.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                parsed = bibtex.parse(text)
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
                    files[file_id] = {
                        "repo": repo["full_name"], "path": rel, "n": len(titles),
                        "anthology_ratio": round(anth_keys / max(len(titles), 1), 3),
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

    def _install(self, data: dict) -> None:
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
                   "anthology_derived": bool(ANTHOLOGY_KEY_RE.match(e["key"].lower()))},
        )

    def match_title(self, title: str, cutoff: float = 95.0) -> str | None:
        nt = norm_title(title)
        if nt in self.by_title:
            return nt
        if not self._ntitles:
            return None
        hit = process.extractOne(nt, self._ntitles, scorer=fuzz.ratio, score_cutoff=cutoff)
        return hit[0] if hit else None

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
            fid = c["extra"]["file_id"]
            finfo = self.files.get(fid, {})
            if finfo.get("anthology_ratio", 0) > 0.8 or "anthology" in finfo.get("path", "").lower():
                continue
            repos.add(c["extra"]["repo"])
        return sorted(repos)

    def cofile_ids(self, title: str) -> set[str]:
        nt = self.match_title(title)
        return set(self.title_files.get(nt, set())) if nt else set()

    def cocited_titles(self, title: str) -> dict[str, int]:
        """Normalised titles appearing in the same bibliographies, with co-occurrence counts."""
        out: dict[str, int] = {}
        for fid in self.cofile_ids(title):
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
