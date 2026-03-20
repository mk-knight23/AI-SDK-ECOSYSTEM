# Project Brain: ecosystem

## Purpose
Provide a unified launcher and comparison layer across all Kazi's Agents Army framework adapters.

## Scope
- Normalized mission schema
- Framework adapter discovery
- Environment validation per adapter
- Consistent run and smoke-test interface

## Current State
- Shared routing core available in `implementations/core/agents_army_core`.
- Framework-specific adapters created for 10 framework targets.

## Next Build
- Add a single CLI: `python ecosystem_runner.py --framework <name> --mission "..."`.
- Add benchmark/eval harness for quality/cost/latency comparison.
- Add deployment matrix and IaC stubs for each framework target.
