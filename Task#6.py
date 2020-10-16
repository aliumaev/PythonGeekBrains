# nice авп ъghj jапро hjjпаро вапрghgh cool я думал это будет иметь какое то отношение к 6-й задаче но нет
# 6. Реализовать функцию c, принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(*args: str):
    myStr = str()
    for arg in args:
        myStr += arg.title()
    return myStr

print(int_func())

while True:
    userStr = input("Enter word in english (or press x to exit): ").lower()
    if userStr == "x":
        break
    print(int_func(userStr))