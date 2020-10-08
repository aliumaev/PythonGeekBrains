# Lesson #1
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

while True:
    n = input("Please enter integer number n: ")

    if n.isdigit():
        n = int(n)
        result = n+n*n+n*n*n
        print(f"n+n*n+n*n*n = {n}+{n}*{n}+{n}*{n}*{n} = {result}")
        break
