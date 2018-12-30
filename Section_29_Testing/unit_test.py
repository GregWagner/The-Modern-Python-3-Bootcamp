import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """eat should have a positive message for healthy foods"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because my body is a temple")

    def test_eat_unhealthy(self):
        """eat should indcate you've given up for eating unhealthy foods"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because you only live once")

    def test_eat_healthy_boolean(self):
        """is_healthy must be a bool"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy=22)

    def test_short_nap(self):
        """short naps should be refreshing"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap")

    def test_long_nap(self):
        self.assertEqual(
            nap(3),
            "Ugh, I overselpt. I didn't mean to nap 3 hours")

    def test_is_funny_tim(self):
        self.assertFalse(is_funny("tim"))

    def test_is_funny_anyone_else(self):
        self.assertTrue(is_funny("tammy"))
        self.assertTrue(is_funny("sven"))

    def test_laugh(self):
        self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))
        
if __name__ == "__main__":
    unittest.main()
