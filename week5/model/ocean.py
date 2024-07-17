from week5.model.environment import Environment
from week5.model.location import Location


class Ocean(Environment):

    def __init__(self, width, height):
        self.__grid = [[None for _ in range(width)] for _ in range(height)]

    def clear(self):
        width = len(self.__grid[0])
        height = len(self.__grid)
        self.__grid = [[None for _ in range(width)] for _ in range(height)]

    def get_agent(self, location):
        x = location.get_x()
        y = location.get_y()
        return self.__grid[y][x]

    def set_agent(self, agent, location):
        x = location.get_x()
        y = location.get_y()
        self.__grid[y][x] = agent

    def get_height(self):
        return len(self.__grid)

    def get_width(self):
        return len(self.__grid[0])

    def adjacent_agents(self, location):
        agents = []

        # Define offsets for adjacent locations
        offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        # Iterate over each offset to find adjacent locations
        for offset_x, offset_y in offsets:
            adjacent_col = (location.get_x() + offset_x) % self.get_width()
            adjacent_row = (location.get_y() + offset_y) % self.get_height()

            agent = self.__grid[adjacent_row][adjacent_col]
            if agent:
                agents.append(agent)

        return agents

    def free_adjacent_locations(self, location):
        free_locations = []

        # Define offsets for adjacent locations
        offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        # Iterate over each offset to find adjacent locations
        for offset_x, offset_y in offsets:
            adjacent_col = (location.get_x() + offset_x) % self.get_width()
            adjacent_row = (location.get_y() + offset_y) % self.get_height()

            if self.__grid[adjacent_row][adjacent_col] is None:
                free_locations.append(Location(adjacent_col, adjacent_row))

        return free_locations