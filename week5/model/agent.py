from abc import ABC, abstractmethod


class Agent(ABC):

    def __init__(self, location, energy, age):
        self.__energy = energy
        self.__location = location
        self.__age = age

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_energy(self):
        return self.__energy

    def set_energy(self, energy):
        self.__energy = energy

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    @abstractmethod
    def act(self, environment):
        pass


