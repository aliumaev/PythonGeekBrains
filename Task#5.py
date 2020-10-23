# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

txtFile = open("txtFileForTask#5.txt", "r+")

for i in range(randint(10, 100)):
    txtFile.write(f"{randint(10, 1000)} ")

fileInfo = txtFile.readline(0).split()
print(fileInfo)

print(f"Сумма всех чисел в файле: {sum(map(float, fileInfo))}")

txtFile.close()