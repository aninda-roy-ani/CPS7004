from week5.model.location import Location
from week5.model.sardine import Sardine
from week5.model.shark import Shark


class Tui:

    def display_environment(self, environment):
        for row in range(environment.get_height()):
            for col in range(environment.get_width()):
                location = Location(col, row)
                agent = environment.get_agent(location)
                if agent is None:
                    print("~", end="")
                elif isinstance(agent, Shark):
                    print("S", end="")
                elif isinstance(agent, Sardine):
                    print("F", end="")
            print()