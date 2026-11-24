#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt, exactly as the competition requires: a single line of
UTF-8 text, 120 characters or fewer, no trailing newline.
"""

import os

LINE = "Write tonight's code as if the tired engineer reading it at 3 a.m. is you — because it will be."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
