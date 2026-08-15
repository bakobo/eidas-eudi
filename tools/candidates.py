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
        validity="amended",
        validity_note="Amended by CIR (EU) 2026/1731; corrigendum R(01) affects only the "
        "Irish version, so this English text is unaffected by it",
        expect_in_title="person identification data",
    ),
    Candidate(
        celex="32024R2979",
        citation="Commission Implementing Regulation (EU) 2024/2979",
        title="Integrity and core functionalities of European Digital Identity Wallets",
        authority_tier="delegated",
        validity="amended",
        validity_note="Amended by CIR (EU) 2026/1731; corrigenda R(01)/R(02) affect only the "
        "Swedish and Irish versions, so this English text is unaffected by them",
        expect_in_title="core functionalities",
    ),
    Candidate(
        celex="32024R2980",
        citation="Commission Implementing Regulation (EU) 2024/2980",
        title="Ecosystem, notification and certification of wallets",
        authority_tier="delegated",
        validity="amended",
        validity_note="Amended by CIR (EU) 2026/1731; corrigendum R(01) affects only the "
        "Irish version, so this English text is unaffected by it",
        expect_in_title="Wallet",
    ),
    Candidate(
        celex="32024R2982",
        citation="Commission Implementing Regulation (EU) 2024/2982",
        title="Protocols and interfaces for the European Digital Identity Framework",
        authority_tier="delegated",
        validity="amended",
        validity_note="Amended by CIR (EU) 2026/1731",
        expect_in_title="protocols and interfaces",
    ),
    # ------------------------------------------------------------------
    # Scope extension 2026-08-15: completing the Nov 2024 wallet package.
    # Added for the KERI↔foreign-ecosystem interop program
    # (~/code/bakobo/interop, tick 4txn). Every CELEX below was verified
    # against EUR-Lex by title fetch on 2026-08-15 before being added here.
    #
    # 2024/2981 completes the five-act package published together on
    # 2024-12-04, and CIR 2026/1731 has since amended the annexes of all
    # four format/protocol acts (a standards-and-specifications refresh).
    # Deliberately NOT held: the corrigenda to 2977/2979/2980 and the
    # -20241204 consolidated texts that fold them in. The corrigenda
    # affect only the Irish and Swedish language versions (checked in
    # Cellar 2026-08-15: the corrigendum works carry no ENG expression,
    # and the only consolidation Cellar holds is GLE), so the English
    # originals stored here are the accurate English texts. No
    # consolidation incorporating 2026/1731 exists yet in any language.
    Candidate(
        celex="32024R2981",
        citation="Commission Implementing Regulation (EU) 2024/2981",
        title="Certification of European Digital Identity Wallets",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="certification of European Digital Identity Wallets",
    ),
    Candidate(
        celex="32026R1731",
        citation="Commission Implementing Regulation (EU) 2026/1731",
        title="Amendment of 2024/2977, 2024/2979, 2024/2980, 2024/2982: applicable standards and specifications",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="as regards applicable standards and specifications",
    ),
    # ------------------------------------------------------------------
    # Scope extension 2026-08-14: the QTSP/trust-service layer.
    # Added for the AZ↔EU trust-infrastructure research program
    # (~/code/tti/az-landscape/PROGRAM.md). Every CELEX below was verified
    # against EUR-Lex by title fetch on 2026-08-14 before being added here.
    #
    # The 2015–2016 layer the corpus lacked:
    Candidate(
        celex="32015D0296",
        citation="Commission Implementing Decision (EU) 2015/296",
        title="Member State cooperation on electronic identification (Art. 12(7))",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="cooperation between Member States on electronic identification",
    ),
    Candidate(
        celex="32015R0806",
        citation="Commission Implementing Regulation (EU) 2015/806",
        title="Form of the EU trust mark for qualified trust services",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="EU trust mark",
    ),
    Candidate(
        celex="32015R1501",
        citation="Commission Implementing Regulation (EU) 2015/1501",
        title="Interoperability framework (Art. 12(8))",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="interoperability framework",
    ),
    Candidate(
        celex="32015D1505",
        citation="Commission Implementing Decision (EU) 2015/1505",
        title="Technical specifications and formats relating to trusted lists (Art. 22(5))",
        authority_tier="delegated",
        validity="amended",
        validity_note="Amended by Implementing Decision (EU) 2025/2164 (TS 119 612 version bump)",
        expect_in_title="trusted lists",
    ),
    Candidate(
        celex="32015D1984",
        citation="Commission Implementing Decision (EU) 2015/1984",
        title="Circumstances, formats and procedures of eID notification (Art. 9(5))",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="procedures of notification",
    ),
    Candidate(
        celex="32016D0650",
        citation="Commission Implementing Decision (EU) 2016/650",
        title="Standards for security assessment of qualified signature/seal creation devices",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="security assessment of qualified signature and seal creation devices",
    ),
    # The May 2025 wallet-wave additions (join 2024/2977–2982):
    Candidate(
        celex="32025R0846",
        citation="Commission Implementing Regulation (EU) 2025/846",
        title="Cross-border identity matching of natural persons",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="identity matching",
    ),
    Candidate(
        celex="32025R0847",
        citation="Commission Implementing Regulation (EU) 2025/847",
        title="Reactions to security breaches of European Digital Identity Wallets",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="security breaches",
    ),
    Candidate(
        celex="32025R0848",
        citation="Commission Implementing Regulation (EU) 2025/848",
        title="Registration of wallet-relying parties",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="registration of wallet-relying parties",
    ),
    # The Jul–Dec 2025 qualified-trust-services wave:
    Candidate(
        celex="32025R1567",
        citation="Commission Implementing Regulation (EU) 2025/1567",
        title="Management of remote QSCDs as qualified trust services",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="remote qualified electronic signature creation devices",
    ),
    # Added 2026-08-15 with the wallet-package completion above (tick 4txn):
    Candidate(
        celex="32025R1569",
        citation="Commission Implementing Regulation (EU) 2025/1569",
        title="Qualified EAAs and pub-EAAs from authentic sources (incl. catalogue of attestation schemes)",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="qualified electronic attestations of attributes",
    ),
    Candidate(
        celex="32025R1572",
        citation="Commission Implementing Regulation (EU) 2025/1572",
        title="Notification of intention and verification for initiating qualified trust services",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="notification of intention",
    ),
    Candidate(
        celex="32025R1943",
        citation="Commission Implementing Regulation (EU) 2025/1943",
        title="Reference standards for qualified certificates (signature and seal)",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="reference standards for qualified certificates",
    ),
    Candidate(
        celex="32025R1944",
        citation="Commission Implementing Regulation (EU) 2025/1944",
        title="Reference standards for QERDS processes and interoperability",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="qualified electronic registered delivery services",
    ),
    Candidate(
        celex="32025R1946",
        citation="Commission Implementing Regulation (EU) 2025/1946",
        title="Qualified preservation services for qualified signatures and seals",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="qualified preservation services",
    ),
    Candidate(
        celex="32025R2160",
        citation="Commission Implementing Regulation (EU) 2025/2160",
        title="Risk management for the provision of non-qualified trust services",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="non-qualified trust services",
    ),
    Candidate(
        celex="32025R2162",
        citation="Commission Implementing Regulation (EU) 2025/2162",
        title="Accreditation of conformity assessment bodies assessing QTSPs",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="accreditation of conformity assessment bodies",
    ),
    Candidate(
        celex="32025D2164",
        citation="Commission Implementing Decision (EU) 2025/2164",
        title="Amendment of 2015/1505: trusted-list template standard version",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="common template for the trusted lists",
    ),
    Candidate(
        celex="32025R2530",
        citation="Commission Implementing Regulation (EU) 2025/2530",
        title="Requirements for QTSPs providing qualified trust services",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="requirements for qualified trust service providers",
    ),
    Candidate(
        celex="32025R2531",
        citation="Commission Implementing Regulation (EU) 2025/2531",
        title="Reference standards and specifications for qualified electronic ledgers",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="qualified electronic ledgers",
    ),
    Candidate(
        celex="32025R2532",
        citation="Commission Implementing Regulation (EU) 2025/2532",
        title="Reference standards and specifications for qualified electronic archiving",
        authority_tier="delegated",
        validity="in-force",
        validity_note="",
        expect_in_title="qualified electronic archiving",
    ),
]
