# Agent Work Packet and Report Template

**Purpose:** Standardize task delegation, evidence, and handoffs across AI agents.

## A. Task packet (coordinator fills before delegation)

- **Task ID:** unique identifier
- **Project / repository:**
- **Base branch / exact SHA:**
- **Assigned role:** Executor / Reviewer / Researcher / Test Engineer
- **Objective:** one bounded outcome
- **Scope:** files, components, or behavior included
- **Out of scope:**
- **Autonomy zone:** GREEN / YELLOW / RED / BLACK
- **Acceptance criteria:** observable, testable statements
- **Required evidence:** commands, test cases, artifacts, CI link
- **Iteration / time / resource limit:**
- **Allowed actions:**
- **Prohibited actions:** merge, default-branch changes, deployment, permission/secrets changes, destructive actions, etc.
- **Stop conditions:** conflict, unclear requirement, unsafe action, repeated failure, or missing permission
- **Expected output:** PR, report, test artifact, or proposal

## B. Agent completion report (executor fills)

### Status
PASS / INCOMPLETE / BLOCKED / FAIL. Status must be supported by evidence.

### Scope and baseline
- Task ID:
- Repository:
- Branch:
- Base SHA:
- Final SHA (if changes):
- Scope completed:

### Changes
- Files changed and purpose:
- PR / commit link:

### Evidence
For every check, report:
- Exact command or CI link:
- Environment / runner:
- Result:
- Test count and failures, if applicable:

Do not claim execution for checks not actually run. Distinguish local evidence from CI evidence.

### Findings and unresolved items
- Verified facts:
- Assumptions:
- Risks:
- Known limitations:
- Blockers:

### Next step
One bounded, dependency-aware recommendation. Do not silently expand scope.

## C. Independent reviewer report

- Exact PR and head SHA reviewed:
- Scope actually inspected:
- Findings, each with file/line or reproducible evidence:
- Acceptance criteria: PASS / FAIL / NOT VERIFIED (individually)
- Test evidence checked:
- Residual risk:
- Recommendation: READY FOR HUMAN DECISION / CHANGES REQUIRED / BLOCKED

Reviewer must inspect the artifacts and diff; an executor's narrative alone is not evidence.

## D. Evidence and decision rules

- Repository artifacts and verified CI results outrank chat statements.
- No agent may merge or modify the default branch.
- GREEN tasks permit bounded, reversible work on isolated branches and draft PRs.
- YELLOW tasks require design proposal and approval before implementation.
- RED decisions remain human-controlled.
- BLACK conditions require stopping and reporting.
- A PASS is not a security certification or production-readiness claim.
- No persistent background activity may be claimed unless a running and observable automation exists.


## E. Evidence matrix (when useful)

| Requirement | Test/check | Evidence (SHA/run/command) | Risk/limitation | Status |
|---|---|---|---|---|
| | | | | open / in review / verified / blocked / done |

Use only rows relevant to the task; do not duplicate established test reports.

## F. Test-safety note

- Use project test helpers and isolated temporary directories.
- Cleanup must be scoped to the test-owned path; never target a home directory or other broad path.
- Report the exact environment and cleanup behavior when relevant.

## G. Audit baseline

- Audited commit SHA (freeze scope):
- Exact files/areas inspected:
- Evidence independently checked:
- Tests rerun / not rerun:
- Findings (severity, location, scenario, evidence):
- Untested areas / limits:
- Recommendation: READY FOR HUMAN DECISION / CHANGES REQUIRED / BLOCKED
