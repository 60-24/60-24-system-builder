# System Builder — Bootstrap v0.1.1

Minimal, deterministic project-generation foundation.

## Requirements
- Python 3.11+
- Runtime uses only the Python standard library.

## Quick start
```bash
python -m unittest discover -s tests -v
python -m system_builder.cli examples/intent.json ./build-output
```

The builder validates a JSON intent, creates a deterministic build plan, writes only new files beneath the chosen output directory, and emits a SHA-256 manifest.

## Safety boundary
This bootstrap does **not** execute generated code, invoke shell commands, access the network, deploy software, integrate an LLM/agent, or modify its own source. It rejects absolute paths and path traversal, and refuses to overwrite existing generated files or the manifest.

## Current maturity
Bootstrap foundation only. Passing local tests does not imply production readiness. CI evidence is recorded by GitHub Actions after the first push.

## Design principle
Human intent → validated specification → deterministic plan → controlled file generation → verifiable evidence.
