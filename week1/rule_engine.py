class RuleEngine():
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def apply_rules(self, input_value):
        for condition, result in self.rules:
            if condition(input_value):
                return result
        return "Default"

