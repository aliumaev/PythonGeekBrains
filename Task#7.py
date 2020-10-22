#
# 7) Реализовать генератор с помощью функции с ключевым словом yield,создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from functools import reduce

exitCode = False
while True:

    nFact = input("Введите число, факториал которого необходимо вычислить (q - выход): ").upper()

    if nFact.isdigit():
        nFact = int(nFact)
        break
    elif nFact == "Q":
        exitCode = True
        break
    else:
        print("Введите пожалуйста целое положительное число.")

if not exitCode:

    def fact(n):
        for i in range(1, n + 1):
            yield i


    def multiplayVslues(n1, n2):
        return n1 * n2


    print(f"{nFact}! = ", end="")
    for el in fact(nFact):
        print(el, end='')
        if el == nFact:
            print(" = ", end="")
        else:
            print("*", end="")

    print(reduce(multiplayVslues, fact(nFact)), end="")
else:
    print("Всего хорошего.")
