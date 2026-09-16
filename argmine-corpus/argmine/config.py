"""Configuration loading and validation.

config.yaml is the single source of truth for the cap, quotas, weights, the per-area
vocabulary used for keyword scoring, the seed hypotheses and criteria_version.
00-field-map.md is rendered from it, so the coverage contract and the scoring code can
never drift apart.
"""
from __future__ import annotations

import os
from pathlib import Path

import yaml

REQUIRED_TOP = ["run", "http", "sources", "scoring", "quotas", "areas", "tiers", "seeds", "searches"]
AREAS = ["formal", "mining", "quality", "dialogue", "llm", "resources"]


class ConfigError(ValueError):
    pass


class Config(dict):
    """dict with a root path and a couple of convenience accessors."""

    def __init__(self, data: dict, root: Path):
        super().__init__(data)
        self.root = root

    # -- paths -------------------------------------------------------------
    def path(self, *parts) -> Path:
        return self.root.joinpath(*parts)

    @property
    def corpus(self) -> Path:
        return self.path("corpus")

    @property
    def deliverables(self) -> Path:
        return self.path("deliverables")

    # -- frequently used values -------------------------------------------
    @property
    def cap(self) -> int:
        return int(self["run"]["cap"])

    @property
    def criteria_version(self) -> int:
        return int(self["run"]["criteria_version"])

    @property
    def contact(self) -> str:
        return self["run"]["contact_email"]

    @property
    def user_agent(self) -> str:
        return self["run"]["user_agent"]

    def area_quota(self, area: str) -> int:
        return int(self["quotas"].get(area, 0))


def find_root(start: Path | None = None) -> Path:
    """Locate the project root (the directory holding config.yaml)."""
    env = os.environ.get("ARGMINE_ROOT")
    if env:
        return Path(env).resolve()
    here = (start or Path.cwd()).resolve()
    for cand in [here, *here.parents]:
        if (cand / "config.yaml").exists() and (cand / "argmine").is_dir():
            return cand
    return Path(__file__).resolve().parent.parent


def load(root: Path | None = None) -> Config:
    root = (root or find_root()).resolve()
    with open(root / "config.yaml", "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    validate(data)
    return Config(data, root)


def validate(data: dict) -> None:
    missing = [k for k in REQUIRED_TOP if k not in data]
    if missing:
        raise ConfigError(f"config.yaml missing top-level keys: {missing}")
    if sorted(data["areas"]) != sorted(AREAS):
        raise ConfigError(f"areas must be exactly {AREAS}, got {sorted(data['areas'])}")
    for area in AREAS:
        spec = data["areas"][area]
        for key in ("number", "name", "definition", "include", "exclude", "vocabulary"):
            if key not in spec:
                raise ConfigError(f"area {area} missing '{key}'")
        if not isinstance(spec["vocabulary"], dict) or not spec["vocabulary"]:
            raise ConfigError(f"area {area} has an empty vocabulary")
        if area not in data["quotas"]:
            raise ConfigError(f"area {area} has no quota")
    w = data["scoring"]["weights"]
    for key in ("cites_norm", "cocite", "keyword", "venue"):
        if key not in w:
            raise ConfigError(f"scoring.weights missing '{key}'")
    total = sum(float(v) for v in w.values())
    if abs(total - 1.0) > 1e-6:
        raise ConfigError(f"scoring.weights must sum to 1.0, got {total}")
    if int(data["run"]["cap"]) <= 0:
        raise ConfigError("run.cap must be positive")
    if sum(int(v) for v in data["quotas"].values()) > int(data["run"]["cap"]):
        raise ConfigError("area quotas sum to more than the cap")
    if not data["seeds"]:
        raise ConfigError("no seeds configured")
