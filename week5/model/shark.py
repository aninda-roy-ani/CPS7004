import random

from week5.model.agent import Agent
from week5.model.sardine import Sardine


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
        sardine_locations = ocean.sarine_locations(self.get_location())
        if len(sardine_locations) > 1:
            index = random.randint(0, len(sardine_locations) - 1)
            sardine_location = sardine_locations[index]
            agent = ocean.get_agent(sardine_location)
            if isinstance(agent, Sardine):
                agent.remove()
                ocean.set_agent(None, self.get_location())
                ocean.set_agent(self, sardine_location)
                self.set_location(sardine_location)
        self.__swim(ocean)
