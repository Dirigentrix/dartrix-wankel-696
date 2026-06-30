class NiniaAgent:
    def __init__(self, agent_id: str, brain=None):
        self.agent_id = agent_id
        self.brain = brain

    def intercept(self, payload: dict):
        print(f\"[Ninia-{self.agent_id}] Intercepted payload: {payload}\")
        if self.brain:
            return self.brain.generate_response(f\"Analyze: {payload}\")
        return \"Local Ninia Analysis: Normal\"
