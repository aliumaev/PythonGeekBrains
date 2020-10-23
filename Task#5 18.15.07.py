# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

txtFile = open("txtFileForTask#5.txt", "w")

for i in range(randint(10, 100)):
    txtFile.write(f"{randint(10, 1000)} ")
txtFile.close()

txtFile = open("txtFileForTask#5.txt", "r")
fileInfo = txtFile.readline().split()
print(f"Информация из файла: {fileInfo}")
print(f"Сумма всех чисел в файле: {sum(map(float, fileInfo))}")
txtFile.close()