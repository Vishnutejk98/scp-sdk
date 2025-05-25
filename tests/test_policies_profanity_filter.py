from scp_sdk.policies.profanity_filter import ProfanityFilterPolicy
from scp_sdk.core.context import EvaluationContext

def test_profanity_allows_clean():
    p = ProfanityFilterPolicy(config={"enabled": True})
    ctx = EvaluationContext("Hello world")
    result = p.enforce(ctx)
    assert result["status"] == "allow"

def test_profanity_custom_blocked_words():
    p = ProfanityFilterPolicy(config={"enabled": True, "blocked_words": ["foo", "bar"]})
    ctx = EvaluationContext("foo is bad")
    result = p.enforce(ctx)
    assert result["status"] == "block"
