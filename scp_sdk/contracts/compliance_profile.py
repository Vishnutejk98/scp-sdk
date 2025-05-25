"""
Compliance profiles bundling multiple policies.
"""

from typing import List


class ComplianceProfile:
    def __init__(self, name: str, policies: List[str]):
        self.name = name
        self.policies = policies

    @staticmethod
    def get_profile(name: str) -> "ComplianceProfile":
        profiles = {
            "HIPAA": ComplianceProfile("HIPAA", ["pii_guard", "time_window"]),
            "GDPR": ComplianceProfile("GDPR", ["pii_guard", "redline_blocker"]),
        }
        return profiles.get(name)
