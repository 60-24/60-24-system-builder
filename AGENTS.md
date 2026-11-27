# System Builder — Agent Operating Rules

## Source of truth
- Repository files and GitHub Issues/PRs are authoritative; chat context is secondary.
- Before work, read this file, the issue, relevant project docs, and current branch/commit.
- Record the exact baseline SHA in the report/PR. If baseline changes, reassess before continuing.

## Routing
- The coordinator assigns a specific Issue to an agent and role. Agents do not select, claim, or expand tasks unilaterally.
- The Issue is the task brief: scope, deliverables, acceptance criteria, restrictions and evidence expectations.
- Do not copy the full Issue into prompts. Send the Issue URL/number plus this repository's instructions and any necessary context not already in the repo.
- If an issue is unassigned, do not assume authorization to work on it.

## Roles
- **Coordinator (ChatGPT or designated human):** prioritizes, routes, resolves conflicts, reviews evidence and authorizes protected decisions.
- **Implementer (Claude/Copilot/other):** executes bounded issue scope, tests, documents, opens PR; no merge.
- **Independent auditor (different agent):** read-only review of frozen commit; reports findings with file/line and reproducible evidence; no implementation.
- **Verifier:** validates acceptance criteria and CI/evidence. Prefer independent verification for security-sensitive changes.

## Autonomy zones
- **GREEN:** bounded tests, documentation, safe fixes, implementation explicitly permitted by Issue.
- **YELLOW:** protocol/API/data-model, cross-layer or material dependency changes; proposal and explicit human approval before implementation.
- **RED:** constitution, trust model, identity/governance, fundamental security policy; human decision.
- **BLACK:** conflict, invariant violation, unsafe action, uncertain state, destructive operation, secret exposure; stop and report.

An Issue can narrow autonomy but cannot grant authority beyond repository policy. GREEN is not permission to change adjacent scope.

## Execution protocol
1. Inspect status, branch, issue, instructions and baseline.
2. Summarize proposed steps and risks in the Issue/PR if materially non-trivial.
3. Implement the smallest coherent change; avoid unrelated edits.
4. Add or update tests as appropriate and run relevant commands.
5. Review the diff, scope and safety implications.
6. Open a PR; keep it draft if validation is incomplete or a decision is pending.
7. Report commit SHA, changed files, commands/results, evidence links, limitations and unresolved risks.
8. Do not merge, deploy, publish releases, change secrets/permissions, or initiate additional agents unless explicitly authorized.

## Evidence and status
Use only these statuses: **OPEN**, **IN PROGRESS**, **BLOCKED**, **IN REVIEW**, **VERIFIED**, **CLOSED**.
- VERIFIED requires independent or otherwise clearly described verification evidence; a green CI badge alone is not sufficient.
- Distinguish locally executed tests, CI runs, static inspection, mutation checks and unverified assumptions.
- Never report PASS/GREEN without evidence and scope.
- For audit findings, reference frozen SHA and include file/line, severity, impact and reproduction/verification status.

## Task boundaries
- Issue acceptance criteria and restrictions define completion.
- If requirements conflict, scope is unclear, tests expose a security/architecture defect, or changes outside scope appear necessary: stop, comment with evidence and request a decision.
- No unsafe shell commands, deletion outside task scope, credential handling, or secret commits.
- No self-approval or merging one's own work.

## Minimal handoff
Issue/PR report: **baseline SHA; commit SHA; scope/files; tests and actual outcomes; CI links/status; audit/verification; deviations; risks; next decision**.
