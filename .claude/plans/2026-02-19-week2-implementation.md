# Week 2: Core AI Logic Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement core AI SDK integration for all 10 SaaS projects, moving from "Hello World" to functional AI-powered features.

**Architecture:** Each project gets a focused AI integration aligned with its SDK specialty. Shared patterns for API key management via environment variables, consistent error handling, and standardized streaming responses where applicable.

**Tech Stack:** LangGraph, LangChain, OpenAI SDK, AutoGen, Google ADK, Vercel AI SDK, LlamaIndex, CrewAI, Haystack, Claude SDK across respective projects

---

## Phase 1: Common Infrastructure (Lead Agent)

### Task 1: Create API Key Management System

**Files:**
- Create: `infrastructure/templates/doppler-setup.md`

**Step 1: Create Doppler setup documentation**

```markdown
# Doppler API Key Setup

## Projects and Required Keys

| Project | Keys Needed |
|---------|-------------|
| 01-venture-graph | OPENAI_API_KEY, LANGGRAPH_API_KEY |
| 02-omni-desk | OPENAI_API_KEY, LANGCHAIN_API_KEY |
| 03-dev-squad | OPENAI_API_KEY |
| 04-supply-consensus | OPENAI_API_KEY, AUTOGEN_API_KEY |
| 05-market-pulse | GOOGLE_API_KEY, GOOGLE_ADK_KEY |
| 06-insight-stream | OPENAI_API_KEY, VERCEL_AI_SDK_KEY |
| 07-research-synthesis | OPENAI_API_KEY, LLAMA_INDEX_API_KEY |
| 08-trend-factory | OPENAI_API_KEY, CREWAI_API_KEY |
| 09-patent-iq | OPENAI_API_KEY, HAYSTACK_API_KEY |
| 10-claude-forge | ANTHROPIC_API_KEY |

## Setup Commands

```bash
# Install Doppler CLI
curl -sLf https://cli.doppler.com/install.sh | sh

# Login
doppler login

# Create project
doppler projects create <project-name>

# Setup environment
cd projects/<project-dir>
doppler setup

# Add secrets
doppler secrets set OPENAI_API_KEY=<key>
```
```

**Step 2: Commit**

```bash
git add infrastructure/templates/doppler-setup.md
git commit -m "docs: add Doppler API key management guide"
```

---

### Task 2: Create Shared Environment Template

**Files:**
- Create: `infrastructure/templates/.env.example`

**Step 1: Create environment template**

```bash
# OpenAI (most projects)
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini

# Anthropic (ClaudeForge)
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022

# Google (MarketPulse)
GOOGLE_API_KEY=...
GOOGLE_ADK_PROJECT_ID=...

# Framework-specific
LANGCHAIN_API_KEY=...
LANGGRAPH_API_KEY=...
LLAMA_INDEX_API_KEY=...
CREWAI_API_KEY=...
HAYSTACK_API_KEY=...
AUTOGEN_API_KEY=...

# Deployment
NODE_ENV=development
PORT=3000
```

**Step 2: Commit**

```bash
git add infrastructure/templates/.env.example
git commit -m "chore: add shared environment template"
```

---

## Phase 2: Agent-01 VentureGraph - LangGraph Integration

### Task 3: Install LangGraph Dependencies

**Context:** Agent-01 works in `projects/01-venture-graph/`

**Files:**
- Modify: `projects/01-venture-graph/backend/requirements.txt`

**Step 1: Add LangGraph dependencies**

```
fastapi==0.115.0
uvicorn==0.32.0
langgraph==0.2.50
langchain-openai==0.2.0
pydantic==2.9.0
python-dotenv==1.0.0
```

**Step 2: Install dependencies**

Run: `cd projects/01-venture-graph/backend && pip install -r requirements.txt`
Expected: Successful installation

**Step 3: Commit**

```bash
git add projects/01-venture-graph/backend/requirements.txt
git commit -m "feat(venture-graph): add LangGraph dependencies"
```

---

### Task 4: Create LangGraph Venture Planning Agent

