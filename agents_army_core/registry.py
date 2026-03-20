from .models import AgentSpec


AGENTS = [
    AgentSpec("ZEUS", "Master Orchestrator", "coordination", ["orchestrate", "plan", "coordinate", "manage project"], "Own lifecycle and quality gates."),
    AgentSpec("ATLAS", "Full-Stack Engineering God", "engineering", ["build", "code", "architect", "refactor", "implement"], "Ship robust software across stacks."),
    AgentSpec("SENTINEL", "Security Guardian", "security", ["secure", "audit", "pentest", "compliance", "threat model"], "Apply fail-closed security posture."),
    AgentSpec("FORGE", "DevOps & Infrastructure Titan", "infra", ["deploy", "infrastructure", "ci/cd", "kubernetes", "monitor", "cloud"], "Automate deployment and operations."),
    AgentSpec("NEXUS", "AI & Data Intelligence", "ai-data", ["ai", "ml", "llm", "rag", "data pipeline", "prompt", "eval"], "Design AI systems and eval loops."),
    AgentSpec("PIXEL", "Design & UX Master", "design", ["design", "ux", "ui", "accessibility", "brand", "design system"], "Ensure human-centered experience."),
    AgentSpec("PULSE", "Product & Growth Engine", "product-growth", ["prd", "roadmap", "growth", "marketing", "seo", "pricing", "launch"], "Drive product and growth outcomes."),
    AgentSpec("TITAN", "Testing & QA", "quality", ["test", "tdd", "e2e", "performance test", "quality gate", "verification"], "Provide evidence-based verification."),
    AgentSpec("HERMES", "Automation & Integrations", "automation", ["automate", "integrate", "bot", "workflow", "mcp", "webhook"], "Connect systems and automate flows."),
    AgentSpec("ORACLE", "Research & Strategy", "research", ["research", "analyze", "competitive", "market", "strategy", "financial model"], "Deliver evidence-backed strategy."),
]
