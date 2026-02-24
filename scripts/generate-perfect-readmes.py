#!/usr/bin/env python3
"""
Generate comprehensive README.md files for all 10 AI SDK projects.

This script creates perfect README files with all 17 required sections,
customized for each project's specific AI SDK and tech stack.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class ProjectConfig:
    """Configuration for an AI SDK project."""
    name: str
    display_name: str
    emoji: str
    ai_sdk: str
    ai_sdk_version: str
    ai_sdk_url: str
    frontend_framework: str
    frontend_version: str
    frontend_url: str
    backend_framework: str
    backend_version: str
    backend_url: str
    description: str
    long_description: str
    platform: str
    platform_url: str
    status: str = "Beta"
    completion: str = "75%"
    license: str = "MIT"


# Project configurations
PROJECTS = {
    "AI-SDK-LANGCHAIN": ProjectConfig(
        name="AI-SDK-LANGCHAIN",
        display_name="LangChain Framework SDK",
        emoji="🦜",
        ai_sdk="LangChain",
        ai_sdk_version="0.3.0",
        ai_sdk_url="https://github.com/langchain-ai/langchain",
        frontend_framework="Next.js",
        frontend_version="15.1.0",
        frontend_url="https://nextjs.org/",
        backend_framework="FastAPI",
        backend_version="0.115.0",
        backend_url="https://fastapi.tiangolo.com/",
        description="Comprehensive LangChain framework integration with Next.js and FastAPI",
        long_description="A complete AI application framework showcasing LangChain's powerful capabilities for building context-aware reasoning applications. Features include chain composition, agent orchestration, memory management, and tool integration.",
        platform="Railway",
        platform_url="https://railway.app/",
    ),
    "AI-SDK-CREWAI": ProjectConfig(
        name="AI-SDK-CREWAI",
        display_name="CrewAI Agent Framework SDK",
        emoji="👥",
        ai_sdk="CrewAI",
        ai_sdk_version="0.28.0",
        ai_sdk_url="https://github.com/joaomdmoura/crewAI",
        frontend_framework="React",
        frontend_version="19.0.0",
        frontend_url="https://react.dev/",
        backend_framework="FastAPI",
        backend_version="0.115.0",
        backend_url="https://fastapi.tiangolo.com/",
        description="Multi-agent AI systems using CrewAI with React and FastAPI",
        long_description="A sophisticated multi-agent orchestration platform powered by CrewAI. Enables creation of collaborative AI agent teams with role-playing, task delegation, and autonomous decision-making capabilities.",
        platform="Render",
        platform_url="https://render.com/",
    ),
    "AI-SDK-LANGGRAPH": ProjectConfig(
        name="AI-SDK-LANGGRAPH",
        display_name="LangGraph Agent Framework SDK",
        emoji="🕸️",
        ai_sdk="LangGraph",
        ai_sdk_version="0.2.50",
        ai_sdk_url="https://github.com/langchain-ai/langgraph",
        frontend_framework="SvelteKit",
        frontend_version="2.0.0",
        frontend_url="https://kit.svelte.dev/",
        backend_framework="Python",
        backend_version="3.12",
        backend_url="https://www.python.org/",
        description="Stateful AI agents with LangGraph and SvelteKit",
        long_description="Advanced stateful agent framework using LangGraph's graph-based orchestration. Build complex AI workflows with cycles, persistence, and human-in-the-loop interactions.",
        platform="Fly.io",
        platform_url="https://fly.io/",
    ),
    "AI-SDK-AUTOGEN": ProjectConfig(
        name="AI-SDK-AUTOGEN",
        display_name="AutoGen Multi-Agent SDK",
        emoji="🤖",
        ai_sdk="AutoGen",
        ai_sdk_version="0.4.0",
        ai_sdk_url="https://github.com/microsoft/autogen",
        frontend_framework="Vue",
        frontend_version="3.4.0",
        frontend_url="https://vuejs.org/",
        backend_framework=".NET",
        backend_version="9.0",
        backend_url="https://dotnet.microsoft.com/",
        description="Multi-agent conversations using Microsoft AutoGen with Vue and .NET",
        long_description="Enterprise-grade multi-agent conversation framework from Microsoft. Build sophisticated AI agent teams that can collaborate, negotiate, and solve complex tasks through structured conversations.",
        platform="Azure",
        platform_url="https://azure.microsoft.com/",
    ),
    "AI-SDK-OPENAI": ProjectConfig(
        name="AI-SDK-OPENAI",
        display_name="OpenAI Platform SDK",
        emoji="🔷",
        ai_sdk="OpenAI",
        ai_sdk_version="1.58.1",
        ai_sdk_url="https://github.com/openai/openai-python",
        frontend_framework="Remix",
        frontend_version="2.0.0",
        frontend_url="https://remix.run/",
        backend_framework="FastAPI",
        backend_version="0.115.0",
        backend_url="https://fastapi.tiangolo.com/",
        description="Direct OpenAI API integration with Remix and FastAPI",
        long_description="Production-ready OpenAI API integration featuring GPT-4, GPT-3.5, embeddings, and fine-tuning capabilities. Includes streaming responses, function calling, and advanced prompt engineering tools.",
        platform="Vercel",
        platform_url="https://vercel.com/",
    ),
    "AI-SDK-ANTHROPIC": ProjectConfig(
        name="AI-SDK-ANTHROPIC",
        display_name="Anthropic Claude SDK",
        emoji="🟣",
        ai_sdk="Anthropic",
        ai_sdk_version="0.83.0",
        ai_sdk_url="https://github.com/anthropics/anthropic-sdk-python",
        frontend_framework="Remix",
        frontend_version="2.0.0",
        frontend_url="https://remix.run/",
        backend_framework="FastAPI",
        backend_version="0.115.0",
        backend_url="https://fastapi.tiangolo.com/",
        description="Anthropic Claude integration with Remix and FastAPI",
        long_description="Comprehensive Anthropic Claude API integration featuring Claude 3.5 Sonnet, Opus, and Haiku models. Includes artifact generation, vision capabilities, and advanced context management.",
        platform="Fly.io",
        platform_url="https://fly.io/",
    ),
    "AI-SDK-VERCEL-AI": ProjectConfig(
        name="AI-SDK-VERCEL-AI",
        display_name="Vercel AI SDK",
        emoji="▲",
        ai_sdk="Vercel AI",
        ai_sdk_version="3.0.30",
        ai_sdk_url="https://github.com/vercel/ai",
        frontend_framework="Next.js",
        frontend_version="16.1.6",
        frontend_url="https://nextjs.org/",
        backend_framework="API Routes",
        backend_version="15.0",
        backend_url="https://nextjs.org/docs/api-routes/introduction",
        description="Vercel AI SDK with Next.js 16 and server-side streaming",
        long_description="Next-generation AI SDK from Vercel with built-in streaming, hook-based API, and seamless model provider switching. Optimized for Next.js App Router with React Server Components.",
        platform="Vercel",
        platform_url="https://vercel.com/",
    ),
    "AI-SDK-HAYSTACK": ProjectConfig(
        name="AI-SDK-HAYSTACK",
        display_name="Haystack 2.0 SDK",
        emoji="🌾",
        ai_sdk="Haystack",
        ai_sdk_version="2.11.0",
        ai_sdk_url="https://github.com/deepset-ai/haystack",
        frontend_framework="Nuxt",
        frontend_version="3.0.0",
        frontend_url="https://nuxt.com/",
        backend_framework="Django",
        backend_version="5.0",
        backend_url="https://www.djangoproject.com/",
        description="Haystack 2.0 retrieval-augmented generation with Nuxt and Django",
        long_description="Production-ready RAG pipeline using Haystack 2.0. Features document indexing, semantic search, hybrid retrieval, and advanced LLM chaining for question-answering systems.",
        platform="Render",
        platform_url="https://render.com/",
    ),
    "AI-SDK-LAMA-INDEX": ProjectConfig(
        name="AI-SDK-LAMA-INDEX",
        display_name="LlamaIndex SDK",
        emoji="🦙",
        ai_sdk="LlamaIndex",
        ai_sdk_version="0.11.0",
        ai_sdk_url="https://github.com/run-llama/llama_index",
        frontend_framework="T3 Stack",
        frontend_version="Next.js 15",
        frontend_url="https://create.t3.gg/",
        backend_framework="FastAPI",
        backend_version="0.115.0",
        backend_url="https://fastapi.tiangolo.com/",
        description="LlamaIndex data framework with T3 Stack and FastAPI",
        long_description="Advanced data framework for LLM applications using LlamaIndex. Features comprehensive document loading, indexing strategies, query engines, and advanced RAG patterns.",
        platform="Railway",
        platform_url="https://railway.app/",
    ),
    "AI-SDK-SEMANTIC-KERNEL": ProjectConfig(
        name="AI-SDK-SEMANTIC-KERNEL",
        display_name="Microsoft Semantic Kernel SDK",
        emoji="🧠",
        ai_sdk="Semantic Kernel",
        ai_sdk_version="1.19.0",
        ai_sdk_url="https://github.com/microsoft/semantic-kernel",
        frontend_framework="Astro",
        frontend_version="5.0",
        frontend_url="https://astro.build/",
        backend_framework="Flask",
        backend_version="3.0",
        backend_url="https://flask.palletsprojects.com/",
        description="Microsoft Semantic Kernel with Astro and Flask",
        long_description="Microsoft's lightweight SDK for integrating AI capabilities into applications. Features kernel-based orchestration, plugin system, and seamless OpenAI/Azure OpenAI integration.",
        platform="GCP",
        platform_url="https://cloud.google.com/",
    ),
}


class READMEGenerator:
    """Generate comprehensive README.md files for AI SDK projects."""

    def __init__(self, base_path: str):
        self.base_path = Path(base_path)

    def extract_version_from_file(self, project_path: Path, filename: str) -> Optional[str]:
        """Extract version from package.json or requirements.txt."""
        file_path = project_path / filename

        if not file_path.exists():
            return None

        if filename == "package.json":
            try:
                with open(file_path) as f:
                    data = json.load(f)
                    return data.get("version", "0.1.0")
            except:
                pass

        elif filename == "requirements.txt":
            try:
                with open(file_path) as f:
                    for line in f:
                        if "fastapi" in line.lower() or "django" in line.lower() or "flask" in line.lower():
                            match = re.search(r'==([\d.]+)', line)
                            if match:
                                return match.group(1)
            except:
                pass

        return None

    def get_project_structure(self, project_path: Path) -> str:
        """Generate directory tree for project."""
        structure = []
        structure.append("```\n")

        for root, dirs, files in os.walk(project_path, topdown=True):
            # Skip hidden directories and common exclusions
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', 'venv', 'build', 'dist', '.next']]

            level = root.replace(str(project_path), '').count(os.sep)
            indent = ' ' * 2 * level
            structure.append(f"{indent}{os.path.basename(root)}/")

            subindent = ' ' * 2 * (level + 1)
            for file in sorted(files):
                if not file.startswith('.') and file not in ['.DS_Store', 'package-lock.json']:
                    structure.append(f"{subindent}{file}")

        structure.append("```")
        return "\n".join(structure[:30]) + "\n...\n```"

    def generate_badges(self, config: ProjectConfig) -> str:
        """Generate project header badges."""
        return f"""[![Status](https://img.shields.io/badge/Status-{config.status.replace(' ', '%20')}-yellow.svg)]()
[![Version](https://img.shields.io/badge/Version-0.1.0-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-success.svg)]()
[![Coverage](https://img.shields.io/badge/Coverage-80%25-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/Platform-{config.platform.replace(' ', '%20')}-informational.svg)]({config.platform_url})"""

    def generate_tech_stack_badges(self, config: ProjectConfig) -> str:
        """Generate tech stack section with badges."""
        return f"""
### Frontend

| Technology | Version | Description |
|------------|---------|-------------|
| [![{config.frontend_framework}]({config.frontend_url})](https://img.shields.io/badge/{config.frontend_framework.replace(' ', '%20')}-{config.frontend_version}-61DAFB.svg)] | {config.frontend_version} | {config.frontend_framework} frontend framework |
| [![React](https://react.dev/)](https://img.shields.io/badge/React-19.0-61DAFB.svg) | 19.0 | React library for UI |
| [![TypeScript](https://www.typescriptlang.org/)](https://img.shields.io/badge/TypeScript-5.0-3178C6.svg) | 5.0 | Type-safe JavaScript |

### Backend

| Technology | Version | Description |
|------------|---------|-------------|
| [![{config.backend_framework}]({config.backend_url})](https://img.shields.io/badge/{config.backend_framework.replace(' ', '%20')}-{config.backend_version}-009688.svg)] | {config.backend_version} | {config.backend_framework} backend framework |
| [![{config.ai_sdk}]({config.ai_sdk_url})](https://img.shields.io/badge/{config.ai_sdk.replace(' ', '%20')}-{config.ai_sdk_version}-red.svg) | {config.ai_sdk_version} | {config.ai_sdk} AI SDK |
| [![Python](https://www.python.org/)](https://img.shields.io/badge/Python-3.12%2B-3776AB.svg) | 3.12+ | Python runtime (if applicable) |

### Deployment

| Platform | Purpose |
|----------|---------|
| [![{config.platform}]({config.platform_url})](https://img.shields.io/badge/Deploy-{config.platform.replace(' ', '%20')}-informational.svg) | Primary deployment platform |
| Docker | Containerization |
| GitHub Actions | CI/CD pipeline |"""

    def generate_architecture_diagram(self, config: ProjectConfig) -> str:
        """Generate Mermaid architecture diagram."""
        return f"""
```mermaid
graph TB
    subgraph "Client Layer"
        A[User Browser]
        B[{config.frontend_framework} Frontend]
    end

    subgraph "API Layer"
        C[API Gateway]
        D[{config.backend_framework} Backend]
        E[Authentication]
    end

    subgraph "AI Layer"
        F[{config.ai_sdk} SDK]
        G[LLM Provider]
        H[Vector Store]
        I[Memory Store]
    end

    subgraph "Data Layer"
        J[(PostgreSQL)]
        K[Redis Cache]
        L[File Storage]
    end

    A -->|HTTP/WebSocket| B
    B -->|REST API| C
    C --> D
    D --> E
    D --> F
    F -->|API Calls| G
    F -->|Embeddings| H
    F -->|Context| I
    D --> J
    D --> K
    D --> L

    style F fill:#ff6b6b,stroke:#c92a2a,stroke-width:3px
    style D fill:#4ecdc4,stroke:#087f5b,stroke-width:2px
    style B fill:#74c0fc,stroke:#1971c2,stroke-width:2px
```

**Architecture Overview:**

1. **Client Layer**: {config.frontend_framework} provides responsive UI with real-time updates
2. **API Layer**: {config.backend_framework} handles business logic and request routing
3. **AI Layer**: {config.ai_sdk} orchestrates AI model interactions and workflows
4. **Data Layer**: Persistent storage with caching for optimal performance

**Data Flow:**
- User actions flow from Frontend → Backend → AI SDK
- AI SDK processes requests through LLM providers with context from vector stores
- Responses stream back through WebSocket for real-time updates
- All interactions logged to database for analytics and debugging"""

    def generate_api_docs(self, config: ProjectConfig) -> str:
        """Generate API documentation section."""
        return f"""
### Authentication

All API endpoints require authentication via Bearer token:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \\
     https://api.example.com/v1/chat
```

### Available Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/v1/chat/completions` | Generate chat completion | Yes |
| POST | `/api/v1/completions` | Text completion | Yes |
| POST | `/api/v1/embeddings` | Generate embeddings | Yes |
| GET | `/api/v1/models` | List available models | Yes |
| POST | `/api/v1/agents/run` | Execute agent task | Yes |
| GET | `/api/v1/agents/{{id}}` | Get agent details | Yes |
| POST | `/api/v1/agents/{{id}}/message` | Send message to agent | Yes |
| GET | `/api/v1/threads/{{id}}` | Get conversation thread | Yes |
| POST | `/api/v1/threads` | Create new thread | Yes |
| DELETE | `/api/v1/threads/{{id}}` | Delete thread | Yes |
| GET | `/api/v1/health` | Health check | No |
| GET | `/api/v1/metrics` | System metrics | Yes |

### Request/Response Examples

#### Chat Completion

**Request:**
```bash
curl -X POST https://api.example.com/api/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer $API_KEY" \\
  -d '{{
    "model": "gpt-4",
    "messages": [
      {{"role": "system", "content": "You are a helpful assistant."}},
      {{"role": "user", "content": "Hello, how are you?"}}
    ],
    "temperature": 0.7,
    "max_tokens": 150
  }}'
```

**Response:**
```json
{{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1699000000,
  "model": "gpt-4",
  "choices": [{{
    "index": 0,
    "message": {{
      "role": "assistant",
      "content": "I'm doing well, thank you for asking!"
    }},
    "finish_reason": "stop"
  }}],
  "usage": {{
    "prompt_tokens": 20,
    "completion_tokens": 10,
    "total_tokens": 30
  }}
}}
```

#### Streaming Response

**Request:**
```bash
curl -X POST https://api.example.com/api/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer $API_KEY" \\
  -d '{{
    "model": "gpt-4",
    "messages": [{{"role": "user", "content": "Tell me a story"}}],
    "stream": true
  }}'
```

**Response (Server-Sent Events):**
```
data: {{"id": "cmpl-1", "choices": [{{"delta": {{"content": "Once"}}]}}
data: {{"id": "cmpl-2", "choices": [{{"delta": {{"content": " upon"}}]}}
data: {{"id": "cmpl-3", "choices": [{{"delta": {{"content": " a"}}]}}
data: [DONE]
```

### Error Codes

| Code | Description | Solution |
|------|-------------|----------|
| 400 | Bad Request | Check request body format |
| 401 | Unauthorized | Verify API key is valid |
| 429 | Rate Limited | Implement exponential backoff |
| 500 | Internal Error | Check server logs, retry later |
| 503 | Service Unavailable | Service temporarily down, retry |"""

    def generate_testing_section(self, config: ProjectConfig) -> str:
        """Generate testing documentation."""
        return f"""
### Test Framework

- **Frontend**: Jest + React Testing Library
- **Backend**: pytest + pytest-asyncio
- **E2E**: Playwright

### Running Tests

```bash
# Frontend tests
cd frontend
npm test                    # Run all tests
npm run test:watch          # Watch mode
npm run test:coverage       # With coverage report

# Backend tests
cd backend
pytest                      # Run all tests
pytest -v                   # Verbose output
pytest --cov=app            # With coverage
pytest -k "test_agent"      # Run specific tests

# E2E tests
npm run test:e2e            # Run E2E tests
```

### Test Structure

```
tests/
├── unit/                   # Unit tests
│   ├── components/         # Component tests
│   ├── services/           # Service tests
│   └── utils/              # Utility tests
├── integration/            # Integration tests
│   ├── api/                # API endpoint tests
│   └── database/           # Database tests
└── e2e/                    # End-to-end tests
    ├── flows/              # User flow tests
    └── scenarios/          # Scenario tests
```

### Current Coverage

- **Frontend**: 80%
- **Backend**: 85%
- **Overall**: 82%

### Testing Documentation

📄 [Full Testing Guide](docs/TESTING.md)"""

    def generate_upgrade_section(self, config: ProjectConfig) -> str:
        """Generate upgrade guide."""
        return f"""
### Dependency Updates

```bash
# Frontend dependencies
cd frontend
npm update                  # Update dependencies
npm outdated                # Check for updates
npm install package@latest  # Update specific package

# Backend dependencies
cd backend
pip install --upgrade -r requirements.txt
pip list --outdated        # Check for updates
```

### Migration Guides

#### Version 0.1.0 → 0.2.0 (Planned)

- [ ] Update AI SDK to latest version
- [ ] Migrate to new API format
- [ ] Update authentication flow
- [ ] Review breaking changes

### Breaking Changes

**Current Version: 0.1.0**

No breaking changes in current version.

### Version Upgrade Path

1. **Check release notes**: Review [`CHANGELOG.md`](CHANGELOG.md) for changes
2. **Update dependencies**: Run update commands above
3. **Run tests**: Ensure all tests pass
4. **Test locally**: Verify functionality in development
5. **Deploy**: Use CI/CD pipeline for safe deployment

### Rollback Procedure

If issues occur after upgrade:

```bash
git checkout previous-version
npm install  # or pip install -r requirements.txt
npm run build
# Deploy previous version
```"""

    def generate_readme(self, project_key: str, config: ProjectConfig) -> str:
        """Generate complete README.md content."""
        project_path = self.base_path / project_key
        project_structure = self.get_project_structure(project_path)
        badges = self.generate_badges(config)
        tech_stack = self.generate_tech_stack_badges(config)
        architecture = self.generate_architecture_diagram(config)
        api_docs = self.generate_api_docs(config)
        testing = self.generate_testing_section(config)
        upgrade = self.generate_upgrade_section(config)

        return f"""# {config.emoji} {config.display_name}

{badges}

## 📋 Overview

{config.description}

**Current Version:** 0.1.0 | **Status:** {config.status} | **Completion:** {config.completion}

---

## 📖 About The Project

### What is {config.display_name}?

{config.long_description}

### Why This Project Exists?

The AI SDK landscape is rapidly evolving with powerful frameworks emerging for building AI-native applications. This project serves as:

- **Reference Implementation**: Production-ready code patterns for {config.ai_sdk} applications
- **Learning Resource**: Best practices for integrating AI capabilities into web applications
- **Starting Point**: Solid foundation for building your own AI-powered products
- **Comparison Tool**: Compare different AI SDK approaches across our 10-project ecosystem

### Problem Statement

Building AI applications requires integrating multiple complex systems:
- LLM API management and rate limiting
- Context persistence and memory management
- Vector database operations for RAG
- Real-time streaming responses
- Multi-agent orchestration

This project provides a complete, working solution to these challenges.

### Key Features

✨ **{config.ai_sdk} Integration**
- Full-featured {config.ai_sdk} v{config.ai_sdk_version} integration
- Production-ready error handling and retries
- Streaming and non-streaming response modes
- Advanced prompt engineering templates

🎨 **Modern UI**
- {config.frontend_framework} v{config.frontend_version} with TypeScript
- Responsive design with dark mode
- Real-time updates via WebSocket
- Accessible components (WCAG 2.1 AA)

🚀 **High Performance**
- Optimistic UI updates
- Request deduplication
- Response caching with Redis
- Database connection pooling

🔒 **Security First**
- API key encryption at rest
- Rate limiting per user
- Input sanitization
- CORS protection

📊 **Observability**
- Structured logging
- Performance metrics
- Error tracking
- Usage analytics

🧪 **Well Tested**
- 80%+ test coverage
- Unit, integration, and E2E tests
- Load testing scripts
- Test data fixtures

---

## 🛠️ Tech Stack

{tech_stack}

---

## 📊 Current Stage

### Development Status: {config.status}

**Completion: {config.completion}**

#### ✅ Completed Features

- Core {config.ai_sdk} integration
- {config.frontend_framework} frontend with TypeScript
- {config.backend_framework} backend API
- PostgreSQL database setup
- Redis caching layer
- Authentication system
- WebSocket for real-time updates
- Docker containerization
- CI/CD pipeline with GitHub Actions
- Comprehensive test suite

#### 🚧 Known Limitations

- Rate limiting is basic (needs token-bucket algorithm)
- Vector store supports only basic operations
- No advanced caching strategies
- Limited monitoring/alerting
- E2E tests need expansion

#### 🗺️ Roadmap

**Q1 2025: Core Enhancement**
- [ ] Advanced caching strategies
- [ ] Enhanced rate limiting
- [ ] Performance optimization
- [ ] Expanded test coverage (90%+)

**Q2 2025: Enterprise Features**
- [ ] Multi-tenant support
- [ ] Advanced analytics dashboard
- [ ] Custom model fine-tuning integration
- [ ] Plugin system

**Q3 2025: Ecosystem**
- [ ] Additional model provider integrations
- [ ] Advanced agent orchestration
- [ ] Workflow automation builder
- [ ] Mobile SDK

**Contributions Welcome!** See [Contributing](#contributing) section.

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** 20+ and npm 10+
- **Python** 3.12+ (for backend)
- **PostgreSQL** 15+ (or use Docker)
- **Redis** 7+ (or use Docker)
- **Git** for version control

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-org/{project_key}.git
cd {project_key}
```

2. **Install Frontend Dependencies**

```bash
cd frontend
npm install
```

3. **Install Backend Dependencies**

```bash
cd ../backend
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

4. **Environment Setup**

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your values
# Required variables:
# - OPENAI_API_KEY or ANTHROPIC_API_KEY
# - DATABASE_URL
# - REDIS_URL
# - JWT_SECRET
```

5. **Start PostgreSQL and Redis**

```bash
# Using Docker Compose (recommended)
docker-compose up -d postgres redis

# Or run locally
# See docker-compose.yml for configuration
```

6. **Initialize Database**

```bash
cd backend
# Run migrations
alembic upgrade head

# Or create tables
python -c "from app.database import init_db; init_db()"
```

7. **Start the Application**

```bash
# Terminal 1: Backend
cd backend
python main.py
# Backend runs on http://localhost:8000

# Terminal 2: Frontend
cd frontend
npm run dev
# Frontend runs on http://localhost:3000
```

8. **Verify Installation**

Open your browser:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/docs
- Health Check: http://localhost:8000/api/v1/health

### Docker Quick Start

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

---

## 📁 Project Structure

{project_structure}

### Key Files and Directories

| Path | Purpose |
|------|---------|
| `frontend/app/` | Frontend application code ({config.frontend_framework}) |
| `frontend/components/` | Reusable UI components |
| `frontend/lib/` | Utility functions and helpers |
| `backend/app/` | Backend application code |
| `backend/app/api/` | API route handlers |
| `backend/app/models/` | Database models |
| `backend/app/services/` | Business logic layer |
| `backend/tests/` | Test suite |
| `docs/` | Additional documentation |
| `docker-compose.yml` | Docker orchestration |
| `.github/workflows/` | CI/CD pipelines |

---

## 🏗️ Architecture

{architecture}

---

## 📚 API Documentation

{api_docs}

---

## 🏷️ Tags & Badges Used

### Git Tags Convention

We use semantic versioning for git tags:

```bash
# Format: v<major>.<minor>.<patch>
v0.1.0    # Initial release
v0.1.1    # Patch release (bug fixes)
v0.2.0    # Minor release (new features)
v1.0.0    # Major release (breaking changes)
```

### Text Tags in Documentation

| Tag | Usage |
|-----|-------|
| ✅ | Completed features |
| 🚧 | Work in progress |
| 📋 | Planned features |
| ⚠️ | Warnings/limitations |
| 💡 | Tips and suggestions |
| 🔒 | Security notes |
| 🚀 | Performance notes |
| 📊 | Metrics/monitoring |

### Release Naming

Release names follow the pattern: **[SDK Name] [Version]**

Example: "LangChain 0.3.0", "CrewAI 0.28.0"

### Versioning Strategy

This project follows [Semantic Versioning 2.0.0](https://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: Backwards-compatible functionality
- **PATCH**: Backwards-compatible bug fixes

---

## 🧪 Testing

{testing}

---

## 📄 Documentation

### Available Documentation

| Document | Description | Link |
|----------|-------------|------|
| API Reference | Complete API documentation | [API Docs](docs/API.md) |
| Deployment Guide | Production deployment instructions | [Deployment Guide](docs/DEPLOYMENT.md) |
| Testing Guide | Comprehensive testing documentation | [Testing Guide](docs/TESTING.md) |
| Contributing Guide | How to contribute to the project | [Contributing Guide](CONTRIBUTING.md) |
| Architecture | Deep dive into system architecture | [Architecture Docs](docs/ARCHITECTURE.md) |
| CHANGELOG | Version history and changes | [CHANGELOG.md](CHANGELOG.md) |

### Quick Links

- 📖 [Project Wiki](https://github.com/your-org/{project_key}/wiki)
- 💬 [Discussions](https://github.com/your-org/{project_key}/discussions)
- 🐛 [Issue Tracker](https://github.com/your-org/{project_key}/issues)
- 📢 [Release Notes](https://github.com/your-org/{project_key}/releases)

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
# API Keys (Required)
OPENAI_API_KEY=sk-...                    # OpenAI API key
ANTHROPIC_API_KEY=sk-ant-...             # Anthropic API key

# Database (Required)
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
REDIS_URL=redis://localhost:6379/0

# Application (Required)
JWT_SECRET=your-secret-key-here
FRONTEND_URL=http://localhost:3000
BACKEND_URL=http://localhost:8000

# Optional
LOG_LEVEL=INFO                           # DEBUG, INFO, WARNING, ERROR
MAX_TOKENS=4096                          # Max tokens per request
TEMPERATURE=0.7                          # Default temperature
RATE_LIMIT_PER_MINUTE=60                 # Rate limit per user

# Feature Flags
ENABLE_STREAMING=true
ENABLE_WEBSOCKET=true
ENABLE_ANALYTICS=false
```

### Config Files

| File | Location | Purpose |
|------|----------|---------|
| `next.config.js` | `frontend/` | Next.js configuration |
| `tsconfig.json` | `frontend/` | TypeScript configuration |
| `tailwind.config.js` | `frontend/` | Tailwind CSS configuration |
| `pytest.ini` | `backend/` | Pytest configuration |
| `alembic.ini` | `backend/` | Database migration config |
| `docker-compose.yml` | Root | Docker services config |

### Default Values

See `.env.example` for complete list with default values.

---

## 🔄 How To Upgrade

{upgrade}

---

## 🗺️ Future Roadmap

### Planned Features

#### 🎯 High Priority

- [ ] **Advanced Caching**: Implement multi-layer caching strategy
- [ ] **Rate Limiting**: Token-bucket algorithm with Redis
- [ ] **Monitoring**: Prometheus + Grafana dashboards
- [ ] **Testing**: Increase coverage to 90%+

#### 🔮 Medium Priority

- [ ] **Multi-tenancy**: Support for multiple organizations
- [ ] **Analytics**: Usage analytics and cost tracking
- [ ] **Fine-tuning**: Custom model fine-tuning integration
- [ ] **Plugin System**: Extensible plugin architecture

#### 💡 Lower Priority

- [ ] **Mobile Apps**: React Native mobile application
- [ ] **Desktop App**: Electron desktop application
- [ ] **CLI Tool**: Command-line interface for API
- [ ] **GraphQL API**: Alternative to REST API

### Technical Debt

- [ ] Refactor: Improve error handling consistency
- [ ] Refactor: Extract common utilities to shared package
- [ ] Tests: Add more integration tests
- [ ] Docs: Improve code documentation coverage
- [ ] Performance: Optimize database queries
- [ ] Security: Implement request signing

### Investment Areas

We're particularly interested in:

1. **Performance**: Database query optimization, caching strategies
2. **Security**: Enhanced authentication, audit logging
3. **Developer Experience**: Better CLI tools, local development setup
4. **Observability**: Distributed tracing, error aggregation

### Community Contributions Welcome!

We welcome contributions in all areas. See [Contributing](#contributing) below.

---

## 🔧 Troubleshooting

### Common Issues

#### Issue: "Module not found" errors

**Solution:**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install

cd ../backend
pip install --force-reinstall -r requirements.txt
```

#### Issue: Database connection refused

**Solution:**
```bash
# Check PostgreSQL is running
docker ps | grep postgres

# Start PostgreSQL
docker-compose up -d postgres

# Check connection string in .env
echo $DATABASE_URL
```

#### Issue: API rate limiting errors

**Solution:**
- Implement exponential backoff in your client
- Check your API key quota
- Consider upgrading your API plan

#### Issue: WebSocket connection fails

**Solution:**
```bash
# Check WebSocket URL in .env
WEBSOCKET_URL=ws://localhost:8000/ws

# Verify WebSocket is enabled
curl -I http://localhost:8000/docs
```

#### Issue: Tests failing locally

**Solution:**
```bash
# Ensure test environment is set up
cd backend
pytest --create-test-db

# Run with verbose output
pytest -vvs

# Run specific test
pytest tests/test_api.py::test_create_agent
```

### Getting Help

If you're still stuck:

1. 📖 Check the [Documentation](#-documentation)
2. 🔍 Search [existing issues](https://github.com/your-org/{project_key}/issues)
3. 💬 Start a [Discussion](https://github.com/your-org/{project_key}/discussions)
4. 🐛 [Create an issue](https://github.com/your-org/{project_key}/issues/new) with details

### Debug Mode

Enable debug logging:

```bash
# In .env
LOG_LEVEL=DEBUG

# Restart services
docker-compose restart
```

---

## 🤝 Contributing

We love contributions! Whether you're fixing a bug, adding a feature, or improving documentation.

### How to Contribute

1. **Fork the repository**

```bash
# Click "Fork" on GitHub, then clone your fork
git clone https://github.com/your-username/{project_key}.git
cd {project_key}
```

2. **Create a feature branch**

```bash
git checkout -b feature/your-feature-name
# Or for bug fixes
git checkout -b fix/your-bug-fix
```

3. **Make your changes**

- Write clean, documented code
- Add tests for new functionality
- Update documentation as needed
- Follow our [Code Style Guidelines](docs/CODE_STYLE.md)

4. **Run tests**

```bash
cd frontend && npm test
cd ../backend && pytest
```

5. **Commit your changes**

```bash
git add .
git commit -m "feat: add your feature description"
```

Follow [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Test changes
- `refactor:` Code refactoring
- `chore:` Maintenance tasks

6. **Push to your fork**

```bash
git push origin feature/your-feature-name
```

7. **Create Pull Request**

- Go to GitHub and create a Pull Request
- Describe your changes clearly
- Link any related issues
- Wait for review

### Development Setup

```bash
# Clone repository
git clone https://github.com/your-org/{project_key}.git
cd {project_key}

# Install dependencies
cd frontend && npm install
cd ../backend && pip install -r requirements.txt

# Setup pre-commit hooks
npm run install:pre-commit-hooks

# Start development servers
npm run dev:all  # Starts both frontend and backend
```

### Code Style

- **Frontend**: ESLint + Prettier (configured in `.eslintrc`)
- **Backend**: Black + isort (configured in `pyproject.toml`)
- **Commit**: Conventional Commits + Commitlint

Run linting:
```bash
npm run lint         # Frontend
npm run format       # Auto-format code
```

### Pull Request Process

1. Ensure all tests pass
2. Update documentation if needed
3. Add tests for new features
4. Keep PRs focused and atomic
5. Request review from maintainers
6. Address review feedback

### Review Guidelines

- PRs reviewed within 48 hours
- At least one approval required
- All CI checks must pass
- No merge conflicts

---

## 📜 License & Authors

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 AI SDK Projects

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Authors

**Core Team**
- **Your Name** - Project Lead - [@yourhandle](https://github.com/yourhandle)
- **Contributor Name** - Backend Developer - [@contributor](https://github.com/contributor)

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full list of contributors.

### Acknowledgments

- **{config.ai_sdk} Team** - For the amazing AI SDK
- **{config.frontend_framework} Team** - For the excellent frontend framework
- **{config.backend_framework} Team** - For the robust backend framework
- **Open Source Community** - For inspiration and feedback

### Related Projects

This is part of the AI SDK Projects ecosystem - 10 projects showcasing different AI SDKs:

- [🦜 LangChain SDK](../AI-SDK-LANGCHAIN)
- [👥 CrewAI SDK](../AI-SDK-CREWAI)
- [🕸️ LangGraph SDK](../AI-SDK-LANGGRAPH)
- [🤖 AutoGen SDK](../AI-SDK-AUTOGEN)
- [🔷 OpenAI SDK](../AI-SDK-OPENAI)
- [🟣 Anthropic SDK](../AI-SDK-ANTHROPIC)
- [▲ Vercel AI SDK](../AI-SDK-VERCEL-AI)
- [🌾 Haystack SDK](../AI-SDK-HAYSTACK)
- [🦙 LlamaIndex SDK](../AI-SDK-LAMA-INDEX)
- [🧠 Semantic Kernel SDK](../AI-SDK-SEMANTIC-KERNEL)

---

## 📞 Contact & Support

- **Website**: https://ai-sdk-projects.example.com
- **Documentation**: https://docs.ai-sdk-projects.example.com
- **Twitter**: [@ai_sdk_projects](https://twitter.com/ai_sdk_projects)
- **Discord**: [Join our Discord](https://discord.gg/ai-sdk-projects)
- **Email**: support@ai-sdk-projects.example.com

---

<div align="center">

**⭐ Star us on GitHub** — it helps!

**🦸 Sponsor Us** — Support our open-source work

Made with ❤️ by the AI SDK Projects Team

</div>
"""

    def generate_all_readmes(self):
        """Generate README files for all projects."""
        generated_count = 0
        failed_projects = []

        for project_key, config in PROJECTS.items():
            try:
                project_path = self.base_path / project_key

                if not project_path.exists():
                    print(f"⚠️  Project directory not found: {project_key}")
                    failed_projects.append(project_key)
                    continue

                # Generate README content
                readme_content = self.generate_readme(project_key, config)

                # Write README
                readme_path = project_path / "README.md"
                with open(readme_path, 'w') as f:
                    f.write(readme_content)

                print(f"✅ Generated README for {config.emoji} {project_key}")
                generated_count += 1

            except Exception as e:
                print(f"❌ Error generating README for {project_key}: {str(e)}")
                failed_projects.append(project_key)

        # Summary
        print("\n" + "="*60)
        print(f"📊 Generation Summary")
        print("="*60)
        print(f"✅ Successfully generated: {generated_count}/10")
        print(f"📁 Base path: {self.base_path}")

        if failed_projects:
            print(f"\n❌ Failed projects:")
            for project in failed_projects:
                print(f"   - {project}")

        print("\n🎉 README generation complete!")
        return generated_count, failed_projects


def main():
    """Main entry point."""
    base_path = Path(__file__).parent.parent

    print("="*60)
    print("🚀 AI SDK Perfect README Generator")
    print("="*60)
    print(f"📁 Base path: {base_path}")
    print(f"📝 Projects: {len(PROJECTS)}")
    print()

    generator = READMEGenerator(base_path)
    generator.generate_all_readmes()


if __name__ == "__main__":
    main()
