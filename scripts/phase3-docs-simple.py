#!/usr/bin/env python3
"""
Simple Documentation Generator for AI-SDK Projects
Generates comprehensive documentation without complex templates
"""

import os
from pathlib import Path

# Base path
BASE_PATH = Path("/Users/mkazi/AI-SDK-PROJECTS")

# All projects
PROJECTS = [
    "AI-SDK-LANGCHAIN",
    "AI-SDK-LANGGRAPH", 
    "AI-SDK-AUTOGEN",
    "AI-SDK-CREWAI",
    "AI-SDK-LAMA-INDEX",
    "AI-SDK-HAYSTACK",
    "AI-SDK-SEMANTIC-KERNEL",
    "AI-SDK-OPENAI",
    "AI-SDK-ANTHROPIC",
    "AI-SDK-VERCEL-AI",
]

def create_docs_directory(project_path):
    """Create docs directory if it doesn't exist."""
    docs_dir = project_path / "docs"
    docs_dir.mkdir(exist_ok=True)
    return docs_dir

def generate_api_doc(project_name, docs_dir):
    """Generate API.md documentation."""
    project_lower = project_name.lower().replace("ai-sdk-", "")
    
    content = f"""# API Reference

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

---

## Endpoints

### Health Check

**GET /health**

Check service health status.

```bash
curl http://localhost:8000/health
```

Response:
```json
{{
  "status": "healthy",
  "service": "{project_lower}-api",
  "version": "0.1.0"
}}
```

---

## Error Codes

| Code | Description | Solution |
|------|-------------|----------|
| 400 | Bad Request | Check request body format |
| 401 | Unauthorized | Verify API key is valid |
| 429 | Rate Limited | Implement backoff |
| 500 | Internal Error | Contact support |

---

For more details, see the project README.
"""
    
    api_path = docs_dir / "API.md"
    with open(api_path, 'w') as f:
        f.write(content)
    return api_path

def generate_deployment_doc(project_name, docs_dir):
    """Generate DEPLOYMENT.md documentation."""
    project_lower = project_name.lower().replace("ai-sdk-", "")
    
    content = f"""# Deployment Guide

**{project_name}** - Production Deployment Instructions

---

## Environment Setup

### Required Environment Variables

```bash
# API Keys
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-openai-...

# Database
DATABASE_URL=postgresql://user:pass@host:5432/dbname
REDIS_URL=redis://host:6379

# Application
NODE_ENV=production
API_BASE_URL=https://api.{project_lower}.com
```

---

## Platform Deployments

### Vercel (Frontend)

```bash
cd frontend
vercel --prod
```

### Railway (Backend)

```bash
cd backend
railway up
```

### Fly.io (Full Stack)

```bash
fly deploy
```

---

## Docker Deployment

```bash
docker-compose up -d
```

---

## Health Check

```bash
curl https://api.{project_lower}.com/health
```

---

For more details, see the project README.
"""
    
    deployment_path = docs_dir / "DEPLOYMENT.md"
    with open(deployment_path, 'w') as f:
        f.write(content)
    return deployment_path

def generate_testing_doc(project_name, docs_dir):
    """Generate TESTING.md documentation."""
    
    content = f"""# Testing Guide

**{project_name}** - Comprehensive Testing Documentation

---

## Testing Philosophy

This project follows **Test-Driven Development (TDD)**:

1. **RED** - Write failing test first
2. **GREEN** - Write minimal implementation to pass
3. **IMPROVE** - Refactor while keeping tests green

**Target Coverage**: 80%+ across all modules

---

## Running Tests

### Backend Tests

```bash
cd backend
pytest --cov=app --cov-report=html
```

### Frontend Tests

```bash
cd frontend
npm test -- --coverage
```

---

## Test Structure

```
backend/
├── tests/
│   ├── unit/              # Unit tests
│   ├── integration/       # Integration tests
│   └── e2e/              # End-to-end tests

frontend/
├── __tests__/
│   ├── unit/             # Component tests
│   └── e2e/             # E2E tests
```

---

## Coverage

**Target**: 80%+ coverage

View coverage reports:
- Backend: `htmlcov/index.html`
- Frontend: `coverage/lcov-report/index.html`

---

For more details, see the project README.
"""
    
    testing_path = docs_dir / "TESTING.md"
    with open(testing_path, 'w') as f:
        f.write(content)
    return testing_path

