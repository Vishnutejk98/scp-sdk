"""
Custom exceptions for SCP SDK.
"""


class SCPError(Exception):
    """Base SCP exception."""

    pass


class PolicyViolationError(SCPError):
    """Raised on policy violations."""

    pass


class ConfigurationError(SCPError):
    """Raised on configuration or internal errors."""

    pass
