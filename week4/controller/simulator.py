import time

from week4.model.location import Location
from week4.model.ocean import Ocean
from week4.model.sardine import Sardine
from week4.model.shark import Shark
from week4.view.tui import Tui


class Simulator:

    def __init__(self):
        self.__ocean = Ocean(10, 10)
        self.__tui = Tui()
        self.__agents = []

        shark_location = Location(5,5)
        shark = Shark(shark_location)
        self.__agents.append(shark)
        self.__ocean.set_agent(shark, shark_location)

        shark_location = Location(4, 4)
        shark = Sardine(shark_location)
        self.__agents.append(shark)
        self.__ocean.set_agent(shark, shark_location)
        shark_location = Location(7, 8)
        shark = Sardine(shark_location)
        self.__agents.append(shark)
        self.__ocean.set_agent(shark, shark_location)
        shark_location = Location(2, 3)
        shark = Sardine(shark_location)
        self.__agents.append(shark)
        self.__ocean.set_agent(shark, shark_location)


    def run(self):
        self.__tui.display_environment(self.__ocean)

        while(True):
            print()
            print()
            print()
            print()
            print()
            for agent in self.__agents:
                agent.act(self.__ocean)
            self.__tui.display_environment(self.__ocean)
            time.sleep(1)


if __name__ == "__main__":
    sim = Simulator()
    sim.run()
