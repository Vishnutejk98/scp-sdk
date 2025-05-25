from scp_sdk.core.base import BasePolicy
from scp_sdk.core.exceptions import PolicyViolationError

DEFAULT_PROFANITY = {"damn", "hell", "badword1", "badword2"}

class ProfanityFilterPolicy(BasePolicy):
    name = "profanity_filter"
    description = "Detects and blocks profane language."
    rules = ["Basic profanity word blocking"]

    def __init__(self, func=None, config=None):
        super().__init__(config)
        self.func = func
        self.enabled = self.config.get("enabled", True) if self.config else True
        blocked = self.config.get("blocked_words") if self.config else None
        self.blocked_words = set(blocked) if blocked else DEFAULT_PROFANITY

    def enforce(self, context):
        if not self.enabled:
            return {"status": "allow"}

        data = context.data.lower()
        words = data.split()  # split by whitespace

        for word in self.blocked_words:
            if word in words:
                return {"status": "block", "message": f"Profanity detected: '{word}'"}

        return {"status": "allow"}

