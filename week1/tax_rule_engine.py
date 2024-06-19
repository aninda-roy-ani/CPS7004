from week1.rule_engine import RuleEngine


engine = RuleEngine()
engine.add_rule(lambda x: x <= 12570, "Personal Allowance, 0% Tax Rate")
engine.add_rule(lambda x: 12570 < x <= 50270, "Basic rate, 20% Tax Rate")
engine.add_rule(lambda x: 15270 < x <= 125140, "Higher rate, 40% Tax Rate")
engine.add_rule(lambda x: x > 125140, "Additional rate, 45% Tax Rate")

result = engine.apply_rules(15000)
print(result)