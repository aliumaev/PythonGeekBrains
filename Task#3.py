# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

myFile = open("txtFileForTask#3", "r", encoding="UTF-8")
info = myFile.readlines(0)

print(f"Всего сотрудников: {len(info)}")
employeeInfo = {}

for employee in info:
    employeeInfo[employee.split()[0]] = employee.split()[1]

print("Сотрудники с окладом меньше 20,000: ")
for key,value in employeeInfo.items():
    if float(value) < 20000:
        print(f"{key} {value}")

print(f"Средний уровень дохода сотрудников: {sum(map(float, list(employeeInfo.values())))/len(info)}")

myFile.close()