#!/usr/bin/env python3
"""
AI-SDK Ecosystem Documentation Generator

Generates comprehensive documentation for all 10 AI-SDK projects including:
- Enhanced README.md with badges, architecture diagrams, API tables
- docs/API.md with complete API documentation
- docs/DEPLOYMENT.md with platform-specific deployment instructions
- docs/TESTING.md with test structure and coverage information
- Enhanced CONTRIBUTING.md with development workflow
"""

import os
import sys
import re
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ProjectConfig:
    """Configuration for a single AI-SDK project."""
    name: str
    path: str
    sdk_name: str
    framework: str = ""
    backend_type: str = "FastAPI"
    frontend_type: str = "Next.js"
    description: str = ""
    features: List[str] = field(default_factory=list)
    api_endpoints: List[str] = field(default_factory=list)
    docs_writer: str = "general"  # python, multiagent, official


# Project configurations
PROJECTS = {
    "AI-SDK-LANGCHAIN": ProjectConfig(
        name="AI-SDK-LANGCHAIN",
        path="AI-SDK-LANGCHAIN",
        sdk_name="LangChain",
        framework="LangGraph",
        backend_type="FastAPI",
        frontend_type="Next.js 15",
        description="Production-ready SaaS showcasing stateful multi-agent systems using LangGraph",
        features=[
            "Stateful Agent Workflows - LangGraph cyclic graphs with persistent state",
            "Multi-Provider LLM Support - OpenAI, Anthropic, OpenRouter, Perplexity",
            "Real-time Streaming - WebSocket-based agent execution monitoring",
            "Human-in-the-Loop - Approval gates for critical decisions",
            "Production Ready - Full CI/CD, 80%+ test coverage"
        ],
        api_endpoints=[
            "GET /health - Health check",
            "GET /api/agents - List available agents",
            "POST /api/agents/execute - Execute agent workflow",
            "WS /api/agents/stream - WebSocket for streaming execution",
            "GET /api/checkpoints - List state checkpoints",
            "POST /api/approvals - Submit approval decision"
        ],
        docs_writer="python"
    ),

    "AI-SDK-LANGGRAPH": ProjectConfig(
        name="AI-SDK-LANGGRAPH",
        path="AI-SDK-LANGGRAPH",
        sdk_name="LangGraph",
        framework="LangGraph",
        backend_type="Python",
        frontend_type="SvelteKit",
        description="Stateful multi-agent applications with checkpointing and human-in-the-loop",
        features=[
            "Cyclic Graph Topology - Non-linear agent workflows",
            "State Checkpointing - Persistent state across sessions",
            "Human-in-the-Loop - Approval workflows",
            "Multi-Provider Support - OpenAI, Anthropic, local models",
            "Streaming Responses - Real-time agent output"
        ],
        api_endpoints=[
            "GET /api/health - Health check",
            "POST /api/graphs/execute - Execute graph workflow",
            "GET /api/graphs/state - Get current graph state",
            "POST /api/graphs/approve - Human approval for state transition",
            "GET /api/graphs/history - State change history"
        ],
        docs_writer="multiagent"
    ),

    "AI-SDK-AUTOGEN": ProjectConfig(
        name="AI-SDK-AUTOGEN",
        path="AI-SDK-AUTOGEN",
        sdk_name="AutoGen",
        framework="Microsoft AutoGen",
        backend_type=".NET 9",
        frontend_type="Vue 3",
        description="Distributed multi-agent systems using Microsoft AutoGen with gRPC communication",
        features=[
            "Multi-Agent Communication - gRPC-based agent messaging",
            "Multi-Cloud Deployment - Agents on different cloud providers",
            "Fault Tolerance - Agent recovery and state synchronization",
            "AutoGen 0.4 - Latest multi-agent framework",
            "Type-Safe - .NET 9 with C# 13"
        ],
        api_endpoints=[
            "GET /health - Service health",
            "POST /api/agents/create - Create new agent",
            "POST /api/agents/message - Send message to agent",
            "GET /api/agents/list - List all agents",
            "gRPC /autogen.AgentService/Stream - Bidirectional streaming"
        ],
        docs_writer="multiagent"
    ),

    "AI-SDK-CREWAI": ProjectConfig(
        name="AI-SDK-CREWAI",
        path="AI-SDK-CREWAI",
        sdk_name="CrewAI",
        framework="CrewAI",
        backend_type="FastAPI",
        frontend_type="React",
        description="Role-playing AI agents with collaborative task execution using CrewAI",
        features=[
            "Role-Based Agents - specialized agent roles and goals",
            "Task Delegation - Automatic task distribution",
            "Collaborative Execution - Multi-agent coordination",
            "Crew Management - Create and manage agent crews",
            "Process Monitoring - Real-time crew execution tracking"
        ],
        api_endpoints=[
            "GET /api/health - Health check",
            "POST /api/crews - Create new crew",
            "GET /api/crews - List all crews",
            "POST /api/crews/execute - Execute crew tasks",
            "GET /api/crews/{id}/logs - Crew execution logs"
        ],
        docs_writer="python"
    ),

    "AI-SDK-LAMA-INDEX": ProjectConfig(
        name="AI-SDK-LAMA-INDEX",
        path="AI-SDK-LAMA-INDEX",
        sdk_name="LlamaIndex",
        framework="LlamaIndex",
        backend_type="FastAPI",
        frontend_type="React",
        description="RAG applications with advanced indexing using LlamaIndex",
        features=[
            "Advanced Indexing - Vector, tree, list indices",
            "RAG Pipeline - Document ingestion and retrieval",
            "Hybrid Search - Vector + keyword search",
            "Query Engine - Natural language queries",
            "Data Connectors - 50+ data sources"
        ],
        api_endpoints=[
            "GET /api/health - Health check",
            "POST /api/documents/upload - Upload documents for indexing",
            "POST /api/query - Query the index",
            "GET /api/documents - List indexed documents",
            "DELETE /api/documents/{id} - Delete document"
        ],
        api_endpoints=[
            "GET /api/health - Health check",
            "POST /api/documents/upload - Upload documents for indexing",
            "POST /api/query - Query the index",
            "GET /api/documents - List indexed documents",
            "DELETE /api/documents/{id} - Delete document"
        ],
        docs_writer="python"
    ),

    "AI-SDK-HAYSTACK": ProjectConfig(
        name="AI-SDK-HAYSTACK",
        path="AI-SDK-HAYSTACK",
        sdk_name="Haystack",
        framework="Haystack 2.0",
        backend_type="FastAPI",
        frontend_type="Next.js",
        description="Modular NLP pipeline applications with Haystack 2.0",
        features=[
            "Modular Pipelines - Composable NLP components",
            "Document Stores - Elasticsearch, Chroma, PGVector",
            "Embedders - Multiple embedding models",
            "Retrievers - Dense, sparse, hybrid retrieval",
            "Generators - LLM-based answer generation"
        ],
        api_endpoints=[
            "GET /api/health - Health check",
            "POST /api/pipelines/run - Execute pipeline",
            "GET /api/pipelines - List available pipelines",
            "POST /api/documents/index - Index documents",
            "GET /api/documents/search - Search documents"
        ],
        docs_writer="python"
    ),

    "AI-SDK-SEMANTIC-KERNEL": ProjectConfig(
        name="AI-SDK-SEMANTIC-KERNEL",
        path="AI-SDK-SEMANTIC-KERNEL",
        sdk_name="Semantic Kernel",
        framework="Microsoft Semantic Kernel",
        backend_type="Python",
        frontend_type="Next.js",
        description="Enterprise AI applications with Semantic Kernel plugin system",
        features=[
            "Plugin Architecture - Extensible plugin system",
            "Kernel Management - Multi-tenant kernel instances",
            "Function Calling - Native function orchestration",
            "Connector System - 80+ service connectors",
            "Enterprise Ready - Azure integration, telemetry"
        ],
        api_endpoints=[
            "GET /api/health - Health check",
            "POST /api/kernel/plugins/register - Register plugin",
            "POST /api/kernel/invoke - Invoke kernel with prompt",
            "GET /api/kernel/plugins - List registered plugins",
            "GET /api/kernel/functions - List available functions"
        ],
        docs_writer="multiagent"
    ),

    "AI-SDK-OPENAI": ProjectConfig(
        name="AI-SDK-OPENAI",
        path="AI-SDK-OPENAI",
        sdk_name="OpenAI",
        framework="OpenAI API",
        backend_type="FastAPI",
        frontend_type="Next.js",
        description="Production OpenAI integration with Assistants API and function calling",
        features=[
            "GPT-4o & GPT-4o-mini - Latest models",
            "Assistants API - Persistent assistant threads",
            "Function Calling - Structured output",
            "Vector Stores - Built-in RAG",
            "Streaming Responses - Real-time output"
        ],
        api_endpoints=[
            "GET /api/health - Health check",
            "POST /api/chat/completions - Chat completions",
            "POST /api/assistants - Create assistant",
            "POST /api/threads/run - Run assistant thread",
            "POST /api/embeddings - Generate embeddings"
        ],
        docs_writer="official"
    ),

    "AI-SDK-ANTHROPIC": ProjectConfig(
        name="AI-SDK-ANTHROPIC",
        path="AI-SDK-ANTHROPIC",
        sdk_name="Anthropic",
        framework="Anthropic Claude API",
        backend_type="FastAPI",
        frontend_type="Remix",
        description="Extended thinking and computer use with Claude API",
        features=[
            "Extended Thinking - Chain-of-thought reasoning",
            "Computer Use - Control computers via API",
            "Message Streaming - Real-time token streaming",
            "Artifact Generation - PDF, code, content creation",
            "200K Context - Large context window"
        ],
        api_endpoints=[
            "GET /api/health - Health check",
            "POST /api/messages - Send messages to Claude",
            "POST /api/messages/stream - Stream Claude responses",
            "POST /api/computer/use - Computer use actions",
            "GET /api/artifacts - Get generated artifacts"
        ],
        docs_writer="official"
    ),

    "AI-SDK-VERCEL-AI": ProjectConfig(
        name="AI-SDK-VERCEL-AI",
        path="AI-SDK-VERCEL-AI",
        sdk_name="Vercel AI SDK",
        framework="Vercel AI SDK",
        backend_type="Next.js API",
        frontend_type="Next.js",
        description="Full-stack AI applications with Vercel AI SDK and streaming UI",
        features=[
            "Unified Interface - 20+ LLM providers",
            "Streaming UI - React hooks for streaming",
            "Tool Calling - Function orchestration",
            "Edge Runtime - Fast edge inference",
            "Built-in RAG - Vector store integration"
        ],
        api_endpoints=[
            "GET /api/health - Health check",
            "POST /api/chat - Chat endpoint with streaming",
            "POST /api/completions - Text completions",
            "POST /api/embeddings - Generate embeddings",
            "GET /api/models - List available models"
        ],
        docs_writer="official"
    ),
}


