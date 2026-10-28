import random
bot = random.randint(1, 10)
play = int(input("ведите число"))
while play != bot:
    if play > bot:
        print("ты не угадал моё число, меньше твоего")
    else:
        print("ты не угадал моё число, больше твоего")
    play = int(input("вы неугадали, попробуй ещё раз ввести число"))
if play == bot:
    print(f"ты угадал! моё число: {bot}")
    bot = random.randint(1, 25)
    play2 = int(input("ведите число"))
    while play != bot:
        if play > bot:
            print("ты не угадал моё число, меньше твоего")
        else:
            print("ты не угадал моё число, больше твоего")
        play = int(input("вы неугадали, попробуй ещё раз ввести число"))
    if play == bot:
        print(f"ты угадал! моё число: {bot}")