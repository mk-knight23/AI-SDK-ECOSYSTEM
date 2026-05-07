from dataclasses import dataclass
from typing import List

from .models import MissionRequest
from .router import route_mission


@dataclass(frozen=True)
class MissionPlan:
    mission: str
    primary: str
    support: List[str]
    phases: List[str]
    primary_skills: List[str]


def build_mission_plan(request: MissionRequest) -> MissionPlan:
    routed = route_mission(request)
    phases = [
        "Discovery",
        "Design",
        "Implementation",
        "Verification",
        "Deployment",
    ]
    return MissionPlan(
        mission=request.text,
        primary=routed.primary.code,
        support=[a.code for a in routed.support],
        phases=phases,
        primary_skills=routed.primary.required_skills,
    )


def render_system_instructions(plan: MissionPlan) -> str:
    return (
        "You are Kazi's Agents Army runtime. "
        f"Primary agent: {plan.primary}. "
        f"Support agents: {', '.join(plan.support)}. "
        f"Mission: {plan.mission}. "
        f"Skill focus: {', '.join(plan.primary_skills)}. "
        f"Execution phases: {' -> '.join(plan.phases)}. "
        "Always produce evidence-backed outputs and include verification notes."
    )
