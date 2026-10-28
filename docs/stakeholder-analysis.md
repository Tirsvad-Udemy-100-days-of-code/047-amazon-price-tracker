# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version<br>Accepted after review (RC-002 Go) | [f9765fd] |

---

## Purpose

Identify who is involved in the Amazon price tracker, how much they influence it and what each needs. The method is the power/interest grid (Mendelow); concerns are mapped to FURPS+ (Functionality, Usability, Reliability, Performance, Supportability, plus constraints).

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer, reviewer | Tirsvad | High | High | Manage Closely | A working, tested solution and a clean repository |
| S02 | Udemy coursists | Course participants who share and compare solutions | Udemy community | Low | High | Keep Informed | Readable, runnable code with the assignment's function names, and run instructions |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | Low | Low | Monitor | A clear description, topics, README and no unnecessary runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews and accepts every artifact.
- **Keep Informed (S02):** cannot change the project but uses it directly, so the code and README must be easy to follow.
- **Monitor (S03):** casual readers; the repository page is their only contact.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The bot finds the price and alerts when it is below target | Functionality |
| CN-002 | S01 | Passwords and tokens never reach the repository | Functionality (security) |
| CN-003 | S02 | Function names match the assignment and the code is readable | Usability |
| CN-004 | S02 | The README explains how to set up the venv, run and test | Usability |
| CN-005 | S03 | Description, topics and README explain the repository | Usability |
| CN-006 | S03 | No runtime dependencies beyond the necessary | Supportability |

## Communication Requirements

| Channel | Frequency | Deliverable type | Phase |
| --- | --- | --- | --- |
| Chat with S01 | Per milestone | Pull request for review | MIL-001 to MIL-006 |
| README and wiki | Once, then per change | Documentation for S02 and S03 | MIL-001, MIL-006 |

## Conflicting Interests and Mitigations

| Conflict | Mitigation |
| --- | --- |
| S02 wants the code to follow the course (single script) while S01 wants layered, tested code | Keep the assignment's function names and a short `main.py`; the layers stay thin |
| S03 wants no dependencies while the scraper needs three | Only `requests`, `beautifulsoup4` and `python-dotenv`; dev tools stay in a `dev` extra |

## Traceability Analysis

| Stakeholder | Actor / use case | Business Case objective |
| --- | --- | --- |
| S01 | Runs the tracker, reviews every step | [BC-001] objectives 1 to 5 |
| S02 | Reads and runs the code | [BC-001] objectives 1 to 4 and 6 |
| S03 | Reads the repository page | [BC-001] objective 6 |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | [f9765fd] | |

---

[BC-001]: ./business-case.md
[f9765fd]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/commit/f9765fd3743f46c189359e713fd050c8e1a598b6
