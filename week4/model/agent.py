from abc import ABC, abstractmethod


class Agent(ABC):

    def __init__(self, location):
        self.__location = location

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    @abstractmethod
    def act(self, environment):
        pass


