# AI-SDK Ecosystem Transformation Design

**Date:** 2026-02-20
**Status:** Approved
**Author:** Claude Code + User

---

## Overview

Transform the current monorepo `claude5-starter-kit` into an **AI SDK Ecosystem** - a showcase hub linking to 10 independent, production-ready AI SDK framework repositories.

---

## Goals

1. **Showcase Hub**: Transform main repo into a card-grid portfolio website
2. **Independent Repos**: Each AI SDK project becomes its own GitHub repository
3. **SDK-Focused Naming**: Repository names reflect AI frameworks (LANGCHAIN, CREWAI, etc.)
4. **Zero Dependencies**: All 10 repos are completely independent of each other
5. **Live & Evolving**: All repos pushed to GitHub, maintained over time

---

## Repository Structure

### Before
```
mk-knight23/claude5-starter-kit/
  └── projects/
      ├── 01-venture-graph/
      ├── 02-omni-desk/
      ├── 03-dev-squad/
      ├── 04-supply-consensus/
      ├── 05-market-pulse/
      ├── 06-insight-stream/
      ├── 07-research-synthesis/
      ├── 08-trend-factory/
      ├── 09-patent-iq/
      └── 10-claude-forge/
```

### After
```
mk-knight23/
  ├── AI-SDK-ECOSYSTEM (showcase hub)
  │   └── index.html (card grid portfolio)
  │
  ├── AI-SDK-LANGCHAIN
  ├── AI-SDK-CREWAI
  ├── AI-SDK-LANGGRAPH
  ├── AI-SDK-AUTOGEN
  ├── AI-SDK-OPENAI
  ├── AI-SDK-VERCEL-AI
  ├── AI-SDK-ANTHROPIC
  ├── AI-SDK-HAYSTACK
  ├── AI-SDK-SEMANTIC-KERNEL
  └── AI-SDK-LAMA-INDEX
```

---

## The 10 AI SDK Repositories

| Repo Name | Source Project | AI SDK Focus | Description |
|-----------|----------------|--------------|-------------|
| **AI-SDK-LANGCHAIN** | 01-VentureGraph | LangChain | Framework for building LLM applications |
| **AI-SDK-CREWAI** | 02-OmniDesk | CrewAI | Multi-agent orchestration framework |
| **AI-SDK-LANGGRAPH** | 03-DevSquad | LangGraph | Stateful agent workflows by LangChain |
| **AI-SDK-AUTOGEN** | 04-SupplyConsensus | AutoGen | Microsoft's multi-agent framework |
| **AI-SDK-OPENAI** | 05-MarketPulse | OpenAI | OpenAI SDK & Assistants API |
| **AI-SDK-VERCEL-AI** | 06-InsightStream | Vercel AI | Vercel AI SDK for React/Next.js |
| **AI-SDK-ANTHROPIC** | 07-ResearchSynthesis | Anthropic | Claude API & Message streaming |
| **AI-SDK-HAYSTACK** | 08-TrendFactory | Haystack | Deepset's NLP framework |
| **AI-SDK-SEMANTIC-KERNEL** | 09-PatentIQ | Semantic Kernel | Microsoft's AI orchestration |
| **AI-SDK-LAMA-INDEX** | 10-ClaudeForge | LlamaIndex | Data framework for LLM apps |

---

## Showcase Website Design

### Format: Single `index.html` with Card Grid Portfolio

**Key Features:**
- Responsive 3-column grid (mobile: 1-column)
- Dark mode support
- GitHub API integration for live star counts
- Smooth animations on hover
- Direct "View on GitHub" buttons

### Card Design
```
┌─────────────────────────┐
│  🦜 LANGCHAIN           │
│  Framework              │
│                         │
│  ⭐ 1,234 stars         │
│  🟢 Updated 2h ago      │
│                         │
│  [View on GitHub]       │
└─────────────────────────┘
```

### Tech Stack
- **Single HTML file** - No build step required
- **Vanilla CSS** - Modern, responsive, dark mode
- **GitHub REST API** - Live stats via fetch()
- **GitHub Pages** - Zero-cost hosting

---

## Implementation Phases

### Phase 1: Repository Preparation
1. Rename `claude5-starter-kit` → `AI-SDK-ECOSYSTEM`
2. Create 10 new GitHub repositories via `gh repo create`
3. Clean up current repo (remove `projects/` folder)

### Phase 2: Project Migration
1. Initialize each new repo with proper .gitignore
2. Copy project files to corresponding repos
3. Update READMEs with new repo names
4. Set up CI/CD for each repo

### Phase 3: Showcase Build
1. Create `index.html` with card grid layout
2. Add CSS styling (responsive, dark mode, animations)
3. Integrate GitHub API for live stats
4. Deploy to GitHub Pages

### Phase 4: Documentation Updates
1. Update main showcase README
2. Add ecosystem badges to all 10 repos
3. Create contributing guidelines
4. Update all cross-references

---

## GitHub Repository Commands

```bash
# Rename current repo
gh repo rename AI-SDK-ECOSYSTEM

# Create 10 new repos
gh repo create AI-SDK-LANGCHAIN --public --description "LangChain Framework SDK - Production-ready AI agent stack"
gh repo create AI-SDK-CREWAI --public --description "CrewAI Agent Framework SDK - Multi-agent orchestration"
gh repo create AI-SDK-LANGGRAPH --public --description "LangGraph SDK - Stateful agent workflows"
gh repo create AI-SDK-AUTOGEN --public --description "Microsoft AutoGen SDK - Multi-agent framework"
gh repo create AI-SDK-OPENAI --public --description "OpenAI SDK - Assistants API & GPT integration"
gh repo create AI-SDK-VERCEL-AI --public --description "Vercel AI SDK - React/Next.js AI integration"
gh repo create AI-SDK-ANTHROPIC --public --description "Anthropic Claude SDK - Claude API integration"
gh repo create AI-SDK-HAYSTACK --public --description "Haystack SDK - Deepset NLP framework"
gh repo create AI-SDK-SEMANTIC-KERNEL --public --description "Microsoft Semantic Kernel SDK"
gh repo create AI-SDK-LAMA-INDEX --public --description "LlamaIndex SDK - Data framework for LLMs"
```

---

## Success Criteria

- [ ] Main repo renamed to `AI-SDK-ECOSYSTEM`
- [ ] 10 independent repos created and visible on GitHub
- [ ] Showcase `index.html` displays all 10 projects in card grid
- [ ] Each repo has updated README with proper descriptions
- [ ] GitHub Pages deployed and accessible
- [ ] No cross-repo dependencies
- [ ] All repos have CI/CD pipelines

---

## Notes

- All repo names are **UPPERCASE** for consistency
- Each repo is **completely independent** - no linking between them
- Showcase serves only as a **directory/portal** to the 10 repos
- Future updates to individual repos don't affect the showcase
