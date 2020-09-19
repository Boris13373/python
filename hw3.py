class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}

class Position(Worker):
    def get_name(self):
        return f"{self.name} {self.surname}"
    def get_profit(self):
        return f"{sum(self._income.values())}"
m = Position("Boris", "Britva", "Cleaner", 20000, 140000)
print(m.get_name())
print(m.position)
print(m.get_profit())