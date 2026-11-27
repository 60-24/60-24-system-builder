# Agent Cycle v0.1 — Operational Contract

## Goal
Enable bounded, evidence-based multi-agent work using GitHub as the queue and shared truth. This is a manual-routing first cycle—not an autonomous orchestrator or permission escalation.

## Cycle
1. **Queue:** coordinator selects a ready Issue.
2. **Route:** designate implementer/auditor/verifier and provide Issue URL. The Issue remains the full brief.
3. **Inspect:** agent reads repository instructions, issue, dependencies and frozen baseline.
4. **Execute:** agent stays within scope and autonomy zone; writes/tests only as permitted.
5. **Evidence:** PR/report includes baseline and commit SHA, files, tests, CI, limitations.
6. **Review:** independent review or coordinator verification; findings become comments or separate bounded Issues.
7. **Decision:** coordinator/human decides acceptance, merge and any scope/security escalation.
8. **Learn:** recurring workflow corrections are incorporated into repository instructions or issues—not hidden in chat.

## Issue readiness checklist
- [ ] One bounded outcome
- [ ] Scope and non-scope
- [ ] Acceptance criteria (observable)
- [ ] Autonomy zone and permitted changes
- [ ] Required baseline/inputs
- [ ] Evidence/report requirements
- [ ] Stop/escalation conditions
- [ ] Agent/role assignment or explicit routing

## Task routing message (short)
> Work on Issue #N in this repository. Read AGENTS.md and all referenced project docs first. Treat the Issue as the task contract; do not broaden scope. Freeze and report the baseline SHA. Follow its autonomy zone and stop conditions. Open a PR (draft if incomplete); do not merge. Report changed files, commit SHA, actual tests/CI, verification evidence, limitations and risks.

## Multi-agent rules
- One implementer per Issue/branch to reduce collisions.
- Audits are read-only and target an exact SHA; auditor should not be the implementer.
- Separate Issues for concurrent work; avoid concurrent edits to the same files.
- Conflicting findings are not averaged: coordinator checks evidence and resolves or escalates.
- Agent assignment/issue creation is not proof of execution. PR, CI and evidence must be inspected.
- Never grant agents broad credentials or bypass protections to make automation easier.

## Rollout
**Phase 0:** instructions and issues, coordinator routes manually; collect evidence.
**Phase 1:** automate routing/notifications only after repeatable cycle is demonstrated.
**Phase 2:** automate bounded execution and verification with protected permissions and fail-closed gates.
Do not advance phases without recorded evidence and review.

## Human approval gates
Require explicit approval before: merge; YELLOW/RED implementation; permissions/secrets; destructive or irreversible actions; release/deploy; scope expansion; resolving conflicting security evidence.
