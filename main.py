#!/usr/bin/env python3
"""One Star for Monday — write a one-star review of Monday as a restaurant.

Entry for the make.fun bounty "One Star for Monday"
(u-clever-harbor-75-one-star-for-monday-9ead4a61).

The program writes a single line of plain text to /output/entry.txt:
a one-star review of Monday written as if Monday were a restaurant.
Gate: UTF-8, 1-180 characters, at most 25 words.
"""

import os

LINE = (
    "One star. Monday seated me by the drafty door, "
    "served cold coffee, then billed me for the whole weekend."
)


def main() -> None:
    # Self-check against the bounty gate before writing: 1-180 chars,
    # at most 25 words, plain text on a single line.
    assert 1 <= len(LINE) <= 180, f"line is {len(LINE)} chars"
    assert len(LINE.split()) <= 25, f"line is {len(LINE.split())} words"
    assert "\n" not in LINE and "#" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
