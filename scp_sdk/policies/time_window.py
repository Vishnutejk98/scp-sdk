"""
Time-based policy allowing enforcement only during allowed hours.
"""

from datetime import datetime
from scp_sdk.core.base import BasePolicy


class TimeWindowPolicy(BasePolicy):
    name = "time_window"
    description = "Allows operation only during configured allowed hours."
    rules = ["Allowed hours enforcement"]

    def __init__(self, config=None):
        super().__init__(config)
        self.allowed_hours = self.config.get("allowed_hours", list(range(9, 18)))

    def enforce(self, context):
        if not self.enabled:
            return {"status": "allow"}

        current_hour = datetime.now().hour
        if current_hour not in self.allowed_hours:
            return {
                "status": "block",
                "message": f"Operation attempted at disallowed hour: {current_hour}"
            }

        return {"status": "allow"}
