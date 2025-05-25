
# 🚦 Safe Context Protocol (SCP SDK)

A **pluggable governance and policy enforcement layer** for multi-agent systems, LLM workflows, LangGraph pipelines, and API integrations.

> Ensure trust, compliance, and safety by wrapping your systems with configurable policy checks like **PII detection**, **profanity filtering**, **custom redlines**, and **time-based rules**.

---

## 🔍 What Is SCP SDK?

SCP (Safe Context Protocol) SDK is a **governance enforcement framework** that:

- Intercepts and inspects data flow in **agentic systems**, **LangGraph nodes**, or **toolkits**.
- Applies a chain of **configurable and composable policies**.
- Can enforce **regulatory contracts** like HIPAA or GDPR.
- Provides a **standardized context object** and runtime for evaluation.
- Is designed to plug into existing AI and automation pipelines (MCP, ACP, LangGraph, FastAPI, etc.)

---

## ✨ Existing Functionalities

- ✅ **PII Detection**: Blocks sensitive information like phone numbers, emails, etc.
- 💬 **Profanity Filtering**: Detects and blocks predefined or custom profane words.
- 📛 **Redline Rules**: Blocks disallowed terms or internal phrases.
- ⏰ **Time Windows**: Ensures operations happen only during allowed hours.
- 🔓 **Allow-All Policy**: For testing or fallback scenarios.
- 🔧 **Custom YAML Configuration**: Define and activate policies declaratively.
- 🔁 **Composable Runtime**: Chain and enforce multiple policies in order.
- 📜 **Policy Contracts & Compliance Profiles**: Support profiles like HIPAA, GDPR.
- 📚 **Audit Logging**: In-memory audit logs with reason and timestamps.
- ⚙️ **Plugin-Ready SDK**: Works with LangGraph, LangChain, or API middleware.

---

## 🛠️ Installation

```bash
pip install git+https://github.com/your-org/scp-sdk.git
```

---

## 📁 Config Example (YAML)

```yaml
policies:
  pii_guard:
    enabled: true
  profanity_filter:
    enabled: true
    blocked_words:
      - damn
      - hell
  redline_blocker:
    enabled: true
    rules:
      - confidential
      - internal use only
  time_window:
    enabled: true
    allowed_hours: [9, 10, 11, 12, 13, 14, 15, 16, 17]

profiles:
  hipaa:
    - pii_guard
    - time_window
```

---

## 🧪 Quick Start Example

### Step 1: Load and Apply Policies

```python
from scp_sdk.core.runtime import SCPRuntime
from scp_sdk.core.context import EvaluationContext
from scp_sdk.config import load_config_from_yaml

# Load policy configuration
config = load_config_from_yaml("config/policy_config.yaml")

# Create runtime engine with loaded policies
runtime = SCPRuntime(config)

# Evaluate data
context = EvaluationContext("Send me your SSN at user@example.com")
result = runtime.evaluate(context)

print(result)  # {'status': 'block', 'reason': 'PII detected in content'}
```

### Step 2: Wrap Functions with SCP

```python
@runtime.wrap
def my_handler(data):
    return {"response": f"Processed: {data}"}

result = my_handler("My number is 123-45-6789")
print(result)  # Will raise a policy violation
```

---

## 🤝 Contributing

We welcome contributors from the community to enhance the SDK.

### Ways You Can Contribute

- Add new policy types (e.g. **toxicity**, **bias detection**, **custom classifier**)
- Improve config schema validation
- Add support for distributed auditing or DB-backed audit store
- Enhance logging and visualization tools
- Write more test cases for edge coverage

### Start Here

1. Fork the repo
2. Clone locally and install dependencies
3. Make your changes and write tests
4. Submit a pull request!

We appreciate your input—every contribution helps secure the future of safe agentic and AI systems.

---

## 📜 License

MIT License – Use freely with attribution.
