#!/usr/bin/env python3
"""One-line comedy entry: a coffee-shop mirror gag.

The program writes a single joke line to entry.txt. It uses only the
Python standard library, prints nothing but the line, and always
produces the same bytes on every run.
"""

import hashlib
import os
import pathlib


PUNCHLINE = (
    "I asked the barista for the strongest coffee she had, "
    "and she just slid a mirror across the counter."
)


def target_path() -> pathlib.Path:
    """Resolve where entry.txt goes, honouring MAKEFUN_OUTPUT_DIR."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return pathlib.Path(folder) / "entry.txt"


def main() -> None:
    line = PUNCHLINE.strip()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "the entry must be exactly one line"

    destination = target_path()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(line + "\n", encoding="utf-8")

    digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    print(line)
    print(f"chars={len(line)} sha256={digest}")


if __name__ == "__main__":
    main()
