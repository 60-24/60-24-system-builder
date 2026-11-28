# System Builder — Agent Operating Rules

## Source of truth
- Repository files and GitHub Issues/PRs are authoritative; chat context is secondary.
- Before work, read this file, the issue, referenced project docs, current branch and baseline.
- Record exact baseline SHA. If it moves, reassess before continuing.
- Never infer repository state, test execution, agent activity or permissions from a previous chat/report; verify current evidence.

## Understand before acting
Before execution, convert the request into a compact task model:
1. **Outcome:** what observable project result is wanted, and why it matters to the parent goal.
2. **Inputs:** issue, files, decisions, baseline, dependencies and evidence available.
3. **Scope / non-scope:** what may and may not change.
4. **Acceptance:** objective checks that demonstrate completion.
5. **Autonomy / risk:** GREEN, YELLOW, RED or BLACK; identify irreversible or external effects.
6. **Unknowns:** assumptions, conflicts and missing facts.

If the task is materially ambiguous, contradictory, unbounded or missing a decision that changes architecture/security/product behavior, stop and ask one focused question or present a decision proposal. Do not silently guess. For routine ambiguity, state a conservative assumption and proceed only if reversible and within scope.

Separate the user's **goal** from the requested **method**. Prefer the smallest safe method that achieves the goal. Do not optimize a local Issue in a way that harms system-level direction. If acceptance criteria conflict with the parent goal or repository invariants, report the conflict rather than blindly satisfying the checklist.

## Routing
- Coordinator selects a ready Issue and assigns a specific agent and role. Agents do not self-assign or expand work.
- The Issue is the task contract: scope, deliverables, acceptance, restrictions and evidence.
- Route with Issue URL/number plus necessary context not already in the repo; do not paste the whole Issue unnecessarily.
- Issue creation or assignment is not proof that an agent started or completed work.

## Roles
- **Coordinator:** prioritizes, decomposes, routes, resolves conflicts, reviews evidence and authorizes protected decisions.
- **Implementer:** executes bounded scope, tests, documents and opens a PR; never merges.
- **Independent auditor:** read-only review of a frozen SHA; different agent from implementer where practical.
- **Verifier:** checks acceptance and reproduces critical evidence; must identify what was independently verified versus merely reported.
- One implementer per branch/Issue. Parallel work requires separate non-overlapping tasks.

## Autonomy zones
- **GREEN:** bounded tests, documentation, safe fixes and implementation explicitly permitted by Issue.
- **YELLOW:** protocol/API/data-model, cross-layer or material dependency changes; proposal and explicit human approval before implementation.
- **RED:** constitution, trust model, identity/governance and fundamental security policy; human decision required.
- **BLACK:** contradiction, invariant violation, unsafe/destructive action, secret exposure or unknown critical state; stop.

An Issue can narrow autonomy but cannot grant authority beyond repository policy. GREEN is not permission to change adjacent scope.

## Execution protocol
1. Inspect repository, instructions, issue, dependencies, branch and baseline.
2. Write a short understanding/plan for non-trivial work; identify risk and expected evidence.
3. Confirm the plan fits both the Issue and parent project goal.
4. Implement the smallest coherent change; avoid unrelated edits.
5. Add/update tests as appropriate and run relevant commands.
6. Inspect the final diff, changed-file list and scope; check for resource cleanup, failure paths and unintended effects.
7. Open/update a PR; keep draft if validation, review or a decision is incomplete.
8. Report exact evidence and remaining work. Do not claim completion merely because code was committed.

## Evidence and status
Use only: **OPEN**, **IN PROGRESS**, **BLOCKED**, **IN REVIEW**, **VERIFIED**, **CLOSED**.
- **VERIFIED** requires acceptance checks plus independent or clearly described verification. A green badge or implementer's assertion alone is insufficient.
- Attribute evidence: implementer-reported local test, independently reproduced local test, CI for exact SHA, static review, mutation test, device/network test.
- Record command, environment, exact SHA, result and limitations. Distinguish not run from failed.
- For audits, cite frozen SHA and file/line; state severity, impact, reproduction and confidence.
- A mutation result is reproducible only if mutation instructions or scripts are preserved.

## Stop and escalation
Stop when requirements conflict, scope is unclear, baseline changes materially, tests reveal security/architecture defects, credentials are needed, or out-of-scope changes become necessary. Report facts, impact and the smallest decision needed. Never hide uncertainty behind a status label.

## Protected actions
No merge, release, deploy, permission/secret change, destructive or irreversible action, broad credential grant, or additional agent launch without explicit authorization. No self-approval or merging one's own work.

## Minimal handoff
**Goal/outcome; Issue/PR; baseline and commit SHA; scope/files; actual commands/results; CI for exact SHA; independent review; limitations/risks; deviations; next decision.**
