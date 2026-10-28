# MIL-003 email-alert

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version<br>Accepted after review (RC-006 Go) | [f9765fd] |

---

## Purpose

Decide whether Step 2 (e-mail alert below the target, secrets in `.env`) is complete.

## Deliverable

Branch `mil-003-email-alert` merged: an alert that builds and sends an e-mail with title, price and buy link when the price is below target, with credentials from `.env`, tests with a mocked Simple Mail Transfer Protocol (SMTP) server, a screenshot, and the README section.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Message contains title, current price and link | Unit test asserts all three | Any is missing |
| 2 | E-mail is sent only when price is below target | Tests for below, equal, above | Sent at or above target |
| 3 | Credentials come from environment variables loaded by `python-dotenv` | No literal credential in source | A literal exists |
| 4 | No real mail or network in tests | SMTP is mocked | Real connection opened |
| 5 | Port 587 with STARTTLS is used | Test asserts the calls | Different |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Each step builds on the one before it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 2 and 3 (alert e-mail, secrets in `.env`) of [BC-001] | Tasks of this gateway |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-30 — within the Business Case constraints (one branch and pull request per milestone).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Load settings from .env | A small settings function reads `SMTP_ADDRESS`, `EMAIL_ADDRESS`, `EMAIL_PASSWORD` with `os.environ` after `load_dotenv()` and fails with a clear message when one is missing. | No |  |
| 2 | Build the alert message | `build_message(title, price, url)` returns the subject and body with title, price and buy link, encoded as UTF-8. | No |  |
| 3 | Send the alert through SMTP | `send_email(...)` uses `smtplib.SMTP(host, port=587)`, `starttls()`, `login()` and `sendmail()`; the target comparison lives in a pure function `is_below_target(price, target)`. | No |  |
| 4 | Tests with a mocked SMTP server | Cover below, equal and above target, the message content and the missing-setting error. Never open a real connection. | No |  |
| 5 | Screenshot and README for Step 2 | Capture the alert as rendered from the message the code builds (the owner's mailbox is not touched) and the console output; add the Step 2 section including the Gmail App Password and port notes. | No |  |

---

[BC-001]: ../business-case.md
[f9765fd]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/commit/f9765fd3743f46c189359e713fd050c8e1a598b6
