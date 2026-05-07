# AI-SDK-ECOSYSTEM

Unified control plane for Kazi's AI SDK adapter fleet.

## What this ecosystem implements

The ecosystem turns a mission into a routed execution plan, then delegates that mission to the right adapter: OpenAI Agents, Vercel AI SDK, LangGraph, LangChain, LlamaIndex, Haystack, CrewAI, AutoGen, Semantic Kernel, and Anthropic.

## Adapter fleet

| Repository | SDK | Primary skills |
| --- | --- | --- |
| AI-SDK-ANTHROPIC | Anthropic | Claude API operations, policy design |
| AI-SDK-AUTOGEN | AutoGen | multi-agent conversation design, handoff protocols |
| AI-SDK-CREWAI | CrewAI | role design, task decomposition |
| AI-SDK-HAYSTACK | Haystack | retrieval pipelines, document stores |
| AI-SDK-LAMA-INDEX | LlamaIndex | RAG ingestion, index design |
| AI-SDK-LANGCHAIN | LangChain | chain composition, tool calling |
| AI-SDK-LANGGRAPH | LangGraph | state machines, durable execution |
| AI-SDK-OPENAI | OpenAI Agents | OpenAI Agents SDK, tool calling |
| AI-SDK-SEMANTIC-KERNEL | Semantic Kernel | plugin architecture, enterprise copilots |
| AI-SDK-VERCEL-AI | Vercel AI SDK | edge-native streaming, TypeScript agent UX |

## Shared skill architecture

- ZEUS: orchestration and lifecycle governance
- ATLAS: full-stack implementation
- SENTINEL: security and compliance
- FORGE: deployment and operations
- NEXUS: AI, RAG, and evaluation
- PIXEL: UX and accessibility
- PULSE: product and launch strategy
- TITAN: testing and verification
- HERMES: automation and integrations
- ORACLE: research and strategy

## Run the fleet

```bash
python3 ecosystem_runner.py --mission "build secure AI workflow and deploy"
```

Run one adapter:

```bash
python3 ecosystem_runner.py --framework langgraph --mission "add durable workflow and evals"
```

## Test

```bash
python3 -m pytest
```

## Portfolio story

This repo is the control-plane layer that shows the full AI engineering range: SDK fluency, architecture, orchestration, safety, testing, deployment planning, and product positioning.
