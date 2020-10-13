# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

userFillingList = True
firstRequest = True
userList = list()
newUserList = list()

while userFillingList:
    if firstRequest:
        inputStr = input("Введите первый элемент списка:  ")
        firstRequest = False
        userList.append(inputStr)
    else:
        inputStr = input('Введите новый элемент срписка или "x" для завершения:  ')
        if inputStr == "x":
            userFillingList = False
        else:
            userList.append(inputStr)

print(f"Исходный список: {userList}")

for i in range(0, len(userList), 1):
    if i % 2 == 0:
        newUserList.append(userList[i])
    else:
        newUserList.insert(i-1, userList[i])

print(f"Обработанный список: {newUserList}")