from robot-mars import *
import unittest

# todo: document tests, make tests less implementation specific

class RobotTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = new Robot(0, 0, 'N')
        self.assertEqual(self.robot.orientation, 0)
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.assertEqual(self.robot.get_position(), Position(0,0))

class SimulationTestCase(unitest.TestCase):
    def setUp(self):
        self.robot = new Robot(0, 0, 'N')
        self.simulation = new Simulation(self.robot)

    def testSimulation(self):
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.assertEqual(self.robot.get_position(), Position(0,0))
        self.simulation.send_command("F")
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.assertEqual(self.robot.get_position(), Position(0,1))
