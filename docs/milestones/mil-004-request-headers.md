# MIL-004 request-headers

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version<br>Accepted after review (RC-007 Go) | pending |

---

## Purpose

Decide whether Step 3 (browser-like request headers) is complete.

## Deliverable

Branch `mil-004-request-headers` merged: requests carry the headers from `constants.py`, tests prove it, a screenshot and a README section.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Request sends at least `User-Agent` and `Accept-Language` | Test inspects the prepared request | Headers missing |
| 2 | Headers live in `constants.py`, not in the logic | Search finds one definition | Duplicated |
| 3 | Host and X-Amzn-Trace-Id are not copied | Test asserts absence | Present |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Each step builds on the one before it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4 (request headers) of [BC-001] | Tasks of this gateway |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-31 — within the Business Case constraints (one branch and pull request per milestone).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Define the request headers in constants | Add `User-Agent`, `Accept-Language`, `Accept`, `Accept-Encoding`, `Sec-Fetch-*` and `Priority` as in the lecture, leaving out `Host` and `X-Amzn-Trace-Id`. | No |  |
| 2 | Send the headers with the request | The fetch function passes `headers=` to `requests.get` and sets a timeout. | No |  |
| 3 | Tests for the headers | Use a mocked `requests.get` or a prepared request to assert the headers and the timeout. | No |  |
| 4 | Screenshot and README for Step 3 | Capture the headers the browser sends (myhttpheader.com / httpbin.org/headers) next to the ones the bot sends; add the Step 3 section. | No |  |

---

[BC-001]: ../business-case.md
