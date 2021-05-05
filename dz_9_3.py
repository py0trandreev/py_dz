class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage":wage, "bonus":bonus}

class Position(Worker):
    def get_full_name(self):
        return "{} {}".format(self.name, self.surname)

    def get_total_income(self):
        income_dir = self._income
        return "{}".format(income_dir['wage'] + income_dir['bonus'])


pos1 = Position("Петров", "Артем", "менеджер", 20000, 5000)
print("{} руб.".format(pos1.get_full_name()))
print("{} руб.".format(pos1.get_total_income()))

pos2 = Position("Иванова", "Марина", "бухгалтер", 15000, 3000)
print("{} руб.".format(pos2.get_full_name()))
print("{} руб.".format(pos2.get_total_income()))