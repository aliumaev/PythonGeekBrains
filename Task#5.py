# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.


def summList(myList: list):
    summResult = 0
    for element in myList:
        summResult += element
    return summResult

OverAllSumm = 0
completed = False

while not completed:
    while True:
        userNumbers = input("\nВведите числа через пробел, (для выхода нажмите x): ")
        try:
            userNumbers = userNumbers.split(" ")
            i = 0
            newUserNumbers = list()
            for element in userNumbers:
                if userNumbers[i].upper() != "X":
                    newUserNumbers.append(int(element))
                else:

                    completed = True
                    break
                i += 1
            OverAllSumm += summList(myList=newUserNumbers)
            print(f"Итоговая сумма = {OverAllSumm}")
            break
        except ValueError:
            print("\nОдно или несколько значений из веденных данных не являются числами. \nПожалуйста праверьте и введите еще раз.")



