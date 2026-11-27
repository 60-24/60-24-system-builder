# Multi-Agent Autonomy Protocol v0.1

**Status:** Draft — repository proposal  
**Applies to:** System Builder initially; reusable by P2P only after a separate review.  
**Authority:** Repository state and test evidence override conversational claims.

## Purpose

Move project work from prompt-by-prompt assistance to bounded, evidence-driven agent cycles. Agents may independently inspect, plan, implement, test, document, and prepare pull requests inside explicit autonomy boundaries. This protocol does not grant agents unrestricted authority.

## Roles (capabilities, not fixed model identities)

- **Coordinator / Architect:** decomposes goals, tracks dependencies and status, assigns work, checks contracts and evidence.
- **Executor:** makes the smallest coherent change, tests it, and records results.
- **Independent Reviewer:** examines the diff, specification, tests, risks and evidence; does not rely solely on the executor's summary.
- **Human:** sets goals and values; decides constitutional, high-risk, irreversible or explicitly reserved changes.

One model may perform multiple roles, but independent review should preferably be performed by a different agent or process.

## Work cycle

1. **INSPECT:** verify repository, branch, current state, docs, open work and CI.
2. **UNDERSTAND:** identify applicable requirements, invariants and constraints.
3. **GAP:** define a bounded problem and measurable acceptance criteria.
4. **RED:** add a failing test or reproducible evidence where feasible.
5. **IMPLEMENT:** make the smallest change in an isolated branch/worktree.
6. **GREEN:** run tests, lint/build/security checks applicable to the change.
7. **EVIDENCE:** record commands, results, commit, diff and limitations. Never claim a test ran if it did not.
8. **AUDIT:** review changed files, test coverage, risks and acceptance criteria.
9. **STONE:** close only when acceptance criteria and evidence are satisfied; otherwise mark BLOCKED or INCOMPLETE.
10. **NEXT:** select the next safe, dependency-ready task; avoid unbounded loops.

## Autonomy zones

- **GREEN — autonomous:** inspection, non-destructive research, tests, documentation, isolated implementation, refactoring, bug fixes and draft PRs within established requirements.
- **YELLOW — proposal first:** protocol/API/data-model changes, dependency additions, cross-project changes, significant architectural choices, or changes with broad effects. Prepare impact analysis and tests; obtain approval before committing implementation.
- **RED — human decision:** constitutional, identity/trust, privacy/governance, security policy, irreversible migrations, release/publishing and production-impacting decisions.
- **BLACK — stop:** contradictions, unknown permissions, suspected secret exposure, unsafe environment, destructive actions, or inability to establish trustworthy evidence.

## Boundaries

- Prefer repository-native tools, isolated branches and minimal diffs.
- Never expose, copy or commit secrets; do not request broad credentials.
- Do not delete, force-push, rewrite history, merge to protected/default branch, deploy, purchase or change permissions without explicit authorization.
- No agent may treat another agent's assertion as verification; inspect artifacts and reproduce checks where possible.
- Never claim background or cross-session work unless an actual scheduler/agent environment is running and observable.
- A task must have a bounded objective, acceptance criteria, budget/iteration limit and stop condition.
- When blocked, record the exact blocker and safe next step; do not repeatedly retry failed permission actions.

## Task contract

Every delegated task should contain:

- Objective and scope
- Repository and base ref
- Frozen constraints / autonomy zone
- Acceptance criteria
- Required tests and evidence
- Explicit prohibited actions
- Stop / escalation conditions

## Handoff and durable memory

Store durable project state in versioned repository artifacts, not only chat context. A closeout/handoff should include:

- status (PASS, INCOMPLETE, BLOCKED, FAIL)
- current commit and branch
- completed work and changed files
- exact verification commands/results
- outstanding risks and dependencies
- next recommended bounded task

## Minimal reporting

Report only: **Status | Evidence | Risks/Blockers | Next step**. Use links/commit identifiers when available. Distinguish verified facts from assumptions.

## Adoption

This protocol is a draft for System Builder. It does not automatically govern P2P. Adoption in another repository requires checking that repository's constitution, agent instructions and autonomy boundaries.


## Evidence and verification standard (proposal)

- Work states are `open`, `in review`, `verified`, `blocked`, and `done`. `open` or `in review` never imply completion. `done` requires acceptance criteria and evidence; `verified` describes checks independently confirmed.
- Evidence records the exact commit SHA, CI run/link or local command, environment/runner, outcome, and limitations. Tests not rerun in a check must be explicitly identified as historical/reported evidence, not fresh verification.
- Independent audits use a frozen commit SHA and report scope inspected, findings with file/line and reproducible evidence, unverified areas, and recommendation. Auditors should inspect artifacts rather than rely on summaries.
- Where practical, track requirements in a compact matrix: requirement → test/check → evidence → risk → status. Avoid duplicating existing repository records.
- Protocol/format compatibility should be protected by contract tests or equivalent deterministic fixtures. Changes must not silently alter wire-format behavior.
- Test helpers and scripts must use isolated, bounded temporary paths and safe cleanup. Never use broad/destructive cleanup targets (for example, `$HOME`) or unchecked recursive deletion.
- CI security checks (secret scanning, dependency checks and SAST where supported) are supplemental evidence; findings are triaged and their limits documented.
- Significant architecture decisions should use concise ADRs. Keep decision records proportionate and avoid redundant documentation.
- Security, identity, trust, privacy, encryption, key lifecycle, repository protection settings and merge/release decisions remain human-gated where they fall in RED/YELLOW boundaries. This standard does not itself authorize such changes.
