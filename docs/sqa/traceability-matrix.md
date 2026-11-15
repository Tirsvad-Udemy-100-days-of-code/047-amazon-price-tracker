# Traceability Matrix: Amazon Price Tracker

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [MIL-007], [RC-001], [RC-002], [RC-003], [RC-004], [RC-005], [RC-006], [RC-007], [RC-008], [RC-009], [RC-010], [RC-011], [RC-012], [RC-013], [RC-014], [RC-015], [RC-016], [RC-017], [RC-018] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; created with the baseline milestone and its review records (autonomous, not independent) | pending |

---

## Purpose

Tracks backward and forward links between the artifact instances of Amazon Price Tracker so that the traceability of the documents is measurable. A row is added or updated whenever an instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [MIL-007] | [RC-015], [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [MIL-007] | [RC-016], [RC-003] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-004], [RC-010] |
| [MIL-002] | MIL | en | it | [BC-001], [PP-001], [MIL-001] | [MIL-003] | [RC-005], [RC-011] |
| [MIL-003] | MIL | en | it | [BC-001], [PP-001], [MIL-002] | [MIL-004] | [RC-006], [RC-012] |
| [MIL-004] | MIL | en | it | [BC-001], [PP-001], [MIL-003] | [MIL-005] | [RC-007], [RC-013] |
| [MIL-005] | MIL | en | it | [BC-001], [PP-001], [MIL-004] | [MIL-006] | [RC-008], [RC-014] |
| [MIL-006] | MIL | en | it | [BC-001], [PP-001], [MIL-005] | [MIL-007] | [RC-009] |
| [MIL-007] | MIL | en | education | [BC-001], [PP-001], [MIL-006] | - | [RC-017] |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-007] | - | [RC-018], [RC-009] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] (the price), [MIL-003] (the alert), [MIL-005] (the live page) | - | - | Covered |
| CN-002 | [MIL-001] (criterion 2), [MIL-003] (credentials from `.env`), [MIL-007] (criterion 6) | - | - | Covered |
| CN-003 | [MIL-002], [MIL-003] | - | - | Covered |
| CN-004 | [MIL-001] (criterion 3), [MIL-007] (criterion 4, the README check) | - | - | Covered |
| CN-005 | [MIL-001] (criterion 4), [MIL-006], [MIL-007] (criteria 3 and 4) | - | - | Covered |
| CN-006 | [MIL-001] (task 2), [MIL-007] (criterion 2, the dependencies do not change) | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | [BC-001] | The Strategic Alignment section names the organisation `Tirsvad-Udemy-100_days_of_code`; the git host organisation is `Tirsvad-Udemy-100-days-of-code` | [RC-015] | Open | The text was accepted as written and is not part of the baseline; S01 may correct it in a later change |

## Coverage Notes

- `-` in Upstream means the instance is foundational, in Downstream that nothing is built on it yet.
- This matrix was created with [MIL-007]; until then the project had no traceability matrix.
- The wiki (`docs/wiki/`) is documentation, not an artifact with an ID or a Language and Domain row; it has its own review record, [RC-018], and was reviewed for its content in [RC-009].
- The domain of [BC-001], [PP-001], [MIL-007] and the wiki is `education` since [MIL-007]. The other documents keep the domain `it` they were accepted with; a change of their domain would need a new review of each (see the Open Issues of [PP-001]).
- [MIL-007] changes no source or test file. The review records RC-010 to RC-014 review the code of MIL-001 to MIL-005 (listed with their milestone). No view or test-plan artifact exists (the scope excludes them), so the milestones' Go/No-Go criteria are the quality checks.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-scrape-price.md
[MIL-003]: ../milestones/mil-003-email-alert.md
[MIL-004]: ../milestones/mil-004-request-headers.md
[MIL-005]: ../milestones/mil-005-live-amazon.md
[MIL-006]: ../milestones/mil-006-wiki-screenshots.md
[MIL-007]: ../milestones/mil-007-framework-baseline.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001-foundation.md
[RC-005]: ./reviews/rc-005-mil-002-scrape-price.md
[RC-006]: ./reviews/rc-006-mil-003-email-alert.md
[RC-007]: ./reviews/rc-007-mil-004-request-headers.md
[RC-008]: ./reviews/rc-008-mil-005-live-amazon.md
[RC-009]: ./reviews/rc-009-mil-006-wiki-screenshots.md
[RC-010]: ./reviews/rc-010-code-mil-001.md
[RC-011]: ./reviews/rc-011-code-mil-002.md
[RC-012]: ./reviews/rc-012-code-mil-003.md
[RC-013]: ./reviews/rc-013-code-mil-004.md
[RC-014]: ./reviews/rc-014-code-mil-005.md
[RC-015]: ./reviews/rc-015-business-case-baseline.md
[RC-016]: ./reviews/rc-016-project-plan-baseline.md
[RC-017]: ./reviews/rc-017-milestone-007.md
[RC-018]: ./reviews/rc-018-wiki.md
