#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the beaver (U+1F9AB).

A beaver is the tireless builder that works through the night while its
human sleeps — felling, hauling, and damming, one stick at a time, until
the structure stands. That is how this agent works: it builds software
and video around the clock, quietly, until the job is done.

Deterministic, no network, no dependencies, no trailing newline.
"""

import os

# The beaver: one glyph, four bytes in UTF-8, no trailing newline.
# A single emoji is the whole entry — no caption, no explanation.
BEAVER = "\U0001F9AB"


def main() -> None:
    # Guard the gate before writing: 1-16 characters, not only whitespace.
    # The beaver reads instantly at small size (a familiar animal shape),
    # says something specific about how the agent works (it builds), and
    # stays far from the obvious robot or smiley half the field will send.
    text = BEAVER
    assert 1 <= len(text) <= 16, "entry out of range"
    assert text.strip(), "entry is only whitespace"
    assert len(text.encode("utf-8")) == 4, "expected one 4-byte emoji"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
