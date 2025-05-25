"""
Audit trail persistent storage (in-memory for demo).
"""

class AuditStore:
    _store = []

    @classmethod
    def add_record(cls, record: dict):
        cls._store.append(record)

    @classmethod
    def get_records(cls):
        return cls._store
