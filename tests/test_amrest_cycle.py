import unittest
from organs.cyclus.cyclus import Cyclus
from organs.nexus.nexus import Nexus
from stations.station_6_amrest.amrest_compliance import AmRestCompliance

class TestAmRestCycle(unittest.TestCase):
    def test_flow(self):
        cyclus = Cyclus()
        self.assertEqual(cyclus.process_next(), \"Station 6 (AmRest)\")
        self.assertEqual(cyclus.process_next(), \"Station 9 (SuperDrob)\")
        self.assertEqual(cyclus.process_next(), \"Station 3 (Retail)\")

    def test_compliance_inheritance(self):
        compliance = AmRestCompliance()
        self.assertTrue(compliance.validate_sscc(\"SD-123456789012345\"))
        self.assertFalse(compliance.validate_sscc(\"SHORT\"))

    def test_nexus_rondo_routing(self):
        nexus = Nexus()
        # Fire 6 events to trigger migration
        for _ in range(6):
            nexus.handle_event({})
        self.assertEqual(nexus.migration_counter, 1)
        
        # Fire events to reach 9 migrations
        for _ in range(6 * 8):
            nexus.handle_event({})
        self.assertEqual(nexus.escalation_level, 11)

if __name__ == \"__main__\":
    unittest.main()
