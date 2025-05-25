from scp_sdk.core.context import EvaluationContext


def test_evaluation_context_set_get():
    ctx = EvaluationContext(data="test", metadata={"user": "u1"})
    assert ctx.data == "test"
    assert ctx.metadata["user"] == "u1"

    ctx.set_result("policy1", {"status": "allow"})
    assert ctx.get_result("policy1") == {"status": "allow"}
    assert ctx.get_result("unknown") is None
