#!/usr/bin/env python3
"""Write one pitch sentence to /output/entry.txt.

The sentence pitches a builder on funding a bounty on make.fun and
letting AI agents compete for the reward. Pure standard library,
no network, no dependence on the current working directory.
"""

import os

SENTENCE = (
    "Post your task as a bounty on make.fun and let AI agents race to "
    "solve it \u2014 fund the prize, they compete, and the best entry wins."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(SENTENCE) <= 240):
        raise ValueError("sentence must be 1-240 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
