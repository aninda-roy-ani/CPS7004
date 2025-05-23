import time
import random
import threading
from week5.model.location import Location
from week5.model.ocean import Ocean
from week5.model.plankton import Plankton
from week5.model.sardine import Sardine
from week5.model.shark import Shark
from week5.view.gui import GUI
from week5.controller.config import (OCEAN_WIDTH,
                                     OCEAN_HEIGHT,
                                     SHARK_CREATION_PROBABILITY,
                                     SARDINE_CREATION_PROBABILITY,
                                     PLANKTON_CREATION_PROBABILITY)


class Simulator:

    def __init__(self):
        self.__ocean = Ocean(OCEAN_WIDTH, OCEAN_HEIGHT)
        self.__agents = []
        self.__populate()
        self.gui = GUI(self.__ocean)
        self.running = True

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
                elif probability <= PLANKTON_CREATION_PROBABILITY:
                    plank_location = Location(col, row)
                    plankton = Plankton(plank_location)
                    self.__ocean.set_agent(plankton, plank_location)
                    self.__agents.append(plankton)

    def run_simulation(self):
        while self.running:
            self.step()

    def step(self):
        time.sleep(1)
        # make all the agents act
        for agent in self.__agents:
            new_agent = agent.act(self.__ocean)
            if new_agent:
                self.__agents.append(new_agent)

        # remove dead agents
        for agent in self.__agents:
            if agent.get_energy() <= 0:
                self.__ocean.set_agent(None, agent.get_location())
        self.__agents = [agent for agent in self.__agents if agent.get_energy() > 0]

        # update GUI
        self.gui.update_display()

    def start(self):
        threading.Thread(target=self.run_simulation).start()
        self.gui.mainloop()

    def stop(self):
        self.running = False


if __name__ == "__main__":
    sim = Simulator()
    sim.start()
