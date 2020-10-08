# Lesson #1
# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


while True:
    initialTime = input("Enter time in seconds: ")

    if initialTime.isdigit():
        seconds = int(initialTime)
        hours = seconds//3600
        minutes = (seconds % 3600)//60
        seconds = int((seconds % 3600) % 60)
        print(f"{hours}:{minutes}:{seconds}")
        break