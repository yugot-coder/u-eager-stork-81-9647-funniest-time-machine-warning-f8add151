#!/usr/bin/env python3
"""Write the funniest time machine warning label to /output/entry.txt.

Stdlib only. Deterministic: the same bytes on every run.
"""
import os

ENTRY = "WARNING: Do not operate while paradoxes are in progress. If you meet yourself, do not lend yourself money."
OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY
    if not (1 <= len(text) <= 120):
        raise SystemExit(f"entry length {len(text)} outside 1-120 characters")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
