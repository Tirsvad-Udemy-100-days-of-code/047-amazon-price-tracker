# RC-003 Project Plan review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none (the reviewer reads English and knows the domain IT; mode: AI as stand-in for S01)
- Mode: autonomous, not independent (AI as stand-in for S01); the author and the stand-in are both the AI working for S01

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-10-28, end 2026-11-04, constraint: soft target, one pull request per gateway (BC-001 Constraints) |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Six rows, each with document, decision date and owner S01 |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates match the Target Date of each MIL document and lie in the window |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage table maps every in-scope item to a gateway |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain MIL-001 to MIL-006; windows follow the order and do not overlap |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies section says a No-Go moves later windows and that S01 decides about the end date |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owner and reviewer use S01; no governance document exists, which the plan states |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Planning Assumptions give the source of the dates and say no earlier baseline exists |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan Risks have mitigations and one traces to the Business Case risk 1 |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues list two items; neither contradicts the plan |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Main deliverable text is taken from each MIL Deliverable section |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column says 'none (technical tasks)' |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt bars match the table windows; the chain matches the dependency list |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Milestone column says 'not yet synced' |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | One Project Plan; Version History holds the change |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has `Language | en` and `Domain | it` |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry domain list |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English; the stand-in reads English |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Executive types use IT Executive English, technical types IT Professional English, as the registry says; plain sentences, no jargon beyond IT terms |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No dictionary (DICT) exists in this project; terms are used consistently (price, target price, alert, gateway) and no synonyms for them were found |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No `<name>.<language>.md` twin exists |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no language change since an earlier accepted version |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The stand-in reads English and knows the IT domain; not independent of the author (recorded in Mode) |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (SMTP, CAPTCHA, ROI, API, QC, ISO/IEC) are spelled out on first use |

## Overall Verdict

Go — all criteria pass; acceptance by the Product Owner is made by the stand-in.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None: no Fail and no Pending criterion | S01 | 2026-10-28 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
