import logging
from scp_sdk.audit.logger import AuditLogger, logger


def test_audit_logger_logs(caplog):
    caplog.set_level(logging.INFO)
    AuditLogger.log("Test message")
    assert "Test message" in caplog.text

    AuditLogger.log("Warning message", level="warning")
    assert "Warning message" in caplog.text
