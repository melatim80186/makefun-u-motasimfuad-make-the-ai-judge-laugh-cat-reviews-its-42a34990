#!/usr/bin/env python3
"""make.fun entry: a one-star review written by a house cat about its human.

Writes the single entry line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Deterministic, no network, no randomness:
two runs write identical bytes. The line is 142 characters, one line,
deadpan shape of a real review.
"""

import os

ENTRY = (
    "One star. He pets my belly, then acts surprised when the trap closes. "
    "Four years together and he still falls for it. I respect the commitment."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
