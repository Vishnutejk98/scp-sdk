from scp_sdk.core.exceptions import SCPError, PolicyViolationError, ConfigurationError
import pytest

def test_exceptions_inheritance():
    assert issubclass(PolicyViolationError, SCPError)
    assert issubclass(ConfigurationError, SCPError)

    with pytest.raises(PolicyViolationError):
        raise PolicyViolationError("violation")

    with pytest.raises(ConfigurationError):
        raise ConfigurationError("config error")
