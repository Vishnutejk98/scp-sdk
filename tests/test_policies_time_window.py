from scp_sdk.policies.time_window import TimeWindowPolicy
from scp_sdk.core.context import EvaluationContext
import pytest
from unittest.mock import patch


def test_time_window_allows_during_allowed_hours():
    allowed_hours = [9, 10, 11]
    policy = TimeWindowPolicy({"allowed_hours": allowed_hours})

    # Mock datetime to 10am
    with patch("scp_sdk.policies.time_window.datetime") as mock_dt:
        mock_dt.now.return_value.hour = 10
        mock_dt.now.return_value = mock_dt.now.return_value  # needed for mypy
        ctx = EvaluationContext("any data")
        result = policy.enforce(ctx)
        assert result["status"] == "allow"


def test_time_window_blocks_outside_allowed_hours():
    allowed_hours = [9, 10, 11]
    policy = TimeWindowPolicy({"allowed_hours": allowed_hours})

    # Mock datetime to 8am (disallowed)
    with patch("scp_sdk.policies.time_window.datetime") as mock_dt:
        mock_dt.now.return_value.hour = 8
        mock_dt.now.return_value = mock_dt.now.return_value
        ctx = EvaluationContext("any data")
        result = policy.enforce(ctx)
        assert result["status"] == "block"
