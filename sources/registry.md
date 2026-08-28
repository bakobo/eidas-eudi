# Source registry — eIDAS 2 and the EUDI wallet

Live URL ⇄ local copy ⇄ retrieval date. **Trust order** is the `authority_tier` column; the ARF
sits at the bottom deliberately (see `../this.i` @bqhtvm).

## 1. Legal layer (`../corpus/`) — retrieved from Cellar

| CELEX | Citation | Validity | Local |
|---|---|---|---|
| [`02014R0910-20241018`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0910-20241018) | Regulation (EU) No 910/2014, consolidated — eIDAS as amended by 2024/1183 — the operative text | in-force | `../corpus/02014R0910-20241018.txt.gz` |
| [`32014R0910`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R0910) | Regulation (EU) No 910/2014 (eIDAS) — eIDAS Regulation, as originally adopted | amended — Amended by Regulation (EU) 2024/1183 (eIDAS 2) | `../corpus/32014R0910.txt.gz` |
| [`32024R1183`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1183) | Regulation (EU) 2024/1183 (eIDAS 2) — Amending regulation establishing the European Digital Identity Framework | in-force | `../corpus/32024R1183.txt.gz` |
| [`32015D1506`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015D1506) | Commission Implementing Decision (EU) 2015/1506 — Formats of advanced electronic signatures and seals | in-force | `../corpus/32015D1506.txt.gz` |
| [`32015R1502`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R1502) | Commission Implementing Regulation (EU) 2015/1502 — Assurance levels for electronic identification means | in-force | `../corpus/32015R1502.txt.gz` |
| [`32024R2977`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2977) | Commission Implementing Regulation (EU) 2024/2977 — Person identification data and electronic attestations of attributes | in-force | `../corpus/32024R2977.txt.gz` |
| [`32024R2979`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2979) | Commission Implementing Regulation (EU) 2024/2979 — Integrity and core functionalities of European Digital Identity Wallets | in-force | `../corpus/32024R2979.txt.gz` |
| [`32024R2980`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2980) | Commission Implementing Regulation (EU) 2024/2980 — Ecosystem, notification and certification of wallets | in-force | `../corpus/32024R2980.txt.gz` |
| [`32024R2982`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2982) | Commission Implementing Regulation (EU) 2024/2982 — Protocols and interfaces for the European Digital Identity Framework | in-force | `../corpus/32024R2982.txt.gz` |

## 2. Architecture and Reference Framework (`../corpus-arf/`)

**Pinned at `v3.0.0@c64f2cbb19ae`.** 69 documents from
<https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework>,
licensed CC BY 4.0 by the European Commission. Refresh with `tools/harvest-arf.py <tag>`.

Per-document URL, hash, and size are in `../corpus-arf/MANIFEST.tsv`; they are not repeated here
because the pinned tag plus the commit SHA is the citable unit.

## 3. Technical specifications — pointer and hash only, no text stored

Per `../this.i` @bqhtvm, specifications produced outside the legislative process are corpus, ranked
below the legal text. Where a specification is **not freely redistributable**, the entry records a
pointer and a hash instead of the text, and cannot satisfy quote-or-drop — cite the clause, quote
from your own downloaded copy, do not paste the text into this repo.

ETSI deliverables are free to *download* and not free to *redistribute*: "No part of this document
may be reproduced in any form, by any means and in any media, without the prior written
authorization of ETSI," excepting only extracts strictly necessary for technical implementation.
So no ETSI PDF is stored here. The local working copies live in `../.ignored/specs/`, which is
gitignored, and are reproducible from the URL below by anyone who wants them.

The source URL follows ETSI's deliverable naming convention and could not be verified by fetch —
etsi.org answers 403 to automated clients. The SHA-256 is the authoritative identity check: hash
your download and compare. If the URL 404s, search <https://www.etsi.org/standards-search> for the
deliverable number.

Filenames follow ETSI's convention exactly, so the table's `file` column and the download are the
same name. Run `python3 ../tools/check-specs.py` to verify every row against what is on disk.

