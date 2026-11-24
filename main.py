"""Say What Actually Broke entry writer.

The line is a deadpan DNS error in the voice of a veteran SRE: it opens
with the plain failure ("DNS is not resolving"), repeats the oldest
in-joke in the trade ("It is never the DNS") twice, then flips it on the
final beat ("It is the DNS this time") and closes with the one action
that fixes it ("Check the typo"). The twist lands last, the failure and
the next step are both named in plain words, and the whole thing fits a
real product error dialog without embarrassing the team.
"""

import os

LINE = "DNS is not resolving. It is not the DNS. It is never the DNS. It is the DNS this time. Check the typo."

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = LINE
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
