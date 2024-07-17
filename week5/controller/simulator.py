import time
import random

from week5.model.location import Location
from week5.model.ocean import Ocean
from week5.model.sardine import Sardine
from week5.model.shark import Shark
from week5.view.tui import Tui
from week5.controller.config import (OCEAN_WIDTH,
                                     OCEAN_HEIGHT,
                                     SHARK_CREATION_PROBABILITY,
                                     SARDINE_CREATION_PROBABILITY)


class Simulator:

    def __init__(self):
        self.__ocean = Ocean(OCEAN_WIDTH, OCEAN_HEIGHT)
        self.__tui = Tui()
        self.__agents = []
        self.__populate()

    def __populate(self):
        for row in range(OCEAN_HEIGHT):
            for col in range(OCEAN_WIDTH):
                probability = random.random()
                if probability <= SHARK_CREATION_PROBABILITY:
                    shark_location = Location(col, row)
                    shark = Shark(shark_location)
                    self.__ocean.set_agent(shark, shark_location)
                    self.__agents.append(shark)
                elif probability <= SARDINE_CREATION_PROBABILITY:
                    sardine_location = Location(col, row)
                    sardine = Sardine(sardine_location)
                    self.__ocean.set_agent(sardine, sardine_location)
                    self.__agents.append(sardine)

    def run(self):
        self.__tui.display_environment(self.__ocean)

        while True:
            # make all the agents act
            for agent in self.__agents:
                new_agent = agent.act(self.__ocean)
                if new_agent:
                    self.__agents.append(new_agent)

            # display updated environment
            print()
            print()
            self.__tui.display_environment(self.__ocean)

            # remove dead agents
            dead_agents = []
            for agent in self.__agents:
                if agent.get_energy() <= 0:
                    dead_agents.append(agent)
            self.__agents = [agent for agent in self.__agents if agent not in dead_agents]

            # sleep for a short while
            time.sleep(1)


if __name__ == "__main__":
    sim = Simulator()
    sim.run()
