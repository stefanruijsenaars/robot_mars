from robot_mars import *
import unittest

# todo: document tests, make tests less implementation specific

class RobotTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(0, 0, 'N')
        self.assertEqual(self.robot.orientation, 0)
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.assertEqual(self.robot.get_position(), Point(0,0))

    def test_robot(self):
        self.assertEqual(1,1)

class SimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(0, 0, 'N')
        self.simulation = Simulation(self.robot)

    def test_simulation(self):
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.assertEqual(self.robot.get_position(), Point(0,0))
        self.simulation.send_commands("F")
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.assertEqual(self.robot.get_position(), Point(0,1))
        self.simulation.send_commands("FF")
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.assertEqual(self.robot.get_position(), Point(0,3))

if __name__ == '__main__':
    unittest.main()
