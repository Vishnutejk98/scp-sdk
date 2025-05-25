"""
Permissive policy allowing all data.
Useful for testing or fallback scenarios.
"""

from scp_sdk.core.base import BasePolicy


class AllowAllPolicy(BasePolicy):
    name = "allow_all"
    description = "Permissive policy allowing all data without checks."
    rules = []

    def enforce(self, context):
        # Always allow
        return {"status": "allow"}
