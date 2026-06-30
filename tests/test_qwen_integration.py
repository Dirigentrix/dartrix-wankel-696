import unittest
import os
from organs.leon.qwen_brain import QwenBrain

class TestQwenIntegration(unittest.TestCase):
    def test_path_fix(self):
        # Issue 1: Fix syntax error
        path = os.path.abspath(__file__)
        self.assertTrue(path.endswith(\"test_qwen_integration.py\"))

    def test_brain_init(self):
        brain = QwenBrain()
        self.assertIsNotNone(brain)

if __name__ == \"__main__\":
    unittest.main()