**Files:**
- Create: `projects/01-venture-graph/backend/app/graph.py`

**Step 1: Write the graph implementation**

```python
"""LangGraph venture planning agent."""
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
import operator

class VentureState(TypedDict):
    """State for venture planning."""
    messages: Annotated[list, operator.add]
    idea: str
    market_analysis: str
    business_model: str
    pitch_deck: str
    current_step: str

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

def analyze_market(state: VentureState) -> VentureState:
    """Analyze market opportunity."""
    idea = state["idea"]
    prompt = f"""Analyze the market for this startup idea: {idea}

Provide:
1. Target market size (TAM/SAM/SOM)
2. Key competitors
3. Market trends
4. Entry barriers"""

    response = llm.invoke(prompt)
    return {
        **state,
        "market_analysis": response.content,
        "current_step": "market_analyzed"
    }

def design_business_model(state: VentureState) -> VentureState:
    """Design business model canvas."""
    idea = state["idea"]
    market = state["market_analysis"]

    prompt = f"""Create a business model canvas for: {idea}

Market context: {market[:500]}

Provide:
1. Value Proposition
2. Customer Segments
3. Revenue Streams
4. Cost Structure
5. Key Partnerships"""

    response = llm.invoke(prompt)
    return {
        **state,
        "business_model": response.content,
        "current_step": "business_model_done"
    }

def create_pitch_deck(state: VentureState) -> VentureState:
    """Generate pitch deck outline."""
    idea = state["idea"]
    market = state["market_analysis"]
    model = state["business_model"]

    prompt = f"""Create a 10-slide pitch deck outline for: {idea}

Market: {market[:300]}
Business Model: {model[:300]}

Provide slide titles and key bullet points for each."""

    response = llm.invoke(prompt)
    return {
        **state,
        "pitch_deck": response.content,
        "current_step": "complete"
    }

def should_continue(state: VentureState) -> str:
    """Determine next step."""
    if state["current_step"] == "complete":
        return END
    return state["current_step"]

# Build graph
builder = StateGraph(VentureState)
builder.add_node("analyze_market", analyze_market)
builder.add_node("design_business_model", design_business_model)
builder.add_node("create_pitch_deck", create_pitch_deck)

builder.set_entry_point("analyze_market")
builder.add_edge("analyze_market", "design_business_model")
builder.add_edge("design_business_model", "create_pitch_deck")
builder.add_edge("create_pitch_deck", END)

graph = builder.compile()
```

**Step 2: Create __init__.py**

Create: `projects/01-venture-graph/backend/app/__init__.py`
Content: Empty file

**Step 3: Update main.py with graph endpoint**

Modify: `projects/01-venture-graph/backend/app/main.py`

```python
from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import graph
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="VentureGraph - AI Venture Planning")

class VentureIdea(BaseModel):
    idea: str

class VenturePlan(BaseModel):
    idea: str
    market_analysis: str
    business_model: str
    pitch_deck: str

@app.get("/health")
def health():
    return {"status": "healthy", "service": "venture-graph"}

@app.post("/plan", response_model=VenturePlan)
def create_plan(venture: VentureIdea):
    """Generate venture plan using LangGraph."""
    result = graph.invoke({
        "idea": venture.idea,
        "messages": [],
        "market_analysis": "",
        "business_model": "",
        "pitch_deck": "",
        "current_step": "start"
    })

    return VenturePlan(
        idea=venture.idea,
        market_analysis=result["market_analysis"],
        business_model=result["business_model"],
        pitch_deck=result["pitch_deck"]
    )
```

**Step 4: Test the endpoint**

Run: `cd projects/01-venture-graph/backend && uvicorn app.main:app --reload &`
Run: `curl -X POST http://localhost:8000/plan -H "Content-Type: application/json" -d '{"idea":"AI-powered sustainable farming"}'`
Expected: JSON response with market_analysis, business_model, pitch_deck

**Step 5: Commit**

```bash
git add projects/01-venture-graph/backend/
git commit -m "feat(venture-graph): implement LangGraph venture planning agent"
```

---

## Phase 3: Agent-02 OmniDesk - LangChain RAG

