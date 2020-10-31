# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def Cunsumption(self):
        pass

class Cloth(ABC):
    CheckSize = 0

    def Cunsumption(self):
        pass

    @property
    def CheckSize(self):
        return self.CheckSize

    @CheckSize.setter
    def CheckSize(self, CheckSize):
        if CheckSize > 10:
            print("Понадобится больше 10 м ткани. Придется заказать больше.")

        else:
            print("Понадобится меньше 10 м ткани. Все что нужно есть в наличии.")



class Suit(Cloth):
    def __init__(self, H):
        super().__init__()
        self.H = H

    def calcMaterial(self):
        result = round((2 * self.H + 0.3)/100, 2)
        Cloth().CheckSize = result
        return result

    def __str__(self):
        return f"На ваш костюм уйдет {self.calcMaterial()} метров ткани."

    def Cunsumption(self):
        pass

class Coat(Cloth):
    def __init__(self, V):
        super().__init__()
        self.V = V

    def calcMaterial(self):
        result = round((self.V / 6.5 + 0.5), 2)
        Cloth().CheckSize = result
        return result

    def __str__(self):
        return f"На ваше пальто уйдет {self.calcMaterial()} метров ткани."

    def Cunsumption(self):
        pass


mySuit = Suit(H=210)
myCoat = Coat(V=70)

print(mySuit)
print(myCoat)