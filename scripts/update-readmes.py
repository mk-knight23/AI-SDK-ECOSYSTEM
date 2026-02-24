#!/usr/bin/env python3
"""
Update all READMEs with Architecture, API, and Troubleshooting sections
"""

from pathlib import Path

BASE_PATH = Path("/Users/mkazi/AI-SDK-PROJECTS")

SECTIONS_TO_ADD = """
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
---

"""

PROJECTS = [
    "AI-SDK-ANTHROPIC",
    "AI-SDK-LANGGRAPH",
    "AI-SDK-OPENAI",
    "AI-SDK-SEMANTIC-KERNEL",
    "AI-SDK-VERCEL-AI",
]

def update_readme(project_name):
    """Update README with new sections."""
    readme_path = BASE_PATH / project_name / "README.md"
    
    if not readme_path.exists():
        print(f"  ⊘ README not found")
        return None
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    # Check if already has all sections
    if "## 🏗️ Architecture" in content and "## 📡 API Endpoints" in content:
        print(f"  ✓ Already enhanced")
        return readme_path
    
    # Find the position to insert (before License or at the end)
    if "## 📄 License" in content:
        content = content.replace("## 📄 License", SECTIONS_TO_ADD + "## 📄 License")
    elif "## License" in content:
        content = content.replace("## License", SECTIONS_TO_ADD + "## License")
    elif "**Built with" in content:
        content = content.replace("**Built with", SECTIONS_TO_ADD + "\n**Built with")
    elif "**Part of" in content:
        content = content.replace("**Part of", SECTIONS_TO_ADD + "\n**Part of")
    else:
        # Append at the end
        content = content + SECTIONS_TO_ADD
    
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"  ✓ Enhanced")
    return readme_path

def main():
    print("Updating READMEs that need enhancement...")
    print()
    
    for project_name in PROJECTS:
        print(f"{project_name}:")
        update_readme(project_name)
    
    print()
    print("Done!")

if __name__ == "__main__":
    main()
