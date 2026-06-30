from typing import Dict
from .cyclus_core import CyclusCore
from .nexus_core import NexusCore
from organs.passportos.pulse_store import PulseStore

class DualCoreManager:
    def __init__(self, brain=None, store: PulseStore = None):
        self.cyclus = CyclusCore()
        self.nexus = NexusCore(brain)
        self.store = store
        self.mode = \"STABLE\"

    def process(self, event: Dict = None) -> Dict:
        step_result = self.cyclus.next_step()
        anomaly = self.nexus.calculate_anomaly(event or {})
        
        self.mode = self._determine_mode_with_qwen(anomaly)
        
        result = {
            \"mode\": self.mode,
            \"step\": step_result,
            \"nexus_analysis\": self.nexus.get_status()
        }

        # If a store is linked, record the pulse automatically
        if self.store:
            self.store.record_pulse(result)

        return result

    def _determine_mode_with_qwen(self, anomaly: float) -> str:
        if anomaly > 0.8: return \"CRITICAL\"
        if anomaly > 0.4: return \"UNSTABLE\"
        return \"STABLE\"
