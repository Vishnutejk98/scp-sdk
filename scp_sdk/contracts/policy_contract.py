"""
Base policy contract and schema definitions.
"""

from typing import List, Dict


class PolicyContract:
    """
    Defines the schema and rules for a policy.
    """

    def __init__(self, name: str, description: str, rules: List[str]):
        self.name = name
        self.description = description
        self.rules = rules

    def validate(self, config: Dict) -> bool:
        # Basic validation placeholder
        # Extend with schema validation or DSL parsing
        return isinstance(config, dict)
