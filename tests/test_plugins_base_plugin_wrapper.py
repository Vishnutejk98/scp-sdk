import pytest
from scp_sdk.plugins.base_plugin_wrapper import BasePluginWrapper
from scp_sdk.core.runtime import GovernanceCore
from scp_sdk.policies.allow_all import AllowAllPolicy
from scp_sdk.core.exceptions import PolicyViolationError


def test_wrapper_allows_and_calls_func():
    core = GovernanceCore([AllowAllPolicy()])
    def func(data): return data + " processed"

    wrapper = BasePluginWrapper(core, func)
    output = wrapper("input")
    assert output == "input processed"


def test_wrapper_blocks_policy_violation():
    from scp_sdk.policies.pii_guard import PIIGuardPolicy
    core = GovernanceCore([PIIGuardPolicy()])
    wrapper = BasePluginWrapper(core, lambda x: x)

    with pytest.raises(PolicyViolationError):
        wrapper("My SSN is 123-45-6789")