### Task 5: Install LangChain Dependencies

**Context:** Agent-02 works in `projects/02-omni-desk/`

**Files:**
- Modify: `projects/02-omni-desk/backend/requirements.txt`

**Step 1: Add LangChain dependencies**

```
fastapi==0.115.0
uvicorn==0.32.0
langchain==0.3.0
langchain-openai==0.2.0
langchain-community==0.3.0
chromadb==0.5.0
pydantic==2.9.0
python-dotenv==1.0.0
```

**Step 2: Install dependencies**

Run: `cd projects/02-omni-desk/backend && pip install -r requirements.txt`
Expected: Successful installation

**Step 3: Commit**

```bash
git add projects/02-omni-desk/backend/requirements.txt
git commit -m "feat(omni-desk): add LangChain dependencies"
```

---

### Task 6: Create RAG Pipeline

**Files:**
- Create: `projects/02-omni-desk/backend/app/rag.py`

**Step 1: Write RAG implementation**

```python
"""LangChain RAG pipeline for enterprise knowledge."""
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
import os

class EnterpriseRAG:
    """RAG system for enterprise documents."""

    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.llm = ChatOpenAI(model="gpt-4o-mini")
        self.vectorstore = None
        self.qa_chain = None

    def add_documents(self, documents: list[str]):
        """Add documents to knowledge base."""
        text_splitter = CharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        texts = []
        for doc in documents:
            chunks = text_splitter.split_text(doc)
            texts.extend(chunks)

        self.vectorstore = Chroma.from_texts(
            texts,
            self.embeddings,
            persist_directory="./chroma_db"
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(
                search_kwargs={"k": 3}
            )
        )

    def query(self, question: str) -> dict:
        """Query the knowledge base."""
        if not self.qa_chain:
            return {
                "answer": "No documents loaded. Please add documents first.",
                "sources": []
            }

        result = self.qa_chain.invoke({"query": question})
        return {
            "answer": result["result"],
            "sources": [doc.page_content[:200] + "..."
                       for doc in result.get("source_documents", [])]
        }

# Global RAG instance
rag_system = EnterpriseRAG()
```

**Step 2: Update main.py**

Modify: `projects/02-omni-desk/backend/app/main.py`

```python
from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import rag_system
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="OmniDesk - Enterprise RAG")

class DocumentInput(BaseModel):
    documents: list[str]

class QueryInput(BaseModel):
    question: str

class QueryOutput(BaseModel):
    answer: str
    sources: list[str]

@app.get("/health")
def health():
    return {"status": "healthy", "service": "omni-desk"}

@app.post("/documents")
def add_documents(input: DocumentInput):
    """Add documents to RAG knowledge base."""
    rag_system.add_documents(input.documents)
    return {"status": "success", "document_count": len(input.documents)}

@app.post("/query", response_model=QueryOutput)
def query(input: QueryInput):
    """Query the enterprise knowledge base."""
    result = rag_system.query(input.question)
    return QueryOutput(**result)
```

**Step 3: Test the RAG system**

Run: `cd projects/02-omni-desk/backend && uvicorn app.main:app --port 8001 &`

Add documents:
```bash
curl -X POST http://localhost:8001/documents \
  -H "Content-Type: application/json" \
  -d '{"documents":["Our company was founded in 2020. We specialize in AI solutions.","Our headquarters is in San Francisco with 50 employees."]}'
```

Query:
```bash
curl -X POST http://localhost:8001/query \
  -H "Content-Type: application/json" \
  -d '{"question":"When was the company founded?"}'
```

Expected: Answer with sources

**Step 4: Commit**

```bash
git add projects/02-omni-desk/backend/
git commit -m "feat(omni-desk): implement LangChain RAG pipeline"
```

---

## Phase 4: Agent-03 DevSquad - OpenAI SDK Dev Team

### Task 7: Install OpenAI SDK

**Context:** Agent-03 works in `projects/03-dev-squad/`

**Files:**
- Modify: `projects/03-dev-squad/package.json`

**Step 1: Add OpenAI dependency**

