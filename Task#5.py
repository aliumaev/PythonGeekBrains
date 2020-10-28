# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный.
# Метод для каждого экземпляра.

class Stationary():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Started drawing.")

class Pen(Stationary):
    def draw(self):
        print(f'Started drawing "{self.title}" using {self.__class__.__name__}')


class Pencil(Stationary):
    def draw(self):
        print(f'Started drawing "{self.title}" using {self.__class__.__name__}')


class Handle(Stationary):
    def draw(self):
        print(f'Started drawing "{self.title}" using {self.__class__.__name__}')


A = Pen("Hello")
A.draw()

B = Pencil("Ali")
B.draw()

C = Handle("Nice to meet you!")
C.draw()