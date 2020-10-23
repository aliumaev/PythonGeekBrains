# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# [{"firm_1": 5000.0, "firm_2": -1000.0, "firm_3": 4500.0, "firm_4": -9000.0}, {"average_profit": 4750.0}]
# Подсказка: использовать менеджеры контекста.

import json

with open("txtFIleForTask#7", "r+") as txtFile:
    myDict = {}
    info = [n for n in txtFile.readlines(0)]
    myDict = {n.split()[0]: n.split()[1:] for n in info}
    averageProfit = float(0)
    newDict = {}
    n = 0
    for key, value in myDict.items():
        profit = float(value[1]) - float(value[2])
        averageProfit += (0, profit)[profit > 0]
        n += profit > 0
        newDict[key] = profit
        print(f"Профит {key} составит: {profit}")
    averageProfit /= n

    print(f"\nСредний доход составит: {averageProfit}")


data = [newDict, {"average_profit":averageProfit }]

with open("my_JSONfileForTask#7.json", "w") as write_f:
    json.dump(data, write_f)