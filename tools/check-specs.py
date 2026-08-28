#!/usr/bin/env python3
"""Report which registered technical specifications are on this machine, and verify them.

Why this exists
---------------
Some specifications this corpus depends on cannot be stored in it: **this is a public repo**, and
ETSI deliverables are free to download but not free to republish, so `this.i` @bqhtvm settles on
pointer-and-hash. The citation half of that is right and unchanged. The storage half used to be a
gitignored `.ignored/specs/`, which had one failure mode: the *asset* was invisible to git, so a
reader who looked at the tracked tree concluded the specification had never been acquired, and
re-acquired it. That happened, costing a round trip to a human and a wrong claim in a memo
("neither is held locally") about a document that had been on disk for twelve days.

The documents now live in the private `bakobo/not-for-redistribution` repo, which gives them a
backup and a history without putting them in a public tree. This tool reads the registry table in
`sources/registry.md` §3 and reports what is actually present, so nobody has to know where the
bytes ended up or remember which document to open.

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

# Where the bytes live, most-current first. The private sibling repo is the home; the legacy
# gitignored path is kept so a clone that predates the move still resolves rather than reporting
# a false MISSING -- which is the exact error this tool exists to prevent, and it would be
# embarrassing to reintroduce it while fixing it.
SEARCH = [
    ROOT.parent / "not-for-redistribution" / "etsi",
    ROOT / ".ignored" / "specs",
]


def locate(filename: str) -> Path | None:
    for d in SEARCH:
        p = d / filename
        if p.exists():
            return p
    return None

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
        path = locate(e["file"])
        if path is None:
            print(f"  MISSING   {name} {e['version']}")
            print(f"            looked for {e['file']} in:")
            for d in SEARCH:
                print(f"              {d}")
            print("            The first is the private bakobo/not-for-redistribution repo —")
            print("            clone it beside this one if you have not. Otherwise: ETSI 403s")
            print("            automated clients, so download in a browser from")
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
        print("All present and hash-verified.")
        print("Reminder: this repo is PUBLIC and these documents are not republishable —")
        print("cite the clause, quote from your own copy, never paste the text into this tree.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