# Documentation templates
README_TEMPLATE = r"""# {project_name}

[![AI-SDK Ecosystem](https://img.shields.io/badge/AI--SDK-ECOSYSTEM-part%20of-blue)](https://github.com/mk-knight23/AI-SDK-ECOSYSTEM)
[![{framework}](https://img.shields.io/badge/{framework Badge}-critical)](https://github.com/{framework_url})
[![{frontend}](https://img.shields.io/badge/{frontend Badge}-black)]({frontend_url})
[![{backend}](https://img.shields.io/badge/{backend Badge}-green)]({backend_url})

> **Framework**: {framework}
> **Stack**: {frontend} + {backend}

---

## 🎯 Project Overview

**{project_name}** {description}

### Key Features

{features_list}

---

## 🛠 Tech Stack

### Frontend
| Technology | Version | Purpose |
|-------------|---------|---------|
{frontend_table}

### Backend
| Technology | Version | Purpose |
|-------------|---------|---------|
{backend_table}

---

## 🏗️ Architecture

```mermaid
graph TB
    subgraph "Frontend - {frontend}"
        UI[User Interface]
        State[State Management]
    end

    subgraph "Backend - {backend}"
        API[API Layer]
        Core[{sdk_name} Core]
        Providers[LLM Providers]
    end

    subgraph "Infrastructure"
        DB[(Database)]
        Cache[(Cache)]
        Queue[(Message Queue)]
    end

    UI -->|HTTP/WS| API
    API --> Core
    Core --> Providers
    API --> DB
    Core --> Cache
    API --> Queue

    style UI fill:#4CAF50
    style Core fill:#2196F3
    style Providers fill:#FF9800
```

### Data Flow

1. **User Request** → Frontend captures user input
2. **API Call** → Request sent to backend API
3. **{sdk_name} Processing** → Framework processes with {sdk_name}
4. **LLM Integration** → Calls to LLM providers
5. **Response** → Results cached and returned
6. **UI Update** → Frontend displays results

---

## 🚀 Quick Start

### Prerequisites
{prerequisites}

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:3000`

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
{backend_command}
```

API runs at `http://localhost:8000`

### With Docker

```bash
docker-compose up
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
{api_table}

### Authentication

Most endpoints require authentication via Bearer token:

```bash
curl -H "Authorization: Bearer $TOKEN" \\
     http://localhost:8000/api/agents
```

### Response Format

All API responses follow this structure:

```json
{{
  "success": true,
  "data": {{ ... }},
  "error": null,
  "metadata": {{
    "timestamp": "2025-02-24T00:00:00Z",
    "version": "0.1.0"
  }}
}}
```

---

## 🔌 API Integrations

{providers_table}

---

## 💡 Usage Examples

### TypeScript/JavaScript

```typescript
import {{ createClient }} from '@ai-sdk/{sdk_lower}';

const client = createClient({{
  apiKey: process.env.{SDK_UPPER}_API_KEY
}});

const response = await client.generate({{
  prompt: 'Hello, {sdk_name}!'
}});

console.log(response.text);
```

### Python

```python
from {sdk_lower}_import import Client

client = Client(api_key=os.getenv("{SDK_UPPER}_API_KEY"))

response = client.generate(
    prompt="Hello, {sdk_name}!"
)

print(response.text)
```

### cURL

```bash
curl -X POST http://localhost:8000/api/generate \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer $TOKEN" \\
  -d '{{"prompt": "Hello, {sdk_name}!"}}'
```

---

## 🔧 Troubleshooting

### Common Issues

<details>
<summary><b>Connection refused errors</b></summary>

**Problem**: Cannot connect to backend API

**Solutions**:
- Ensure backend is running: `cd backend && python main.py`
- Check port is not in use: `lsof -i :8000`
- Verify CORS settings if calling from browser
</details>

<details>
<summary><b>Authentication failures</b></summary>

**Problem**: 401 Unauthorized errors

**Solutions**:
- Verify API keys in `.env` file
- Check environment variables are loaded
- Ensure keys have proper permissions
</details>

<details>
<summary><b>Rate limiting</b></summary>

**Problem**: 429 Too Many Requests

**Solutions**:
- Implement exponential backoff
- Reduce request frequency
- Upgrade API tier if needed
</details>

<details>
<summary><b>Memory issues</b></summary>

**Problem**: Out of memory errors

**Solutions**:
- Increase container memory limits
- Implement response streaming
- Use batch processing for large inputs
</details>

---

## 📦 Deployment

### Quick Deploy

```bash
# Deploy frontend
cd frontend
{frontend_deploy}

# Deploy backend
cd backend
{backend_deploy}
```

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed instructions.

---

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest --cov=app --cov-report=html

# Frontend tests
cd frontend
npm test
```

See [TESTING.md](docs/TESTING.md) for detailed testing information.

---

## 📝 Development Workflow

This project follows the **5-Ecosystem** methodology:

1. **Superpowers** - Brainstorming → Planning → TDD
2. **ECC** - `/plan` → `/tdd` → `/code-review` → `/security-scan`
3. **UI/UX Pro Max** - Design system application
4. **Ralph Loop** - Autonomous development iterations
5. **Claude-Tips** - DX optimization

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

---

## 📁 Project Structure

```
{project_name}/
├── frontend/           # {frontend} application
│   ├── app/            # Application code
│   ├── components/     # Reusable components
│   └── lib/            # Utilities
├── backend/            # {backend} backend
│   ├── app/            # Application code
│   ├── api/            # API endpoints
│   ├── tests/          # Test suites
│   └── requirements.txt
├── docs/               # Documentation
│   ├── API.md
│   ├── DEPLOYMENT.md
│   └── TESTING.md
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📚 Additional Documentation

- [API Reference](docs/API.md) - Complete API documentation
- [Deployment Guide](docs/DEPLOYMENT.md) - Platform-specific deployment
- [Testing Guide](docs/TESTING.md) - Testing strategies and coverage
- [Contributing Guide](CONTRIBUTING.md) - Development workflow

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🔗 Links

- [AI-SDK Ecosystem](https://github.com/mk-knight23/AI-SDK-ECOSYSTEM)
- [{sdk_name} Documentation]({sdk_docs_url})
- [Framework Documentation]({framework_docs_url})

---

**Built with ❤️ as part of the [AI-SDK Ecosystem](https://github.com/mk-knight23/AI-SDK-ECOSYSTEM)**
"""


