import unittest
from week5.model.location import Location
from week5.model.agent import Agent


class TestAgent(unittest.TestCase):
    def test_init(self):
        loc = Location(3, 4)
        agent = Agent(loc)
        self.assertEqual(agent.get_location(), loc)

    def test_set_location(self):
        loc1 = Location(1, 2)
        loc2 = Location(5, 6)
        agent = Agent(loc1)
        self.assertEqual(agent.get_location(), loc1)
        agent.set_location(loc2)
        self.assertEqual(agent.get_location(), loc2)


if __name__ == '__main__':
    unittest.main()
