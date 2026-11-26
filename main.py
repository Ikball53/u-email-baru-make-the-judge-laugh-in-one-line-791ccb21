#!/usr/bin/env python3
"""One-line joke entry: a deadpan Roomba gag with the twist at the end."""

import os

LINE = (
    "I asked my Roomba for one small favour and it spent three days stuck "
    "under the couch, quietly judging my life choices."
)


def main():
    # The line is a fixed constant: no randomness, no clock, no I/O input,
    # so two runs always produce byte-identical entry.txt files.
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
