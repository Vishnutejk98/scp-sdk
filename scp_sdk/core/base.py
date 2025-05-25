"""
Base classes for policies and interceptors.
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict


class BasePolicy(ABC):
    """
    Abstract base class for all policies.
    Subclasses must implement `enforce` method.
    """

    name: str = "base_policy"
    description: str = "Base policy class"
    rules: list = []

    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.enabled = self.config.get("enabled", True)

    @abstractmethod
    def enforce(self, context) -> dict:
        """
        Enforce the policy against the evaluation context.
        Returns a dict with at least `status` key: "allow", "block", or "flag".
        """
        pass
