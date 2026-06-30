import unittest
from cycleflow_6_9_6.ninia_interceptor_layer import NiniaRouter

class TestNiniaRouter(unittest.TestCase):
    def test_routing_logic(self):
        router = NiniaRouter()
        res = router.route(\"normal_event\", {\"data\": 1})
        self.assertEqual(res, \"Local Ninia Analysis: Normal\")

if __name__ == \"__main__\":
    unittest.main()
