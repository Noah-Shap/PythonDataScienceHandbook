"""Shared run context: config, HTTP layer, registry, source clients, run log."""
from __future__ import annotations

import json

from .cache import Http
from .registry import Registry
from .sources.acl import AclAnthology
from .sources.arxiv import ArXiv
from .sources.bibcorpus import BibCorpus
from .sources.crossref import Crossref
from .sources.github import GitHub
from .sources.openalex import OpenAlex
from .sources.s2 import SemanticScholar
from .sources.unpaywall import Unpaywall
from .util import iso_now


class Context:
    def __init__(self, cfg, args=None, log=print):
        self.cfg = cfg
        self.args = args
        self.log = log
        self.dry_run = bool(getattr(args, "dry_run", False))
        self.http = Http(cfg, offline=bool(getattr(args, "offline", False)))
        self.registry = Registry(cfg)
        self.acl = AclAnthology(cfg, self.http)
        self.bib = BibCorpus(cfg, self.http)
        self.gh = GitHub(cfg, self.http)
        self.openalex = OpenAlex(cfg, self.http)
        self.s2 = SemanticScholar(cfg, self.http)
        self.crossref = Crossref(cfg, self.http)
        self.arxiv = ArXiv(cfg, self.http)
        self.unpaywall = Unpaywall(cfg, self.http)
        self.run_log_path = cfg.corpus / "run_log.jsonl"

    # -- sources -----------------------------------------------------------
    def probe_sources(self) -> dict:
        """Probe every configured remote source once; local sources report themselves."""
        enabled = set(self.cfg["sources"]["enabled"])
        for client in (self.openalex, self.s2, self.crossref, self.arxiv, self.unpaywall, self.gh):
            if client.name in enabled:
                self.http.probe(client.name, client.probe_url)
        if "acl" in enabled:
            self.http.status["acl"] = {
                "reachable": self.acl.available(),
                "reason": f"local clone at {self.cfg['sources']['acl_anthology']['clone_dir']}"
                          if self.acl.available() else "not cloned",
                "_probed_this_run": True}
        if "bibcorpus" in enabled:
            n = len(self.bib.load_repos())
            self.http.status["bibcorpus"] = {
                "reachable": n > 0,
                "reason": f"{n} bibliography repositories configured",
                "_probed_this_run": True}
        self.http.save_status()
        return self.http.status

    def live(self, name: str) -> bool:
        st = self.http.status.get(name)
        return bool(st and st.get("reachable"))

    @property
    def source_status(self) -> dict:
        return {k: {kk: vv for kk, vv in v.items() if not kk.startswith("_")}
                for k, v in self.http.status.items()}

    # -- run log -----------------------------------------------------------
    def log_phase(self, phase: str, summary: dict) -> None:
        row = {"phase": phase, "at": iso_now(), "cap": self.cfg.cap,
               "criteria_version": self.cfg.criteria_version, "summary": summary}
        self.run_log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.run_log_path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")

    def run_log(self) -> list[dict]:
        if not self.run_log_path.exists():
            return []
        return [json.loads(l) for l in self.run_log_path.read_text().splitlines() if l.strip()]

    def save(self) -> None:
        if not self.dry_run:
            self.registry.save()
            self.http.save_status()

    # -- local sources -----------------------------------------------------
    def prepare_local_sources(self, log=None) -> dict:
        """Make the local sources usable: clone and index the ACL Anthology, discover,
        clone and index the BibTeX corroboration corpus. Idempotent and cheap on re-runs -
        nothing is re-cloned and an index is rebuilt only when its clone's commit moves."""
        log = log or self.log
        if getattr(self, "_prepared", False):
            return self._prepare_summary
        out = {}
        force = bool(getattr(self.args, "force_index", False))
        enabled = set(self.cfg["sources"]["enabled"])
        if "acl" in enabled:
            if self.acl.ensure_clone(log=log):
                out["acl_papers"] = self.acl.build_index(force=force, log=log)
                out["acl_commit"] = self.acl.head()[:12]
        if "bibcorpus" in enabled:
            self.bib.discover_from_search_cache(self.gh, log=log)
            repos = self.bib.ensure_clones(log=log)
            out["bib_repos"] = sum(1 for r in repos if r.get("cloned"))
            out["bib_entries"] = self.bib.build_index(force=force, log=log)
        self.probe_sources()
        self._prepared = True
        self._prepare_summary = out
        return out
