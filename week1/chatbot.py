class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if rule["condition"] in text.lower():
                return f"Bot: {rule['response']}"
        return "Bot: I don't understand."


# Example usage
rule_engine = RuleEngine()

if __name__ == "__main__":
    # Add rules
    rule_engine.add_rule("hello", "Hi there!")
    rule_engine.add_rule("how are you?", "I'm good! What about you?")
    rule_engine.add_rule("i'm fine too", "Alright!")
    rule_engine.add_rule("it's a good day", "Yeah! After a lot of days!")
    rule_engine.add_rule("it's a bad day", "Feeling sorry for you!")
    rule_engine.add_rule("thank you", "You're welcome!")
    rule_engine.add_rule("fuck you", "Fuck you too!")
    rule_engine.add_rule("son of a bitch", "Stop using mean words!")
    rule_engine.add_rule("bitch", "You son of a bitch!")
    rule_engine.add_rule("love you", "Oh! Thanks! Love you too!")
    rule_engine.add_rule("wish me", "All the best!")
    rule_engine.add_rule("goodbye", "Goodbye!")

    # Have conversation
    while True:
        user_input = input("You: ")
        response = rule_engine.apply_rules(user_input)
        print(response)

        if user_input.lower() == "goodbye":
            break