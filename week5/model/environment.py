from abc import ABC, abstractmethod
from week5.model.location import Location
from week5.model.agent import Agent


class Environment(ABC):

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_agent(self, location: Location):
        pass

    @abstractmethod
    def set_agent(self, agent: Agent, location: Location):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_width(self):
        pass