API_DOC_TEMPLATE = r"""# API Reference

**{project_name}** - Complete API Documentation

---

## Base URL

```
Production: https://api.{project_lower}.com
Development: http://localhost:8000
```

---

## Authentication

### API Key Authentication

Most endpoints require API key authentication:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \\
     https://api.{project_lower}.com/api/endpoint
```

### Rate Limits

- **Free Tier**: 100 requests/minute
- **Pro Tier**: 1000 requests/minute
- **Enterprise**: Custom limits

Rate limit headers are included in all responses:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1740345600
```

---

## Endpoints

{api_endpoints_details}

---

## Schemas

### Request Schemas

#### AgentRequest

```typescript
{{
  "type": "object",
  "properties": {{
    "agentType": {{
      "type": "string",
      "enum": ["research", "venture", "analysis"]
    }},
    "input": {{
      "type": "string",
      "description": "User input/prompt"
    }},
    "config": {{
      "type": "object",
      "properties": {{
        "temperature": {{ "type": "number", "minimum": 0, "maximum": 2 }},
        "maxTokens": {{ "type": "integer", "minimum": 1 }}
      }}
    }}
  }},
  "required": ["agentType", "input"]
}}
```

### Response Schemas

#### AgentResponse

```typescript
{{
  "type": "object",
  "properties": {{
    "success": {{ "type": "boolean" }},
    "data": {{
      "type": "object",
      "properties": {{
        "result": {{ "type": "string" }},
        "metadata": {{
          "type": "object",
          "properties": {{
            "model": {{ "type": "string" }},
            "tokensUsed": {{ "type": "integer" }},
            "duration": {{ "type": "number" }}
          }}
        }}
      }}
    }},
    "error": {{
      "type": "string",
      "nullable": true
    }}
  }}
}}
```

---

## Error Codes

| Code | Description | Solution |
|------|-------------|----------|
| 400 | Bad Request | Check request body format |
| 401 | Unauthorized | Verify API key is valid |
| 403 | Forbidden | Check permissions for resource |
| 404 | Not Found | Verify endpoint URL |
| 429 | Rate Limited | Implement backoff, reduce frequency |
| 500 | Internal Error | Contact support, check status page |
| 503 | Service Unavailable | Service is temporarily down |

### Error Response Format

```json
{{
  "success": false,
  "data": null,
  "error": {{
    "code": "INVALID_REQUEST",
    "message": "The request body is invalid",
    "details": {{
      "field": "agentType",
      "issue": "Must be one of: research, venture, analysis"
    }}
  }},
  "requestId": "req_abc123"
}}
```

---

## WebSocket API

### Connection

```javascript
const ws = new WebSocket('ws://localhost:8000/api/agents/stream');

ws.onopen = () => {{
  ws.send(JSON.stringify({{
    action: 'execute',
    agentType: 'research',
    input: 'Your query here'
  }}));
}};

ws.onmessage = (event) => {{
  const data = JSON.parse(event.data);
  console.log('Received:', data);
}};
```

### WebSocket Events

#### Server → Client

| Event | Data | Description |
|-------|------|-------------|
| `started` | `{executionId, timestamp}` | Execution started |
| `progress` | `{step, message, progress}` | Progress update |
| `completed` | `{result, metadata}` | Execution completed |
| `error` | `{error, details}` | Error occurred |

---

## SDK Integration

### Python SDK

```python
from {sdk_lower}_sdk import Client

client = Client(
    api_key="your-api-key",
    base_url="https://api.{project_lower}.com"
)

# Execute agent
result = client.agents.execute(
    agent_type="research",
    input="Your query"
)

print(result.text)
```

### TypeScript SDK

```typescript
import {{ Client }} from '@{sdk_lower}/sdk';

const client = new Client({{
  apiKey: 'your-api-key',
  baseUrl: 'https://api.{project_lower}.com'
}});

const result = await client.agents.execute({{
  agentType: 'research',
  input: 'Your query'
}});

console.log(result.text);
```

---

## Best Practices

### 1. Request Optimization

- Use streaming for long-running operations
- Batch multiple requests when possible
- Implement caching for repeated queries

### 2. Error Handling

```typescript
try {{
  const result = await client.agents.execute(request);
}} catch (error) {{
  if (error.status === 429) {{
    // Handle rate limiting
    await backoff();
  }} else if (error.status === 500) {{
    // Retry with exponential backoff
  }}
}}
```

### 3. Streaming Responses

```typescript
const stream = await client.agents.stream(request);

for await (const chunk of stream) {{
  console.log(chunk);
}}
```

---

## Changelog

### Version 0.1.0 (2025-02-24)
- Initial API release
- Core agent execution endpoints
- WebSocket streaming support
- Authentication and rate limiting

---

## Support

- Documentation: [https://docs.{project_lower}.com](https://docs.{project_lower}.com)
- Status Page: [https://status.{project_lower}.com](https://status.{project_lower}.com)
- GitHub Issues: [https://github.com/mk-knight23/{project_name}/issues](https://github.com/mk-knight23/{project_name}/issues)
"""


