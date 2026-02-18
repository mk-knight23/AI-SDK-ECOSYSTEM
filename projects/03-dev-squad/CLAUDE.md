# DevSquad

**Project:** DevSquad (SvelteKit + Node.js SaaS)
**SDK Focus:** Developer collaboration platform
**Tech Stack:** SvelteKit 2.x, Svelte 5, TypeScript, Node.js

## MANDATORY WORKFLOW

1. Superpowers → Brainstorm → Plan → TDD
2. ECC → /plan → /tdd → /code-review → /security-scan
3. UI/UX Pro Max → Apply design system
4. Claude-Tips → /dx:handoff before end of session

## AGENTS TO USE

- /architect for system design
- /tdd-guide for test-first implementation
- /security-reviewer before API key usage

## CURRENT SPRINT: Week 1

- [x] Scaffold SvelteKit project
- [x] Create Hello World page
- [x] Create /health endpoint
- [x] Docker containerization
- [x] CI/CD pipeline
- [ ] Deploy to Fly.io

## Deployment Target

Fly.io (configured in fly.toml)

## API Keys (Doppler)

- FLY_API_TOKEN (GitHub secret for CI/CD)

## Project Structure

```
src/routes/
├── +page.svelte          # Hello World landing page
└── health/
    └── +server.ts        # Health check API endpoint
```

## Available Scripts

- `npm run dev` - Development server (port 5173)
- `npm run build` - Production build
- `npm run preview` - Preview production build (port 4173)
- `npm run check` - TypeScript type checking

## Docker

Multi-stage Dockerfile for production builds.
Build: `docker build -t devsquad:latest .`
Run: `docker run -p 3000:3000 devsquad:latest`

## CI/CD

GitHub Actions workflow:
1. Type check and build
2. Docker build and test
3. Deploy to Fly.io (main branch only)
