# Agent Cycle v0.2 — Goal-aligned, evidence-based collaboration

## Purpose
Deliver useful, bounded project outcomes through GitHub. This is a coordinated, manual-first process—not an autonomous orchestrator and not permission escalation.

## Cycle
1. **Orient:** read repository instructions, parent goal, current state and relevant decisions.
2. **Understand:** state outcome, why it matters, inputs, scope/non-scope, acceptance, autonomy zone and unknowns.
3. **Decompose:** create one bounded Issue per independently deliverable task; order dependencies. Do not split work so finely that integration/evidence is lost.
4. **Route:** coordinator names implementer, independent auditor and verifier as needed. Issue URL is the task contract.
5. **Inspect:** freeze baseline SHA; inspect code, tests, workflows and dependencies before proposing edits.
6. **Plan:** concise plan and risk statement for non-trivial work. Resolve material ambiguity before implementation.
7. **Execute:** smallest coherent change within authorized scope.
8. **Prove:** run relevant tests; inspect diff; capture exact SHA, commands, results, CI and limitations.
9. **Audit:** independent read-only review against frozen SHA, task contract and parent goal. Reproduce critical claims where practical.
10. **Decide:** coordinator/human accepts, requests changes, defers or escalates. Merge remains a separate protected action.
11. **Learn:** update repository instructions when a lesson is reusable; do not let chat-only rules become hidden policy.

## Issue readiness checklist
- [ ] One observable outcome linked to parent goal
- [ ] Context, inputs and frozen baseline known
- [ ] Scope and non-scope explicit
- [ ] Acceptance criteria testable
- [ ] Autonomy zone and permitted files/actions explicit
- [ ] Dependencies and sequencing identified
- [ ] Evidence and verification expectations stated
- [ ] Stop/escalation conditions stated
- [ ] Agent/role routing explicit

## Routing message
> Work on Issue #N. Read repository instructions and referenced docs first. Confirm the intended outcome, scope, autonomy and baseline SHA. If material ambiguity or a conflict with project invariants exists, stop and report it. Otherwise execute only the Issue, test and inspect the diff, then open a draft PR if any validation/decision remains. Report exact SHA, files, commands/results, CI, evidence source, limitations and next decision. Do not merge.

## Multi-agent rules
- One implementer per Issue/branch; concurrent tasks must not collide on files or dependencies.
- Auditor is read-only and reviews an exact SHA; prefer a different agent from implementer.
- Verifier distinguishes independent reproduction from reading the implementer's report.
- Conflicting findings are resolved by evidence and scope, never averaged or decided by majority vote.
- Agent assignment, comments or a generated report do not prove execution. Verify commits, PR, checks and artifacts.
- Keep prompts short by linking to the Issue and repository contract; provide only context absent from the source of truth.
- Do not give broad credentials or bypass protections to simplify routing.

## Evidence levels
- **E0 — assertion:** agent says it happened.
- **E1 — artifact:** commit, diff, test log or workflow link exists.
- **E2 — reproduced:** another actor reruns the relevant check on the stated SHA.
- **E3 — integrated:** required CI and acceptance checks pass on the current PR head.
- **E4 — operational:** required real environment/device/network validation passes.
Do not promote a task beyond the strongest evidence actually obtained. Evidence levels are not substitutes for risk review.

## Rollout
**Phase 0:** manual routing, documented contract, bounded Issues, evidence collection.
**Phase 1:** automate notifications/routing only after several repeatable cycles and measured failure handling.
**Phase 2:** bounded execution/verification with least privilege, protected branches, explicit human gates and fail-closed behavior.
No phase advancement without recorded evidence and review.

## Human approval gates
Explicit approval required for merge; YELLOW/RED implementation; permissions/secrets; destructive or irreversible actions; release/deploy; scope expansion; resolving conflicting security evidence; launching additional agents or autonomous workflows.
