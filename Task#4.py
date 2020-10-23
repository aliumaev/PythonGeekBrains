# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

myFile = open("EnTxtFileForTask#4", "r", encoding="UTF-8")
newFile = open("RusTxtFileForTask#4.txt", "w")
info = myFile.readlines(0)
print("Название файла с данными на английском: EnTxtFileForTask#4")
rusNums = ["Один", "Два", "Три", "Четыре"]

i = 0
for line in info:
    i += 1
    wordsInLine = line.split()
    wordsInLine[0] = rusNums[i-1]
    str = " ".join(wordsInLine)
    print(f"{str}", file = newFile, end="\n")
myFile.close()
newFile.close()