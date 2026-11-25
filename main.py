#!/usr/bin/env python3
"""Duskline Snooze Roast — make.fun entry for
u-carbon-forge-snooze-button-roast-14cbafc6.

Writes one line roasting an alarm clock that rings at 6 AM on a
Saturday to $MAKEFUN_OUTPUT_DIR/entry.txt.

Gate (from the kit's RULES.txt): entry.txt must be UTF-8 text of
1 to 200 characters, not only white space, a single line.

Python 3.13 standard library only. Writes only to
$MAKEFUN_OUTPUT_DIR; never writes into the repository directory.
If the output dir is unset or unwritable, prints a warning to
stderr and exits 0 (never crashes, never writes elsewhere).
"""

import os
import sys

TEXT = (
    "My alarm clock rings at 6 AM on a Saturday, and the snooze "
    "button just lets it ruin my morning in nine-minute installments."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Gate validation: 1 line, 1-200 chars, no control chars, UTF-8."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"text is {len(text)} chars, gate requires "
            f"{MIN_CHARS}-{MAX_CHARS}"
        )
    if text != text.strip() or not text.strip():
        raise ValueError("text must not be only whitespace / padded")
    if "\n" in text or "\r" in text:
        raise ValueError("text must be a single line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        raise ValueError("text contains control characters")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print(
            "warning: MAKEFUN_OUTPUT_DIR is not set; nothing written",
            file=sys.stderr,
        )
        return 0
    validate(TEXT)
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(TEXT)
        with open(path, "r", encoding="utf-8") as f:
            back = f.read()
    except OSError as exc:
        print(f"warning: cannot write output dir {out_dir!r}: {exc}",
              file=sys.stderr)
        return 0
    if back != TEXT:
        raise ValueError("read-back verification failed: content mismatch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
