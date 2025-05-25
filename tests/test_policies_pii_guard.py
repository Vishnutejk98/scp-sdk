import pytest
from scp_sdk.policies.pii_guard import PIIGuardPolicy
from scp_sdk.core.context import EvaluationContext


def test_pii_detect_blocks_ssn():
    p = PIIGuardPolicy()
    ctx = EvaluationContext("My SSN is 123-45-6789")
    result = p.enforce(ctx)
    assert result["status"] == "block"


def test_pii_allows_clean_text():
    p = PIIGuardPolicy()
    ctx = EvaluationContext("Hello world!")
    result = p.enforce(ctx)
    assert result["status"] == "allow"


def test_pii_disabled_allows_any():
    p = PIIGuardPolicy({"enabled": False})
    ctx = EvaluationContext("My SSN is 123-45-6789")
    result = p.enforce(ctx)
    assert result["status"] == "allow"
