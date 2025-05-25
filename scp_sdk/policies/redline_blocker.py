"""
Custom redline or business rule blocking policy.
"""

from scp_sdk.core.base import BasePolicy


class RedlineBlockerPolicy(BasePolicy):
    name = "redline_blocker"
    description = "Blocks content violating configured redline rules."
    rules = ["Custom string matching for redline terms"]

    def __init__(self, config=None):
        super().__init__(config)
        self.rules = self.config.get("rules", [])

    def enforce(self, context):
        if not self.enabled:
            return {"status": "allow"}

        data = (context.data or "").lower()
        for rule in self.rules:
            if rule.lower() in data:
                return {"status": "block", "message": f"Redline rule violation: '{rule}'"}

        return {"status": "allow"}
