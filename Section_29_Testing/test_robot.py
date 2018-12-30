import unittest
from robot import Robot

class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_name(self):
        self.assertEqual(self.mega_man.say_name(),
            "BEEP BOOP BEEP. I AM MEGA MAN")
        self.assertEqual(self.mega_man.battery, 49)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
