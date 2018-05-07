from robot-mars import *
import unittest

# todo: document tests, make tests less implementation specific

class RobotTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = new Robot(0, 0, 'N')
        self.assertEqual(self.robot.orientation, 0)
        self.assertEqual(self.robot.get_orientation(), 'N')
