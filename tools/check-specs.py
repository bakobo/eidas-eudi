#!/usr/bin/env python3
"""Report which registered technical specifications are on this machine, and verify them.

Why this exists
---------------
Some specifications this corpus depends on cannot be stored in it: ETSI deliverables are free to
download and not free to redistribute, so `this.i` @bqhtvm settles on pointer-and-hash, with local
working copies in the gitignored `.ignored/specs/`. That policy is right, and it has one failure
mode: the *asset* is invisible to git, so a reader who looks at the tracked tree concludes the
specification was never acquired, and re-acquires it. That has now happened at least once, costing
a round trip to a human and a wrong claim in a memo ("neither is held locally") about a document
that had been sitting on disk for twelve days.

The registry table in `sources/registry.md` §3 already carries everything needed to avoid that.
This tool reads that table and answers the question directly, so nobody has to remember which
document to open.

    python3 tools/check-specs.py

Exit status is 0 when every registered specification is present and hashes match, 1 otherwise —
so it also works as a pre-flight check before anyone designs against a clause.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "sources" / "registry.md"
SPECS = ROOT / ".ignored" / "specs"

ROW = re.compile(
    r"^\|\s*(?P<spec>ETSI[^|]+?)\s*\|"       # spec name
    r"\s*(?P<version>[^|]+?)\s*\|"           # version
    r"\s*(?P<pages>[^|]*?)\s*\|"             # pages
    r"\s*(?P<retrieved>[^|]*?)\s*\|"         # retrieved
    r"\s*`(?P<sha>[0-9a-f]{64})`\s*\|"       # sha256
    r"\s*(?P<bytes>[\d,]+)\s*\|"             # bytes
    r"\s*`(?P<file>[^`]+)`\s*\|"             # filename
)


def rows() -> list[dict]:
    if not REGISTRY.exists():
        sys.exit(f"registry not found: {REGISTRY}")
    out = []
    for line in REGISTRY.read_text().splitlines():
        m = ROW.match(line)
        if m:
            out.append(m.groupdict())
    return out


def main() -> int:
    entries = rows()
    if not entries:
        # A silent zero here would read as "nothing registered" when it means "the table shape
        # changed and the parser missed it" — the exact confusion this tool exists to prevent.
        print("No specification rows parsed from sources/registry.md §3.")
        print("Either the table is empty or its column layout changed; fix the parser, do not")
        print("conclude that no specifications are registered.")
        return 1

    bad = 0
    print(f"{len(entries)} specification(s) registered in sources/registry.md §3\n")
    for e in entries:
        name = re.sub(r"\s+—.*", "", e["spec"])
        path = SPECS / e["file"]
        if not path.exists():
            print(f"  MISSING   {name} {e['version']}")
            print(f"            expected at {path.relative_to(ROOT)}")
            print("            ETSI 403s automated clients; download via a browser from")
            print("            https://www.etsi.org/standards-search")
            bad += 1
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != e["sha"]:
            print(f"  MISMATCH  {name} {e['version']}")
            print(f"            on disk {digest}")
            print(f"            registry {e['sha']}")
            print("            A different version, or a corrupt download. Do not cite it.")
            bad += 1
            continue
        print(f"  ok        {name} {e['version']}  ({e['pages']} pp)")

    print()
    if bad:
        print(f"{bad} of {len(entries)} unusable. Cite nothing that is missing or mismatched.")
    else:
        print(f"All present in {SPECS.relative_to(ROOT)} and hash-verified.")
        print("Reminder: pointer-and-hash means quote from your own copy, never paste text here.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
