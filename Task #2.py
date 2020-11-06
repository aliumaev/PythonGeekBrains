# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

from random import randint

class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    applesN = randint(10,20)
    userInput = input(f"\nУ вас в корзине {applesN} яблок, на сколько человек вы хотите их разделить? ")

    try:
        if int(userInput) == 0:
            raise MyOwnError("Ошибка. Нельзя делить яблоки на ноль человек.")
        result = applesN / int(userInput)
        print(f"Каждый получит по {round(result, 2)} яблок")
        
    except ValueError:
        print("Ошибка, введите целое положительное число.")
        continue
    except MyOwnError as err:
        print(err)
        continue
    break
