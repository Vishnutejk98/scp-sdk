"""
EvaluationContext keeps state and metadata for policy evaluation.
"""

from typing import Any, Dict, Optional


class EvaluationContext:
    def __init__(self, data: Any, metadata: Optional[Dict] = None):
        self.data = data
        self.metadata = metadata or {}
        self.policy_results = {}

    def set_result(self, policy_name: str, result: Dict):
        self.policy_results[policy_name] = result

    def get_result(self, policy_name: str):
        return self.policy_results.get(policy_name)
