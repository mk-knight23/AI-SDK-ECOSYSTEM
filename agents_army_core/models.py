from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class AgentSpec:
    code: str
    name: str
    domain: str
    invoke_keywords: List[str]
    objective: str


@dataclass(frozen=True)
class MissionRequest:
    text: str
    strict: bool = False


@dataclass(frozen=True)
class RoutedMission:
    request: MissionRequest
    primary: AgentSpec
    support: List[AgentSpec]