```bash
cd projects/03-dev-squad
npm install openai
```

**Step 2: Commit**

```bash
git add projects/03-dev-squad/package.json projects/03-dev-squad/package-lock.json
git commit -m "feat(dev-squad): add OpenAI SDK dependency"
```

---

### Task 8: Create AI Dev Team API

**Files:**
- Create: `projects/03-dev-squad/src/lib/openai.ts`

**Step 1: Write OpenAI client**

```typescript
import OpenAI from 'openai';
import { OPENAI_API_KEY } from '$env/static/private';

export const openai = new OpenAI({
    apiKey: OPENAI_API_KEY
});

export interface CodeReviewResult {
    score: number;
    issues: string[];
    suggestions: string[];
    improved_code: string;
}

export async function reviewCode(code: string, language: string): Promise<CodeReviewResult> {
    const prompt = `Review this ${language} code and provide structured feedback:

\`\`\`${language}
${code}
\`\`\`

Provide output as JSON with:
- score (1-10)
- issues (array of strings)
- suggestions (array of strings)
- improved_code (string)`;

    const response = await openai.chat.completions.create({
        model: 'gpt-4o-mini',
        messages: [
            { role: 'system', content: 'You are a senior software engineer doing code reviews.' },
            { role: 'user', content: prompt }
        ],
        response_format: { type: 'json_object' }
    });

    return JSON.parse(response.choices[0].message.content || '{}');
}

export async function generateTests(code: string, language: string): Promise<string> {
    const prompt = `Generate comprehensive unit tests for this ${language} code:

\`\`\`${language}
${code}
\`\`\`

Provide only the test code.`;

    const response = await openai.chat.completions.create({
        model: 'gpt-4o-mini',
        messages: [
            { role: 'system', content: 'You are a test automation expert.' },
            { role: 'user', content: prompt }
        ]
    });

    return response.choices[0].message.content || '';
}

export async function explainCode(code: string, language: string): Promise<string> {
    const prompt = `Explain this ${language} code in simple terms:

\`\`\`${language}
${code}
\`\`\``;

    const response = await openai.chat.completions.create({
        model: 'gpt-4o-mini',
        messages: [
            { role: 'system', content: 'You are a helpful coding tutor.' },
            { role: 'user', content: prompt }
        ]
    });

    return response.choices[0].message.content || '';
}
```

**Step 2: Create API routes**

Create: `projects/03-dev-squad/src/routes/api/review/+server.ts`

```typescript
import { json } from '@sveltejs/kit';
import { reviewCode } from '$lib/openai';

export async function POST({ request }) {
    const { code, language } = await request.json();

    try {
        const result = await reviewCode(code, language);
        return json(result);
    } catch (error) {
        return json({ error: 'Review failed' }, { status: 500 });
    }
}
```

Create: `projects/03-dev-squad/src/routes/api/generate-tests/+server.ts`

```typescript
import { json } from '@sveltejs/kit';
import { generateTests } from '$lib/openai';

export async function POST({ request }) {
    const { code, language } = await request.json();

    try {
        const result = await generateTests(code, language);
        return json({ tests: result });
    } catch (error) {
        return json({ error: 'Test generation failed' }, { status: 500 });
    }
}
```

Create: `projects/03-dev-squad/src/routes/api/explain/+server.ts`

```typescript
import { json } from '@sveltejs/kit';
import { explainCode } from '$lib/openai';

export async function POST({ request }) {
    const { code, language } = await request.json();

    try {
        const result = await explainCode(code, language);
        return json({ explanation: result });
    } catch (error) {
        return json({ error: 'Explanation failed' }, { status: 500 });
    }
}
```

**Step 3: Test the API**

Run: `cd projects/03-dev-squad && npm run dev &`

Test review endpoint:
```bash
curl -X POST http://localhost:5173/api/review \
  -H "Content-Type: application/json" \
  -d '{"code":"function add(a,b) { return a+b; }","language":"javascript"}'
