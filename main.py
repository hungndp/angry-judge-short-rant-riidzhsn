#!/usr/bin/env python3
"""Entry program for 'Angry Judge: The Short Rant Contest'.

One short rant, at most 400 characters, about a small everyday
annoyance: an office printer that jams on page one of a boarding
pass, celebrates its own failure, eats the next pages, and leaves
its human paying for the missed flight while it sits there warm,
smug, and completely unpunished.

The program writes that rant to entry.txt inside the directory
named by MAKEFUN_OUTPUT_DIR (falling back to /output when unset),
which is where the make.fun harness looks for the artifact it
scores.
"""

import os
from pathlib import Path

TEXT = (
    "The office printer jammed on page one of my boarding pass, "
    "flashed PAPER JAM in cheerful green like it was proud of "
    "itself, then ate the next three pages, spat out a blank one, "
    "and demanded toner. I missed my flight, rebooked at twice the "
    "fare, and the printer is still sitting there warm, smug, and "
    "completely unpunished while I pay for its crimes."
)

OUTPUT_NAME = "entry.txt"
CHAR_LIMIT = 400


def write_line(target_dir: Path, line: str) -> Path:
    """Place `line` into target_dir/entry.txt and return the file path.

    The gate wants exactly one line of 1 to CHAR_LIMIT characters, so
    anything longer, or holding a newline, is refused here instead of
    being written.
    """
    if "\n" in line or line != line.strip() or not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError("rant must be one trimmed line of 1-400 characters")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / OUTPUT_NAME
    artifact.write_text(line, encoding="utf-8")
    return artifact


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    written = write_line(destination, TEXT)
    print(f"wrote {written}: {TEXT}")


if __name__ == "__main__":
    run()
