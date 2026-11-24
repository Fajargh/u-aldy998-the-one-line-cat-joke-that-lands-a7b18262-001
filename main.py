#!/usr/bin/env python3
"""Write one one-line cat joke to /output/entry.txt.

The joke: a setup (cat knocks the phone off the table) and a turn
(the cat blames the owner) - a fresh angle on the classic
cat-knocks-things-off-the-table behaviour, with no padding.
"""

import os

JOKE = (
    "My cat knocked my phone off the table, watched it shatter, "
    "then looked at me like I'd dropped it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
