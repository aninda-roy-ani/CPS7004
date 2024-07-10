from week4.model.environment import Environment
from week4.model.location import Location
from week4.model.agent import Agent


class Ocean(Environment):

    def __init__(self, width, height):
        self.__grid = [[None for _ in range(width)] for _ in range(height)]

    def clear(self):
        width = len(self.__grid[0])
        height = len(self.__grid)
        self.__grid = [[None for _ in range(width)] for _ in range(height)]

    def get_agent(self, location: Location):
        return self.__grid[location.get_y()][location.get_x()]

    def set_agent(self, agent, location):
        if isinstance(location, Location):
            y = location.get_y()
            x = location.get_x()
            self.__grid[y][x] = agent

    def get_height(self):
        return len(self.__grid)

    def get_width(self):
        return len(self.__grid[0])

    def free_nearby_locations(self, location):
        free_locations = []

        offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for offset_x, offset_y in offsets:
            col = (location.get_x() + offset_x) % self.get_width()
            row = (location.get_y() + offset_y) % self.get_height()

            if self.__grid[row][col] is None:
                free_locations.append(Location(col, row))

        return free_locations




