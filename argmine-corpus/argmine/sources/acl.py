"""ACL Anthology as a local source.

The brief asks for the Anthology to be read locally rather than scraped: the repo
``acl-org/acl-anthology`` is shallow-cloned (sparse, ``data/`` only) and its XML is
parsed into a SQLite index with an FTS5 table over title+abstract. The index is
rebuilt only when the clone's commit changes, so re-runs cost nothing.

This is the highest-precision source available for the NLP venues that carry most of
the field: ACL, EMNLP, NAACL, EACL, COLING, LREC, TACL, Computational Linguistics and
the ArgMining workshop series.
"""
from __future__ import annotations

import json
import re
import sqlite3
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

from ..util import norm_title
from .base import candidate

SCHEMA_VERSION = 3
OLDSTYLE_RE = re.compile(r"^[A-Z]\d{2}$")


def _text(el) -> str:
    if el is None:
        return ""
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip()


URL_RE = re.compile(r"https?://(?:www\\.)?aclanthology\\.org/([^/\\s]+)/?")


def anthology_url_id(collection_id: str, volume_id: str, paper_id: str) -> str:
    """Fallback id construction when a paper carries no canonical-URL comment.

    Old style is four digits after the dash, split differently per collection letter
    (``W15-0101`` is volume 01 paper 01; ``J19-4006`` is volume 4 paper 006); new style
    is ``2024.argmining-1.1``. The canonical URL comment in the XML is preferred over
    this reconstruction wherever it exists.
    """
    if OLDSTYLE_RE.match(collection_id):
        try:
            vol, pap = int(volume_id), int(paper_id)
        except ValueError:
            return f"{collection_id}-{volume_id}{paper_id}"
        if collection_id[0] in "WS":          # workshop-style: 2-digit volume, 2-digit paper
            return f"{collection_id}-{vol:02d}{pap:02d}"
        return f"{collection_id}-{vol}{pap:03d}"
    return f"{collection_id}-{volume_id}.{paper_id}"


def _comment_id(paper) -> str:
    """The Anthology writes each paper's canonical URL as the first child comment."""
    for child in list(paper)[:2]:
        if not isinstance(child.tag, str) and child.text:
            m = URL_RE.search(child.text.strip())
            if m:
                return m.group(1)
    return ""


