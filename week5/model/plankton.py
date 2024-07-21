import random

from week5.controller.config import (MAX_PLANKTON_ENERGY,
                                     PLANKTON_REPRODUCTION_PROBABILITY,
                                     MAX_PLANKTON_AGE)
from week5.model.agent import Agent


class Plankton(Agent):

    def __init__(self, location):
        super().__init__(location, MAX_PLANKTON_ENERGY, 0)

    def __reproduce(self, ocean):
        if random.random() <= PLANKTON_REPRODUCTION_PROBABILITY:
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
        if self.get_age() >= MAX_PLANKTON_AGE:
            self.set_energy(0)
            ocean.set_agent(None, self.get_location())
            return None
        self.set_age(self.get_age() + 1)
        return self.__reproduce(ocean)

