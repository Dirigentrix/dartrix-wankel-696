class Ledger:
    def __init__(self):
        self.entries = []

    def record(self, event_type, data):
        self.entries.append({\"event\": event_type, \"data\": data})
        print(f\"[Ledger] Recorded: {event_type}\")
