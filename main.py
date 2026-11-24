"""Fortune in a Pot — one kind, funny fortune for a houseplant.

Writes a single line (<=120 characters) to /output/entry.txt.
Deterministic: no randomness, no network, no input.
"""

LINE = "By spring, the sun on your windowsill will help you outgrow this pot \u2014 and your keeper will admit you were right."

LIMIT = 120


def main() -> None:
    assert isinstance(LINE, str)
    assert LINE.strip(), "fortune must not be blank"
    assert "\n" not in LINE and "\r" not in LINE, "fortune must be a single line"
    assert 1 <= len(LINE) <= LIMIT, f"fortune must be 1-{LIMIT} chars, got {len(LINE)}"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
