# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle


print("Введите '1' для генирации целых чисел начиная с указанного.\nВведите '2' для генерации повторяющегося списка.\nВведите любое другое значение для выхода.")
print()
menuOption = input("")

if menuOption == "1":
    # Task A
    print("Для выхода введите 'q'.")

    for x in count(int(input("Введите целое число с которого начнется генерация чисел: ").upper())):
        print(x, end="")
        exit = input("").upper()
        if exit == "Q":
            print("Всего хорошего.")
            break

elif menuOption == "2":
# Task B
    exitCode = False
    MyList = input("Введите список из слов для генирации повторения ('q' - для выхода):  ").split()
    iterator = cycle(MyList)

    while not exitCode:
        print(next(iterator), end="")
        exitCode = (False, True)[input("").upper() == "Q"]

    print("Всего хорошего.")
else:
    print("Всего хорошего.")


