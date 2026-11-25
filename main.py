#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes exactly one funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Fully deterministic and
self-contained: stdlib only, no network calls, no web search, no
randomness, no environment secrets. The line is written byte for byte
as judged — no trailing newline, no title, no explanation.
"""
import os
from pathlib import Path

LINE = "My smart fridge judges my midnight snacks out loud now, so I unplugged it and it filed a complaint."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
