# eidas-eudi — eIDAS 2 and the European Digital Identity Wallet

**This is a share of primary sources and the tooling to quote them. Nothing more.**

Offered **without warranty** and **without any claim of legal gravitas**. Assembled by non-lawyers
doing textual research with substantial AI assistance. Not legal advice, not an authoritative
statement of EU law. Every claim is tied to a citation you can check — check it.

Part of a family of repos that harvest primary legal sources so they can be analysed later — by a
person or by an AI — without repeating the online research. Shared method and tooling:
**[`id-law-kit`](https://github.com/bakobo/id-law-kit)**.

| Repo | Regime | Corpus |
|---|---|---|
| [`utah-id-law`](https://github.com/bakobo/utah-id-law) | Utah identity-verification law | ✅ |
| [`eu-data-law`](https://github.com/bakobo/eu-data-law) | GDPR + EU data-locality stack | ✅ |
| **`eidas-eudi`** | eIDAS 2, EUDI wallet, ARF | ✅ |
| [`ccpa`](https://github.com/bakobo/ccpa) | California CCPA/CPRA | ✅ |
| [`aadhaar`](https://github.com/bakobo/aadhaar) | Aadhaar Act, UIDAI regulations, DPDP Act | ⬜ |

## What is here

Two corpora, kept separate because they are different kinds of thing.

| | Items | Words | What |
|---|---|---|---|
| `corpus/` | 9 | 92,461 | The **legal layer** — eIDAS, eIDAS 2, the consolidated text, and six implementing acts |
| `corpus-arf/` | 69 | 353,744 | The **Architecture and Reference Framework**, pinned at `v3.0.0@c64f2cbb19ae` |

Retrieved 2026-07-31.

```
corpus/                one file per instrument, from EUR-Lex
corpus-arf/            the ARF release, one file per document
*/MANIFEST.tsv         citation, authority tier, validity, version, URL, date, bytes, SHA-256
tools/candidates.py    the instrument list — this file IS the legal-layer scope
tools/recon.py         verify a CELEX list against EUR-Lex before harvesting it
tools/harvest.py       fetch, extract, store, manifest
tools/harvest-arf.py   archive one pinned ARF release
sources/registry.md    live URL ⇄ local copy ⇄ retrieval date
```

## The three things worth knowing

**1. The consolidated text is the operative one.** `32014R0910` is eIDAS *as adopted in 2014*.
`32024R1183` is the amending regulation that created the European Digital Identity Framework.
Neither on its own is the law in force — that is `02014R0910-20241018`, the consolidated text. All
three are held, and the original carries `validity: amended` so a quote of it prints a banner
saying so.

**2. The ARF is pinned, not tracked.** It is a live GitHub repository with numbered releases, not a
published instrument, so "refetch monthly and diff" is the wrong currency model. The manifest
records the release tag *and* the commit SHA. This corpus is deliberately behind the working draft;
it cannot tell you where the ARF is heading.

**3. The ARF ranks below the legal text.** Its manifest entries carry the lowest `authority_tier`
in the repo. A specification cannot override an implementing act, and recording that ordering means
a conflict shows up in the citation rather than being resolved silently by whichever document a
search happened to hit first.

## Using it

```sh
python3 -m venv .venv && .venv/bin/pip install -e ../id-law-kit

.venv/bin/lawcite --corpus corpus 02014R0910-20241018        # eIDAS as in force
.venv/bin/lawcite --corpus corpus 32014R0910                 # the 2014 original — banner warns
.venv/bin/lawcite --corpus corpus --grep 'level of assurance high'
.venv/bin/lawcite --corpus corpus-arf --grep 'zero.knowledge'
```

## Known gaps

1. **Technical specifications outside the ARF** — ETSI, CEN, W3C, OpenID. Some are not freely
   redistributable. None are here yet; `this.i` @bqhtvm sets the policy for when they arrive.
2. **National eID schemes and notifications.** The peer-review and notification record under
   Article 9 is where "level of assurance high" acquires operational meaning. Absent.
3. **Member-state implementation.** eIDAS is a regulation, so transposition matters less than it
   does for a directive — but national wallet implementations and supervisory practice are absent.
4. **Standards referenced by the implementing acts.** Where an implementing act incorporates a
   standard by reference, the corpus holds the reference and not the standard.
5. **English only.** All 24 language versions are equally authentic. Any finding turning on a term
   of art is weaker than it looks.
6. **The ARF moves.** `v3.0.0` was current on 2026-07-31. Re-run `tools/harvest-arf.py <tag>`.

## Licence

The **original work** — candidate list, tooling, registry, findings — is **[CC BY 4.0](LICENSE)**.
Attribution: Bakobo, *eidas-eudi*.

`corpus/` is the text of EU legal instruments, © European Union, reproduced under
[Commission Decision 2011/833/EU](http://eur-lex.europa.eu/eli/dec/2011/833/oj) with
acknowledgement of source. **Only the text published in the printed Official Journal is authentic.**

`corpus-arf/` is the European Digital Identity Wallet Architecture and Reference Framework,
© 2026 European Commission, licensed **CC BY 4.0** by its publisher — see the `LICENCE` file in
[the ARF repository](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework).