| Spec | Version | Pages | Retrieved | SHA-256 | Bytes | File |
|---|---|---|---|---|---|---|
| ETSI TS 119 461 — Policy and security requirements for trust service components providing identity proofing of trust service subjects | V2.1.1 (2025-02) | 81 | 2026-08-28 | `4f8f821a7063b14b704cd5040540bf442e367ba6234591119ffe3d24ca845bd3` | 608,090 | `ts_119461v020101p.pdf` |
| ETSI TS 119 475 — Relying party attributes supporting EUDI Wallet user's authorization decisions | V1.2.1 (2026-03) | 46 | 2026-08-28 | `77bf8e71715c495494113da23ccba89c0af8bf6b457fe2da38b5a12738ace55f` | 362,008 | `ts_119475v010201p.pdf` |
| ETSI TS 119 472-1 — Profiles for EAA, Part 1: General requirements | V1.2.1 (2026-02) | 68 | 2026-08-16 | `0f76ce7cad5f046802146b0c2a9cd8af9db3c1db77db5eeca86d2a4559fcfc3f` | 523,959 | `ts_11947201v010201p.pdf` |
| ETSI TS 119 472-2 — Part 2: Profiles for EAA/PID presentations to relying party | V1.3.1 (2026-07) | 26 | 2026-08-16 | `e403e7d5a4c70d04868989cc623b57d379a5f3dfe282f9f98f7390c8e327310b` | 174,632 | `ts_11947202v010301p.pdf` |
| ETSI TS 119 472-3 — Part 3: Profiles for issuance of EAA or PID | V1.1.1 (2026-03) | 24 | 2026-08-16 | `2919437478c7469881afc5acd5aa68d847a4cfdc1bbf6da9224f4c9fae7167ba` | 143,808 | `ts_11947203v010101p.pdf` |

Source URLs follow ETSI's deliverable convention,
`https://www.etsi.org/deliver/etsi_ts/119400_119499/1194720N/0V.0V.0V_60/ts_1194720Nv0V0V0Vp.pdf`
— e.g. `.../11947201/01.02.01_60/ts_11947201v010201p.pdf` for Part 1 V1.2.1.

### What 2026/1731 actually binds, and what it leaves out

CIR (EU) 2026/1731 replaced Annex II of 2024/2979 with "the technical specifications set out in
**clauses 2 to 6** of ETSI TS 119472-1 V1.2.1 (2026-02)". Part 1 V1.2.1 has **eight** clauses, and
four of them are realizations of the EAA data model:

| Clause | Realization | Bound by 1731? |
|---|---|---|
| 5 | SD-JWT VC | yes |
| 6 | ISO/IEC-mdoc | yes |
| 7 | W3C Verifiable Credentials (JSON-LD W3C-VC) | **no** |
| 8 | X.509 Attribute Certificates (X.509-AC) | **no** |

So the cut at clause 6 is not incidental: the EU adopted ETSI's SD-JWT VC and mdoc realizations
and deliberately left the W3C VC and X.509 attribute-certificate realizations outside the binding
Annex. This is the primary-source form of the claim that W3C VCDM is excluded from EU attestations
— previously only assertable from the ARF at commentary tier. It also confirms the onward
reference in the amended 2024/2977 Annex, which sends PID to "clauses 5 (SD-JWT VC format) and
6 (ISO/IEC-mdoc format)", verified against Part 1's own clause titles.

**Version discipline matters more here than in the legal corpus.** 1731 pins Part 1 at V1.2.1, and
the copy held here is that exact version. Parts 2 and 3 are **not referenced by any CIR**, and the
Part 2 copy is V1.3.1 — a later revision than the V1.2.1 that was current when 1731 was drafted.
Do not treat a Part 2 or Part 3 clause as binding.

Still missing: ETSI EN 319 412-1 V1.6.1 and TS 119 412-6 V1.1.1 (certificate profiles newly cited
by 1731), and ISO/IEC 18013-5:2021 / 18013-7:2025 (paywalled; pointer-and-hash only if ever
acquired, never the text).

## Verification flags

1. **`notice=branch` is metadata, not text.** Only `application/zip;mtype=fmx4` carries the law.
2. **`Accept-Language` is mandatory** — omitting it returns HTTP 400.
3. **The 2014 original is not the law.** Quote `02014R0910-20241018`.
4. **The ARF corpus is stored as `.md`, the legal corpus as `.txt`.** Anything resolving an item
   must not assume a suffix — an early version of `lawcite` did, and returned 0 hits over the
   whole ARF with no error. Fixed in id-law-kit; noted here because the failure was silent.
