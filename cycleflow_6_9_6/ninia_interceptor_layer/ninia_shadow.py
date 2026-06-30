import time

class NiniaShadow:
    \"\"\"Trace and observation class for Ninia actions\"\"\"
    def __init__(self):
        self.logs = []

    def trace(self, action: str, data: dict):
        entry = {
            \"timestamp\": time.time(),
            \"action\": action,
            \"data\": data
        }
        self.logs.append(entry)