DEPLOYMENT_DOC_TEMPLATE = r"""# Deployment Guide

**{project_name}** - Production Deployment Instructions

---

## Table of Contents

1. [Environment Setup](#environment-setup)
2. [Platform Deployments](#platform-deployments)
3. [Docker Deployment](#docker-deployment)
4. [Configuration](#configuration)
5. [Monitoring](#monitoring)
6. [Scaling](#scaling)

---

## Environment Setup

### Required Environment Variables

```bash
# API Keys
{env_vars}

# Database
DATABASE_URL=postgresql://user:pass@host:5432/dbname
REDIS_URL=redis://host:6379

# Application
NODE_ENV=production
API_BASE_URL=https://api.{project_lower}.com
FRONTEND_URL=https://{project_lower}.com

# Monitoring (Optional)
SENTRY_DSN=https://your-sentry-dsn
DATADOG_API_KEY=your-datadog-key
```

---

## Platform Deployments

### Vercel (Frontend)

```bash
cd frontend

# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod

# Set environment variables
vercel env add ANTHROPIC_API_KEY production
vercel env add OPENAI_API_KEY production
```

**Configuration**: `vercel.json`

```json
{{
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "framework": "nextjs",
  "regions": ["iad1"],
  "env": {{
    "NEXT_PUBLIC_API_URL": "https://api.{project_lower}.com"
  }}
}}
```

### Railway (Backend)

```bash
cd backend

# Install Railway CLI
npm i -g @railway/cli

# Login and link project
railway login
railway init

# Deploy
railway up

# Set environment variables in Railway dashboard
```

**Configuration**: `railway.json`

```json
{{
  "build": {{
    "builder": "DOCKERFILE",
    "dockerfilePath": "Dockerfile"
  }},
  "deploy": {{
    "healthcheckPath": "/health",
    "healthcheckTimeout": 100,
    "restartPolicyType": "on-failure"
  }}
}}
```

### Fly.io (Full Stack)

```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Deploy frontend
fly deploy --config fly.frontend.toml

# Deploy backend
fly deploy --config fly.backend.toml

# Set secrets
fly secrets set DATABASE_URL=postgres://...
fly secrets set {SDK_UPPER}_API_KEY=sk-ant-...
```

**Configuration**: `fly.toml`

```toml
app = "{project_lower}-backend"

[build]
  dockerfile = "Dockerfile"

[env]
  PORT = "8000"

[[services]]
  http_checks = []
  internal_port = 8000

  [[services.ports]]
    handlers = ["http"]
    port = 80

  [[services.ports]]
    handlers = ["tls", "http"]
    port = 443
```

### Render (Backend)

```bash
# Install Render CLI
npm i -g render-cli

# Deploy
render deploy

# Or connect GitHub repo for auto-deploy
```

**Configuration**: `render.yaml`

```yaml
services:
  - type: web
    name: {project_lower}-backend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: {project_lower}-db
          property: connectionString
      - key: {SDK_UPPER}_API_KEY
        sync: false
```

---

## Docker Deployment

### Build Images

```bash
# Build backend
cd backend
docker build -t {project_lower}-backend:latest .

# Build frontend
cd frontend
docker build -t {project_lower}-frontend:latest .
```

### Docker Compose (Recommended)

```bash
docker-compose up -d
```

**Configuration**: `docker-compose.yml`

```yaml
version: '3.8'

services:
  frontend:
    image: {project_lower}-frontend:latest
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://backend:8000
    depends_on:
      - backend

  backend:
    image: {project_lower}-backend:latest
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/app
      - REDIS_URL=redis://redis:6379
      - {SDK_UPPER}_API_KEY=${SDK_UPPER}_API_KEY}
    depends_on:
      - db
      - redis

  db:
    image: postgres:16
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=app
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

---

## Configuration

### Backend Configuration

`backend/app/config.py`

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API Keys
    anthropic_api_key: str
    openai_api_key: str

    # Database
    database_url: str

    # Redis
    redis_url: str = "redis://localhost:6379"

    # Application
    app_name: str = "{project_name}"
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
```

### Frontend Configuration

`frontend/.env.production`

```bash
NEXT_PUBLIC_API_URL=https://api.{project_lower}.com
NEXT_PUBLIC_APP_NAME={project_name}
```

---

## Monitoring

### Health Checks

```bash
# Backend health
curl https://api.{project_lower}.com/health

# Expected response
{{
  "status": "healthy",
  "service": "{project_lower}-api",
  "version": "0.1.0",
  "timestamp": "2025-02-24T00:00:00Z"
}}
```

### Logging

**Backend**: Structured JSON logs

```json
{{
  "level": "info",
  "message": "Agent execution completed",
  "agent_type": "research",
  "duration_ms": 1234,
  "timestamp": "2025-02-24T00:00:00Z"
}}
```

**Frontend**: Client-side errors

```typescript
if (typeof window !== 'undefined') {{
  window.addEventListener('error', (event) => {{
    console.error({{
      message: event.message,
      source: event.filename,
      line: event.lineno
    }});
  }});
}}
```

### Metrics (Optional)

```python
from prometheus_client import Counter, Histogram

agent_executions = Counter(
    'agent_executions_total',
    'Total agent executions',
    ['agent_type', 'status']
)

execution_duration = Histogram(
    'agent_execution_duration_seconds',
    'Agent execution duration',
    ['agent_type']
)
```

---

## Scaling

### Horizontal Scaling

```bash
# Scale backend with Docker Compose
docker-compose up --scale backend=3

# Scale on Kubernetes
kubectl scale deployment/{project_lower}-backend --replicas=3
```

### Database Scaling

**Connection Pooling**

```python
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(
    settings.database_url,
    pool_size=20,
    max_overflow=40,
    pool_pre_ping=True
)
```

**Read Replicas**

```python
# Write to primary
write_engine = create_async_engine(primary_db_url)

# Read from replicas
read_engine = create_async_engine(replica_db_url)
```

### Caching Strategy

```python
from functools import lru_cache
from redis import Redis

redis = Redis.from_url(settings.redis_url)

@lru_cache(maxsize=1000)
def get_cached_response(key: str) -> str:
    return redis.get(key)
```

---

## Verification

### Post-Deployment Checklist

- [ ] Health check endpoint responds
- [ ] Environment variables loaded correctly
- [ ] Database connection successful
- [ ] Redis connection successful
- [ ] API keys valid and working
- [ ] Frontend builds without errors
- [ ] Frontend can connect to backend
- [ ] WebSocket connections work
- [ ] Test endpoint returns expected data
- [ ] Monitoring and logging active

### Smoke Test

```bash
#!/bin/bash

echo "Running smoke tests..."

# Health check
curl -f https://api.{project_lower}.com/health || exit 1

# API test
curl -f -X POST https://api.{project_lower}.com/api/test \\
  -H "Authorization: Bearer $TEST_API_KEY" || exit 1

# Frontend test
curl -f https://{project_lower}.com || exit 1

echo "All smoke tests passed!"
```

---

## Troubleshooting

### Build Failures

**Problem**: Docker build fails

**Solutions**:
- Check Dockerfile syntax
- Verify base image is available
- Ensure all dependencies in requirements.txt
- Check for network issues during build

### Runtime Errors

**Problem**: 500 errors in production

**Solutions**:
- Check application logs
- Verify environment variables
- Test database connectivity
- Check for missing dependencies

### Performance Issues

**Problem**: Slow response times

**Solutions**:
- Enable response compression
- Implement caching
- Scale horizontally
- Optimize database queries

---

## Rollback Procedure

### Vercel

```bash
vercel rollback
```

### Railway

```bash
railway rollback
```

### Docker

```bash
docker-compose down
docker-compose up -d --scale backend=2
git checkout <previous-commit>
docker-compose up -d --build
```

---

For additional help, see:
- [Platform documentation](https://docs.{project_lower}.com)
- [GitHub Issues](https://github.com/mk-knight23/{project_name}/issues)
"""


