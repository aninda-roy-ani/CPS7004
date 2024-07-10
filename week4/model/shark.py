import random

from week4.model.agent import Agent


class Shark(Agent):

    def __init__(self, location):
        super().__init__(location)

    def __swim(self, ocean):
        free_locations = ocean.free_nearby_locations(self.get_location())
        if len(free_locations) > 0:
            index = random.randint(0, len(free_locations)-1)
            free_location = free_locations[index]
            ocean.set_agent(None, self.get_location())
            ocean.set_agent(self, free_location)
            self.set_location(free_location)

    def __eat(self, ocean):
        pass

    def act(self, ocean):
        self.__swim(ocean)
