"""
Audit logging helper utilities.
"""

import logging

logger = logging.getLogger("scp_sdk.audit")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class AuditLogger:
    @staticmethod
    def log(message: str, level="info"):
        log_func = getattr(logger, level, logger.info)
        log_func(message)