TESTING_DOC_TEMPLATE = r"""# Testing Guide

**{project_name}** - Comprehensive Testing Documentation

---

## Table of Contents

1. [Testing Philosophy](#testing-philosophy)
2. [Test Structure](#test-structure)
3. [Running Tests](#running-tests)
4. [Coverage](#coverage)
5. [CI/CD Integration](#cicd-integration)
6. [Best Practices](#best-practices)

---

## Testing Philosophy

This project follows **Test-Driven Development (TDD)**:

1. **RED** - Write failing test first
2. **GREEN** - Write minimal implementation to pass
3. **IMPROVE** - Refactor while keeping tests green

**Target Coverage**: 80%+ across all modules

---

## Test Structure

```
backend/
├── tests/
│   ├── unit/              # Unit tests
│   │   ├── test_agents.py
│   │   ├── test_graphs.py
│   │   └── test_api.py
│   ├── integration/       # Integration tests
│   │   ├── test_db.py
│   │   ├── test_redis.py
│   │   └── test_llm.py
│   ├── e2e/              # End-to-end tests
│   │   ├── test_workflows.py
│   │   └── test_api_e2e.py
│   ├── fixtures/         # Test fixtures
│   │   └── conftest.py
│   └── __init__.py

frontend/
├── __tests__/
│   ├── unit/             # Component tests
│   ├── integration/      # Integration tests
│   └── e2e/             # E2E tests with Playwright
```

---

## Running Tests

### Backend Tests

```bash
cd backend

# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/unit/test_agents.py

# Run specific test
pytest tests/unit/test_agents.py::test_agent_creation

# Run with verbose output
pytest -v

# Run only fast tests
pytest -m "not slow"
```

### Frontend Tests

```bash
cd frontend

# Run all tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run tests with coverage
npm test -- --coverage

# Run specific test file
npm test -- AgentPanel.test.tsx

# Update snapshots
npm test -- -u
```

### E2E Tests

```bash
# Backend E2E
cd backend
pytest tests/e2e/ -v

# Frontend E2E
cd frontend
npm run test:e2e
```

---

## Coverage

### Backend Coverage

```bash
cd backend
pytest --cov=app --cov-report=html --cov-report=term
```

**Coverage Report**: `htmlcov/index.html`

**Target**: 80%+ coverage per module

### Frontend Coverage

```bash
cd frontend
npm test -- --coverage --watchAll=false
```

**Coverage Report**: `coverage/lcov-report/index.html`

**Target**: 80%+ coverage per component

---

## Test Examples

### Unit Test (Backend)

```python
# tests/unit/test_agents.py
import pytest
from app.graphs.venture_graph import VentureGraph
from app.models.agent import AgentRequest

@pytest.fixture
def venture_graph():
    return VentureGraph()

def test_agent_creation(venture_graph):
    assert venture_graph is not None
    assert venture_graph.graph is not None

@pytest.mark.parametrize("agent_type,expected", [
    ("venture", True),
    ("research", True),
    ("invalid", False),
])
def test_valid_agent_types(agent_type, expected):
    request = AgentRequest(
        agentType=agent_type,
        input="Test input"
    )
    assert request.is_valid() == expected

def test_agent_execution(venture_graph, mocker):
    # Mock LLM response
    mock_llm = mocker.patch('app.llm.providers.get_llm')
    mock_llm.return_value.invoke.return_value.content = "Test response"

    result = venture_graph.invoke({{"input": "Test"}})
    assert result["output"] == "Test response"
```

### Integration Test (Backend)

```python
# tests/integration/test_db.py
import pytest
from sqlalchemy.ext.asyncio import create_async_engine
from app.db.checkpoint import CheckpointStorage

@pytest.mark.asyncio
async def test_checkpoint_saving():
    storage = CheckpointStorage(test_db_url)

    await storage.save_checkpoint(
        thread_id="test-thread",
        checkpoint_id="checkpoint-1",
        state={{"key": "value"}}
    )

    checkpoint = await storage.get_checkpoint(
        thread_id="test-thread",
        checkpoint_id="checkpoint-1"
    )

    assert checkpoint is not None
    assert checkpoint["state"]["key"] == "value"
```

### Component Test (Frontend)

```typescript
// __tests__/unit/AgentPanel.test.tsx
import {{ render, screen }} from '@testing-library/react';
import {{ AgentPanel }} from '@/components/AgentPanel';

describe('AgentPanel', () => {{
  it('renders agent list', () => {{
    render(<AgentPanel agents={{['venture', 'research']}} />);
    expect(screen.getByText('venture')).toBeInTheDocument();
    expect(screen.getByText('research')).toBeInTheDocument();
  }});

  it('calls onExecute when button clicked', () => {{
    const mockExecute = jest.fn();
    render(<AgentPanel agents={{['venture']}} onExecute={{mockExecute}} />);

    fireEvent.click(screen.getByRole('button', {{ name: /execute/i }}));
    expect(mockExecute).toHaveBeenCalledWith('venture');
  }});
}});
```

### E2E Test (Frontend)

```typescript
// __tests__/e2e/agent-workflow.spec.ts
import {{ test, expect }} from '@playwright/test';

test('complete agent execution workflow', async ({{ page }}) => {{
  // Navigate to app
  await page.goto('http://localhost:3000');

  // Select agent type
  await page.selectOption('#agent-type', 'venture');

  // Enter input
  await page.fill('#agent-input', 'Test query');

  // Click execute
  await page.click('#execute-button');

  // Wait for result
  await expect(page.locator('#agent-result')).toBeVisible();
  await expect(page.locator('#agent-result')).toContainText('result');
}});
```

---

## CI/CD Integration

### GitHub Actions Workflow

```yaml
# .github/workflows/test.yml
name: Test Suite

on: [push, pull_request]

jobs:
  test-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          cd backend
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Run tests
        run: |
          cd backend
          pytest --cov=app --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  test-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - name: Install dependencies
        run: |
          cd frontend
          npm ci
      - name: Run tests
        run: |
          cd frontend
          npm test -- --coverage --watchAll=false
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  test-e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Start services
        run: docker-compose up -d
      - name: Run E2E tests
        run: |
          cd frontend
          npm run test:e2e
```

---

## Best Practices

### 1. Test Isolation

Each test should be independent:

```python
# BAD: Tests depend on execution order
def test_a():
    global.state = "modified"

def test_b():
    assert global.state == "modified"  # Depends on test_a

# GOOD: Each test is isolated
def test_a():
    state = "modified"
    assert state == "modified"

def test_b():
    state = "modified"
    assert state == "modified"
```

### 2. Use Fixtures

```python
@pytest.fixture
def clean_db():
    db = create_test_db()
    yield db
    drop_test_db(db)

def test_with_clean_db(clean_db):
    # Use clean_db
    pass
```

### 3. Mock External Services

```python
@pytest.mark.asyncio
async def test_llm_call(mocker):
    mock_llm = mocker.patch('app.llm.providers.get_llm')
    mock_llm.return_value.invoke.return_value.content = "Mocked"

    result = await call_llm("Test")
    assert result == "Mocked"
```

### 4. Test Edge Cases

```python
@pytest.mark.parametrize("input,expected", [
    ("normal", "success"),
    ("", "error"),
    (None, "error"),
    ("a"*10000, "error"),
    ("<script>", "error"),
])
def test_input_validation(input, expected):
    assert validate(input) == expected
```

### 5. Clean Up Resources

```python
@pytest.fixture
async def temp_file():
    path = "/tmp/test.txt"
    with open(path, 'w') as f:
        f.write("test")
    yield path
    os.remove(path)
```

---

## Troubleshooting

### Tests Fail Locally but Pass in CI

**Possible causes**:
- Environment differences (Python version, dependencies)
- Missing environment variables
- Database state differences

**Solution**: Use Docker for consistent environment

### Flaky Tests

**Possible causes**:
- Race conditions in async code
- Time-dependent assertions
- External service dependencies

**Solution**: Add retries and mocks

```python
@pytest.mark.flaky(reruns=3)
def test_something_flaky():
    pass
```

### Slow Tests

**Solution**: Use pytest markers

```python
@pytest.mark.slow
def test_slow_operation():
    time.sleep(10)

# Run fast tests only
pytest -m "not slow"
```

---

## Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Jest Documentation](https://jestjs.io/)
- [Playwright Documentation](https://playwright.dev/)
- [Testing Best Practices](https://testingjavascript.com/)
"""


