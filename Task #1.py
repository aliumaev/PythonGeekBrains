# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date():
    UserDate = str()

    def __init__(self, UserDate):
        self.UserDate = UserDate
        Date.UserDate = UserDate

    @classmethod
    def GetDate(clc):
        try:
            result = list(map(int, clc.UserDate.split("-")))
        except ValueError:
            return "error. Value is not number"
        return result

    @staticmethod
    def Validate(yourDate):
        if 0 < yourDate[0] <= 30 and 0 < yourDate[1] <= 12:
            return f"Date is correct: {yourDate[0]}/{yourDate[1]}/{yourDate[2]}"
        else:
            return f"Date is NOT correct: {yourDate[0]}/{yourDate[1]}/{yourDate[2]}"


a = Date("12-08-2020")

print(Date.Validate(a.GetDate()))