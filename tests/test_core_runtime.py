import pytest
from scp_sdk.core.runtime import GovernanceCore
from scp_sdk.core.exceptions import PolicyViolationError, ConfigurationError
from scp_sdk.core.base import BasePolicy
from scp_sdk.core.context import EvaluationContext


class DummyAllowPolicy(BasePolicy):
    name = "dummy_allow"

    def enforce(self, context):
        return {"status": "allow"}


class DummyBlockPolicy(BasePolicy):
    name = "dummy_block"

    def enforce(self, context):
        return {"status": "block", "message": "Blocked by dummy"}


def test_add_policy_and_enforce_allow():
    core = GovernanceCore()
    policy = DummyAllowPolicy()
    core.add_policy(policy)

    result = core.enforce("test data")
    assert result["status"] == "allow"


def test_enforce_block_raises():
    core = GovernanceCore()
    core.add_policy(DummyBlockPolicy())

    with pytest.raises(PolicyViolationError):
        core.enforce("blocked data")


def test_enforce_invalid_status_raises():
    class InvalidPolicy(BasePolicy):
        name = "invalid"

        def enforce(self, context):
            return {"status": "unknown"}

    core = GovernanceCore([InvalidPolicy()])

    with pytest.raises(ConfigurationError):
        core.enforce("data")
