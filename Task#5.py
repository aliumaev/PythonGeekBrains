# 5) Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

myList = [element for element in range(100, 1001, 2)]

def multiplayFunc(prev_el, el):
    return el * prev_el

print(reduce(multiplayFunc, myList))






