from robot_mars import *
import unittest

# todo: document tests, make tests less implementation specific

class RobotTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(0, 0, 'N')
        self.assertEqual(self.robot.orientation, 0)
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.assertEqual(self.robot.get_position(), Point(0,0))

    def test_move_forward(self):
        self.robot.move_forward()
        self.assertEqual(self.robot.get_position(), Point(0,1))

    def test_move_backward(self):
        self.robot.move_forward()
        self.assertEqual(self.robot.get_position(), Point(0,1))
        self.robot.move_backward()
        self.assertEqual(self.robot.get_position(), Point(0,0))


    def test_turn_left(self):
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.robot.turn_left()
        self.assertEqual(self.robot.get_orientation(), 'W')
        self.robot.turn_left()
        self.assertEqual(self.robot.get_orientation(), 'S')
        self.robot.turn_left()
        self.assertEqual(self.robot.get_orientation(), 'E')
        self.robot.turn_left()
        self.assertEqual(self.robot.get_orientation(), 'N')

    def test_turn_right(self):
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.robot.turn_right()
        self.assertEqual(self.robot.get_orientation(), 'E')
        self.robot.turn_right()
        self.assertEqual(self.robot.get_orientation(), 'S')
        self.robot.turn_right()
        self.assertEqual(self.robot.get_orientation(), 'W')
        self.robot.turn_right()
        self.assertEqual(self.robot.get_orientation(), 'N')


class SimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(0, 0, 'N')
        self.simulation = Simulation(self.robot, 100, 100)

    def test_simulation(self):
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.assertEqual(self.robot.get_position(), Point(0,0))
        self.simulation.send_commands("F")
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.assertEqual(self.robot.get_position(), Point(0,1))
        self.simulation.send_commands("FF")
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.assertEqual(self.robot.get_position(), Point(0,3))
        self.simulation.send_commands("RF")
        self.assertEqual(self.robot.get_orientation(), 'E')
        self.assertEqual(self.robot.get_position(), Point(1,3))
        self.simulation.send_commands("B")
        self.assertEqual(self.robot.get_position(), Point(0,3))

    def test_grid(self):
        self.simulation = Simulation(self.robot, 3, 3)
        # start in lower left corner
        self.assertEqual(self.robot.get_orientation(), 'N')
        self.assertEqual(self.robot.get_position(), Point(0,0))
        self.simulation.send_commands("F")
        self.assertEqual(self.robot.get_position(), Point(0,1))
        self.simulation.send_commands("F")
        self.assertEqual(self.robot.get_position(), Point(0,2))
        self.simulation.send_commands("F")
        self.assertEqual(self.robot.get_position(), Point(0,0))
        self.simulation.send_commands("R")
        self.simulation.send_commands("F")
        self.assertEqual(self.robot.get_position(), Point(1,0))
        self.simulation.send_commands("F")
        self.assertEqual(self.robot.get_position(), Point(2,0))
        self.simulation.send_commands("F")
        self.assertEqual(self.robot.get_position(), Point(0,0))




if __name__ == '__main__':
    unittest.main()
