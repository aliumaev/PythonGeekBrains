# 1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#     В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
#     Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# Этот скрипт для задания 1
from sys import argv

ScriptName, hours, perHour, bonus = argv

def employeeSalary():
    try:
        result = float(hours) * float(perHour) + float(bonus)
        print(f"The Salary of employee is: {result}")
    except ValueError:
        print("Incorrect parameters")



employeeSalary()