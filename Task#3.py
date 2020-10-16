# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


while True:
    number1 = input("Enter number 1: ")
    number2 = input("Enter number 2: ")
    number3 = input("Enter number 3: ")
    if number1.isdigit() and number2.isdigit() and number3.isdigit():
        number1 = int(number1)
        number2 = int(number2)
        number3 = int(number3)
        break

def summArgs(n, m, k):
   return n+m+k - min(n, m, k)

print(f"The summ of greates two numbers is: {summArgs(number1, number2, number3)}")