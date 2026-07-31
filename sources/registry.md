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

## Verification flags

1. **`notice=branch` is metadata, not text.** Only `application/zip;mtype=fmx4` carries the law.
2. **`Accept-Language` is mandatory** — omitting it returns HTTP 400.
3. **The 2014 original is not the law.** Quote `02014R0910-20241018`.
4. **The ARF corpus is stored as `.md`, the legal corpus as `.txt`.** Anything resolving an item
   must not assume a suffix — an early version of `lawcite` did, and returned 0 hits over the
   whole ARF with no error. Fixed in id-law-kit; noted here because the failure was silent.
