"""
PII detection and blocking policy implementation.
"""

import re
from scp_sdk.core.base import BasePolicy

PII_PATTERNS = [
    r"\b\d{3}-\d{2}-\d{4}\b",                          # SSN
    r"\b(?:\d[ -]*?){13,16}\b",                        # Credit card
    r"\b\d{10}\b",                                     # Phone number
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,}"  # Email
]


class PIIGuardPolicy(BasePolicy):
    name = "pii_guard"
    description = "Detects and blocks Personally Identifiable Information (PII)."
    rules = ["SSN detection", "Email detection", "Credit card detection", "Phone number detection"]

    def enforce(self, context):
        if not self.enabled:
            return {"status": "allow"}

        data = context.data or ""
        for pattern in PII_PATTERNS:
            if re.search(pattern, data):
                return {"status": "block", "message": "PII detected in content"}

        return {"status": "allow"}
