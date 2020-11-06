# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex():

    def __init__(self, i, x):
        self.i = i
        self.x = x

    def __add__(self, other):
        return complex(self.i, self.x) + complex(other.i, other.x)

    def __mul__(self, other):
        return complex(self.i, self.x) * complex(other.i, other.x)

a = Complex(10, 5)
b = Complex(2, 3)

print(a+b)
print(a*b)