# MIL-001 foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version<br>Accepted after review (RC-004 Go) | [f9765fd] |

---

## Purpose

Decide whether the repository is ready for feature work: project configuration, environment instructions, documentation skeleton and host metadata are in place.

## Deliverable

Branch `mil-001-foundation` merged: `pyproject.toml`, `.gitignore`, `.env.example`, `constants.py`, `Doxyfile`, README from the framework template, a passing smoke test, and the repository description and topics on the host (set through its application programming interface, API).

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pip install -e .[dev]` works in a fresh `.venv` on Python 3.13 or newer | `python -m pytest` exits 0 | Install or tests fail |
| 2 | `.env` is ignored and no secret is tracked | `git ls-files` lists no `.env` | A secret is tracked |
| 3 | README follows the template and explains venv, `python -m pip install --upgrade pip`, run and test | `framework/scripts/check-readme.sh` passes | Check fails |
| 4 | Repository description and at least five topics are set | Read back from the Gitea API | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway; it has no predecessor |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 6 (repository set-up, README, metadata) and the Constraints section of [BC-001] | Tasks of this gateway |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-28 — within the Business Case constraints (one branch and pull request per milestone).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Set a one-sentence description and topics (python, web-scraping, beautifulsoup, smtp, udemy, 100-days-of-code) on the Gitea repository through its API. The token is read from the personal `.env` at call time; it is never copied into the project, imported or tested. | No |  |
| 2 | Create pyproject.toml and package layout | Python `>=3.13`, setuptools `src` layout with package `amazon_price_tracker`, runtime dependencies `requests`, `beautifulsoup4`, `python-dotenv` only, a `dev` extra with `pytest`, and pytest config (`pythonpath`, `testpaths`). | No |  |
| 3 | Add constants.py and .env.example | `constants.py` holds the practice URL, target price, default headers and environment variable names. `.env.example` lists `SMTP_ADDRESS`, `EMAIL_ADDRESS`, `EMAIL_PASSWORD` with placeholders so S02 knows what to create. | No |  |
| 4 | Add Python .gitignore and Doxyfile | Standard Python `.gitignore` plus `.env`, `.venv`, `docs/doxygen`. A `Doxyfile` that reads `src/` and writes HTML to `docs/doxygen`; source comments use the Doxygen style (`@brief`, `@param`, `@return`). | No |  |
| 5 | Write README from the framework template | Fill `framework/templates/README-template.md`: overview, requirements, setup with `python -m venv .venv`, activation on Windows and Linux, `python -m pip install --upgrade pip`, run, tests, license, links, appendix. | No |  |
| 6 | Add smoke test | A first test that imports the package and checks `constants` so the test run and CI path work before features arrive. | No |  |

---

[BC-001]: ../business-case.md
[f9765fd]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/commit/f9765fd3743f46c189359e713fd050c8e1a598b6
