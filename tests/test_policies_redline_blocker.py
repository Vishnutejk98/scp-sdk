from scp_sdk.policies.redline_blocker import RedlineBlockerPolicy
from scp_sdk.core.context import EvaluationContext


def test_redline_blocks_custom_rule():
    p = RedlineBlockerPolicy({"rules": ["secret"]})
    ctx = EvaluationContext("This contains secret info")
    result = p.enforce(ctx)
    assert result["status"] == "block"


def test_redline_allows_no_rule_hit():
    p = RedlineBlockerPolicy({"rules": ["secret"]})
    ctx = EvaluationContext("Clean message")
    result = p.enforce(ctx)
    assert result["status"] == "allow"


def test_redline_disabled_allows_any():
    p = RedlineBlockerPolicy({"rules": ["secret"], "enabled": False})
    ctx = EvaluationContext("secret info")
    result = p.enforce(ctx)
    assert result["status"] == "allow"
