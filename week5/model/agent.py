from abc import ABC, abstractmethod


class Agent(ABC):

    def __init__(self, location, energy):
        self.__energy = energy
        self.__location = location

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_energy(self):
        return self.__energy

    def set_energy(self, energy):
        self.__energy = energy

    @abstractmethod
    def act(self, environment):
        pass


