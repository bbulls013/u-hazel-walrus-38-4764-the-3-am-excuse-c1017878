"""The 3 AM Excuse: one line from a hardware wallet that will not sign."""

import os

LINE = (
    "Denied: my screen says 'confirm?', your 3 AM thumb says 'help', "
    "and I don't sign ransom notes."
)


OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 200 and LINE.strip()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
