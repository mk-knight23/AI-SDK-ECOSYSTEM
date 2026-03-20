"""Shared Kazi's Agents Army core contracts and routing logic."""

from .execution import MissionPlan, build_mission_plan, render_system_instructions
from .models import AgentSpec, MissionRequest, RoutedMission
from .registry import AGENTS
from .router import route_mission

__all__ = [
    "AgentSpec",
    "MissionRequest",
    "RoutedMission",
    "MissionPlan",
    "build_mission_plan",
    "render_system_instructions",
    "AGENTS",
    "route_mission",
]
