import random
def level_one():
    print("Вы гуляли по крышам, как вдруг провалились в чей-то дом. Вам повезло,дома никого не было. Но для того что-бы выбраться, вам нужно пройти через 3 комнаты с электронными замками, пороль из которых содержит по 1 цыфре. Сейчаз вы находитесь в спальне. Для того, что-бы перейти в гостинную, введите значение от 1 до 10, у вас 3 попытки:")
    atteps1 = 0
    max_atteps1 = 3
    current_level = 1
    number_level_1 = random.randint(1, 10)
    while atteps1 < max_atteps1:
        user_input1 = input(f"попытка {atteps1 + 1}:  ")
        if not user_input1.isdigit():
            print("введите число от 1 до 10")
            continue

        user_quess1 = int(user_input1)

        if user_quess1 < 1 or user_quess1 > 10:
            print("вы указали цифру или число вне придела!""введите значение от 1 до 10.")
            continue

        if user_quess1 == number_level_1:
            print(" поздравляю вы прошли во 2 комнату")
            return True
        else:
            if user_quess1 > number_level_1:
                print("Неправильно, пароль меньше введённого числа")
            else:
                print("Неправильно, пароль больше введённого числа")
            atteps1 += 1

    print("Вы исчерпали все попытки в спальне. Сработала сигрнализация, через некоторое время вас поймали. Игра окончена")
    print(f"Пароль был: {number_level_1}.")
    return level_one()


def level_two():
    print("вы попали в гостинную. Что-бы пройти в прихожую, введите значение от 1 до 25.")
    atteps = 0
    max_atteps = 4
    current_level = 1
    number_level_2 = random.randint(1, 5)
    while atteps < max_atteps:
        user_input2 = input(f"попытка {atteps + 1}:  ")
        if not user_input2.isdigit():
            print("введите число от 1 до 25")
            continue

        user_quess2 = int(user_input2)

        if user_quess2 < 1 or user_quess2 > 25:
            print("введите значение от 1 до 25."
                  "вы указали цифру или число вне придела!")
            continue

        if user_quess2 == number_level_2:
            print(" поздравляю вы прошли в прихожую")
            return True
        else:
            if user_quess2 > number_level_2:
                print("Неправильно, пароль меньше введённого числа")
            else:
                print("Неправильно, пароль больше введённого числа")
            atteps += 1

    print("Вы исчерпали все попытки в гостинной. Сработала сигрнализация, через некоторое время вас поймали. Игра окончена")
    print(f"Пароль был: {number_level_2}.")
    return level_one()

def level_3():
    print("вы попали в прихожую. Что-бы выйти из дома, введите значение от 1 до 50.")
    atteps2 = 0
    max_atteps2 = 5
    current_level = 1
    number_level_3 = random.randint(1, 5)
    while atteps2 < max_atteps2:
        user_input3 = input(f"попытка {atteps2 + 1}:  ")
        if not user_input3.isdigit():
            print("введите число от 1 до 50")
            continue

        user_quess3 = int(user_input3)

        if user_quess3 < 1 or user_quess3 > 50:
            print("введите значение от 1 до 50."
                    "вы указали цифру или число вне придела!")
            continue

        if user_quess3 == number_level_3:
            print("Поздравляю! Вы вышли на свободу! Бегите скорее домой, вас заждалась мама")
            return True
        else:
            if user_quess3 > number_level_3:
                print("Неправильно, пароль меньше введённого числа")
            else:
                print("Неправильно, пароль больше введённого числа")
            atteps2 += 1

    print("Вы исчерпали все попытки. Сработала сигрнализация, через некоторое время вас поймали. Игра окончена")
    print(f"Пароль был: {number_level_3}.")
    return level_two()

if level_one():
    level_two()
    if level_two():
        level_3()





