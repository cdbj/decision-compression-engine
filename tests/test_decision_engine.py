from decision_engine import generate_decision_brief


def test_generate_decision_brief_strips_whitespace():
    brief = generate_decision_brief(
        goal="  grow revenue  ",
        constraints=["  demand is seasonal  ", "  ", ""],
        bottleneck="  low conversion  ",
    )
    assert brief.goal == "grow revenue"
    assert brief.constraints == ["demand is seasonal"]
    assert brief.bottleneck == "low conversion"


def test_generate_decision_brief_allows_empty_fields():
    brief = generate_decision_brief(goal="", constraints=[], bottleneck="")
    assert brief.goal == ""
    assert brief.constraints == []
    assert brief.bottleneck == ""
