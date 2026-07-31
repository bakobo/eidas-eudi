#!/usr/bin/env python3
"""Archive one pinned release of the Architecture and Reference Framework.

The ARF is not a published instrument; it is a live GitHub repository with numbered releases. So
`utah-id-law`'s currency model — refetch monthly, diff the manifest hashes — is the wrong shape.
There is no monthly codification, and a finding about "the ARF" means nothing without saying which
release. This pins a tag and records the commit SHA as the version identity. See `this.i` @m6imom.

The ARF also sits below the legal instruments in authority: a specification cannot override an
implementing act, and recording that ordering in the manifest is what makes a conflict visible in
a citation rather than silently resolved by whichever document a search hit first (@bqhtvm).

    python3 tools/harvest-arf.py v3.0.0
"""

import argparse
import datetime
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from lawcorpus.manifest import Manifest, ManifestItem
from lawcorpus.store import CorpusStore

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus-arf"
REPO = "https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework.git"


def run(*cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("tag", help="release tag to pin, e.g. v3.0.0")
    args = p.parse_args(argv)

    tmp = Path(tempfile.mkdtemp(prefix="arf-"))
    try:
        print(f"Cloning {args.tag}...")
        run("git", "clone", "-q", "--depth", "1", "--branch", args.tag, REPO, str(tmp / "arf"))
        repo = tmp / "arf"
        sha = run("git", "rev-parse", "HEAD", cwd=repo)
        print(f"  {args.tag} = {sha}")

        store = CorpusStore(CORPUS)
        retrieved = datetime.date.today().isoformat()
        items = []
        for md in sorted((repo / "docs").rglob("*.md")):
            rel = md.relative_to(repo / "docs")
            # "technical-specifications/ts4-zkp.md" -> "technical-specifications__ts4-zkp"
            item_id = str(rel.with_suffix("")).replace("/", "__")
            text = md.read_text(encoding="utf-8", errors="replace")
            if not text.strip():
                print(f"  skipping empty {rel}")
                continue
            written = store.write(item_id, text, suffix=".md")
            items.append(
                ManifestItem(
                    item_id=item_id,
                    citation=f"EUDI ARF {args.tag} — {rel}",
                    title=first_heading(text) or str(rel),
                    # Below every legal instrument in this repo, deliberately.
                    authority_tier="commentary",
                    validity="in-force",
                    validity_note="",
                    version_id=f"{args.tag}@{sha[:12]}",
                    lang="eng",
                    source_url=f"{REPO[:-4]}/blob/{args.tag}/docs/{rel}",
                    retrieved=retrieved,
                    media_type="text/markdown",
                    bytes=written.bytes,
                    sha256=written.sha256,
                )
            )
        Manifest(items).write(CORPUS / "MANIFEST.tsv")
        total = sum(i.bytes for i in items)
        print(f"\nStored {len(items)} document(s), {total:,} bytes, pinned at {args.tag}@{sha[:12]}")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def first_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return ""


if __name__ == "__main__":
    raise SystemExit(main())
