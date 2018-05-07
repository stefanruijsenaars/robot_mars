from collections import namedtuple

Point = namedtuple('Point', ['x','y'])

class Robot:
    """Models a robot with a position and an orientation.

    Attributes:
        orientation (int): direction the robot is facing, where 0 is N, 1 is E, 2 is S, 3 is W
        x (Point): position of the robot
    """

    # Directions, respectively: N E S W.
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))

    # Dictionary that translates input chars into internal representation.
    ORIENTATIONS = {
       'N': 0,
       'E': 1,
       'S': 2,
       'W': 3
    }

    CHAR_ORIENTATIONS = ['N', 'E', 'S', 'W']

    def __init__(self, x, y, orientation):
        """Args:
            orientation (str): direction the robot is facing ('N', 'E', 'S', 'W')
            x (int): x coordinate of the robot
            y (int): y coordinate of the robot
            alive (bool): whether the robot is alive or not

        """
        self.position = Point(x, y)
        self.orientation = self.ORIENTATIONS[orientation.upper()]


class Simulation:
    """Simulates robot movements based on instructions.

       Attributes:
        robot (Robot, we assume there to be only one)
        grid (Grid, optional)

    """

    def __init__(self, robot, grid = None):
        if grid:
            self.grid = grid
        else:
            pass
        self.robot = robot

    def send_command(self, command):
        pass
