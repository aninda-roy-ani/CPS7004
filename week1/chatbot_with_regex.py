import re

class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if re.search(rule["condition"], text, re.IGNORECASE):
                return f"Bot: {rule['response']}"
        return "Bot: I don't understand."



if __name__ == "__main__":
    rule_engine = RuleEngine()
    # Add rules
    rule_engine.add_rule(r'\bhello\b|\bhi\b|\bhey\b', "Hi there!")
    rule_engine.add_rule("how are you?", "I'm good! What about you?")
    rule_engine.add_rule("i'm fine too", "Alright!")
    rule_engine.add_rule(r"^it's.+day$", "Yeah! True!")
    rule_engine.add_rule(r"\bi.+sad\b", "Feeling sorry for you!")
    rule_engine.add_rule(r'\bthank.*you.*\b', "You're welcome!")
    rule_engine.add_rule("love you", "Oh! Thanks! Love you too!")
    rule_engine.add_rule(r"\bwish me\b", "All the best!")
    rule_engine.add_rule(r"\bbye\b", "Goodbye!")
    rule_engine.add_rule(r'\bmy name is (.+)\b', r'Nice to meet you, {0}!')

    # Have conversation
    while True:
        user_input = input("You: ")
        response = rule_engine.apply_rules(user_input)
        print(response)

        if user_input.lower() == "goodbye":
            break