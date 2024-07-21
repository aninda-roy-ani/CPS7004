import random

from week5.controller.config import (MAX_SARDINE_ENERGY,
                                     MIN_SARDINE_MOVE_ENERGY,
                                     SARDINE_REPRODUCTION_PROBABILITY,
                                     MIN_SARDINE_REPRODUCE_ENERGY,
                                     MAX_SARDINE_AGE)
from week5.model.agent import Agent
from week5.model.plankton import Plankton


class Sardine(Agent):

    def __init__(self, location):
        super().__init__(location, MAX_SARDINE_ENERGY, 0)

    def __eat(self, ocean):
        if self.get_energy() < MAX_SARDINE_ENERGY:
            current_location = self.get_location()
            potential_food = ocean.adjacent_agents(current_location)
            for thing in potential_food:
                if isinstance(thing, Plankton):
                    energy = self.get_energy() + thing.get_energy()
                    if energy > MAX_SARDINE_ENERGY:
                        energy = MAX_SARDINE_ENERGY
                    self.set_energy(energy)
                    thing.set_energy(0)

                    target_location = thing.get_location()
                    ocean.set_agent(None, current_location)
                    ocean.set_agent(self, target_location)
                    self.set_location(target_location)

    def __swim(self, ocean):
        if self.get_energy() >= MIN_SARDINE_MOVE_ENERGY:
            current_location = self.get_location()
            free_locations = ocean.free_adjacent_locations(current_location)
            if len(free_locations) > 1:
                index = random.randint(0, len(free_locations) - 1)
                free_location = free_locations[index]
                ocean.set_agent(None, current_location)
                ocean.set_agent(self, free_location)
                self.set_location(free_location)
                self.set_energy(self.get_energy() - MIN_SARDINE_MOVE_ENERGY)

    def __reproduce(self, ocean):
        if random.random() <= SARDINE_REPRODUCTION_PROBABILITY \
                and self.get_energy() >= MIN_SARDINE_REPRODUCE_ENERGY:
            current_location = self.get_location()
            free_locations = ocean.free_adjacent_locations(current_location)
            if len(free_locations) > 1:
                index = random.randint(0, len(free_locations) - 1)
                free_location = free_locations[index]

                baby_sardine = Sardine(free_location)
                ocean.set_agent(baby_sardine, free_location)
                self.set_energy(self.get_energy() - MIN_SARDINE_REPRODUCE_ENERGY)
                return baby_sardine
        return None

    def act(self, ocean):
        if self.get_age() >= MAX_SARDINE_AGE:
            self.set_energy(0)
            ocean.set_agent(None, self.get_location())
            return None
        self.set_age(self.get_age() + 1)
        self.__eat(ocean)
        self.__swim(ocean)
        return self.__reproduce(ocean)

