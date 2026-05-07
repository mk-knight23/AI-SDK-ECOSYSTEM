from agents_army_core import MissionRequest, build_mission_plan, render_system_instructions


def test_ecosystem_routes_security_mission_to_sentinel():
    plan = build_mission_plan(MissionRequest("secure audit and threat model deployment"))

    assert plan.primary == "SENTINEL"
    assert "application security" in plan.primary_skills


def test_system_instructions_include_skill_focus():
    plan = build_mission_plan(MissionRequest("deploy and monitor the platform"))
    instructions = render_system_instructions(plan)

    assert "Skill focus:" in instructions
    assert "Execution phases:" in instructions
