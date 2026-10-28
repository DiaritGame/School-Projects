import random
число = random.randint(1,10)
attempts = 3
print("Введите число от 1 до 10. У тебя 3 попытки")
for _ in range(attempts):
    ass = int(input("Введите число: "))
    if ass == число:
        print("Победа!")
        break
    else:
        print("Не угадал!")
else:
    print(f"Игра окончена. Загаданное число: {число}")
