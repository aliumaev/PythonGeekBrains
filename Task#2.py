# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

name = input("Name: ")
lastName = input("Last name: ")
birthday = input("Your birthday: ")
city = input("City of origin: ")
email = input("email: ")
number = input("Phone number: ")


def createStr(name, lastName, birthday, city, email, number):
    return f"Name: {lastName} {name}, birthday: {birthday}, city: {city}, email: {email}, number: {number}"


print(createStr(lastName=lastName, name=name, birthday=birthday, city=city, email=email, number=number))
