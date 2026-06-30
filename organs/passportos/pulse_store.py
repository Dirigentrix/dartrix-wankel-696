import json
from datetime import datetime
from typing import Dict, List, Optional

class PulseStore:
    \"\"\"
    PassportOS PulseStore - Single source of truth for CycleFlow pulses.
    Stores and retrieves synchronized dual-core states.
    \"\"\"
    def __init__(self, persistence_path: Optional[str] = None):
        self.persistence_path = persistence_path
        self.pulses: List[Dict] = []
        self.meta = {
            \"version\": \"1.0.0-modular\",
            \"archetype\": \"PULSE_STORE\",
            \"initialized_at\": datetime.now().isoformat()
        }

    def record_pulse(self, pulse_data: Dict):
        \"\"\"Records a synchronized pulse from the DualCore system.\"\"\"
        entry = {
            \"pulse_id\": len(self.pulses) + 1,
            \"timestamp\": datetime.now().isoformat(),
            \"data\": pulse_data
        }
        self.pulses.append(entry)
        if self.persistence_path:
            self._persist()
        print(f\"[PulseStore] Recorded pulse {entry['pulse_id']}\")
        return entry[\"pulse_id\"]

    def get_last_pulse(self) -> Optional[Dict]:
        return self.pulses[-1] if self.pulses else None

    def get_history(self, limit: int = 10) -> List[Dict]:
        return self.pulses[-limit:]

    def _persist(self):
        try:
            with open(self.persistence_path, 'w') as f:
                json.dump({\"meta\": self.meta, \"pulses\": self.pulses}, f, indent=2)
        except Exception as e:
            print(f\"[PulseStore] Persistence error: {e}\")

class PulseStoreIntegration:
    \"\"\"Helper to link PulseStore with DualCoreManager/RondoEngine.\"\"\"
    @staticmethod
    def sync(manager, store: PulseStore, event: Dict = None):
        # Trigger manager processing
        result = manager.process(event or {})
        # Log result to store
        store.record_pulse(result)
        return result
