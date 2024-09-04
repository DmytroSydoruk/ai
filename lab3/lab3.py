class ExpertSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, condition, conclusion):
        self.rules.append((condition, conclusion, ))

    def infer(self):
        new_facts = set()
        while True:
            applied_rule = False
            for condition, conclusion in self.rules:
                if condition.issubset(self.facts) and conclusion not in self.facts:
                    new_facts.add(conclusion)
                    applied_rule = True
            if not applied_rule:
                break
            self.facts.update(new_facts)

        return self.facts

es = ExpertSystem()

es.add_fact("курс_USD_росте")
es.add_fact("висока_інфляція")
es.add_fact("політична_нестабільність")


es.add_rule({"курс_USD_росте", "висока_інфляція"}, "прогноз_зростання_EUR")
es.add_rule({"інфляція_знижується"}, "прогноз_зростання_нацвалюти")
es.add_rule({"зростання_ВВП"}, "прогноз_зміцнення_нацвалюти")
es.add_rule({"зовнішній_борг_зростає"}, "прогноз_зниження_нацвалюти")
es.add_rule({"рівень_безробіття_зростає"}, "прогноз_зниження_нацвалюти")

es.add_rule({"політична_нестабільність"}, "прогноз_зниження_нацвалюти")
es.add_rule({"нова_міжнародна_торгова_угода"}, "прогноз_зміцнення_нацвалюти")
es.add_rule({"введення_санкцій"}, "прогноз_зниження_нацвалюти")


es.add_rule({"ринок_акцій_зростає"}, "прогноз_зміцнення_нацвалюти")
es.add_rule({"ринок_облігацій_падає"}, "прогноз_зниження_нацвалюти")

result = es.infer()
print("Отримані прогнози:", result)
