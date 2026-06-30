import unittest
import sys
import os

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from organs.cycleflow_6_9_6.nexus_core import NexusCore
from organs.cycleflow_6_9_6.dualcore_manager import DualCoreManager
from organs.cycleflow_6_9_6.ninia_router import NiniaRouter

class MockBrain:
    def generate_response(self, prompt):
        return f\"Mock response for: {prompt[:20]}...\"

class TestCycleFlowWithQwen(unittest.TestCase):
    def test_nexus_qwen_integration(self):
        brain = MockBrain()
        nexus = NexusCore(brain=brain)
        nexus.register_agent(\"NINIA-01\")
        
        self.assertIn(\"NINIA-01\", nexus.agents)
        status = nexus.get_status()
        self.assertEqual(len(status[\"registered_agents\"]), 1)

    def test_dualcore_sync(self):
        manager = DualCoreManager()
        result = manager.pulse({\"mirror\": True})
        self.assertEqual(result[\"pulse\"], 1)
        self.assertEqual(result[\"nexus_status\"][\"mirror_count\"], 1)

    def test_ninia_router_and_shadow(self):
        router = NiniaRouter()
        router.add_route(\"AGENT-X\", \"CRITICAL_EVENT\")
        
        self.assertEqual(router.route_event(\"CRITICAL_EVENT\"), \"AGENT-X\")
        self.assertIn(\"AGENT-X\", router.shadows)
        self.assertEqual(router.shadows[\"AGENT-X\"].get_shadow_state()[\"status\"], \"ACTIVE\")

if __name__ == \"__main__\":
    unittest.main()
