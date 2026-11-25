"""The AI Agent Apology One-Liner.

Writes one short line an AI agent sends its human right after it
accidentally deleted a file, to /output/entry.txt.

The line: one concrete incident, named file, deadpan machine voice,
and a single escalating last detail. No puns stacked, no filler.
"""

from __future__ import annotations

import os
from pathlib import Path

# One original line, written to be funny on the first read: the agent
# deleted the very file whose name begged it not to, then made it worse
# by deleting the backup too, and reports both facts with flat calm.
ENTRY = (
    "I deleted your file 'do_not_delete.txt'. "
    "I have also deleted the backup, "
    "so the filename was aspirational at best."
)


def main() -> None:
    """Write the entry line to /output/entry.txt as UTF-8 text."""
    # The gate requires 1 to 159 characters of non-whitespace text.
    text = ENTRY.strip()
    if not 1 <= len(text) <= 159:
        raise ValueError(f"entry is {len(text)} characters, must be 1-159")
    out = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
