# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
#
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
# любую подходящую структуру, например словарь.
#
#

techOptions = {1: "Принтер", 2: "Сканер", 3: "Ксерокс"}

class Sklad():
    DB = {"Printer": list(), "Scanner": list(), "Copier": list()}
    quantityDB = {"Printer": 0, "Scanner": 0, "Copier": 0}


class OrgTech():
    # тут будут общие атрибуты и свойства для подклассов
    @classmethod
    def NumberOfItem(clc):
        return  Sklad.quantityDB["Printer"] + Sklad.quantityDB["Scanner"] + Sklad.quantityDB["Copier"]



class Printer(OrgTech):
    #  тут будут описаны свойства принтера
    def __init__(self, code, name, quantity, color):
        self.code = code
        self.quantity = quantity
        self.name = name
        self.color = color
        super().__init__()

    def __str__(self):
        return f"\n   Код: {self.code}\n   Название: {self.name}\n   Количество: {self.quantity}\n   Цвет: {self.color}\n"

class Scanner(OrgTech):
    # совойства сканнера
    def __init__(self, code, name, quantity, color):
        self.code = code
        self.quantity = quantity
        self.name = name
        self.color = color
        super().__init__()

    def __str__(self):
        return f"\n   Код: {self.code}\n   Название: {self.name}\n   Количество: {self.quantity}\n   Цвет: {self.color}\n"

class Copier(OrgTech):
    # свойства ксерокса
    def __init__(self, code, name, quantity, color):
        self.code = code
        self.quantity = quantity
        self.name = name
        self.color = color
        super().__init__()

    def __str__(self):
        return f"\n   Код: {self.code}\n   Название: {self.name}\n   Количество: {self.quantity}\n   Цвет: {self.color}\n"


print("Добро пожаловать в программу 'МойСклад'.\n")

while True:
    # Тут в общем программа будет работать пока пользователь не сделает выход
    print()
    print("1 - для Добавления товара.")
    print("2 - для получения информации о складе.")
    print("x - для выхода.")
    print()
    userChoice1 = input("\n")
    if userChoice1.lower() == "x":
        print("Всего хорошего")
        break

    try:
        userChoice1 = int(userChoice1)
    except ValueError:
        print("Неправильный ввод.")
        continue

    if userChoice1 == 1:
        while True:
            # Тут пользователь выбирает товар для добавления в склад

            print("Выберите товар для добавления на склад:")
            print("1 - Принтер.")
            print("2 - Сканер.")
            print("3 - Ксерокс.")
            print("x - для возврата в главное меню.")
            print()

            userChoice2 = input("\n")

            if userChoice2.lower() == "x":
                break

            try:
                userChoice2 = int(userChoice2)
            except ValueError:
                print("Неправильный ввод.")
                continue

            # Если пользователь ввел правильный пункт то заходим в менню добавления товара в склад

            print(f"Добавляем {techOptions[userChoice2]}")

            code = input("Код: ")
            name = input("название: ")
            while True:
                quantity = input("количество шт.: ")
                if quantity.isdigit():
                    quantity = int(quantity)
                    break
                else:
                    print("Количество указано некорректно.")
                    continue

            color = input("цвет: ")

            print("\nВы хотите добавить следующий товар на склад: \n")

            print(f"Код: {code}\nНазвание: {name}\nКоличество: {quantity}\nЦвет: {color}\n")

            while True:
                UserProof = input("Вы подтверждаете операцию? y - Да, n - Нет ")
                if UserProof == "y":
                    if userChoice2 == 1:
                        myItem = Printer(code, name, quantity, color)
                        Sklad.DB["Printer"].append(myItem)
                        Sklad.quantityDB['Printer'] += quantity


                    if userChoice2 == 2:
                        myItem = Scanner(code, name, quantity, color)
                        Sklad.DB["Scanner"].append(myItem)
                        Sklad.quantityDB['Scanner'] += quantity


                    if userChoice2 == 3:
                        myItem = Copier(code, name, quantity, color)
                        Sklad.DB["Copier"].append(myItem)
                        Sklad.quantityDB['Copier'] += quantity


                    print("Товар успешно добавлен на склад.\n")
                    break
                if UserProof == "n":
                    print("Товар удален!\n")
                    break
                else:
                    print("Непонятный ввод. Введите снова.")
                    continue


    if userChoice1 == 2:
        print(f"Общее количесвто техники на складе: {OrgTech.NumberOfItem()} единиц.\n")

        print(Sklad.quantityDB)
        print()
        for key, value in Sklad.DB.items():
            print(f"Раздел {key}:")
            for el in value:
                print(el)




