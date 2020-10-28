# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,name,is_police (булево).
# А также методы: go,stop,turn(direction),которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar,SportCar,WorkCar,PoliceCar.Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar)и 40 (WorkCar)должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"car Name{self.name}, car type: {self.__class__.__name__} ")

    def go(self):
        print(f"{self.color} {self.name} is on Go!")
    def stop(self):
        print(f"{self.color} {self.name} is on Stop!")
    def turn(self, direction):
        print(f"{self.color} {self.name} turned {direction}")

    def showSpeed(self):
        print(f"{self.color} {self.name} speed = {self.speed} km/h")

class TownCar(Car):
    def showSpeed(self):
        print(f"{self.color} {self.name} speed = {self.speed} km/h")
        if self.speed > 60:
            print(f"Warning! for speed exceeding 60 km/h")


class WorkCar(Car):
    def showSpeed(self):
        print(f"{self.color} {self.name} speed = {self.speed} km/h")
        if self.speed > 40:
            print("Warning! Speed exceeding 40 km/h")

class SportCar(Car):
    def printName(self):
        print(f"{self.name} is a SportCar")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)



car1 = TownCar(80, "green", "Mazda")

car1.go()
car1.stop()
car1.turn("right")
car1.showSpeed()