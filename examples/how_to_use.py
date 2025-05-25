import yaml
from scp_sdk import GovernanceCore, BasePluginWrapper
from scp_sdk.policies import (
    AllowAllPolicy,
    PIIGuardPolicy,
    ProfanityFilterPolicy,
    RedlineBlockerPolicy,
    TimeWindowPolicy,
)

# Load config.yaml
with open("scp_sdk/config.yaml") as f:
    config = yaml.safe_load(f)

# Create policy instances from config
policy_map = {
    "allow_all": AllowAllPolicy,
    "pii_guard": PIIGuardPolicy,
    "profanity_filter": ProfanityFilterPolicy,
    "redline_blocker": RedlineBlockerPolicy,
    "time_window": TimeWindowPolicy,
}

policies = []
for pname, pconfig in config.get("policies", {}).items():
    if pconfig.get("enabled", False):
        cls = policy_map.get(pname)
        if cls:
            policies.append(cls(pconfig))

# Instantiate GovernanceCore
governance_core = GovernanceCore(policies=policies)

# Wrap any function/node/agent
def example_node(data: str):
    return data + " processed"

wrapped_node = BasePluginWrapper(governance_core, example_node)

# Use wrapped node
result = wrapped_node("This message contains confidential info.")

print(result)  # Will raise PolicyViolationError if blocked
