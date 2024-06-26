class FuzzySystem:
    def __init__(self):
        self.rules = [
            # Rules: (Speed, Distance) -> Braking
            (("slow", "close"), "soft"),
            (("slow", "medium"), "soft"),
            (("slow", "far"), "none"),
            (("medium", "close"), "medium"),
            (("medium", "medium"), "soft"),
            (("medium", "far"), "none"),
            (("fast", "close"), "hard"),
            (("fast", "medium"), "medium"),
            (("fast", "far"), "soft")
        ]

        self.speed_memberships = {
            "slow": lambda x: max(0, 1 - abs((x - 20) / 20)),
            "medium": lambda x: max(0, 1 - abs((x - 50) / 20)),
            "fast": lambda x: max(0, 1 - abs((x - 80) / 20))
        }

        self.distance_memberships = {
            "close": lambda x: max(0, 1 - abs((x - 10) / 10)),
            "medium": lambda x: max(0, 1 - abs((x - 30) / 10)),
            "far": lambda x: max(0, 1 - abs((x - 50) / 10))
        }

    def __fuzzify(self, value, memberships):
        fuzzified = {}
        for term, func in memberships.items():
            fuzzified[term] = func(value)
        return fuzzified

    def __infer(self, speed_antecedents, distance_antecedents):
        inference = {'soft': 0, 'medium': 0, 'hard': 0, 'none': 0}

        for (speed_term, distance_term), action in self.rules:
            degree = min(speed_antecedents[speed_term], distance_antecedents[distance_term])
            inference[action] = max(inference[action], degree)

        return inference

    def __defuzzify(self, consequent):
        return max(consequent, key=consequent.get)

    def evaluate(self, speed, distance):
        speed_antecedents = self.__fuzzify(speed, self.speed_memberships)
        distance_antecedents = self.__fuzzify(distance, self.distance_memberships)
        inference = self.__infer(speed_antecedents, distance_antecedents)
        consequent = self.__defuzzify(inference)
        return consequent


if __name__ == "__main__":
    fuzzy_system = FuzzySystem()
    try:
        speed = float(input("Enter the speed in km/h: "))
        distance = float(input("Enter the distance in meters: "))
        braking_action = fuzzy_system.evaluate(speed, distance)
        print(f"Braking action for speed {speed} km/h and distance {distance} meters: {braking_action}")
    except ValueError:
        print("Please enter valid numbers for speed and distance.")
