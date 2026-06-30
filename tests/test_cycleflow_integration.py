import unittest
from cycleflow_6_9_6.cyclus_nexus_dualcore import DualCoreManager

class TestCycleFlowIntegration(unittest.TestCase):
    def test_dualcore_flow(self):
        manager = DualCoreManager()
        res = manager.process()
        self.assertEqual(res[\"step\"][\"station\"], \"STATION_6\")
        self.assertEqual(res[\"mode\"], \"STABLE\")

if __name__ == \"__main__\":
    unittest.main()