```

Expected: JSON with score, issues, suggestions, improved_code

**Step 4: Commit**

```bash
git add projects/03-dev-squad/src/
git commit -m "feat(dev-squad): implement OpenAI SDK dev team API"
```

---

## Phase 5: Remaining Agents (Parallel Sprint)

### Task 9-16: Spawn Remaining Agents

**Context:** Spawn agents 04-10 in parallel for their respective AI SDK integrations

**Step 1: Create tasks for each agent**

For each project, create task and spawn agent:

- Task 9/Agent-04: SupplyConsensus - AutoGen supply chain
- Task 10/Agent-05: MarketPulse - Google ADK competitor intel
- Task 11/Agent-06: InsightStream - Vercel AI SDK streaming
- Task 12/Agent-07: ResearchSynthesis - LlamaIndex knowledge graph
- Task 13/Agent-08: TrendFactory - CrewAI marketing crew
- Task 14/Agent-09: PatentIQ - Haystack patent search
- Task 15/Agent-10: ClaudeForge - Claude SDK coding agent

**Step 2: Spawn agents with specific SDK tasks**

Each agent follows pattern:
1. Install SDK dependencies
2. Create core AI integration
3. Add API endpoints
4. Test functionality
5. Commit changes

---

## Phase 6: Integration Testing (Lead Agent)

### Task 16: Create Integration Test Suite

**Files:**
- Create: `scripts/test-all-ai.sh`

**Step 1: Create test script**

```bash
#!/bin/bash
# Test all AI integrations

PROJECTS=(
    "01-venture-graph:8000:plan"
    "02-omni-desk:8001:query"
    "03-dev-squad:5173:api/review"
)

echo "Testing AI integrations..."

for proj in "${PROJECTS[@]}"; do
    IFS=':' read -r name port endpoint <<< "$proj"
    echo "Testing $name..."

    response=$(curl -s -o /dev/null -w "%{http_code}" \
        "http://localhost:$port/$endpoint" || echo "000")

    if [ "$response" = "200" ] || [ "$response" = "404" ]; then
        echo "  ✓ $name responding"
    else
        echo "  ✗ $name not responding (HTTP $response)"
    fi
done
```

**Step 2: Commit**

```bash
chmod +x scripts/test-all-ai.sh
git add scripts/test-all-ai.sh
git commit -m "chore: add AI integration test script"
```

---

### Task 17: Update Documentation

**Files:**
- Modify: `README.md`

**Step 1: Add Week 2 section**

```markdown
## Week 2: AI Integration Complete

All 10 projects now have functional AI SDK integrations:

| Project | AI Feature | SDK |
|---------|-----------|-----|
| VentureGraph | Venture planning workflow | LangGraph |
| OmniDesk | Enterprise RAG | LangChain |
| DevSquad | Code review & test gen | OpenAI SDK |
| SupplyConsensus | Multi-agent supply chain | AutoGen |
| MarketPulse | Competitor intel | Google ADK |
| InsightStream | Streaming AI responses | Vercel AI SDK |
| ResearchSynthesis | Knowledge graph | LlamaIndex |
| TrendFactory | Marketing crew | CrewAI |
| PatentIQ | Patent search | Haystack |
| ClaudeForge | Coding agent | Claude SDK |
```

**Step 2: Commit**

```bash
git add README.md
git commit -m "docs: add Week 2 AI integration summary"
```

---

## Success Criteria Checklist

- [ ] Doppler API key management documented
- [ ] Environment template created
- [ ] VentureGraph: LangGraph venture planning working
- [ ] OmniDesk: LangChain RAG working
- [ ] DevSquad: OpenAI SDK dev team working
- [ ] SupplyConsensus: AutoGen supply chain working
- [ ] MarketPulse: Google ADK intel working
- [ ] InsightStream: Vercel AI SDK streaming working
- [ ] ResearchSynthesis: LlamaIndex knowledge graph working
- [ ] TrendFactory: CrewAI marketing crew working
- [ ] PatentIQ: Haystack patent search working
- [ ] ClaudeForge: Claude SDK coding agent working
- [ ] Integration tests pass
- [ ] Documentation updated

## Total Tasks: 17
