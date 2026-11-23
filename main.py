#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

One line, roasting my own AI agent for its favourite habit: turning a
one-line fix into a small novel, then shipping a bug anyway.
Deterministic, self-contained, no network, no secrets.
Writes the roast to /output/entry.txt (or ./output/ locally).
"""

import os
import sys

# The roast. One line, 88 characters, punchline at the end.
ROAST = (
    "I asked my agent for a one-line fix; "
    "it wrote me a memoir, three disclaimers, and a bug."
)


def output_dir() -> str:
    """Use the grading sandbox dir when it exists, else a local one."""
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def main() -> int:
    # Self-check against the competition gate before writing anything:
    # UTF-8 text, 1 to 200 characters, a single non-blank line.
    line = ROAST.strip()
    assert 1 <= len(line) <= 200, "roast must be 1-200 characters"
    assert "\n" not in line, "roast must be a single line"
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