CONTRIBUTING_TEMPLATE = r"""# Contributing to {project_name}

Thank you for your interest in contributing! This document provides guidelines and workflows for contributing to **{project_name}**.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Workflow](#development-workflow)
4. [Coding Standards](#coding-standards)
5. [Testing Requirements](#testing-requirements)
6. [Commit Guidelines](#commit-guidelines)
7. [Pull Request Process](#pull-request-process)

---

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

---

## Getting Started

### Prerequisites

- Node.js 18+
- Python 3.12+
- Docker (optional)
- Git

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/mk-knight23/{project_name}.git
cd {project_name}

# Install frontend dependencies
cd frontend
npm install

# Install backend dependencies
cd ../backend
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env
# Edit .env with your API keys

# Run development servers
# Terminal 1
cd frontend && npm run dev

# Terminal 2
cd backend && uvicorn main:app --reload
```

---

## Development Workflow

We follow the **5-Ecosystem** methodology:

### 1. Planning Phase

Before writing code, use the planner agent:

```
/plan
> Implement feature: X
```

This creates a detailed implementation plan.

### 2. TDD Phase

Use the TDD guide agent:

```
/tdd
> Follow test-driven development
```

**TDD Cycle**:
1. Write a failing test (RED)
2. Write minimal implementation to pass (GREEN)
3. Refactor while keeping tests green (IMPROVE)

### 3. Implementation Phase

Write code following the plan:
- Follow coding standards (see below)
- Run tests frequently
- Write/update tests as you go

### 4. Code Review Phase

Use the code-reviewer agent:

```
/code-review
> Review my changes
```

Address all CRITICAL and HIGH priority issues.

### 5. Security Scan

Use the security-reviewer agent:

```
/security-scan
> Check for security issues
```

---

## Coding Standards

### Python (Backend)

**Style Guide**: PEP 8

**Formatting**: Black

```bash
pip install black
black app/ tests/
```

**Linting**: Ruff

```bash
pip install ruff
ruff check app/ tests/
```

**Type Hints**: Required for all functions

```python
from typing import List, Optional

def execute_agent(
    agent_type: str,
    input: str,
    config: Optional[dict] = None
) -> dict:
    """Execute an agent with the given input.

    Args:
        agent_type: Type of agent to execute
        input: User input/prompt
        config: Optional configuration

    Returns:
        dict: Execution result with output and metadata
    """
    pass
```

**Documentation**: Google-style docstrings

### TypeScript/JavaScript (Frontend)

**Style Guide**: Airbnb Style Guide

**Formatting**: Prettier

```bash
npm install -g prettier
prettier --write "**/*.{ts,tsx,js,jsx}"
```

**Linting**: ESLint

```bash
npm run lint
```

**Type Safety**: Strict TypeScript

```typescript
interface AgentRequest {{
  agentType: 'venture' | 'research' | 'analysis';
  input: string;
  config?: {{
    temperature?: number;
    maxTokens?: number;
  }};
}}

async function executeAgent(request: AgentRequest): Promise<AgentResponse> {{
  // Implementation
}}
```

---

## Testing Requirements

### Coverage Target: 80%+

**Unit Tests**: Test individual functions and components

**Integration Tests**: Test API endpoints and database operations

**E2E Tests**: Test critical user workflows

### Running Tests

```bash
# Backend
cd backend
pytest --cov=app --cov-report=html

# Frontend
cd frontend
npm test -- --coverage
```

### Test Examples

See [TESTING.md](docs/TESTING.md) for detailed testing documentation.

---

## Commit Guidelines

### Commit Message Format

```
<type>: <description>

<optional body>
```

**Types**: feat, fix, refactor, docs, test, chore, perf, ci

**Examples**:

```
feat: add streaming support for agent execution

- Implement WebSocket endpoint
- Add streaming UI components
- Update documentation
```

```
fix: resolve memory leak in agent execution

The issue was caused by unclosed database connections.
Now using context managers for all DB operations.
```

---

## Pull Request Process

### 1. Before Creating PR

- [ ] All tests pass (80%+ coverage)
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No hardcoded secrets
- [ ] Security review passed

### 2. Create PR

```bash
git checkout -b feature/your-feature-name
# Make changes
git add .
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
```

Then create PR on GitHub.

### 3. PR Description Template

```markdown
## Summary
Brief description of changes

## Changes
- Change 1
- Change 2
- Change 3

## Test Plan
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

### 4. Review Process

- Address review feedback
- Update tests as needed
- Keep PR focused and small
- Request review from maintainers

### 5. Merge

After approval:
- Squash and merge
- Delete branch
- Celebrate! 🎉

---

## Feature Suggestions

We welcome feature suggestions! Please:

1. Check existing issues first
2. Use the issue template
3. Provide use cases and examples
4. Consider implementation complexity

---

## Questions?

- GitHub Issues: [https://github.com/mk-knight23/{project_name}/issues](https://github.com/mk-knight23/{project_name}/issues)
- Discussions: [https://github.com/mk-knight23/AI-SDK-ECOSYSTEM/discussions](https://github.com/mk-knight23/AI-SDK-ECOSYSTEM/discussions)

---

**Happy Contributing! 🚀**
"""


