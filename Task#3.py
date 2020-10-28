# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Доход": wage, "Бонус": bonus}

class Position(Worker):

    def GetFullName(self):
        return f"{self.surname} {self.name}"

    def GetTotalIncome(self):
        return self._income["Доход"] + self._income["Бонус"]

Ali = Position("Ali", "Umaev", "Directer", 10000, 2000)

print(Ali.GetFullName())
print(Ali.GetTotalIncome())

