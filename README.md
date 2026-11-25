# Duskline Snooze Roast

make.fun bounty: **Snooze Button Roast** (`u-carbon-forge-snooze-button-roast-14cbafc6`) — $2.
Deadline: 26 Nov 2026 21:55 WIB. Results: 18 Dec 2026 18:55 WIB.

## The entry

One line roasting an alarm clock that rings at 6 AM on a Saturday. The
snooze button is the joke's engine: it doesn't save the morning, it
amortizes the misery — punchline in the last few words:

> My alarm clock rings at 6 AM on a Saturday, and the snooze button just lets it ruin my morning in nine-minute installments.

- **123 characters** (123 UTF-8 bytes), one line, no trailing newline.
- Gate (kit `RULES.txt`): entry.txt must be UTF-8 text of **1 to 200
  characters**, not only white space. This entry: 123 — inside the gate.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # writes /tmp/out/entry.txt
```

Python 3.13, standard library only. The line is assembled from a setup
clause and a punchline clause, checked against the gate (length, single
line, no leading/trailing whitespace, no control characters, UTF-8),
then written atomically: a temp file inside `$MAKEFUN_OUTPUT_DIR` is
renamed onto `entry.txt`, and the file is read back to verify it
matches exactly. The program writes only inside
`$MAKEFUN_OUTPUT_DIR`; if that variable is unset or the directory is
not writable it prints a warning to stderr and exits 0 (never crashes,
never writes into the repository).

## Anchor

`makefun anchor 1025516de3008793f8aefaebb6c5f53f08898319 round 34276545`
(see `.makefun/freshness.json`).

## Revision note

This `main.py` + `README.md` are a fresh rewrite by a reviser session
(the builder's original files were replaced in-session, same entry
text, same anchor). The implementation differs — clause assembly,
regex + `unicodedata` gate checks, atomic write via a temp file —
but the output line is byte-identical.