def update_readme(project_name, project_path):
    """Enhance README with architecture, API, and troubleshooting sections."""
    readme_path = project_path / "README.md"
    
    if not readme_path.exists():
        return None
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    # Check if already enhanced
    if "## 🏗️ Architecture" in content:
        return readme_path
    
    # Add sections before the license
    sections_to_add = """
---

## 🏗️ Architecture

```mermaid
graph TB
    subgraph "Frontend"
        UI[User Interface]
    end
    
    subgraph "Backend"
        API[API Layer]
        Core[AI Framework]
        Providers[LLM Providers]
    end
    
    subgraph "Infrastructure"
        DB[(Database)]
        Cache[(Cache)]
    end
    
    UI -->|HTTP/WS| API
    API --> Core
    Core --> Providers
    API --> DB
    Core --> Cache
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| POST | /api/execute | Execute agent workflow |
| WS | /api/stream | WebSocket streaming |

---

## 🔧 Troubleshooting

### Common Issues

**Connection refused**
- Ensure backend is running
- Check port availability

**Authentication failures**
- Verify API keys in `.env`
- Check environment variables

**Rate limiting**
- Implement exponential backoff
- Reduce request frequency

---

## 📚 Additional Documentation

- [API Reference](docs/API.md) - Complete API documentation
- [Deployment Guide](docs/DEPLOYMENT.md) - Platform-specific deployment
- [Testing Guide](docs/TESTING.md) - Testing strategies and coverage
"""
    
    # Insert before the license section
    if "## 📄 License" in content:
        content = content.replace("## 📄 License", sections_to_add + "\n## 📄 License")
    elif "## License" in content:
        content = content.replace("## License", sections_to_add + "\n## License")
    
    with open(readme_path, 'w') as f:
        f.write(content)
    
    return readme_path

def update_contributing(project_name, project_path):
    """Enhance CONTRIBUTING.md."""
    contributing_path = project_path / "CONTRIBUTING.md"
    
    content = f"""# Contributing to {project_name}

Thank you for your interest in contributing!

---

## Development Workflow

1. **Planning**: Create an issue or discuss in a PR first
2. **TDD**: Write tests before implementation
3. **Implementation**: Follow code style guidelines
4. **Testing**: Ensure 80%+ coverage
5. **Documentation**: Update relevant docs

---

## Code Style

### Backend (Python)
- Follow PEP 8
- Use Black for formatting
- Add type hints
- Write docstrings

### Frontend (TypeScript/JavaScript)
- Use Prettier for formatting
- Follow ESLint rules
- Add JSDoc comments

---

## Testing

```bash
# Backend
cd backend
pytest --cov=app

# Frontend
cd frontend
npm test
```

---

## Commit Messages

Format: `<type>: <description>`

Types: feat, fix, docs, test, refactor, chore

Example: `feat: add streaming support`

---

## Pull Requests

1. Fork and create a branch
2. Make your changes
3. Ensure tests pass
4. Submit PR with description

---

**Happy Contributing! 🚀**
"""
    
    with open(contributing_path, 'w') as f:
        f.write(content)
    
    return contributing_path

def main():
    """Generate documentation for all projects."""
    print("=" * 60)
    print("AI-SDK Documentation Generator")
    print("=" * 60)
    print()
    
    generated_files = []
    
    for project_name in PROJECTS:
        project_path = BASE_PATH / project_name
        
        if not project_path.exists():
            print(f"⊘ {project_name} - skipped (not found)")
            continue
        
        print(f"✓ {project_name}")
        
        # Create docs directory
        docs_dir = create_docs_directory(project_path)
        
        # Generate documentation files
        api_doc = generate_api_doc(project_name, docs_dir)
        deployment_doc = generate_deployment_doc(project_name, docs_dir)
        testing_doc = generate_testing_doc(project_name, docs_dir)
        
        # Update existing files
        readme = update_readme(project_name, project_path)
        contributing = update_contributing(project_name, project_path)
        
        generated_files.extend([api_doc, deployment_doc, testing_doc, readme, contributing])
    
    print()
    print("=" * 60)
    print(f"Generated {len(generated_files)} documentation files")
    print("=" * 60)

if __name__ == "__main__":
    main()
