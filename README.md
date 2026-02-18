# AI SDK Projects - Week 1 Complete

**10 AI SDK SaaS projects scaffolded in parallel using git worktrees and agents.**

**Date:** 2026-02-19 | **Status:** ✅ Week 1 Complete

---

## Projects

| # | Project | Stack | Deployment Target |
|---|---------|-------|-------------------|
| 01 | VentureGraph | Next.js 15 + FastAPI | Railway |
| 02 | OmniDesk | React 19 + FastAPI | Render |
| 03 | DevSquad | SvelteKit + Node.js | Fly.io |
| 04 | SupplyConsensus | Vue 3 + .NET 9 | Azure |
| 05 | MarketPulse | Angular 19 + Go | GCP Cloud Run |
| 06 | InsightStream | Next.js 15 RSC + Vercel AI SDK | Vercel |
| 07 | ResearchSynthesis | Remix + Python | Fly.io |
| 08 | TrendFactory | Nuxt 3 + Django | Render |
| 09 | PatentIQ | Astro 5 + Flask | AWS ECS |
| 10 | ClaudeForge | T3 Stack + Python | Fly.io |

---

## Quick Start

```bash
# Validate all deployments
./scripts/validate-deployments.sh

# Attach to tmux session
tmux attach -t ai-sdk-projects

# Check worktrees
git worktree list
```

---

## Architecture

```
projects/
├── 01-venture-graph/     # Next.js + FastAPI
├── 02-omni-desk/         # React + FastAPI
├── 03-dev-squad/         # SvelteKit + Node.js
├── 04-supply-consensus/  # Vue + .NET 9
├── 05-market-pulse/      # Angular + Go
├── 06-insight-stream/    # Next.js RSC + Vercel AI SDK
├── 07-research-synthesis/# Remix + Python
├── 08-trend-factory/     # Nuxt + Django
├── 09-patent-iq/         # Astro + Flask
└── 10-claude-forge/      # T3 Stack + Python
```

---

## Week 2: AI Integration Complete ✅

All 10 projects now have functional AI SDK integrations:

| Project | AI Feature | SDK |
|---------|-----------|-----|
| VentureGraph | Venture planning workflow | LangGraph |
| OmniDesk | Enterprise RAG | LangChain |
| DevSquad | Code review & test gen | OpenAI SDK |
| SupplyConsensus | Multi-agent supply chain | AutoGen |
| MarketPulse | Competitor intel | Google ADK |
| InsightStream | Streaming AI responses | Vercel AI SDK |
| ResearchSynthesis | Knowledge graph | LlamaIndex |
| TrendFactory | Marketing crew | CrewAI |
| PatentIQ | Patent search | Haystack |
| ClaudeForge | Coding agent | Claude SDK |

### Test AI Integrations

```bash
./scripts/test-all-ai.sh
```

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```sh
# create a new project
npx sv create my-app
```

To recreate this project with the same configuration:

```sh
# recreate this project
npx sv create --template minimal --types ts --install npm .
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```sh
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```sh
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.
