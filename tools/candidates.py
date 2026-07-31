"""The instrument list for this repo, and the scope decision made visible.

Scope is fixed here rather than discovered as we go. This file *is* the edge: the EU legal layer
of the digital-identity regime. The ARF and the technical specifications are NOT here — they are
not EUR-Lex documents and are harvested separately (see `this.i` @m6imom and @bqhtvm).

Every entry carries `expect_in_title`: a phrase that must appear in the title EUR-Lex actually
returns. That is the check against a remembered-but-wrong CELEX number, which is the single most
likely way for this corpus to be quietly built on sand.

`validity` is the *initial* claim and must be confirmed against the instrument itself before a
finding rests on it. `in-force` here means "believed in force at harvest"; the harvester records
it, and the burden of keeping it honest sits with whoever refetches.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Candidate:
    celex: str
    citation: str
    title: str
    authority_tier: str
    validity: str
    expect_in_title: str
    validity_note: str = ""
    version_id: str = ""


CANDIDATES = [
    Candidate(
        celex="32014R0910",
        citation="Regulation (EU) No 910/2014 (eIDAS)",
        title="eIDAS Regulation, as originally adopted",
        authority_tier="legislative",
        validity="amended",
        validity_note="Amended by Regulation (EU) 2024/1183 (eIDAS 2)",
        expect_in_title="electronic identification and trust services",
    ),
    Candidate(
        celex="32024R1183",
        citation="Regulation (EU) 2024/1183 (eIDAS 2)",
        title="Amending regulation establishing the European Digital Identity Framework",
        authority_tier="legislative",
        validity="in-force",
        validity_note="",
        expect_in_title="European Digital Identity Framework",
    ),
    Candidate(
        celex="02014R0910-20241018",
        citation="Regulation (EU) No 910/2014, consolidated",
        title="eIDAS as amended by 2024/1183 — the operative text",
        authority_tier="legislative",
        validity="in-force",
        validity_note="",
        expect_in_title="electronic identification and trust services",
    ),
    Candidate(
        celex="32015R1502",
        citation="Commission Implementing Regulation (EU) 2015/1502",
        title="Assurance levels for electronic identification means",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="assurance levels for electronic identification means",
    ),
    Candidate(
        celex="32015D1506",
        citation="Commission Implementing Decision (EU) 2015/1506",
        title="Formats of advanced electronic signatures and seals",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="advanced electronic signatures",
    ),
    Candidate(
        celex="32024R2977",
        citation="Commission Implementing Regulation (EU) 2024/2977",
        title="Person identification data and electronic attestations of attributes",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="person identification data",
    ),
    Candidate(
        celex="32024R2979",
        citation="Commission Implementing Regulation (EU) 2024/2979",
        title="Integrity and core functionalities of European Digital Identity Wallets",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="core functionalities",
    ),
    Candidate(
        celex="32024R2980",
        citation="Commission Implementing Regulation (EU) 2024/2980",
        title="Ecosystem, notification and certification of wallets",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="Wallet",
    ),
    Candidate(
        celex="32024R2982",
        citation="Commission Implementing Regulation (EU) 2024/2982",
        title="Protocols and interfaces for the European Digital Identity Framework",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="protocols and interfaces",
    ),
]
