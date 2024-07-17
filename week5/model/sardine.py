import random

from week5.controller.config import MAX_SARDINE_ENERGY, MIN_SARDINE_MOVE_ENERGY
from week5.model.agent import Agent


class Sardine(Agent):

    def __init__(self, location):
        super().__init__(location, MAX_SARDINE_ENERGY)

    def __swim(self, ocean):
        pass

    def __eat(self, ocean):
        pass

    def act(self, ocean):
        pass

