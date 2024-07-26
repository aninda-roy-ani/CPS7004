import time
import random
import threading
from flask import Flask, jsonify
from flask_cors import CORS
from week5.model.location import Location
from week5.model.ocean import Ocean
from week5.model.plankton import Plankton
from week5.model.sardine import Sardine
from week5.model.shark import Shark
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

    def get_grid(self):
        grid = []
        for row in range(OCEAN_HEIGHT):
            grid_row = []
            for col in range(OCEAN_WIDTH):
                agent = self.__ocean.get_agent(Location(col, row))
                if agent is None:
                    grid_row.append('empty')
                elif isinstance(agent, Shark):
                    grid_row.append('shark')
                elif isinstance(agent, Sardine):
                    grid_row.append('sardine')
                elif isinstance(agent, Plankton):
                    grid_row.append('plankton')
            grid.append(grid_row)
        return grid

    def start(self):
        threading.Thread(target=self.run_simulation).start()

    def stop(self):
        self.running = False


app = Flask(__name__)
CORS(app)
simulator = Simulator()


@app.route('/api/ocean-grid', methods=['GET'])
def get_ocean_grid():
    grid = simulator.get_grid()
    return jsonify(grid)


if __name__ == "__main__":
    simulator.start()
    app.run(host='0.0.0.0', port=5000)
