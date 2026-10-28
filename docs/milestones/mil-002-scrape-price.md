# MIL-002 scrape-price

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version<br>Accepted after review (RC-005 Go) | [f9765fd] |

---

## Purpose

Decide whether Step 1 of the lecture (BeautifulSoup scrapes the price from the practice page) is complete.

## Deliverable

Branch `mil-002-scrape-price` merged: a scraper that returns the title and the price as a `float`, a saved copy of the practice page used by tests, a screenshot of the step, and the README section for it.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Price from the saved practice page is `99.99` as a `float` | `pytest` asserts it | Wrong value or type |
| 2 | Tests need no network access | Run with the network off passes | A test calls the network |
| 3 | Function names follow the assignment (`get_price`, `get_title`) | Names exist in the module | Different names |
| 4 | Step screenshot is in the README | File exists and is linked | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001: project set-up must be accepted first | Each step builds on the one before it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1 (price as a float) of [BC-001] | Tasks of this gateway |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-29 — within the Business Case constraints (one branch and pull request per milestone).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Save the practice page as a test fixture | Store a copy of https://appbrewery.github.io/instant_pot/ under `tests/fixtures/` so the parser is tested without the network. | No |  |
| 2 | Implement price and title parsing | `get_price(html)` finds the price element, strips the currency sign (`split` or `lstrip`) and returns a `float`; `get_title(html)` returns the product title. Both use BeautifulSoup (`lxml` is not needed; `html.parser`). | No |  |
| 3 | Fetch the page and print the price in main | `main.py` requests the URL from `constants.py`, parses it and prints the title and price. | No |  |
| 4 | Unit tests for the parser | Tests for price as float, title text and a page without a price (clear error). | No |  |
| 5 | Screenshot and README for Step 1 | Capture the run output and the practice page; save under `docs/images/step-1-*.png`; add the Step 1 section to the README. | No |  |

---

[BC-001]: ../business-case.md
[f9765fd]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/commit/f9765fd3743f46c189359e713fd050c8e1a598b6
