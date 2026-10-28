# MIL-006 wiki-screenshots

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version<br>Accepted after review (RC-009 Go) | pending |

---

## Purpose

Decide whether the wiki in English, Danish and Bahasa Malaysia is complete and the screenshots are in place.

## Deliverable

Wiki pages in `en`, `da` and `ms`, one per language per lecture step plus a home page, each explaining what was gained and showing the step screenshot; the wiki is published on the host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Home page and four step pages exist in en, da and ms | File listing | A page is missing |
| 2 | Each step page has its screenshot and a 'What we gained' section | Review | Missing |
| 3 | Wiki follows `framework/process/wiki.md` | Review against the process | Deviates |
| 4 | Wiki is published and reachable | URL returns the page | Not published |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-005 | Each step builds on the one before it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 6 (wiki in three languages, screenshots) of [BC-001] | Tasks of this gateway |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-04 — within the Business Case constraints (one branch and pull request per milestone).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Read the wiki process and plan the page set | Read `framework/process/wiki.md`; fix page names, language switch links and the screenshot folder. | No |  |
| 2 | Write the English wiki | Home plus Step 1 to 4 pages: what we did, the code idea, the screenshot, what we gained. | No |  |
| 3 | Write the Danish wiki | Same page set in Danish, same screenshots. | No |  |
| 4 | Write the Bahasa Malaysia wiki | Same page set in Bahasa Malaysia, same screenshots. | No |  |
| 5 | Publish the wiki and link it from the README | Push the pages to the repository's wiki on the host (stop and report if the wiki is disabled or the push is refused) and link the wiki from the README. | No |  |

---

[BC-001]: ../business-case.md
