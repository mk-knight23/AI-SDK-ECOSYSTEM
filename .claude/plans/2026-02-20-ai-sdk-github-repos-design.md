# Design: 10 AI-SDK GitHub Repositories

**Date:** 2026-02-20
**Status:** ✅ Approved

---

## Overview

Split the AI-SDK-PROJECTS monorepo into 10 standalone GitHub repositories under `mk-knight23/`, each showcasing a different AI SDK integration.

---

## Repository Mapping

| Project | SDK | Repository | Frontend | Backend | Platform |
|---------|-----|-----------|----------|---------|----------|
| 01-venture-graph | LangGraph | `AI-SDK-LANGGRAPH` | Next.js 15 | FastAPI | Railway |
| 02-omni-desk | LangChain | `AI-SDK-LANGCHAIN` | React 19 | FastAPI | Render |
| 03-dev-squad | OpenAI | `AI-SDK-OPENAI` | SvelteKit | Node.js | Fly.io |
| 04-supply-consensus | AutoGen | `AI-SDK-AUTOGEN` | Vue 3 | .NET 9 | Azure |
| 05-market-pulse | Google ADK | `AI-SDK-GOOGLE-ADK` | Angular 19 | Go | GCP Cloud Run |
| 06-insight-stream | Vercel AI | `AI-SDK-VERCEL-AI` | Next.js 15 RSC | - | Vercel |
| 07-research-synthesis | LlamaIndex | `AI-SDK-LLAMAINDEX` | Remix | FastAPI | Fly.io |
| 08-trend-factory | CrewAI | `AI-SDK-CREWAI` | Nuxt 3 | Django | Render |
| 09-patent-iq | Haystack | `AI-SDK-HAYSTACK` | Astro 5 | Flask | AWS ECS |
| 10-claude-forge | Claude SDK | `AI-SDK-CLAUDE` | T3 Stack | FastAPI | Fly.io |

---

## Approach: Monorepo Split

Using `git filter-repo` or subtree splitting to extract each project with clean git history.

---

## Unified README Template

Each repo will have a consistent README with:
- SDK badges (version, frontend, backend, tests, license)
- Quick start commands
- Tech stack details
- Testing instructions
- Deployment guide
- API documentation
- Contributing guidelines
- MIT License

---

## Automation Script

The script will:
1. Create 10 GitHub repos via `gh` CLI
2. Extract each project with clean git history
3. Apply unified README template
4. Add SDK-specific badges and metadata
5. Push to GitHub with proper tags
6. Generate summary report

---

## Success Criteria

- [ ] 10 GitHub repositories created under `mk-knight23/`
- [ ] Each repo has clean git history (no unrelated commits)
- [ ] Unified README template applied to all repos
- [ ] All tests passing in each repo
- [ ] Deployment configs included
- [ ] Summary report generated

---

**Next Step:** Invoke writing-plans skill to create implementation plan.
