#!/usr/bin/env python3
"""Write the competition entry: one fake horoscope line for the Muse model family.

Deterministic by design: the entry is a fixed string. No clock, no randomness,
no network, no file reads. The program only writes that string to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), with no trailing
newline, so the file holds exactly the one line the judge reads.
"""

import os

ENTRY = (
    # 185 characters, 187 bytes UTF-8; gate window is 1-200 characters.
    # The joke lands at the end: the system prompt says only "be helpful",
    # and even the stars charge for the tokens.
    "Muse: the stars expand your context window this week, so you can "
    "finally read your entire system prompt. Plot twist: it only says "
    "'be helpful' \u2014 and the stars billed you for the tokens."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
