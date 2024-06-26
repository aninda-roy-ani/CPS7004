class FuzzySystem:
    def __init__(self):
        self.rules = {
            "very cold": 'heat',
            "cold": 'heat',
            "warm": 'nothing',
            "hot": 'cool',
            "very hot": 'cool'
        }

        self.memberships = {
            "very cold": lambda x: max(0, 1 - abs((x-0)/10)),
            "cold": lambda x: max(0, 1 - abs(x - 10) / 10),
            "warm": lambda x: max(0, 1 - abs(x - 20) / 10),
            "hot": lambda x: max(0, 1 - abs(x - 30) / 10),
            "very hot": lambda x: max(0, 1 - abs(x - 40) / 10)
        }

    def __fuzzify(self, temp_value):
        fuzzified = {}
        for term, func in self.memberships.items():
            fuzzified[term] = func(temp_value)
        return fuzzified
        

    def __infer(self, antecedents):
        inference = {'heat': 0, 'nothing': 0, 'cool': 0}

        for term, value in antecedents.items():
            action = self.rules[term]
            inference[action] += value

        return inference

    def __defuzzify(self, consequent):
        return max(consequent, key=consequent.get)

    def evaluate(self, temperature):
        antecedents = self.__fuzzify(temperature)
        inference = self.__infer(antecedents)
        consequent = self.__defuzzify(inference)
        return consequent


if __name__ == "__main__":
    fuzzy_system = FuzzySystem()
    try:
        temperature = float(input("Enter the temperature in degrees Celsius: "))
        fan_action = fuzzy_system.evaluate(temperature)
        print(f"Action for temperature {temperature}°C: {fan_action}")
    except ValueError:
        print("Please enter a valid number for temperature.")


