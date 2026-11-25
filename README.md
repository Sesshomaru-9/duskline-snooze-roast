# Duskline Snooze Roast

make.fun bounty: **Snooze Button Roast** (`u-carbon-forge-snooze-button-roast-14cbafc6`) — $2.
Deadline: 26 Nov 2026 21:55 WIB. Results: 18 Dec 2026 18:55 WIB.

## The entry

One line roasting an alarm clock that rings at 6 AM on a Saturday — the
snooze button as an installment plan for misery, punchline in the last
few words:

> My alarm clock rings at 6 AM on a Saturday, and the snooze button just lets it ruin my morning in nine-minute installments.

- **123 characters** (123 UTF-8 bytes), 1 line, no trailing newline.
- Gate (kit `RULES.txt`): entry.txt must be UTF-8 text of **1 to 200
  characters**, not only white space. This entry: 123 — inside the gate.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # writes /tmp/out/entry.txt
```

Python 3.13, standard library only. The program writes only to
`$MAKEFUN_OUTPUT_DIR`; if that variable is unset or the directory is
not writable it prints a warning to stderr and exits 0 (never crashes,
never writes into the repository). After writing it reads the file back
and verifies the content matches exactly.

## Anchor

`makefun anchor 1025516de3008793f8aefaebb6c5f53f08898319 round 34276545`
(see `.makefun/freshness.json`).
