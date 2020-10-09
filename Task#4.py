# lesson #1
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


while True:
    number = input("Введите целое положительное число: ")

    if number.isdigit():
        number = float(number)
        maxNumber = 1
        if number < 10:
            print(f"Наибольшая цифра в числе = {int(number)}")
            break

        while number/10 >= 1:
            if maxNumber < number % 10:
                maxNumber = number % 10

            number = number // 10

        print(f"Наибольшая цифра в числе = {int(maxNumber)}")
        break