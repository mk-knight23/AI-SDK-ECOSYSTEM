from .models import MissionRequest, RoutedMission
from .registry import AGENTS


def _score(text: str, keywords: list[str]) -> int:
    s = text.lower()
    return sum(1 for kw in keywords if kw in s)


def route_mission(request: MissionRequest) -> RoutedMission:
    ranked = sorted(AGENTS, key=lambda a: _score(request.text, a.invoke_keywords), reverse=True)
    primary = ranked[0]

    support = []
    for agent in ranked[1:]:
        if _score(request.text, agent.invoke_keywords) > 0:
            support.append(agent)

    if not support:
        # Default support pattern for safer execution.
        support = [a for a in AGENTS if a.code in {"TITAN", "SENTINEL"}]

    return RoutedMission(request=request, primary=primary, support=support)
