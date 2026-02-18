# DevSquad

A SvelteKit-based web application with Node.js backend.

## Tech Stack

- **Frontend**: SvelteKit 2.x + Svelte 5
- **Backend**: SvelteKit API routes (Node.js)
- **Type Safety**: TypeScript
- **Deployment**: Fly.io

## Features

- Hello World landing page
- Health check endpoint at `/health`
- Docker containerization
- CI/CD with GitHub Actions
- Fly.io deployment ready

## Getting Started

### Prerequisites

- Node.js 20+
- npm

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

Open http://localhost:5173

### Build

```bash
npm run build
```

### Preview Production Build

```bash
npm run preview
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Hello World page |
| `/health` | GET | Health check - returns status, timestamp, service name |

## Docker

### Build

```bash
docker build -t devsquad:latest .
```

### Run

```bash
docker run -p 3000:3000 devsquad:latest
```

## Deployment

### Fly.io Setup

1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Login: `fly auth login`
3. Launch app: `fly launch` (or use existing `fly.toml`)
4. Deploy: `fly deploy`

### GitHub Actions

The CI/CD pipeline:
1. Runs type checking and build on every PR
2. Builds Docker image and tests it
3. Deploys to Fly.io on main branch merges

Required secrets:
- `FLY_API_TOKEN`: Fly.io API token for deployment

## Project Structure

```
.
├── src/
│   ├── routes/
│   │   ├── +page.svelte      # Hello World page
│   │   └── health/
│   │       └── +server.ts    # Health endpoint
│   └── app.html              # HTML template
├── .github/
│   └── workflows/
│       └── ci.yml            # CI/CD pipeline
├── Dockerfile                # Multi-stage Docker build
├── fly.toml                  # Fly.io configuration
├── svelte.config.js          # SvelteKit config (Node adapter)
└── package.json
```

## Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run check` - Type check with svelte-check

## License

MIT
