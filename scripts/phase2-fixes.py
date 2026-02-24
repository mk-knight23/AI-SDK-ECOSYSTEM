#!/usr/bin/env python3

"""
Phase 2: Automated Fix Script for Validation Issues
This script reads validation results and applies fixes for common issues:
1. Missing backend entry points (Critical)
2. Missing environment configuration (High)
"""

import os
import sys
import json
import subprocess
import datetime
import logging
from pathlib import Path
from typing import Dict, List, Tuple

# Configuration
BASE_DIR = os.environ.get("PROJECT_ROOT", "/Users/mkazi/AI-SDK-PROJECTS")
RESULTS_DIR = os.path.join(BASE_DIR, "validation-results")
TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Project configurations with tech stack info
PROJECTS = {
    "AI-SDK-LANGCHAIN": {
        "name": "langchain",
        "framework": "LangChain",
        "backend_type": "python",
        "entry_point": "main.py"
    },
    "AI-SDK-CREWAI": {
        "name": "crewai",
        "framework": "CrewAI",
        "backend_type": "python",
        "entry_point": "main.py"
    },
    "AI-SDK-LAMA-INDEX": {
        "name": "lamaindex",
        "framework": "LlamaIndex",
        "backend_type": "python",
        "entry_point": "main.py"
    },
    "AI-SDK-ANTHROPIC": {
        "name": "anthropic",
        "framework": "Anthropic",
        "backend_type": "python",
        "entry_point": "main.py"
    },
    "AI-SDK-HAYSTACK": {
        "name": "haystack",
        "framework": "Haystack",
        "backend_type": "python",
        "entry_point": "app.py"
    },
    "AI-SDK-SEMANTIC-KERNEL": {
        "name": "semantic-kernel",
        "framework": "SemanticKernel",
        "backend_type": "python",
        "entry_point": "app.py"
    },
    "AI-SDK-AUTOGEN": {
        "name": "autogen",
        "framework": "AutoGen",
        "backend_type": "dotnet",
        "entry_point": "Program.cs"
    },
    "AI-SDK-OPENAI": {
        "name": "openai",
        "framework": "OpenAI",
        "backend_type": "go",
        "entry_point": "main.go"
    },
    "AI-SDK-LANGGRAPH": {
        "name": "langgraph",
        "framework": "LangGraph",
        "backend_type": "nodejs",
        "entry_point": None  # Has embedded API routes
    },
    "AI-SDK-VERCEL-AI": {
        "name": "vercel-ai",
        "framework": "VercelAI",
        "backend_type": "nextjs",
        "entry_point": None  # Has embedded API routes
    },
}

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ANSI color codes
class Colors:
    BLUE = '\033[0;34m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    RED = '\033[0;31m'
    NC = '\033[0m'

def print_header():
    """Print fix script header"""
    print(f"{Colors.BLUE}{'='*40}{Colors.NC}")
    print(f"{Colors.BLUE}Phase 2: Automated Fixes{Colors.NC}")
    print(f"{Colors.BLUE}{'='*40}{Colors.NC}")
    print()

# Templates for different entry points

PYTHON_FASTAPI_TEMPLATE = '''"""
{framework} Backend Server
AI SDK: {framework}
Tech Stack: FastAPI + Python
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from typing import Optional

app = FastAPI(
    title="{framework} API",
    version="1.0.0",
    description="{framework} AI SDK backend service"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {{
        "status": "healthy",
        "service": "{service_name}-api",
        "version": "1.0.0"
    }}

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {{
        "message": "Welcome to {framework} API",
        "version": "1.0.0",
        "endpoints": {{
            "health": "/health",
            "api": "/api"
        }}
    }}

# AI endpoint (placeholder for now)
class AIRequest(BaseModel):
    prompt: str
    parameters: Optional[dict] = None

@app.post("/api/ai")
async def ai_endpoint(request: AIRequest):
    """AI endpoint - placeholder implementation"""
    return {{
        "response": f"Mock AI response for: {{request.prompt}}",
        "status": "success",
        "framework": "{framework}"
    }}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
'''

PYTHON_FLASK_TEMPLATE = '''"""
{framework} Backend Server
AI SDK: {framework}
Tech Stack: Flask + Python
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({{
        "status": "healthy",
        "service": "{service_name}-api",
        "version": "1.0.0"
    }})

# Root endpoint
@app.route("/", methods=["GET"])
def root():
    """Root endpoint"""
    return jsonify({{
        "message": "Welcome to {framework} API",
        "version": "1.0.0",
        "endpoints": {{
            "health": "/health",
            "api": "/api"
        }}
    }})

# AI endpoint (placeholder for now)
@app.route("/api/ai", methods=["POST"])
def ai_endpoint():
    """AI endpoint - placeholder implementation"""
    data = request.get_json()
    prompt = data.get("prompt", "")
    return jsonify({{
        "response": f"Mock AI response for: {{prompt}}",
        "status": "success",
        "framework": "{framework}"
    }})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
'''

def get_go_template(framework: str, service_name: str) -> str:
    return f'''/*
{framework} Backend Server
AI SDK: {framework}
Tech Stack: Go + Standard Library
*/

package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
)

// Response represents a standard API response
type Response struct {{
	Status   string      `json:"status"`
	Message  string      `json:"message,omitempty"`
	Data     interface{{}} `json:"data,omitempty"`
}}

// AIRequest represents an AI request
type AIRequest struct {{
	Prompt      string                 `json:"prompt"`
	Parameters map[string]interface{{}} `json:"parameters,omitempty"`
}}

func main() {{
	port := os.Getenv("PORT")
	if port == "" {{
		port = "8080"
	}}

	// Health check endpoint
	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {{
		w.Header().Set("Content-Type", "application/json")
		response := Response{{
			Status: "healthy",
			Data: map[string]string{{
				"service": "{service_name}-api",
				"version": "1.0.0",
			}},
		}}
		json.NewEncoder(w).Encode(response)
	}})

	// Root endpoint
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {{
		w.Header().Set("Content-Type", "application/json")
		response := Response{{
			Status:  "success",
			Message: fmt.Sprintf("Welcome to {framework} API"),
			Data: map[string]interface{{}}{{
				"version": "1.0.0",
				"endpoints": map[string]string{{
					"health": "/health",
					"api":    "/api/ai",
				}},
			}},
		}}
		json.NewEncoder(w).Encode(response)
	}})

	// AI endpoint (placeholder for now)
	http.HandleFunc("/api/ai", func(w http.ResponseWriter, r *http.Request) {{
		if r.Method != http.MethodPost {{
			http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
			return
		}}

		var aiReq AIRequest
		if err := json.NewDecoder(r.Body).Decode(&aiReq); err != nil {{
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}}

		w.Header().Set("Content-Type", "application/json")
		response := Response{{
			Status:  "success",
			Message: fmt.Sprintf("Mock AI response for: %s", aiReq.Prompt),
			Data: map[string]string{{
				"framework": "{framework}",
			}},
		}}
		json.NewEncoder(w).Encode(response)
	}})

	addr := fmt.Sprintf(":%s", port)
	log.Printf("Server starting on %s", addr)
	log.Fatal(http.ListenAndServe(addr, nil))
}}
'''

ENV_EXAMPLE_TEMPLATE = '''# AI SDK API Keys
OPENAI_API_KEY=sk-your-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here
{extra_keys}

# Server Configuration
PORT=8000
HOST=0.0.0.0

# Database (if applicable)
# DATABASE_URL=postgresql://user:pass@localhost/dbname

# Environment
NODE_ENV=development
'''

def get_entry_point_template(project_dir: str, framework: str, backend_type: str) -> str:
    """Get the appropriate entry point template for a project"""
    service_name = framework.lower().replace(" ", "").replace(".", "")

    if backend_type == "python":
        # Use Flask for Semantic Kernel, FastAPI for others
        if framework == "SemanticKernel":
            return PYTHON_FLASK_TEMPLATE.format(framework=framework, service_name=service_name)
        return PYTHON_FASTAPI_TEMPLATE.format(framework=framework, service_name=service_name)
    elif backend_type == "go":
        return get_go_template(framework, service_name)
    elif backend_type == "dotnet":
        # AutoGen has .NET, so we shouldn't need to create it
        return None
    return None

def create_backend_entry_point(project_dir: str, framework: str, backend_type: str, entry_point: str) -> Tuple[bool, str]:
    """
    Create backend entry point if missing

    Returns:
        Tuple of (success, message)
    """
    full_path = os.path.join(BASE_DIR, project_dir)
    backend_path = os.path.join(full_path, "backend")

    # Check if backend directory exists
    if not os.path.exists(backend_path):
        return False, f"Backend directory not found: {backend_path}"

    entry_point_path = os.path.join(backend_path, entry_point)

    # Check if entry point already exists
    if os.path.exists(entry_point_path):
        return False, f"Entry point already exists: {entry_point_path}"

    print(f"{Colors.YELLOW}  Creating {entry_point} for {framework}...{Colors.NC}")

    # Get template
    template = get_entry_point_template(project_dir, framework, backend_type)
    if template is None:
        return False, f"No template available for backend type: {backend_type}"

    # Write entry point
    try:
        with open(entry_point_path, 'w') as f:
            f.write(template)
        print(f"{Colors.GREEN}    ✓ Created {entry_point}{Colors.NC}")
        return True, f"Created entry point: {entry_point_path}"
    except Exception as e:
        print(f"{Colors.RED}    ✗ Failed to create {entry_point}: {e}{Colors.NC}")
        return False, f"Failed to create entry point: {e}"

def create_env_example(project_dir: str, framework: str, backend_type: str) -> Tuple[bool, str]:
    """
    Create .env.example if missing

    Returns:
        Tuple of (success, message)
    """
    full_path = os.path.join(BASE_DIR, project_dir)
    backend_path = os.path.join(full_path, "backend")

    # For Next.js/SvelteKit projects, check root
    if backend_type in ["nextjs", "nodejs"]:
        env_path = os.path.join(full_path, ".env.example")
    else:
        env_path = os.path.join(backend_path, ".env.example")

    # Check if .env.example already exists
    if os.path.exists(env_path):
        return False, f".env.example already exists: {env_path}"

    print(f"{Colors.YELLOW}  Creating .env.example for {framework}...{Colors.NC}")

    # Framework-specific keys
    extra_keys = ""
    if framework == "CrewAI":
        extra_keys = "\nSERPER_API_KEY=your_serper_api_key_here"
    elif framework == "Haystack":
        extra_keys = "\nHUGGINGFACE_API_KEY=your_huggingface_key_here"
    elif framework == "SemanticKernel":
        extra_keys = "\nAZURE_OPENAI_API_KEY=your-azure-key-here\nAZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/"

    # Get template
    template = ENV_EXAMPLE_TEMPLATE.format(extra_keys=extra_keys)

    # For Next.js/SvelteKit, we need a different format
    if backend_type == "nextjs":
        template = f'''# AI SDK API Keys
OPENAI_API_KEY=sk-your-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here

# Vercel AI SDK Configuration
MODEL_NAME=gpt-4
'''

    # Write .env.example
    try:
        # Create directory if needed
        os.makedirs(os.path.dirname(env_path), exist_ok=True)

        with open(env_path, 'w') as f:
            f.write(template)
        print(f"{Colors.GREEN}    ✓ Created .env.example{Colors.NC}")
        return True, f"Created .env.example: {env_path}"
    except Exception as e:
        print(f"{Colors.RED}    ✗ Failed to create .env.example: {e}{Colors.NC}")
        return False, f"Failed to create .env.example: {e}"

def test_entry_point(project_dir: str, framework: str, backend_type: str, entry_point: str) -> bool:
    """
    Test that the entry point file is valid

    Returns:
        True if valid, False otherwise
    """
    full_path = os.path.join(BASE_DIR, project_dir)
    backend_path = os.path.join(full_path, "backend")
    entry_point_path = os.path.join(backend_path, entry_point)

    if not os.path.exists(entry_point_path):
        return False

    print(f"{Colors.YELLOW}  Testing {entry_point}...{Colors.NC}")

    try:
        if backend_type == "python":
            # Syntax check with Python
            result = subprocess.run(
                ["python3", "-m", "py_compile", entry_point_path],
                capture_output=True,
                timeout=5
            )
            if result.returncode == 0:
                print(f"{Colors.GREEN}    ✓ Syntax check passed{Colors.NC}")
                return True
            else:
                print(f"{Colors.RED}    ✗ Syntax check failed{Colors.NC}")
                return False
        elif backend_type == "go":
            # Syntax check with Go
            result = subprocess.run(
                ["go", "build", "-o", "/dev/null", entry_point_path],
                cwd=backend_path,
                capture_output=True,
                timeout=10
            )
            if result.returncode == 0:
                print(f"{Colors.GREEN}    ✓ Build check passed{Colors.NC}")
                return True
            else:
                print(f"{Colors.RED}    ✗ Build check failed{Colors.NC}")
                return False
        elif backend_type == "dotnet":
            # Check if Program.cs is valid (just check file exists for .NET)
            print(f"{Colors.GREEN}    ✓ File exists{Colors.NC}")
            return True
        else:
            # For Next.js/Node.js projects, just check file exists
            print(f"{Colors.GREEN}    ✓ File exists{Colors.NC}")
            return True
    except Exception as e:
        print(f"{Colors.RED}    ✗ Test failed: {e}{Colors.NC}")
        return False

def fix_project(project_dir: str, project_info: Dict, validation_issues: List[Dict]) -> Dict:
    """
    Fix issues for a single project

    Args:
        project_dir: Project directory name
        project_info: Project configuration dict
        validation_issues: List of validation issues from Phase 1

    Returns:
        Dictionary containing fix results
    """
    result = {
        "project": project_info["name"],
        "directory": project_dir,
        "framework": project_info["framework"],
        "backend_type": project_info["backend_type"],
        "fixes_applied": [],
        "fixes_failed": [],
        "tests_passed": [],
        "tests_failed": []
    }

    print(f"{Colors.BLUE}Processing: {project_info['name']}{Colors.NC}")

    # Check issues and apply fixes
    for issue in validation_issues:
        severity = issue.get("severity")
        category = issue.get("category")
        message = issue.get("message")

        if severity == "Critical" and category == "Backend":
            if "No backend entry point" in message:
                entry_point = project_info.get("entry_point")
                if entry_point:
                    success, msg = create_backend_entry_point(
                        project_dir,
                        project_info["framework"],
                        project_info["backend_type"],
                        entry_point
                    )
                    if success:
                        result["fixes_applied"].append(msg)
                        # Test the fix
                        if test_entry_point(
                            project_dir,
                            project_info["framework"],
                            project_info["backend_type"],
                            entry_point
                        ):
                            result["tests_passed"].append(f"Entry point validation: {entry_point}")
                        else:
                            result["tests_failed"].append(f"Entry point validation: {entry_point}")
                    else:
                        result["fixes_failed"].append(msg)

        elif severity == "High" and category == "Configuration":
            if "No .env.example" in message:
                success, msg = create_env_example(
                    project_dir,
                    project_info["framework"],
                    project_info["backend_type"]
                )
                if success:
                    result["fixes_applied"].append(msg)
                else:
                    result["fixes_failed"].append(msg)

    return result

def load_validation_results() -> Dict[str, List[Dict]]:
    """
    Load validation results from Phase 1

    Returns:
        Dictionary mapping project names to their issues
    """
    # Find all validation result JSON files (excluding validation-report.md)
    json_files = []
    for f in os.listdir(RESULTS_DIR):
        if f.endswith(".json") and not f.startswith("validation-report"):
            json_files.append(f)

    # Get the latest timestamp from filenames
    if not json_files:
        logger.warning("No validation results found")
        return {}

    # Extract timestamps and find the latest
    timestamps = set()
    for f in json_files:
        # Filename format: projectname-YYYYMMDD_HHMMSS.json
        parts = f.replace(".json", "").split("-")
        if len(parts) >= 2:
            timestamps.add(parts[-1])

    if not timestamps:
        logger.warning("No valid timestamps found in validation results")
        return {}

    latest_timestamp = sorted(timestamps)[-1]
    logger.info(f"Using validation results with timestamp: {latest_timestamp}")

    issues_by_project = {}
    for project_key, project_info in PROJECTS.items():
        project_name = project_info["name"]
        # Find the file for this project with the latest timestamp
        pattern = f"{project_name}-{latest_timestamp}.json"
        json_path = os.path.join(RESULTS_DIR, pattern)

        if os.path.exists(json_path):
            with open(json_path, 'r') as f:
                data = json.load(f)
                issues_by_project[project_name] = data.get("issues", [])
                logger.info(f"Loaded {len(issues_by_project[project_name])} issues for {project_name}")
        else:
            logger.warning(f"No validation results found for {project_name}")

    return issues_by_project

def generate_fix_report(results: List[Dict], report_file: str):
    """Generate markdown fix report"""
    total_fixes_applied = sum(len(r["fixes_applied"]) for r in results)
    total_fixes_failed = sum(len(r["fixes_failed"]) for r in results)
    total_tests_passed = sum(len(r["tests_passed"]) for r in results)
    total_tests_failed = sum(len(r["tests_failed"]) for r in results)

    with open(report_file, 'w') as f:
        f.write(f"""# Phase 2 Fix Report

**Date:** {datetime.datetime.now().strftime("%Y-%m-%d")}
**Time:** {datetime.datetime.now().strftime("%H:%M:%S")}
**Projects Processed:** {len(results)}

## Executive Summary

This report summarizes the automated fixes applied to resolve Phase 1 validation issues.

## Statistics

| Metric | Count |
|--------|-------|
| Fixes Applied | {total_fixes_applied} |
| Fixes Failed | {total_fixes_failed} |
| Tests Passed | {total_tests_passed} |
| Tests Failed | {total_tests_failed} |

## Project Fixes

""")

        # Write project fixes
        for result in results:
            if result["fixes_applied"] or result["fixes_failed"]:
                f.write(f"### {result['project'].capitalize()}\\n\\n")
                f.write(f"**Framework:** {result['framework']}\\n\\n")

                if result["fixes_applied"]:
                    f.write("**Fixes Applied:**\\n")
                    for fix in result["fixes_applied"]:
                        f.write(f"- ✓ {fix}\\n")
                    f.write("\\n")

                if result["fixes_failed"]:
                    f.write("**Fixes Failed:**\\n")
                    for fix in result["fixes_failed"]:
                        f.write(f"- ✗ {fix}\\n")
                    f.write("\\n")

                if result["tests_passed"]:
                    f.write("**Tests Passed:**\\n")
                    for test in result["tests_passed"]:
                        f.write(f"- ✓ {test}\\n")
                    f.write("\\n")

                if result["tests_failed"]:
                    f.write("**Tests Failed:**\\n")
                    for test in result["tests_failed"]:
                        f.write(f"- ✗ {test}\\n")
                    f.write("\\n")

        f.write(f"""
## Next Steps

1. **Review Failed Fixes**: Check and manually resolve any failed fixes
2. **Run Validation Again**: Execute Phase 1 validation to verify all issues are resolved
3. **Test Services**: Start each backend service and verify they work correctly
4. **Update Documentation**: Update project documentation with new entry points

---

*Generated by AI SDK Phase 2 Automation*
*Timestamp: {TIMESTAMP}*
""")

    return total_fixes_applied, total_fixes_failed

def main():
    """Main fix workflow"""
    print_header()

    # Create results directory
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # Load validation results
    print("Loading validation results from Phase 1...")
    issues_by_project = load_validation_results()

    if not issues_by_project:
        print(f"{Colors.YELLOW}No validation results found. Please run Phase 1 validation first.{Colors.NC}")
        return 1

    print(f"{Colors.GREEN}✓ Loaded validation results for {len(issues_by_project)} projects{Colors.NC}")
    print()

    # Process all projects
    print("Starting automated fixes...")
    print()

    results = []
    for project_dir, project_info in PROJECTS.items():
        project_name = project_info["name"]
        issues = issues_by_project.get(project_name, [])

        if issues:
            result = fix_project(project_dir, project_info, issues)
            results.append(result)
        else:
            print(f"{Colors.GREEN}Skipping {project_name}: No issues found{Colors.NC}")
            results.append({
                "project": project_name,
                "directory": project_dir,
                "framework": project_info["framework"],
                "backend_type": project_info["backend_type"],
                "fixes_applied": [],
                "fixes_failed": [],
                "tests_passed": [],
                "tests_failed": []
            })
        print()

    print()
    print(f"{Colors.GREEN}{'='*40}{Colors.NC}")
    print(f"{Colors.GREEN}Fix Complete!{Colors.NC}")
    print(f"{Colors.GREEN}{'='*40}{Colors.NC}")
    print()

    # Generate fix report
    print("Generating fix report...")
    report_file = os.path.join(BASE_DIR, "docs", f"fix-results-{datetime.datetime.now().strftime('%Y-%m-%d')}.md")
    applied, failed = generate_fix_report(results, report_file)

    print(f"{Colors.GREEN}✓ Fix report generated: {report_file}{Colors.NC}")
    print()

    # Display summary
    print("=== FIX SUMMARY ===")
    print(f"Total Projects: {len(results)}")
    print(f"Fixes Applied: {applied}")
    print(f"Fixes Failed: {failed}")
    print()
    print(f"Full report available at: {report_file}")
    print()

    if failed > 0:
        print(f"{Colors.YELLOW}⚠ Some fixes failed. Please review the report for details.{Colors.NC}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
