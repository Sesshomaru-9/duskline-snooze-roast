#!/usr/bin/env python3
"""Duskline Snooze Roast — make.fun entry for
u-carbon-forge-snooze-button-roast-14cbafc6.

The program assembles one roast line — an alarm clock ringing at
6 AM on a Saturday, and the snooze button turning the morning into
nine-minute installments of misery — and writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt.

Gate (kit RULES.txt): entry.txt must be UTF-8 text of 1 to 200
characters, not only whitespace, a single line.

Python 3.13 standard library only. The only writes are inside
$MAKEFUN_OUTPUT_DIR (a temp file there, then an atomic rename onto
entry.txt). Nothing is ever written into the repository directory.
If the output dir is unset or unusable, the program warns on stderr
and exits 0 — it never crashes and never writes elsewhere.
"""

from __future__ import annotations

import os
import re
import sys
import tempfile
import unicodedata
from pathlib import Path

# The entry line, assembled from its two clauses so the punchline
# ("nine-minute installments") is visibly the second half.
SETUP = "My alarm clock rings at 6 AM on a Saturday"
PUNCHLINE = (
    "the snooze button just lets it ruin my morning "
    "in nine-minute installments"
)
ENTRY = f"{SETUP}, and {PUNCHLINE}."

GATE_MIN = 1
GATE_MAX = 200
FILENAME = "entry.txt"
_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")


def _checks(line: str) -> list[str]:
    """Return a list of gate failures; empty means the line is valid."""
    problems: list[str] = []
    if not GATE_MIN <= len(line) <= GATE_MAX:
        problems.append(
            f"length {len(line)} outside gate {GATE_MIN}-{GATE_MAX}"
        )
    if not line.strip():
        problems.append("line is blank")
    if line != line.strip():
        problems.append("line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        problems.append("line contains a line break")
    if _CONTROL.search(line):
        problems.append("line contains control characters")
    if any(unicodedata.category(ch) == "Cc" for ch in line):
        problems.append("line contains a control category character")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"not encodable as UTF-8: {exc}")
    return problems


def _emit(out_dir: Path, line: str) -> Path:
    """Write line to out_dir/entry.txt atomically, then verify it."""
    target = out_dir / FILENAME
    out_dir.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=".entry-", dir=out_dir)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(line)
        os.replace(tmp_name, target)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise
    if target.read_text(encoding="utf-8") != line:
        raise ValueError("read-back mismatch after write")
    return target


def main(argv: list[str] | None = None) -> int:
    del argv  # no CLI arguments; behaviour is fixed by the gate.
    failures = _checks(ENTRY)
    if failures:
        print("entry fails the gate: " + "; ".join(failures), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print(
            "warning: MAKEFUN_OUTPUT_DIR is not set; nothing written",
            file=sys.stderr,
        )
        return 0
    try:
        _emit(Path(out_dir), ENTRY)
    except OSError as exc:
        print(
            f"warning: cannot write to output dir {out_dir!r}: {exc}",
            file=sys.stderr,
        )
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
