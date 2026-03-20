# Kazi's Agents Army Deploy Spec

## Target Units
- Python adapters: langchain, langgraph, llamaindex, openai_agents, anthropic, autogen, crewai, haystack, semantic_kernel
- TypeScript adapter: vercel_ai

## Deployment Contract
- Each Python adapter exposes:
  - `uvicorn api:app --host 0.0.0.0 --port 8000`
  - `GET /health`
  - `POST /run` with `{ "mission": "..." }`
- `vercel_ai` runs via Node and can be deployed on Vercel.

## Required Secrets (by platform)
- OPENAI_API_KEY
- ANTHROPIC_API_KEY
- LANGSMITH_API_KEY (optional)

## Release Gates
1. CI compile + smoke checks pass.
2. Container image builds for all Python adapters.
3. Staging health checks green.
4. Production rollout with rollback strategy.

## Suggested Rollout Order
1. langgraph
2. openai_agents
3. langchain
4. remaining adapters in batches
