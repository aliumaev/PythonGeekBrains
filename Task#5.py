# lesson #1
# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала
# с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

while True:
    income = input("Введите ежегодную прибыль компании: ")
    expenses = input("Введите ежегодные затраты компании: ")
    if income.isdigit() and expenses.isdigit():
        income = float(income)
        expenses = float(expenses)
        if income > expenses:
            print("Компания приносит прибыль — выручка больше издержек.")
            profit = income-expenses
            profitability = profit/income
            print(f"Рентабельность компании = {profitability}")
            while True:
                employeesN = input("Введите количество сотрудников: ")
                if employeesN.isdigit() and int(employeesN) >= 1:
                    employeesN = int(employeesN)
                    profinOnOneEmployee = profit/employeesN
                    print(f"Прибыль компании в расчете на одного сотрудника = {profinOnOneEmployee}")
                    break

        elif income < expenses:
            print("Компания несет убытки — издержки больше выручки.")
        elif income == expenses:
            print("Убытки равны издержкам.")

        break

