# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, array: [[]]):
        self.array = array

    def __str__(self):
        arrayStr = ""
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                arrayStr += str(self.array[i][j])+" "
            arrayStr += "\n"
        return arrayStr

    def __add__(self, other):

        if len(self.array) == len(other.array) and len(self.array[0]) == len(other.array[0]):
            arraySum = [[] for _ in range(len(self.array))]
            for i in range(len(self.array)):
                for j in range(len(self.array[i])):
                    arraySum[i].append(self.array[i][j] + other.array[i][j])
            return Matrix(arraySum)

        else:
            print("Error the matrix sizes are not the same.")


A = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
B = Matrix([[0, 1, 2], [0, 1, 2], [0, 1, 2]])

C = A + B

print(C + A)
