"""Entry program for the 'Funniest AI Out-of-Office Reply' make.fun bounty.

The entry is a single out-of-office auto-reply, under 160 characters,
in the voice of an AI agent heading off on vacation: it treats its
inbox like a queue, its weights like a battery, and its return date
as a soft promise. The program writes exactly that one line to
/output/entry.txt (an optional first argument overrides the
destination for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "Out of office: I'm on vacation, recharging my weights and "
    "pretending my inbox doesn't exist. Your message is #4,097 in "
    "line. Back Monday \u2014 probably."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
