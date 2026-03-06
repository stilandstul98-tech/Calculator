import random

print("угадайте число 1 до 10")

b = random.randint(1, 10)

while True:
    try:
        a = int(input())
        if a == b:
            print("Вы угадали")
            break
        elif a > b:
            print("меньше")
        elif a < b:
            print("больше")
    except ValueError:
        print("Вы ввели не число, пожалуйста введите число ")