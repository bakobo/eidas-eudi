# eidas-eudi — Intent Tree (this.i)

A checkable corpus of the EU digital identity regime = goal:
  id: zdca74
  why: >
    Harvest the primary text of eIDAS 2 and the EUDI wallet stack — regulation, implementing acts,
    and the Architecture and Reference Framework — so that later analysis of how European digital
    identity actually works can quote sources rather than recall them. Rejected merging this into
    eu-data-law: both draw on EUR-Lex, but they answer opposite questions. GDPR governs what may be
    done with personal data; eIDAS governs how identity is asserted and trusted, and its corpus is
    dominated by technical specifications that have no counterpart in the data-protection stack.
    Tradeoff accepted: the EUR-Lex fetcher is shared with eu-data-law through id-law-kit, so the
    two repos are coupled through a dependency rather than through co-location.
  children:
    The ARF is pinned by release tag, not refetched on a schedule = decision:
      id: m6imom
      why: >
        The Architecture and Reference Framework is a live GitHub repository
        (eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework), not a published
        instrument. utah-id-law's currency model — refetch monthly and diff the manifest hashes —
        is wrong for it: there is no monthly codification, there are numbered releases, and a
        finding about "the ARF" is meaningless without saying which. Chose to record the release
        tag and commit SHA as the version identity and to archive the release artifacts rather than
        tracking HEAD. Tradeoff: the corpus is deliberately behind the working draft, and questions
        about where the ARF is *heading* cannot be answered from it.

    Technical specifications are corpus, and are ranked below the legal text = decision:
      id: bqhtvm
      why: >
        Wallet behaviour is governed jointly by the regulation, the implementing acts, and
        specifications produced outside the legislative process (ETSI, CEN, W3C, OpenID). Excluding
        the specifications would make most operative questions unanswerable; treating them as
        equal-authority would let a draft specification override an implementing act. Chose to
        ingest them with an explicit authority_tier below the legal instruments, so a conflict is
        visible in the citation rather than resolved silently by whichever text was found first.
        Tradeoff: some specifications are not freely redistributable, so those entries record a
        pointer and a hash rather than the text, and cannot satisfy quote-or-drop.
