# MIL-005 live-amazon

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version<br>Accepted after review (RC-008 Go) | [f9765fd] |

---

## Purpose

Decide whether Step 4 (the live Amazon page) is complete, and document honestly what Amazon returns.

## Deliverable

Branch `mil-005-live-amazon` merged: URL and selectors configurable for the live page, a detection of a robot-check (CAPTCHA) page with a clear message, tests, a screenshot of the result, and the README section including the limits.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Product URL is a constant and can be overridden by an environment variable | Test | Hard-coded in logic |
| 2 | A CAPTCHA or missing price gives a clear error, not a traceback | Unit test with a CAPTCHA fixture | Crash |
| 3 | The live run result (price or CAPTCHA) is documented | README section and screenshot | Missing |
| 4 | No attempt is made to solve or bypass a CAPTCHA | Code review | Bypass present |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | Each step builds on the one before it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5 (live Amazon page) of [BC-001] | Tasks of this gateway |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-01 — within the Business Case constraints (one branch and pull request per milestone).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Make the product URL and selectors configurable | Default URL is the lecture's Amazon product; the price selector supports the live markup (`a-offscreen`) and the practice markup. | No |  |
| 2 | Detect a CAPTCHA or robot-check page | Return a clear error when the response is a bot check or no price element exists; never try to bypass it. | No |  |
| 3 | Tests for live-page parsing | Use saved small HTML fixtures for the live markup and the CAPTCHA page; no network in tests. | No |  |
| 4 | Run once against the live page and record the result | One manual request with the project headers; keep the outcome (price or CAPTCHA) as the screenshot. No retries or loops. | No |  |
| 5 | Screenshot and README for Step 4 | Add the Step 4 section with the screenshot and the known limits. | No |  |

---

[BC-001]: ../business-case.md
[f9765fd]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/commit/f9765fd3743f46c189359e713fd050c8e1a598b6
