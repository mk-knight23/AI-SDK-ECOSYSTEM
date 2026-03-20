# Deployment Matrix

| Adapter | Runtime | Packaging | Deployment Target (recommended) |
|---|---|---|---|
| langchain | Python | Docker | Railway / Fly / ECS |
| langgraph | Python | Docker | Fly / Kubernetes |
| llamaindex | Python | Docker | Railway / ECS |
| openai_agents | Python | Docker | ECS / Cloud Run |
| anthropic | Python | Docker | Fly / Cloud Run |
| autogen | Python | Docker | AKS / ECS |
| crewai | Python | Docker | Render / ECS |
| haystack | Python | Docker | Kubernetes |
| semantic_kernel | Python | Docker | Azure Container Apps |
| vercel_ai | Node/TypeScript | Vercel build | Vercel |

## Common Production Requirements
- Secrets manager for API keys
- Centralized logs and traces
- Rate limiting + auth gateway
- Eval and regression test suite
- Rollback-capable release process
