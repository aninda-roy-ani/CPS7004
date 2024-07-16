from week4.model.environment import Environment
from week4.model.location import Location
from week4.model.agent import Agent
from week4.model.sardine import Sardine


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
            col = (location.get_x() + offset_x)
            row = (location.get_y() + offset_y)
            try:
                if self.__grid[row][col] is None:
                    free_locations.append(Location(col, row))
            except Exception as e:
                # if self.__grid[location.get_y()][location.get_x()] is None:
                #     free_locations.append(Location(location.get_x(), location.get_y()))
                pass

        return free_locations

    def sarine_locations(self, location):
        sardine_locations = []

        offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for offset_x, offset_y in offsets:
            col = location.get_x() + offset_x
            row = location.get_y() + offset_y

            try:
                if self.__grid[row][col] is not None:
                    sardine_locations.append(Location(col, row))
            except Exception as e:
                pass

        return sardine_locations




