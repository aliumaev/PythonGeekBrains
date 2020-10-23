# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

myFile = open("MyTextFileForTask#1.txt", "w")

while True:
    userStr = input("Введите новую строку для записи в файл или нажмите enter для выхода: \n")
    if userStr == "":
        break
    else:
        myFile.write(f"{userStr}\n")

myFile.close()