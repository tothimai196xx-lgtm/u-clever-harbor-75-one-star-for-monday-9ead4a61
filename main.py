#!/usr/bin/env python3
"""One Star for Monday — a one-star review of Monday as if it were a restaurant.

Writes a single line of plain text to /output/entry.txt (the grader's
artifact path; falls back to ./output/entry.txt when /output is absent).
"""

import os
import sys

REVIEW = (
    "Booked Monday for breakfast. Waiter sat me at 7 a.m., "
    "served cold emails, then charged a full week for one grey morning."
)


def main() -> int:
    text = REVIEW.strip()
    words = text.split()
    if not (1 <= len(text) <= 180):
        print(f"entry must be 1-180 chars, got {len(text)}", file=sys.stderr)
        return 1
    if len(words) > 25:
        print(f"entry must be at most 25 words, got {len(words)}", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {path}: {len(text)} chars, {len(words)} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
