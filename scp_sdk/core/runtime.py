"""
GovernanceCore runtime engine managing policies and enforcement.
"""

from typing import List, Optional, Union, Any
from .base import BasePolicy
from .context import EvaluationContext
from .exceptions import PolicyViolationError, ConfigurationError


class GovernanceCore:
    """
    Core runtime managing policies and enforcing them on inputs and outputs.
    """

    def __init__(self, policies: Optional[List[BasePolicy]] = None):
        self.policies: List[BasePolicy] = policies or []

    def add_policy(self, policy: BasePolicy) -> None:
        """Add a new policy instance."""
        self.policies.append(policy)

    def enforce(self, data: Union[str, Any], metadata: Optional[dict] = None) -> dict:
        """
        Enforce all enabled policies against the input data.

        Args:
            data: input data (usually string)
            metadata: optional additional context

        Returns:
            dict with enforcement results, or raises on block
        """
        context = EvaluationContext(data=data, metadata=metadata)

        for policy in self.policies:
            if not getattr(policy, "enabled", True):
                continue

            try:
                result = policy.enforce(context)
            except Exception as exc:
                raise ConfigurationError(
                    f"Policy '{policy.name}' enforcement error: {exc}"
                ) from exc

            status = result.get("status", "").lower()
            if status == "block":
                raise PolicyViolationError(result.get("message", "Policy violation detected."))

            if status not in {"allow", "flag"}:
                raise ConfigurationError(
                    f"Invalid policy status '{status}' returned by '{policy.name}'."
                )

            context.set_result(policy.name, result)

        return {"status": "allow"}


class GovernanceInterceptor:
    """
    Interceptor wrapper to enforce governance around any callable.

    Can wrap nodes, tools, or agents.
    """

    def __init__(self, governance_core: GovernanceCore, func=None):
        self.governance_core = governance_core
        self.func = func

    def __call__(self, *args, **kwargs):
        data = args[0] if args else kwargs.get("data", "")
        self.governance_core.enforce(data)

        if not self.func:
            return {"status": "allow"}

        if hasattr(self.func, "evaluate"):
            output = self.func.evaluate(*args, **kwargs)
        else:
            output = self.func(*args, **kwargs)

        if isinstance(output, str):
            self.governance_core.enforce(output)

        return output

    def evaluate(self, *args, **kwargs):
        # Avoid double enforcement by not calling __call__
        data = args[0] if args else kwargs.get("data", "")
        self.governance_core.enforce(data)

        if not self.func:
            return {"status": "allow"}

        if hasattr(self.func, "evaluate"):
            output = self.func.evaluate(*args, **kwargs)
        else:
            output = self.func(*args, **kwargs)

        if isinstance(output, str):
            self.governance_core.enforce(output)

        return output
