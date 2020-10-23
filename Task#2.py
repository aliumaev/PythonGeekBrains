# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

myFile = open("myFileForTask#2", "r", encoding="UTF-8")
info = myFile.readlines(0)
lineNum = len(info)
print("Название файла: myFileForTask#2")
print(f"Общее количество строк: {lineNum}")

i = 0
for line in info:
    i += 1
    wordsInLine = len(line.split())
    print(f"количество слов в {i}-й строке: {wordsInLine}")
myFile.close()