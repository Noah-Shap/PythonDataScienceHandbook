"""A small, dependency-free BibTeX reader.

Only what a bibliography needs: brace-balanced entry extraction, top-level field
splitting, and enough LaTeX cleanup that titles and author names compare correctly
against API metadata.
"""
from __future__ import annotations

import re

ENTRY_RE = re.compile(r"@(\w+)\s*[{(]")
SKIP_TYPES = {"comment", "preamble", "string"}

_ACCENTS = {
    r"\\'": "", r'\\"': "", r"\\`": "", r"\\\^": "", r"\\~": "", r"\\=": "", r"\\\.": "",
    r"\\c": "", r"\\v": "", r"\\u": "", r"\\H": "", r"\\r": "",
}
_SPECIAL = {r"\\ss": "ss", r"\\ae": "ae", r"\\oe": "oe", r"\\o": "o", r"\\l": "l",
            r"\\aa": "aa", r"\\&": "&", r"\\%": "%", r"\\_": "_", r"\\#": "#", r"\\\$": "$"}

DOC_TYPE = {
    "article": "journal", "inproceedings": "conference", "conference": "conference",
    "proceedings": "conference", "book": "book", "inbook": "chapter",
    "incollection": "chapter", "phdthesis": "thesis", "mastersthesis": "thesis",
    "techreport": "preprint", "misc": "", "unpublished": "preprint", "manual": "guideline",
    "booklet": "book",
}


def clean_value(v: str) -> str:
    v = v.strip()
    while len(v) >= 2 and ((v[0] == "{" and v[-1] == "}") or (v[0] == '"' and v[-1] == '"')):
        v = v[1:-1].strip()
    for pat, rep in _SPECIAL.items():
        v = re.sub(pat + r"(?![a-zA-Z])", rep, v)
    for pat, rep in _ACCENTS.items():
        v = re.sub(pat + r"\s*\{?([a-zA-Z])\}?", r"\1", v)
    v = re.sub(r"\\[a-zA-Z]+\s*", " ", v)      # drop remaining LaTeX commands
    v = v.replace("{", "").replace("}", "").replace("\\", "")
    v = re.sub(r"\s+", " ", v).strip()
    return v.strip(" ,")


def split_fields(body: str) -> list[str]:
    out, depth, quote, cur = [], 0, False, []
    for ch in body:
        if ch == '"' and depth == 0:
            quote = not quote
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        if ch == "," and depth == 0 and not quote:
            out.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    if cur:
        out.append("".join(cur))
    return out


def parse(text: str) -> list[dict]:
    """Return [{'entrytype','key','fields':{...}}]."""
    entries, i = [], 0
    while True:
        at = text.find("@", i)
        if at < 0:
            break
        m = ENTRY_RE.match(text, at)
        if not m:
            i = at + 1
            continue
        etype = m.group(1).lower()
        if etype in SKIP_TYPES:
            i = m.end()
            continue
        opener = text[m.end() - 1]
        closer = ")" if opener == "(" else "}"
        depth, j = 1, m.end()
        while j < len(text) and depth:
            c = text[j]
            if c == opener:
                depth += 1
            elif c == closer:
                depth -= 1
            j += 1
        body = text[m.end(): j - 1]
        parts = split_fields(body)
        if not parts:
            i = j
            continue
        key = parts[0].strip().strip(",").strip()
        fields = {}
        for part in parts[1:]:
            if "=" not in part:
                continue
            name, _, value = part.partition("=")
            name = name.strip().lower()
            if name:
                fields[name] = clean_value(value)
        entries.append({"entrytype": etype, "key": key, "fields": fields})
        i = j
    return entries


def authors(field: str) -> list[str]:
    if not field:
        return []
    out = []
    for a in re.split(r"\s+and\s+", field):
        a = a.strip().rstrip(",")
        if not a or a.lower() in {"others", "et al."}:
            continue
        if "," in a:
            last, _, first = a.partition(",")
            a = f"{first.strip()} {last.strip()}".strip()
        out.append(re.sub(r"\s+", " ", a))
    return out


def venue(fields: dict) -> str:
    for key in ("journal", "booktitle", "series", "school", "institution", "publisher", "howpublished"):
        if fields.get(key):
            return fields[key]
    return ""


def doc_type(entrytype: str, fields: dict) -> str:
    v = venue(fields).lower()
    if "arxiv" in v or fields.get("archiveprefix", "").lower() == "arxiv" or "corr" == v.strip():
        return "preprint"
    base = DOC_TYPE.get(entrytype, "")
    if base == "conference" and "workshop" in v:
        return "workshop"
    return base


def year(fields: dict):
    m = re.search(r"(1[89]\d{2}|20\d{2})", fields.get("year", "") or fields.get("date", ""))
    return int(m.group(1)) if m else None
