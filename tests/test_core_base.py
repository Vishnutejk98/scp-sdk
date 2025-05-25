import pytest
from scp_sdk.core.base import BasePolicy


def test_base_policy_abstract():
    with pytest.raises(TypeError):
        BasePolicy()  # Cannot instantiate abstract class

    class DummyPolicy(BasePolicy):
        def enforce(self, context):
            return {"status": "allow"}

    policy = DummyPolicy()
    assert policy.enabled is True
