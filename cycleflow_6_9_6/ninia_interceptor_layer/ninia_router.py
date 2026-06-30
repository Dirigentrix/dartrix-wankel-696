from .ninia_agent import NiniaAgent
from .ninia_shadow import NiniaShadow

class NiniaRouter:
    def __init__(self, brain=None):
        self.agents = {\"alpha\": NiniaAgent(\"Alpha\", brain), \"beta\": NiniaAgent(\"Beta\", brain)}
        self.shadow = NiniaShadow()

    def route(self, event: str, payload: dict):
        self.shadow.trace(f\"ROUTE_{event}\", payload)
        target = \"alpha\" if \"critical\" in event.lower() else \"beta\"
        return self.agents[target].intercept(payload)
