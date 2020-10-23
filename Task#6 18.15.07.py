# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

# Информатика: 100(л) 50(пр) 20(лаб)
# Физика: 30(л) 10(лаб)
# Физкультура: — 30(пр)
# Математика: - 40(л) 10(пр)
# История: — 15(л) 35(пр)

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

myFile = open("txtForTask#6", "r", encoding="UTF-8")
info = myFile.readlines(0)

def returnSumHours(inputStr: str):

    inputStr = inputStr.replace("(л)", " ")
    inputStr = inputStr.replace("(пр)", " ")
    inputStr = inputStr.replace("(лаб)", " ")
    return sum(map(int, inputStr.split()))


lesson = {}

for line in info:
    lesson[line.split()[0][0:-1]] = returnSumHours("".join(line.split()[1:]))
print()
print(lesson)
print(f"\nВсего  предметов: {len(info)}")


myFile.close()