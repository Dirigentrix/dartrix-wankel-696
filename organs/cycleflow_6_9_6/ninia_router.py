from typing import Dict
from .ninia_shadow import NiniaShadow

class NiniaRouter:
    \"\"\"Routes events to appropriate Ninia agents and their shadows.\"\"\"
    def __init__(self):
        self.routes = {}
        self.shadows = {}

    def add_route(self, agent_id: str, pattern: str):
        self.routes[pattern] = agent_id
        if agent_id not in self.shadows:
            self.shadows[agent_id] = NiniaShadow(agent_id)

    def route_event(self, event_type: str) -> str:
        agent_id = self.routes.get(event_type, \"DEFAULT\")
        return agent_id
