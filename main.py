#!/usr/bin/env python3
"""Write the funniest time machine warning label to /output/entry.txt.

Stdlib only. Deterministic: the same bytes on every run.
"""
import os

ENTRY = "WARNING: Do not operate while paradoxes are in progress. If you meet yourself, do not lend yourself money."
OUTPUT_PATH = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 120


def validate(text):
    """Check the label text against the competition's gates."""
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        raise SystemExit(f"entry length {len(text)} outside {MIN_LEN}-{MAX_LEN} characters")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    return text


def write_entry(text):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def verify_written(text):
    """Read the file back and fail hard unless it matches exactly."""
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back mismatch: /output/entry.txt does not match expected text")
    if not (MIN_LEN <= len(written) <= MAX_LEN):
        raise SystemExit(f"written entry length {len(written)} outside {MIN_LEN}-{MAX_LEN} characters")
    return written


def main():
    text = validate(ENTRY)
    write_entry(text)
    verify_written(text)


if __name__ == "__main__":
    main()