class AclAnthology:
    name = "acl"

    def __init__(self, cfg, http=None):
        self.cfg = cfg
        self.http = http
        spec = cfg["sources"]["acl_anthology"]
        self.repo = spec["repo"]
        self.clone_dir = cfg.path(spec["clone_dir"])
        self.sparse = spec.get("sparse_paths", ["data"])
        self.db_path = cfg.corpus / "acl_index.sqlite"
        self._db: sqlite3.Connection | None = None
        self.venues: dict = {}

    # -- clone -------------------------------------------------------------
    def available(self) -> bool:
        return (self.clone_dir / "data" / "xml").is_dir()

    def head(self) -> str:
        try:
            return subprocess.run(
                ["git", "-C", str(self.clone_dir), "rev-parse", "HEAD"],
                capture_output=True, text=True, check=True).stdout.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return ""

    def ensure_clone(self, log=print) -> bool:
        """Idempotent: an existing clone is reused as-is, never re-fetched."""
        if self.available():
            return True
        self.clone_dir.parent.mkdir(parents=True, exist_ok=True)
        log(f"  cloning {self.repo} (sparse: {', '.join(self.sparse)}) ...")
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse",
                 self.repo, str(self.clone_dir)],
                capture_output=True, text=True, check=True, timeout=900)
            subprocess.run(["git", "-C", str(self.clone_dir), "sparse-checkout", "set", *self.sparse],
                           capture_output=True, text=True, check=True, timeout=900)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError) as exc:
            log(f"  ACL Anthology clone failed: {exc}")
            return False
        return self.available()

    # -- index -------------------------------------------------------------
    def db(self) -> sqlite3.Connection:
        if self._db is None:
            self._db = sqlite3.connect(self.db_path)
            self._db.row_factory = sqlite3.Row
        return self._db

    def _index_is_current(self) -> bool:
        if not self.db_path.exists():
            return False
        try:
            cur = self.db().execute("SELECT key, value FROM meta")
            meta = {r["key"]: r["value"] for r in cur}
        except sqlite3.Error:
            return False
        return (meta.get("schema") == str(SCHEMA_VERSION)
                and meta.get("head") == self.head()
                and int(meta.get("papers", 0)) > 0)

    def build_index(self, force: bool = False, log=print) -> int:
        if not self.available():
            return 0
        if self._index_is_current() and not force:
            return int(self.db().execute("SELECT value FROM meta WHERE key='papers'").fetchone()[0])
        if self._db is not None:
            self._db.close()
            self._db = None
        self.db_path.unlink(missing_ok=True)
        db = self.db()
        db.executescript(
            """
            CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);
            CREATE TABLE paper (
                anth_id TEXT PRIMARY KEY, ntitle TEXT, title TEXT, authors TEXT,
                year INTEGER, venue TEXT, venue_acronyms TEXT, doc_type TEXT,
                doi TEXT, abstract TEXT, url TEXT, bibkey TEXT, pages TEXT);
            CREATE INDEX paper_ntitle ON paper(ntitle);
            CREATE INDEX paper_year ON paper(year);
            CREATE VIRTUAL TABLE paper_fts USING fts5(
                anth_id UNINDEXED, title, abstract, tokenize='porter unicode61');
            """
        )
        venues = self._load_venues()
        rows, fts = [], []
        xml_dir = self.clone_dir / "data" / "xml"
        files = sorted(xml_dir.glob("*.xml"))
        for n, path in enumerate(files, 1):
            if n % 250 == 0:
                log(f"  indexed {n}/{len(files)} anthology collections ...")
            try:
                rows_, fts_ = self._parse_collection(path, venues)
            except ET.ParseError:
                continue
            rows.extend(rows_)
            fts.extend(fts_)
        db.executemany(
            "INSERT OR REPLACE INTO paper VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
        db.executemany("INSERT INTO paper_fts VALUES (?,?,?)", fts)
        db.executemany("INSERT INTO meta VALUES (?,?)", [
            ("schema", str(SCHEMA_VERSION)), ("head", self.head()), ("papers", str(len(rows)))])
        db.commit()
        log(f"  ACL Anthology index built: {len(rows)} papers from {len(files)} collections")
        return len(rows)

    def _load_venues(self) -> dict:
        path = self.clone_dir / "data" / "json" / "venues.json"
        if path.exists():
            self.venues = json.loads(path.read_text())
        return self.venues

    def _parse_collection(self, path: Path, venues: dict):
        rows, fts = [], []
        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
        root = ET.parse(path, parser=parser).getroot()
        collection_id = root.get("id", path.stem)
        for volume in root.findall("volume"):
            meta = volume.find("meta")
            if meta is None:
                continue
            booktitle = _text(meta.find("booktitle"))
            year = _text(meta.find("year"))
            acronyms = [_text(v) for v in meta.findall("venue")]
            doc_type = _doc_type(acronyms, booktitle, collection_id, venues)
            vol_id = volume.get("id", "1")
            for paper in volume.findall("paper"):
                title = _text(paper.find("title"))
                if not title:
                    continue
                authors = [
                    " ".join(x for x in [_text(a.find("first")), _text(a.find("last"))] if x)
                    for a in paper.findall("author")
                ]
                pid = paper.get("id", "")
                anth_id = _comment_id(paper) or anthology_url_id(collection_id, vol_id, pid)
                py = _text(paper.find("year")) or year
                abstract = _text(paper.find("abstract"))
                doi = _text(paper.find("doi"))
                rows.append((
                    anth_id, norm_title(title), title, json.dumps(authors, ensure_ascii=False),
                    int(py) if py.isdigit() else None, booktitle, json.dumps(acronyms),
                    doc_type, doi, abstract, f"https://aclanthology.org/{anth_id}/",
                    _text(paper.find("bibkey")), _text(paper.find("pages")),
                ))
                fts.append((anth_id, title, abstract))
        return rows, fts

    # -- queries -----------------------------------------------------------
    JOURNAL_VOLUME_RE = re.compile(r"^(.*?),\s*(Volume|Issue)\b", re.IGNORECASE)

    def _venue(self, row) -> str:
        """The Anthology's journal booktitles carry the volume and issue; a citation wants
        the journal name."""
        venue = row["venue"] or ""
        if row["doc_type"] == "journal":
            m = self.JOURNAL_VOLUME_RE.match(venue)
            if m:
                return m.group(1).strip()
        return venue

    def _row_to_candidate(self, row) -> dict:
        return candidate(
            self.name,
            title=row["title"],
            authors=json.loads(row["authors"]),
            year=row["year"],
            venue=self._venue(row),
            doc_type=row["doc_type"],
            abstract=row["abstract"],
            doi=row["doi"] or "",
            aliases=[f"acl:{row['anth_id']}"],
            urls={"landing": row["url"], "acl": row["url"], "pdf_oa": row["url"].rstrip("/") + ".pdf"},
            extra={"anth_id": row["anth_id"], "bibkey": row["bibkey"], "pages": row["pages"],
                   "venue_acronyms": json.loads(row["venue_acronyms"] or "[]")},
        )

    def lookup_title(self, title: str, year=None, tolerance: int = 2) -> list[dict]:
        if not self.available() or not self.db_path.exists():
            return []
        nt = norm_title(title)
        cur = self.db().execute("SELECT * FROM paper WHERE ntitle = ?", (nt,))
        hits = [self._row_to_candidate(r) for r in cur]
        if year:
            exact = [h for h in hits if h["year"] and abs(h["year"] - int(year)) <= tolerance]
            if exact:
                return exact
        return hits

    def get(self, anth_id: str) -> dict | None:
        if not self.db_path.exists():
            return None
        row = self.db().execute("SELECT * FROM paper WHERE anth_id = ?", (anth_id,)).fetchone()
        return self._row_to_candidate(row) if row else None

    def bibkeys(self) -> set[str]:
        """Every bibkey the Anthology issues - used to spot verbatim re-exports."""
        if not self.db_path.exists():
            return set()
        return {r[0] for r in self.db().execute(
            "SELECT bibkey FROM paper WHERE bibkey IS NOT NULL AND bibkey != ''")}

    def search(self, query: str, limit: int = 100) -> list[dict]:
        """FTS over title+abstract. Returns normalised candidates."""
        if not self.db_path.exists():
            return []
        phrase = '"' + query.replace('"', " ") + '"'
        sql = ("SELECT p.* FROM paper_fts f JOIN paper p ON p.anth_id = f.anth_id "
               "WHERE paper_fts MATCH ? ORDER BY bm25(paper_fts) LIMIT ?")
        try:
            cur = self.db().execute(sql, (phrase, limit))
        except sqlite3.OperationalError:
            return []
        return [self._row_to_candidate(r) for r in cur]

    def venue_papers(self, acronym: str, limit: int = 2000) -> list[dict]:
        """Every paper in a venue (e.g. the whole ArgMining workshop series)."""
        if not self.db_path.exists():
            return []
        cur = self.db().execute(
            "SELECT * FROM paper WHERE venue_acronyms LIKE ? LIMIT ?", (f'%"{acronym}"%', limit))
        return [self._row_to_candidate(r) for r in cur]


def _doc_type(acronyms, booktitle: str, collection_id: str, venues: dict) -> str:
    bt = (booktitle or "").lower()
    for ac in acronyms:
        spec = venues.get(ac.lower(), {})
        if spec.get("type") == "journal":
            return "journal"
    if "ws" in [a.lower() for a in acronyms] or "workshop" in bt or "proceedings of the" in bt and "workshop" in bt:
        return "workshop"
    if collection_id.startswith(("J", "Q")) or "computational linguistics" == bt.strip().lower():
        return "journal"
    return "conference"
