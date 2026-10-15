#!/usr/bin/env python3
"""Check that every relative markdown link in docs/, AGENTS.md, README.md and .cursor/ resolves.
(.mdc rule links are repo-root relative, as Cursor resolves them.)

  python scripts/check_doc_links.py   # exit 1 if any link is broken
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\]\((<[^>]+>|[^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE = re.compile(r"^```.*?^```", re.M | re.S)


def files() -> list[Path]:
    out = [ROOT / "AGENTS.md", ROOT / "README.md"]
    for base in ("docs", ".cursor"):
        out += sorted(p for p in (ROOT / base).rglob("*") if p.suffix in (".md", ".mdc"))
    return out


def main() -> int:
    broken = 0
    for f in files():
        text = FENCE.sub("", f.read_text(encoding="utf-8"))
        for m in LINK.finditer(text):
            target = m.group(1).strip("<>")
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
                continue
            path = unquote(target.split("#", 1)[0])
            if not path:
                continue
            # Cursor .mdc rules resolve links from the repo root.
            base = ROOT if f.suffix == ".mdc" else f.parent
            if not (base / path).exists():
                broken += 1
                print(f"{f.relative_to(ROOT)}: {target}")
    print(f"{broken} broken link(s)")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