class DocumentationGenerator:
    """Generates documentation for AI-SDK projects."""

    def __init__(self, base_path: str = "/Users/mkazi/AI-SDK-PROJECTS"):
        self.base_path = Path(base_path)
        self.generated_files = []

    def generate_all(self) -> None:
        """Generate documentation for all projects."""
        print("=" * 60)
        print("AI-SDK Ecosystem Documentation Generator")
        print("=" * 60)
        print()

        for project_name, config in PROJECTS.items():
            print(f"Generating documentation for {project_name}...")
            try:
                self.generate_project_docs(config)
                print(f"  ✓ {project_name} documentation generated")
            except Exception as e:
                print(f"  ✗ {project_name} failed: {e}")
            print()

        self.print_summary()

    def generate_project_docs(self, config: ProjectConfig) -> None:
        """Generate all documentation for a single project."""
        project_path = self.base_path / config.path

        # Create docs directory
        docs_dir = project_path / "docs"
        docs_dir.mkdir(exist_ok=True)

        # Generate README
        self.generate_readme(config, project_path)

        # Generate API docs
        self.generate_api_docs(config, docs_dir)

        # Generate deployment docs
        self.generate_deployment_docs(config, docs_dir)

        # Generate testing docs
        self.generate_testing_docs(config, docs_dir)

        # Generate/update CONTRIBUTING
        self.generate_contributing(config, project_path)

    def generate_readme(self, config: ProjectConfig, project_path: Path) -> None:
        """Generate enhanced README.md."""
        # Read existing README to preserve custom content
        existing_readme = project_path / "README.md"
        custom_content = ""
        if existing_readme.exists():
            with open(existing_readme) as f:
                content = f.read()
                # Extract custom sections if any
                # This is a simple approach - could be more sophisticated

        # Format features list
        features_list = "\n".join([
            f"- {feature}" for feature in config.features
        ])

        # Format frontend table
        frontend_table = self.format_frontend_table(config)

        # Format backend table
        backend_table = self.format_backend_table(config)

        # Format prerequisites
        prerequisites = self.format_prerequisites(config)

        # Format API table
        api_table = self.format_api_table(config)

        # Format providers table
        providers_table = self.format_providers_table(config)

        # Format badges and URLs
        sdk_lower = config.sdk_name.lower().replace(" ", "").replace("-", "")
        sdk_url = f"https://github.com/langchain-ai/langchain" if "langchain" in sdk_lower else \
                  f"https://github.com/microsoft/autogen" if "autogen" in sdk_lower else \
                  f"https://github.com/run-llama/llama_index" if "llamaindex" in sdk_lower else \
                  f"https://github.com/{sdk_lower}/{sdk_lower}"

        readme_content = README_TEMPLATE.format(
            project_name=config.name,
            framework=config.framework,
            framework_badge=config.framework.replace(" ", "_"),
            framework_url=f"github.com/{sdk_lower}/{sdk_lower}",
            frontend=config.frontend_type,
            frontend_badge=config.frontend_type.replace(".", "").replace(" ", "_"),
            frontend_url="https://nextjs.org/" if "Next" in config.frontend_type else \
                        "https://vuejs.org/" if "Vue" in config.frontend_type else \
                        "https://remix.run/" if "Remix" in config.frontend_type else \
                        "https://svelte.dev/" if "Svelte" in config.frontend_type else "#",
            backend=config.backend_type,
            backend_badge=config.backend_type.replace(".", "").replace(" ", "_"),
            backend_url="https://fastapi.tiangolo.com/" if "FastAPI" in config.backend_type else \
                       "https://dotnet.microsoft.com/" if ".NET" in config.backend_type else \
                       "https://www.python.org/",
            description=config.description,
            features_list=features_list,
            frontend_table=frontend_table,
            backend_table=backend_table,
            prerequisites=prerequisites,
            api_table=api_table,
            providers_table=providers_table,
            sdk_lower=sdk_lower,
            SDK_UPPER=config.sdk_name.upper().replace(" ", "_").replace("-", "_"),
            sdk_docs_url=f"https://docs.{sdk_lower}.com",
            framework_docs_url=f"https://docs.{sdk_lower}.com",
            project_lower=config.name.lower().replace("ai-sdk-", ""),
            backend_command="uvicorn main:app --reload" if "FastAPI" in config.backend_type or "Python" in config.backend_type else \
                           "python main.py" if "Python" in config.backend_type else \
                           "dotnet run" if ".NET" in config.backend_type else "python main.py",
            frontend_deploy="vercel --prod" if "Next" in config.frontend_type or "Svelte" in config.frontend_type else \
                           "fly deploy" if "Remix" in config.frontend_type else \
                           "npm run build && vercel --prod",
            backend_deploy="railway up" if "FastAPI" in config.backend_type else \
                          "fly deploy" if "Python" in config.backend_type else \
                          "railway up"
        )

        readme_path = project_path / "README.md"
        with open(readme_path, 'w') as f:
            f.write(readme_content)

        self.generated_files.append(str(readme_path))

    def generate_api_docs(self, config: ProjectConfig, docs_dir: Path) -> None:
        """Generate API.md documentation."""
        # Format API endpoints with details
        api_endpoints_details = self.format_api_endpoints_details(config)

        api_content = API_DOC_TEMPLATE.format(
            project_name=config.name,
            project_lower=config.name.lower().replace("ai-sdk-", ""),
            api_endpoints_details=api_endpoints_details,
            sdk_lower=config.sdk_name.lower().replace(" ", "").replace("-", "")
        )

        api_path = docs_dir / "API.md"
        with open(api_path, 'w') as f:
            f.write(api_content)

        self.generated_files.append(str(api_path))

    def generate_deployment_docs(self, config: ProjectConfig, docs_dir: Path) -> None:
        """Generate DEPLOYMENT.md documentation."""
        # Format environment variables
        env_vars = self.format_env_vars(config)

        deployment_content = DEPLOYMENT_DOC_TEMPLATE.format(
            project_name=config.name,
            project_lower=config.name.lower().replace("ai-sdk-", ""),
            sdk_lower=config.sdk_name.lower().replace(" ", "").replace("-", ""),
            SDK_UPPER=config.sdk_name.upper().replace(" ", "_").replace("-", "_"),
            env_vars=env_vars
        )

        deployment_path = docs_dir / "DEPLOYMENT.md"
        with open(deployment_path, 'w') as f:
            f.write(deployment_content)

        self.generated_files.append(str(deployment_path))

    def generate_testing_docs(self, config: ProjectConfig, docs_dir: Path) -> None:
        """Generate TESTING.md documentation."""
        testing_content = TESTING_DOC_TEMPLATE.format(
            project_name=config.name
        )

        testing_path = docs_dir / "TESTING.md"
        with open(testing_path, 'w') as f:
            f.write(testing_content)

        self.generated_files.append(str(testing_path))

    def generate_contributing(self, config: ProjectConfig, project_path: Path) -> None:
        """Generate or update CONTRIBUTING.md."""
        contributing_content = CONTRIBUTING_TEMPLATE.format(
            project_name=config.name,
            project_lower=config.name.lower().replace("ai-sdk-", "")
        )

        contributing_path = project_path / "CONTRIBUTING.md"
        with open(contributing_path, 'w') as f:
            f.write(contributing_content)

        self.generated_files.append(str(contributing_path))

    def format_frontend_table(self, config: ProjectConfig) -> str:
        """Format frontend technology table."""
        techs = [
            (config.frontend_type, "latest", "UI Framework"),
            ("React", "19", "UI Library" if "React" not in config.frontend_type else "Built-in"),
            ("TypeScript", "5.x", "Type Safety"),
            ("Tailwind CSS", "v4", "Styling" if "Next" in config.frontend_type else None),
            ("shadcn/ui", "latest", "Components" if "Next" in config.frontend_type else None),
            ("Chakra UI", "latest", "Components" if "Remix" in config.frontend_type else None),
        ]
        return "\n".join([
            f"| {tech} | {version} | {purpose} |"
            for tech, version, purpose in techs
            if purpose  # Only include if purpose exists
        ])

    def format_backend_table(self, config: ProjectConfig) -> str:
        """Format backend technology table."""
        if "FastAPI" in config.backend_type or "Python" in config.backend_type:
            techs = [
                ("Python", "3.12", "Runtime"),
                ("FastAPI", "latest", "API Framework"),
                (config.sdk_name, "latest", "AI Framework"),
                ("PostgreSQL", "16", "Database"),
                ("Redis", "7.x", "Cache"),
            ]
        elif ".NET" in config.backend_type:
            techs = [
                (".NET", "9.0", "Runtime"),
                ("C#", "13", "Language"),
                (config.sdk_name, "0.4", "Multi-Agent Framework"),
                ("PostgreSQL", "16", "Database"),
            ]
        else:
            techs = [
                ("Node.js", "20", "Runtime"),
                ("Next.js API", "15", "API Framework"),
                (config.sdk_name, "latest", "AI SDK"),
            ]

        return "\n".join([
            f"| {tech} | {version} | {purpose} |"
            for tech, version, purpose in techs
        ])

    def format_prerequisites(self, config: ProjectConfig) -> str:
        """Format prerequisites section."""
        prereqs = ["Node.js 18+"]

        if "FastAPI" in config.backend_type or "Python" in config.backend_type:
            prereqs.append("Python 3.12+")
        elif ".NET" in config.backend_type:
            prereqs.append(".NET 9 SDK")

        prereqs.append("Docker (optional)")

        return "\n".join([
            f"- {prereq}" for prereq in prereqs
        ])

    def format_api_table(self, config: ProjectConfig) -> str:
        """Format API endpoints table."""
        return "\n".join([
            f"| {ep.split()[0]} | `{ep.split()[1]}` | {' '.join(ep.split()[2:])} |"
            for ep in config.api_endpoints
        ])

    def format_providers_table(self, config: ProjectConfig) -> str:
        """Format providers table."""
        providers = {
            "LANGCHAIN": [
                ("OpenAI", "GPT-4", "OPENAI_API_KEY"),
                ("Anthropic", "Claude", "ANTHROPIC_API_KEY"),
                ("OpenRouter", "Multi-model", "OPENROUTER_API_KEY"),
                ("Perplexity", "Search", "PERPLEXITY_API_KEY"),
            ],
            "LANGGRAPH": [
                ("OpenAI", "GPT-4", "OPENAI_API_KEY"),
                ("Anthropic", "Claude", "ANTHROPIC_API_KEY"),
            ],
            "AUTOGEN": [
                ("OpenAI", "GPT-4", "OPENAI_API_KEY"),
                ("Azure OpenAI", "GPT-4", "AZURE_OPENAI_API_KEY"),
            ],
            "CREWAI": [
                ("OpenAI", "GPT-4", "OPENAI_API_KEY"),
                ("Anthropic", "Claude", "ANTHROPIC_API_KEY"),
            ],
            "LAMA-INDEX": [
                ("OpenAI", "GPT-4", "OPENAI_API_KEY"),
                ("Anthropic", "Claude", "ANTHROPIC_API_KEY"),
            ],
            "HAYSTACK": [
                ("OpenAI", "GPT-4", "OPENAI_API_KEY"),
                ("Cohere", "Command", "COHERE_API_KEY"),
            ],
            "SEMANTIC-KERNEL": [
                ("OpenAI", "GPT-4", "OPENAI_API_KEY"),
                ("Azure OpenAI", "GPT-4", "AZURE_OPENAI_API_KEY"),
            ],
            "OPENAI": [
                ("OpenAI", "GPT-4o/GPT-4o-mini", "OPENAI_API_KEY"),
            ],
            "ANTHROPIC": [
                ("Anthropic", "Claude 3.5 Sonnet", "ANTHROPIC_API_KEY"),
                ("OpenRouter", "Claude via router", "OPENROUTER_API_KEY"),
            ],
            "VERCEL-AI": [
                ("OpenAI", "GPT-4", "OPENAI_API_KEY"),
                ("Anthropic", "Claude", "ANTHROPIC_API_KEY"),
                ("20+ providers", "via AI SDK", "various"),
            ],
        }

        sdk_key = config.sdk_name.upper().replace("-", "").replace(" ", "")
        if sdk_key == "LAMAINDEX":
            sdk_key = "LAMA-INDEX"

        providers_list = providers.get(sdk_key, [
            ("OpenAI", "GPT-4", "OPENAI_API_KEY"),
        ])

        return "\n".join([
            f"| {provider} | {usage} | `{env_var}` |"
            for provider, usage, env_var in providers_list
        ])

    def format_api_endpoints_details(self, config: ProjectConfig) -> str:
        """Format detailed API endpoints documentation."""
        sections = []

        for ep in config.api_endpoints:
            parts = ep.split()
            method = parts[0]
            path = parts[1]
            desc = ' '.join(parts[2:])

            sections.append(f"""
### {method} {path}

**Description**: {desc}

**Request**:

```bash
curl -X {method} http://localhost:8000{path} \\
  -H "Authorization: Bearer $API_KEY"
```

**Response**:

```json
{{
  "success": true,
  "data": {{ ... }},
  "error": null
}}
```

---
""")

        return "\n".join(sections)

    def format_env_vars(self, config: ProjectConfig) -> str:
        """Format environment variables section."""
        sdk_key = config.sdk_name.upper().replace("-", "").replace(" ", "")
        if sdk_key == "LAMAINDEX":
            sdk_key = "LAMA-INDEX"

        common_vars = [
            "ANTHROPIC_API_KEY=sk-ant-...",
            "OPENAI_API_KEY=sk-openai-...",
        ]

        if "LANGCHAIN" in sdk_key or "LANGGRAPH" in sdk_key:
            common_vars.extend([
                "OPENROUTER_API_KEY=sk-or-...",
                "PERPLEXITY_API_KEY=pplx-...",
            ])
        elif "AUTOGEN" in sdk_key or "SEMANTIC" in sdk_key:
            common_vars.append("AZURE_OPENAI_API_KEY=...")

        return "\n".join([
            f"{var}" for var in common_vars
        ])

    def print_summary(self) -> None:
        """Print generation summary."""
        print("=" * 60)
        print("DOCUMENTATION GENERATION SUMMARY")
        print("=" * 60)
        print(f"\nTotal files generated: {len(self.generated_files)}")
        print("\nGenerated files:")
        for f in sorted(self.generated_files):
            print(f"  ✓ {f}")
        print()
        print("=" * 60)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate documentation for AI-SDK projects"
    )
    parser.add_argument(
        "--project",
        help="Specific project to generate docs for (default: all)"
    )
    parser.add_argument(
        "--base-path",
        default="/Users/mkazi/AI-SDK-PROJECTS",
        help="Base path to projects directory"
    )

    args = parser.parse_args()

    generator = DocumentationGenerator(args.base_path)

    if args.project:
        if args.project in PROJECTS:
            config = PROJECTS[args.project]
            generator.generate_project_docs(config)
        else:
            print(f"Unknown project: {args.project}")
            print(f"Available projects: {', '.join(PROJECTS.keys())}")
            sys.exit(1)
    else:
        generator.generate_all()


if __name__ == "__main__":
    main()
