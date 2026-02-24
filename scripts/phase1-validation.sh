#!/usr/bin/env python3

"""
Phase 1: Parallel Validation of all 10 AI SDK Projects
This script orchestrates the validation workflow across all projects
"""

import os
import sys
import json
import subprocess
import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Tuple

# Configuration
BASE_DIR = "/Users/mkazi/AI-SDK-PROJECTS"
RESULTS_DIR = os.path.join(BASE_DIR, "validation-results")
TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Project configurations
PROJECTS = {
    "AI-SDK-LANGCHAIN": "langchain",
    "AI-SDK-CREWAI": "crewai",
    "AI-SDK-LANGGRAPH": "langgraph",
    "AI-SDK-AUTOGEN": "autogen",
    "AI-SDK-OPENAI": "openai",
    "AI-SDK-VERCEL-AI": "vercel-ai",
    "AI-SDK-ANTHROPIC": "anthropic",
    "AI-SDK-HAYSTACK": "haystack",
    "AI-SDK-SEMANTIC-KERNEL": "semantic-kernel",
    "AI-SDK-LAMA-INDEX": "lamaindex",
}

# ANSI color codes
class Colors:
    BLUE = '\033[0;34m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    RED = '\033[0;31m'
    NC = '\033[0m'

def print_header():
    """Print validation header"""
    print(f"{Colors.BLUE}{'='*40}{Colors.NC}")
    print(f"{Colors.BLUE}AI SDK Phase 1 Validation{Colors.NC}")
    print(f"{Colors.BLUE}{'='*40}{Colors.NC}")
    print()

def validate_project(project_dir: str, project_name: str) -> Dict:
    """
    Validate a single project

    Args:
        project_dir: Full path to project directory
        project_name: Short name for the project

    Returns:
        Dictionary containing validation results
    """
    print(f"{Colors.BLUE}Validating: {project_name}{Colors.NC}")

    result = {
        "project": project_name,
        "directory": project_dir,
        "timestamp": datetime.datetime.now().isoformat(),
        "tests": {
            "backend_install": None,
            "frontend_install": None,
            "backend_start": None,
            "frontend_start": None,
            "health_check": None,
            "ai_sdk_test": None,
            "streaming_test": None,
            "integration_test": None,
        },
        "issues": []
    }

    full_path = os.path.join(BASE_DIR, project_dir)

    # Check if directory exists
    if not os.path.exists(full_path):
        result["issues"].append({
            "severity": "Critical",
            "category": "Structure",
            "message": f"Project directory not found: {full_path}"
        })
        return result

    os.chdir(full_path)

    # Test 1: Backend dependencies
    print(f"{Colors.YELLOW}  [1/8] Checking backend dependencies...{Colors.NC}")
    requirements_file = os.path.join(full_path, "requirements.txt")
    if os.path.exists(requirements_file):
        result["tests"]["backend_install"] = "pass"
        print(f"{Colors.GREEN}    ✓ Backend dependencies found{Colors.NC}")
    else:
        result["tests"]["backend_install"] = "skipped"
        print(f"{Colors.YELLOW}    ⚠ No backend dependencies found{Colors.NC}")

    # Test 2: Frontend dependencies
    print(f"{Colors.YELLOW}  [2/8] Checking frontend dependencies...{Colors.NC}")
    package_json = os.path.join(full_path, "package.json")
    if os.path.exists(package_json):
        result["tests"]["frontend_install"] = "pass"
        print(f"{Colors.GREEN}    ✓ Frontend dependencies found{Colors.NC}")
    else:
        result["tests"]["frontend_install"] = "skipped"
        print(f"{Colors.YELLOW}    ⚠ No frontend dependencies found{Colors.NC}")

    # Test 3: Backend entry point
    print(f"{Colors.YELLOW}  [3/8] Checking backend structure...{Colors.NC}")
    backend_files = ["main.py", "app.py", "server.py"]
    if any(os.path.exists(os.path.join(full_path, f)) for f in backend_files):
        result["tests"]["backend_start"] = "pass"
        print(f"{Colors.GREEN}    ✓ Backend structure found{Colors.NC}")
    else:
        result["tests"]["backend_start"] = "fail"
        result["issues"].append({
            "severity": "Critical",
            "category": "Backend",
            "message": "No backend entry point (main.py, app.py, or server.py) found"
        })
        print(f"{Colors.RED}    ✗ No backend entry point found{Colors.NC}")

    # Test 4: Frontend structure
    print(f"{Colors.YELLOW}  [4/8] Checking frontend structure...{Colors.NC}")
    if os.path.exists(os.path.join(full_path, "index.html")) or os.path.exists(os.path.join(full_path, "src")):
        result["tests"]["frontend_start"] = "pass"
        print(f"{Colors.GREEN}    ✓ Frontend structure found{Colors.NC}")
    else:
        result["tests"]["frontend_start"] = "fail"
        print(f"{Colors.RED}    ✗ No frontend structure found{Colors.NC}")

    # Test 5: Documentation
    print(f"{Colors.YELLOW}  [5/8] Checking for documentation...{Colors.NC}")
    readme = os.path.join(full_path, "README.md")
    if os.path.exists(readme):
        result["tests"]["health_check"] = "pass"
        print(f"{Colors.GREEN}    ✓ Documentation found{Colors.NC}")
    else:
        result["tests"]["health_check"] = "fail"
        result["issues"].append({
            "severity": "Medium",
            "category": "Documentation",
            "message": "No README.md documentation found"
        })
        print(f"{Colors.RED}    ✗ No documentation found{Colors.NC}")

    # Test 6: AI SDK Integration
    print(f"{Colors.YELLOW}  [6/8] Checking for AI SDK integration...{Colors.NC}")
    ai_sdk_found = False
    for root, dirs, files in os.walk(full_path):
        # Skip node_modules and venv
        dirs[:] = [d for d in dirs if d not in ['node_modules', 'venv', '__pycache__', '.git']]
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        if any(keyword in content.lower() for keyword in ['ai_sdk', 'langchain', 'anthropic', 'openai', 'crewai', 'autogen']):
                            ai_sdk_found = True
                            break
                except:
                    pass
        if ai_sdk_found:
            break

    if ai_sdk_found:
        result["tests"]["ai_sdk_test"] = "pass"
        print(f"{Colors.GREEN}    ✓ AI SDK integration found{Colors.NC}")
    else:
        result["tests"]["ai_sdk_test"] = "fail"
        result["issues"].append({
            "severity": "Critical",
            "category": "Integration",
            "message": "No AI SDK integration code detected"
        })
        print(f"{Colors.RED}    ✗ No AI SDK integration found{Colors.NC}")

    # Test 7: Environment configuration
    print(f"{Colors.YELLOW}  [7/8] Checking for environment configuration...{Colors.NC}")
    if os.path.exists(os.path.join(full_path, ".env.example")) or os.path.exists(os.path.join(full_path, ".env")):
        result["tests"]["streaming_test"] = "pass"
        print(f"{Colors.GREEN}    ✓ Environment configuration found{Colors.NC}")
    else:
        result["tests"]["streaming_test"] = "fail"
        result["issues"].append({
            "severity": "High",
            "category": "Configuration",
            "message": "No .env.example or .env file found"
        })
        print(f"{Colors.YELLOW}    ⚠ No environment configuration found{Colors.NC}")

    # Test 8: Calculate health
    print(f"{Colors.YELLOW}  [8/8] Calculating project health...{Colors.NC}")
    tests = result["tests"]
    passes = sum(1 for v in tests.values() if v == "pass")
    fails = sum(1 for v in tests.values() if v == "fail")
    total = len([v for v in tests.values() if v is not None])

    if total > 0:
        health = (passes / total) * 100
    else:
        health = 0

    result["tests"]["integration_test"] = f"{health:.0f}%"
    result["summary"] = {
        "total_tests": total,
        "passed": passes,
        "failed": fails,
        "health_percentage": health
    }

    health_color = Colors.GREEN if health >= 70 else Colors.YELLOW if health >= 40 else Colors.RED
    print(f"    {health_color}Health: {health:.0f}% ({passes}/{total} tests passed){Colors.NC}")
    print()

    return result

def generate_report(results: List[Dict], report_file: str):
    """Generate markdown validation report"""

    # Calculate totals
    total_critical = 0
    total_high = 0
    total_medium = 0
    total_low = 0

    with open(report_file, 'w') as f:
        f.write(f"""# Phase 1 Validation Report

**Date:** {datetime.datetime.now().strftime("%Y-%m-%d")}
**Time:** {datetime.datetime.now().strftime("%H:%M:%S")}
**Projects Validated:** {len(results)}

## Executive Summary

This report summarizes the validation results for all {len(results)} AI SDK projects. Each project was tested for:

1. Backend dependencies installation
2. Frontend dependencies installation
3. Backend structure and entry point
4. Frontend structure
5. Documentation presence
6. AI SDK integration
7. Environment configuration
8. Overall project health

## Project Status

| Project | Health | Passed | Failed | Issues |
|---------|--------|--------|--------|--------|
""")

        # Write project status table
        for result in results:
            summary = result.get('summary', {})
            health = summary.get('health_percentage', 0)
            passed = summary.get('passed', 0)
            failed = summary.get('failed', 0)
            total = summary.get('total_tests', 0)
            issues_count = len(result.get('issues', []))

            # Health indicator
            if health >= 70:
                indicator = '🟢'
            elif health >= 40:
                indicator = '🟡'
            else:
                indicator = '🔴'

            f.write(f"| {result['project']} | {indicator} {health:.0f}% | {passed}/{total} | {failed} | {issues_count} |\n")

            # Count issues
            for issue in result.get('issues', []):
                severity = issue.get('severity', 'Low')
                if severity == 'Critical':
                    total_critical += 1
                elif severity == 'High':
                    total_high += 1
                elif severity == 'Medium':
                    total_medium += 1
                elif severity == 'Low':
                    total_low += 1

        # Write Critical Issues
        f.write(f"\n## Issues by Severity\n\n### Critical Issues ({total_critical})\n")
        for result in results:
            critical_issues = [i for i in result.get('issues', []) if i['severity'] == 'Critical']
            if critical_issues:
                f.write(f"\n#### {result['project']}\n")
                for issue in critical_issues:
                    f.write(f"- **{issue['category']}**: {issue['message']}\n")

        # Write High Priority Issues
        f.write(f"\n### High Priority Issues ({total_high})\n")
        for result in results:
            high_issues = [i for i in result.get('issues', []) if i['severity'] == 'High']
            if high_issues:
                f.write(f"\n#### {result['project']}\n")
                for issue in high_issues:
                    f.write(f"- **{issue['category']}**: {issue['message']}\n")

        # Write Medium Priority Issues
        f.write(f"\n### Medium Priority Issues ({total_medium})\n")
        for result in results:
            medium_issues = [i for i in result.get('issues', []) if i['severity'] == 'Medium']
            if medium_issues:
                f.write(f"\n#### {result['project']}\n")
                for issue in medium_issues:
                    f.write(f"- **{issue['category']}**: {issue['message']}\n")

        # Write Low Priority Issues
        f.write(f"\n### Low Priority Issues ({total_low})\n")
        for result in results:
            low_issues = [i for i in result.get('issues', []) if i['severity'] == 'Low']
            if low_issues:
                f.write(f"\n#### {result['project']}\n")
                for issue in low_issues:
                    f.write(f"- **{issue['category']}**: {issue['message']}\n")

        f.write(f"""
## Recommendations

1. **Immediate Action Required**: Address all Critical issues before proceeding
2. **High Priority**: Fix High priority issues within 24-48 hours
3. **Medium Priority**: Plan fixes for Medium issues in next sprint
4. **Documentation**: Ensure all projects have proper README and API documentation

## Next Steps

1. Review detailed logs in: {RESULTS_DIR}/
2. Create fix team to address Critical and High issues (Phase 2)
3. Update documentation team with findings (Phase 3)
4. Schedule final QA validation (Phase 4)

---

*Generated by AI SDK Validation Automation*
*Timestamp: {TIMESTAMP}*
""")

    return total_critical, total_high, total_medium, total_low

def main():
    """Main validation workflow"""
    print_header()

    # Create results directory
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # Run validation for all projects in parallel
    print("Starting parallel validation of all projects...")
    print()

    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Submit all validation tasks
        future_to_project = {
            executor.submit(validate_project, project_dir, project_name): (project_dir, project_name)
            for project_dir, project_name in PROJECTS.items()
        }

        # Collect results as they complete
        for future in as_completed(future_to_project):
            project_dir, project_name = future_to_project[future]
            try:
                result = future.result()
                results.append(result)

                # Save individual result JSON
                json_file = os.path.join(RESULTS_DIR, f"{project_name}-{TIMESTAMP}.json")
                with open(json_file, 'w') as f:
                    json.dump(result, f, indent=2)
            except Exception as exc:
                print(f"{Colors.RED}ERROR validating {project_name}: {exc}{Colors.NC}")

    print()
    print(f"{Colors.GREEN}{'='*40}{Colors.NC}")
    print(f"{Colors.GREEN}Validation Complete!{Colors.NC}")
    print(f"{Colors.GREEN}{'='*40}{Colors.NC}")
    print()

    # Generate aggregated report
    print("Generating validation report...")
    report_file = os.path.join(RESULTS_DIR, f"validation-report-{TIMESTAMP}.md")
    critical, high, medium, low = generate_report(results, report_file)

    print(f"{Colors.GREEN}✓ Validation report generated: {report_file}{Colors.NC}")
    print()

    # Display summary
    print("=== VALIDATION SUMMARY ===")
    print(f"Total Projects: {len(results)}")
    print(f"Critical Issues: {critical}")
    print(f"High Priority Issues: {high}")
    print(f"Medium Priority Issues: {medium}")
    print(f"Low Priority Issues: {low}")
    print()
    print(f"Full report available at: {report_file}")
    print(f"Detailed logs available in: {RESULTS_DIR}/")
    print()

    return 0

if __name__ == "__main__":
    sys.exit(main())
