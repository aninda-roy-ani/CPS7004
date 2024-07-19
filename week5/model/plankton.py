import random

from week5.controller.config import MAX_PLANKTON_ENERGY
from week5.model.agent import Agent


class Plankton(Agent):

    def __init__(self, location):
        super().__init__(location, MAX_PLANKTON_ENERGY)

    def __reproduce(self, ocean):
        current_location = self.get_location()
        free_locations = ocean.free_adjacent_locations(current_location)
        if len(free_locations) > 1:
            index = random.randint(0, len(free_locations) - 1)
            free_location = free_locations[index]
            new_plankton = Plankton(free_location)
            ocean.set_agent(new_plankton, free_location)
            return new_plankton
        return None

    def act(self, ocean):
        self.__reproduce(ocean)

