"""Unpaywall: open-access PDF resolution for a DOI. Never used to reach paywalled text."""
from __future__ import annotations

import os

from ..util import normalise_doi

BASE = "https://api.unpaywall.org/v2"


class Unpaywall:
    name = "unpaywall"
    probe_url = f"{BASE}/10.1162/coli_a_00364"

    def __init__(self, cfg, http):
        self.cfg, self.http = cfg, http
        # Section 11: UNPAYWALL_EMAIL may differ from the general contact address.
        self.email = os.environ.get("UNPAYWALL_EMAIL") or cfg.contact

    def oa_pdf(self, doi: str) -> dict | None:
        """Returns {'pdf': url, 'landing': url, 'licence': str, 'host_type': str} or None."""
        d = normalise_doi(doi)
        if not d:
            return None
        data = self.http.json(self.name, f"{BASE}/{d}", {"email": self.email})
        if not data or not data.get("is_oa"):
            return None
        loc = data.get("best_oa_location") or {}
        if not loc.get("url_for_pdf"):
            return None
        return {"pdf": loc["url_for_pdf"], "landing": loc.get("url_for_landing_page", ""),
                "licence": loc.get("license") or "", "host_type": loc.get("host_type", "")}
