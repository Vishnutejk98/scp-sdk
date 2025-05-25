"""
Reporting and notification system.
"""

class AuditReporter:
    @staticmethod
    def report(policy_name: str, message: str):
        # For simplicity, just print or could be extended to send alerts
        print(f"[Audit] Policy: {policy_name} - {message}")
