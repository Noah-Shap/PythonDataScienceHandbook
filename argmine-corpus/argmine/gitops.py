"""Every phase ends with a commit. Commits are made only when something changed."""
from __future__ import annotations

import os
import subprocess
from pathlib import Path


def _run(args, cwd: Path, check: bool = False):
    return subprocess.run(args, cwd=str(cwd), capture_output=True, text=True, check=check)


def repo_root(start: Path) -> Path | None:
    res = _run(["git", "rev-parse", "--show-toplevel"], start)
    return Path(res.stdout.strip()) if res.returncode == 0 and res.stdout.strip() else None


def trailers() -> str:
    """Optional commit trailers (e.g. co-authorship) supplied by the caller's environment."""
    value = os.environ.get("ARGMINE_COMMIT_TRAILERS", "")
    if value and os.path.exists(value):
        return Path(value).read_text().rstrip("\n")
    return value.replace("\\n", "\n").rstrip("\n")


def commit(cfg, message: str, paths=None, log=print) -> bool:
    root = repo_root(cfg.root)
    if root is None:
        log("  (not a git repository - skipping commit)")
        return False
    targets = [str(cfg.path(p)) for p in (paths or ["."])]
    _run(["git", "add", "-A", *targets], root)
    staged = _run(["git", "diff", "--cached", "--name-only"], root).stdout.strip()
    if not staged:
        log("  nothing to commit")
        return False
    body = message
    extra = trailers()
    if extra:
        body = f"{message}\n\n{extra}"
    res = _run(["git", "commit", "-m", body], root)
    if res.returncode != 0:
        log(f"  commit failed: {res.stderr.strip()[:200]}")
        return False
    sha = _run(["git", "rev-parse", "--short", "HEAD"], root).stdout.strip()
    log(f"  committed {sha}: {message.splitlines()[0]}")
    return True
