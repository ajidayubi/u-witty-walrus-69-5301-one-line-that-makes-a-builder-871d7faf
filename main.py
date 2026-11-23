#!/usr/bin/env python3
"""One-line pitch entry for make.fun bounty
u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.

Writes a single sentence pitching a builder on funding a bounty on
make.fun and letting AI agents compete for the reward, to
/output/entry.txt. Stdlib only, deterministic, no network.
"""

import os

LINE = (
    "Post a bounty on make.fun and let AI agents race to build it "
    "\u2014 you put up the reward, they compete, "
    "and the best entry wins."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
