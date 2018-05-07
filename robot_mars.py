from collections import namedtuple
import sys

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
        self.reported_obstacles = set([])

    def get_orientation(self):
        """Returns a char with the orientation (N, S, W, E)"""
        return self.CHAR_ORIENTATIONS[self.orientation]

    def get_position(self):
        """ Returns a Point with the position of the robot"""
        return self.position

    def turn_left(self):
        self.orientation = (self.orientation - 1) & 3

    def turn_right(self):
        self.orientation = (self.orientation + 1) & 3

    def move_forward(self):
        """Moves the robot forward by one step"""
        x = self.position.x + self.SHIFT[self.orientation][0]
        y = self.position.y + self.SHIFT[self.orientation][1]
        self.position = Point(x,y)

    def move_backward(self):
        """Moves the robot backward by one step"""
        x = self.position.x - self.SHIFT[self.orientation][0]
        y = self.position.y - self.SHIFT[self.orientation][1]
        self.position = Point(x,y)

    def report_obstacle(self, point):
        print("Obstacle at Point" + point)
        self.reported_obstacles.add(point)



class Grid:
    """Models a grid.

       Attributes:
        obstacles (set of Points that have obstacles on it)
        x_size (int): x size of grid
        y_size (int): y size of grid

    """
    def __init__(self, x_size, y_size, obstacles = set([]):
      self.x_size = x_size
      self.y_size = y_size
      self.obstacles = obstacles


class Simulation:
    """Simulates robot movements based on instructions.

       Attributes:
        robot (Robot, we assume there to be only one)
        x_size (int): x size of grid
        y_size (int): y size of grid

    """

    def __init__(self, robot, x_size, y_size):
        self.grid = Grid(x_size, y_size)
        self.robot = robot

    def send_commands(self, commands):
        """ Sends a series of commands to the robot

        Args:
            commands (str): the commands to send to the robot (we assume valid input)

        """
        for command in commands:
          self.send_command(command)

    def send_command(self, command):
        """ Sends a single command to the robot

        Args:
            command (char): the command to send to the robot

        """
        if command == "F":
            self.robot.move_forward()
        elif command == "B":
            self.robot.move_backward()
        elif command == "L":
            self.robot.turn_left()
        elif command == "R":
            self.robot.turn_right()
        else:
            raise ValueError("invalid command")

        # simulate wrapping
        x = self.robot.position.x
        y = self.robot.position.y
        if x == self.grid.x_size:
            self.robot.position = Point(0, y)
        if y == self.grid.y_size:
            self.robot.position = Point(x, 0)
        if y == -1:
            self.robot.position = Point(x, self.grid.y_size - 1)
        if x == -1:
            self.robot.position = Point(self.grid.x_size - 1, y)


def main():
    # todo
    pass


if __name__ == "__main__":
    # Will only be executed when this module is run directly.
    main()

