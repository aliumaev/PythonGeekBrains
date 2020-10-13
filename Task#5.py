# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

scoreList = [7, 5, 3, 3, 2]
print(f"\nТекущий рейтинг: {scoreList}\n")
userInProgress = True
firstRun = True

while userInProgress:
    while True:
        if firstRun:
            newNumber = input("Введите целое положительное число: ")
            firstRun = False
        else:
            newNumber = input('Введите целое положительное число или нажмите выход "x": ')

        if newNumber.isdigit() and int(newNumber) > 0:
            newNumber = int(newNumber)
            break
        elif newNumber == "x":
            userInProgress = False
            break
    if userInProgress:
        scoreList.append(newNumber)
        scoreList.sort(reverse=True)
        myStr = list()
        for item in scoreList:
            myStr.append(f"{item}")

        myStr = ", ".join(myStr)
        print(f"\nНовый рейтинг: {myStr}")
    else:
        print("\nВсего хорошего!")