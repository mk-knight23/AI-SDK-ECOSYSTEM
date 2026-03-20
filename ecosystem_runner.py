"""Unified runner across sibling AI-SDK-* repositories."""

from pathlib import Path
import argparse
import subprocess

ROOT = Path(__file__).resolve().parents[1]

FRAMEWORK_RUNNERS = {
    "langchain": ROOT / "AI-SDK-LANGCHAIN" / "runner.py",
    "langgraph": ROOT / "AI-SDK-LANGGRAPH" / "runner.py",
    "llamaindex": ROOT / "AI-SDK-LAMA-INDEX" / "runner.py",
    "openai": ROOT / "AI-SDK-OPENAI" / "runner.py",
    "anthropic": ROOT / "AI-SDK-ANTHROPIC" / "runner.py",
    "autogen": ROOT / "AI-SDK-AUTOGEN" / "runner.py",
    "crewai": ROOT / "AI-SDK-CREWAI" / "runner.py",
    "haystack": ROOT / "AI-SDK-HAYSTACK" / "runner.py",
    "semantic-kernel": ROOT / "AI-SDK-SEMANTIC-KERNEL" / "runner.py",
}


def run_one(framework: str, mission: str) -> int:
    runner = FRAMEWORK_RUNNERS[framework]
    cmd = ["python3", str(runner), "--mission", mission]
    print(f"=== {framework} ===")
    proc = subprocess.run(cmd, check=False)
    return proc.returncode


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--framework", choices=list(FRAMEWORK_RUNNERS))
    parser.add_argument("--mission", default="orchestrate secure build and deployment")
    args = parser.parse_args()

    if args.framework:
        raise SystemExit(run_one(args.framework, args.mission))

    code = 0
    for fw in FRAMEWORK_RUNNERS:
        code |= run_one(fw, args.mission)
    raise SystemExit(code)
