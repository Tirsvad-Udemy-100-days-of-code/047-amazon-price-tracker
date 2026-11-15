# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-007] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version<br>Accepted after review (RC-001 Go) | [f9765fd] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective 7, success criterion 7, a scope item, an out-of-scope item, a risk and constraints for the baseline milestone MIL-007; set the domain to education; reviewed in autonomous mode, not independent | pending |

---

## Executive Summary

Online prices on Amazon change often. This project builds a small Python bot that reads a product page, extracts the title and the price, and sends an e-mail through the Simple Mail Transfer Protocol (SMTP) when the price drops below a target. It is the Day 47 assignment of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp", built step by step: scrape a static practice page, send the alert, add request headers, then try the live Amazon page.

## Methodological and Standards Foundation

Planning follows the SQA and QC framework mounted at `framework/` (plan first, review each artifact against its quality control (QC) checklist). Quality is described with the International Organization for Standardization and International Electrotechnical Commission standard ISO/IEC 25010:2023 characteristics. Code follows the `coding-conventions` and `clean-architecture` skills.

## Problem Statement

Checking a product price by hand every day costs time, and a short price drop is easy to miss. The course participant also needs a worked, runnable solution to compare with the course material.

## Business Opportunity

A bot that checks the price on its own and sends an alert lets the participant buy at the right moment. As a public repository it also gives other course participants and visitors a readable example.

## Objectives

1. Extract the product title and price as a `float` from the practice page with BeautifulSoup.
2. Send an e-mail with the title, the price and the buy link when the price is below the target.
3. Keep the SMTP address, e-mail address and password in a `.env` file, outside the source code.
4. Send browser-like request headers (`User-Agent`, `Accept-Language`, and the rest of the course set).
5. Try the same code on the live Amazon page and document what happens.
6. Publish the repository with description, topics, README and a wiki in English, Danish and Bahasa Malaysia, with a screenshot for each lecture step.
7. Bring the finished project to the common baseline of the framework: the adopted framework release, a wiki that follows the framework's page and language-line rules, licence and project URL metadata, a README that lists only the documents of the repository, a traceability matrix and review records for every changed document ([MIL-007]).

## Scope

### In Scope

- Python 3.13 or newer, `venv`, `pyproject.toml`, `pytest`, `constants.py`, Doxygen comments and `Doxyfile`.
- The four lecture steps, each delivered by its own branch and pull request.
- README from the framework template and a three-language wiki explaining what each step teaches.
- The baseline milestone [MIL-007]: the framework release, the wiki in the framework's shape (language line first on each page),  the README without the private framework files in its appendix, licence and project URL metadata, `.editorconfig`, `.env.example`, review records and a traceability matrix. It changes no behaviour of the program.

### Out of Scope

- Scheduling the bot to run daily.
- Solving Amazon CAPTCHAs (Completely Automated Public Turing tests, the robot-check pages) or evading bot detection.
- A user interface or a database.
- Importing, testing or committing the personal `.env` of the repository owner.
- Any change to `src/` or `tests/` in the baseline milestone [MIL-007]. No page of a shop site is requested and no e-mail is sent in that milestone; the tests use saved pages and a fake mail connection.

## Expected Benefits

### Tangible Benefits

- A runnable solution for the four lecture steps with tests.
- A documented repository (README, wiki, screenshots) that others can follow.

### Intangible Benefits

- Practice with scraping, SMTP, environment variables and request headers.
- A clear example of plan-first work for course participants.

## Strategic Alignment

The project supports the participant's learning goal in the 100 Days of Code course and the public portfolio of the `Tirsvad-Udemy-100_days_of_code` organisation.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Price extracted from the practice page | `99.99` as a `float` | Unit test with a saved copy of the page |
| 2 | Alert decision | E-mail text built only when price is below target | Unit tests for below, equal and above |
| 3 | Secrets outside the code | No credential in any tracked file | `.env` is ignored; search of the repository finds none |
| 4 | Test suite | All tests pass without network access | `python -m pytest` exits 0 |
| 5 | Documentation | README, wiki in `en`, `da`, `ms`, one screenshot per step | Files exist and are linked |
| 6 | Repository metadata | Description and at least five topics set on the host | Read back from the host API |
| 7 | The baseline milestone is done (objective 7) | Every wiki page starts with its language line, the wiki has a review record, `framework/scripts/check-readme.sh`, `check-languages.sh` and `check-editorconfig.sh` exit with code 0, `python -m pytest` passes, 100 % of the continuous integration (CI) checks of the pull request of [MIL-007] pass | Files in `docs/`, the script exit codes and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Amazon returns a robot-check page (CAPTCHA) or changes its HTML | The live step does not return a price | The live step is documented as best effort; the static page is the tested baseline |
| A token or password is committed | Credential leak | `.env` in `.gitignore`; tokens are read from `.env` only for repository set-up and never copied into the project |
| The practice page changes | A test breaks | Tests use a saved copy of the page |
| Sending real e-mail by accident | Unwanted mail | Tests mock SMTP; the sender is called only from `main` |
| The documents of the baseline milestone [MIL-007] change documents that were accepted earlier, and the AI stand-in for S01 reviews them | A defect is missed because the review is not independent | Every review record of the baseline says `Mode: autonomous, not independent`, `src/` and `tests/` are not changed, the tests run before and after, and the end-of-run summary lists the reviews for challenge |

## Assumptions

- The Product Owner is S01 and reviews every step; S01 can be reached in chat.
- Gitea (the git host) at `git.tirsystem.com` hosts the repository; a Gitea token is in `.env`.
- The practice page `https://appbrewery.github.io/instant_pot/` stays available.

## Constraints

- Python 3.13 or newer; virtual environment `.venv`.
- Runtime dependencies are only the ones needed: `requests`, `beautifulsoup4`, `python-dotenv`.
- Layout `src/`, `tests/`, `docs/`; constants in `constants.py`.
- One branch and pull request per milestone.
- No GUI is involved, so no GUI test environment is needed.
- The baseline milestone [MIL-007] starts 2026-11-16 and is finished within one week, by 2026-11-23. For that milestone only, an AI stand-in for S01 reviews and accepts the changed documents.
- The Product Owner (PO) language is English and the PO domain is education (it was IT until [MIL-007]; the documents that [MIL-007] does not change keep the domain `it`, see the Open Issues of [PP-001]).

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| A few hours of the participant's time; no licence or hosting cost | A working, tested, documented example and a reusable price alert |

The assessment is qualitative on purpose: this is a learning project with no revenue and no budget, so a monetary return on investment (ROI) would be invented; the only cost is the participant's time, and the benefit is the learning and the reusable repository.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; wants a working solution and a clean repository |
| S02 | Readable, runnable code with the assignment's function names, and README run instructions |
| S03 | A clear description, topics and README, and no runtime dependencies beyond the necessary |

## Recommendation

Proceed — the scope is small, the cost is low and every objective is testable.

---

[f9765fd]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/commit/f9765fd3743f46c189359e713fd050c8e1a598b6
[SA-001]: ./stakeholder-analysis.md
[PP-001]: ./project-plan.md
[MIL-007]: ./milestones/mil-007-framework-baseline.md
