"""
Wrapper class to integrate SCP governance with any callable (node, graph, tool, agent).
"""

from scp_sdk.core.runtime import GovernanceCore


class BasePluginWrapper:
    def __init__(self, governance_core: GovernanceCore, func=None):
        """
        Args:
            governance_core: GovernanceCore instance managing policies.
            func: Callable or object with .evaluate method.
        """
        self.governance_core = governance_core
        self.func = func

    def __call__(self, *args, **kwargs):
        # Extract input text
        data = args[0] if args else kwargs.get("data", "")
        # Enforce governance before call
        self.governance_core.enforce(data)

        if not self.func:
            return {"status": "allow"}

        # Call wrapped function or .evaluate method
        if hasattr(self.func, "evaluate"):
            output = self.func.evaluate(*args, **kwargs)
        else:
            output = self.func(*args, **kwargs)

        # Enforce governance on output if string
        if isinstance(output, str):
            self.governance_core.enforce(output)

        return output
