# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

while True:
    number1 = input("Введите число делимое: ")
    number2 = input("Введите число делитель:")
    while number2.isdigit() and int(number2) == 0:
        number2 = input("На нуль делить нельзя введите другое чилсо:")

    if number1.isdigit() & number2.isdigit():
       number1 = int(number1)
       number2 = int(number2)
       break



def devideNumberes(N1, N2):
    return N1/N2

print(f"{number1}/{number2} = {devideNumberes(number1, number2)}")