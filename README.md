# AI-SDK-ECOSYSTEM

Unified control plane for Kazi's AI SDK adapter fleet.

## Current Features

- Shared Agents Army registry with ZEUS, ATLAS, SENTINEL, FORGE, NEXUS, PIXEL, PULSE, TITAN, HERMES, and ORACLE.
- Mission planning with primary/support agent routing and skill focus.
- `ecosystem_runner.py` for running one adapter or the whole local fleet.
- Deployment specs, secret checklist, Kubernetes template, Docker Compose file, and rollout runbook.
- Smoke scripts for Python adapters and ecosystem routes.
- GitHub Actions workflows for CI, adapter image build/push, and manual deploy.
- Portfolio metadata and a lightweight GitHub Pages card.

## Adapter Feature Inventory

| Repository | SDK | Current implemented feature |
| --- | --- | --- |
| AI-SDK-OPENAI | OpenAI Agents | Agent object creation with safety-oriented mission instructions |
| AI-SDK-VERCEL-AI | Vercel AI SDK | Typed routing and streaming-ready prompt rendering |
| AI-SDK-LANGGRAPH | LangGraph | StateGraph route/plan/verify flow |
| AI-SDK-LANGCHAIN | LangChain | ChatPromptTemplate orchestration |
| AI-SDK-LAMA-INDEX | LlamaIndex | Document indexing and query-engine path |
| AI-SDK-HAYSTACK | Haystack | Pipeline initialization for retrieval workflows |
| AI-SDK-CREWAI | CrewAI | Agent, Task, and Crew scaffold |
| AI-SDK-AUTOGEN | AutoGen | AssistantAgent validation path |
| AI-SDK-SEMANTIC-KERNEL | Semantic Kernel | Kernel initialization for plugin-first copilots |
| AI-SDK-ANTHROPIC | Anthropic | Claude client initialization with policy-first positioning |

## Existing Runtime Flow

1. A mission enters the control plane.
2. The shared router scores it against the Agents Army skill registry.
3. The selected adapter receives a normalized mission contract.
4. The adapter validates its SDK-specific execution path.
5. CI, smoke scripts, and tests protect the contract before release.

## Run The Fleet

```bash
python3 ecosystem_runner.py --mission "build secure AI workflow and deploy"
```

Run a single adapter:

```bash
python3 ecosystem_runner.py --framework langgraph --mission "add durable workflow and evals"
```

## Test

```bash
python3 -m pytest
```

## Documentation Map

- `SKILLSET.md`: platform and framework skill coverage.
- `DEPLOYMENT-MATRIX.md`: recommended deployment target by adapter.
- `deploy/DEPLOY-SPEC.md`: deployment contract.
- `deploy/FIRST-ROLLOUT-RUNBOOK.md`: first staging-to-production rollout path.
- `deploy/SECRETS-CHECKLIST.md`: required secrets.
- `docs/CURRENT_FEATURES.md`: concise inventory of implemented and future features.

## Upgrade Roadmap

- Add a benchmark/evaluation harness for quality, cost, and latency comparison.
- Add adapter discovery instead of the static runner mapping.
- Add live provider execution behind environment-scoped credentials.
- Add centralized observability across all adapter runs.
- Publish the ecosystem as the portfolio hub linking all SDK repos.

## Clean Repository Policy

Generated caches, local secrets, dependency folders, and build output are ignored. Source, docs, tests, deployment specs, and portfolio files are intentionally tracked.
