from scp_sdk.policies.allow_all import AllowAllPolicy


def test_allow_all_policy_allows():
    p = AllowAllPolicy()
    result = p.enforce(None)
    assert result["status"] == "allow"
