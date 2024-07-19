import random

from week5.model.agent import Agent
from week5.model.sardine import Sardine
from week5.controller.config import (MAX_SHARK_ENERGY,
                                     MIN_SHARK_MOVE_ENERGY,
                                     MIN_SHARK_REPRODUCE_ENERGY,
                                     SHARK_REPRODUCTION_PROBABILITY)


class Shark(Agent):

    def __init__(self, location):
        super().__init__(location, MAX_SHARK_ENERGY)

    def __eat(self, ocean):
        if self.get_energy() < MAX_SHARK_ENERGY:
            current_location = self.get_location()
            potential_food = ocean.adjacent_agents(current_location)
            for thing in potential_food:
                if isinstance(thing, Sardine):
                    energy = self.get_energy() + thing.get_energy()
                    if energy > MAX_SHARK_ENERGY:
                        energy = MAX_SHARK_ENERGY
                    self.set_energy(energy)
                    thing.set_energy(0)

                    target_location = thing.get_location()
                    ocean.set_agent(None, current_location)
                    ocean.set_agent(self, target_location)
                    self.set_location(target_location)

    def __swim(self, ocean):
        if self.get_energy() >= MIN_SHARK_MOVE_ENERGY:
            current_location = self.get_location()
            free_locations = ocean.free_adjacent_locations(current_location)
            if len(free_locations) > 1:
                index = random.randint(0, len(free_locations) - 1)
                free_location = free_locations[index]
                ocean.set_agent(None, current_location)
                ocean.set_agent(self, free_location)
                self.set_location(free_location)
                self.set_energy(self.get_energy() - MIN_SHARK_MOVE_ENERGY)

    def __reproduce(self, ocean):
        if random.random() <= SHARK_REPRODUCTION_PROBABILITY \
                and self.get_energy() >= MIN_SHARK_REPRODUCE_ENERGY:
            current_location = self.get_location()
            free_locations = ocean.free_adjacent_locations(current_location)
            if len(free_locations) > 1:
                index = random.randint(0, len(free_locations) - 1)
                free_location = free_locations[index]

                baby_shark = Shark(free_location)
                ocean.set_agent(baby_shark, free_location)
                return baby_shark
        return None

    def act(self, ocean):

        self.__eat(ocean)
        self.__swim(ocean)
        return self.__reproduce(ocean)