print("Вы admin, user или manager?")
a = int(input("Напишите 1 если admin, 2 если user и 3 если manager:"))
if a == 1:
    login_user = input("Введите логин:")
    password_user = input("Введите пароль:")
    sys_login = "Чиловый"
    sys_password = "Парень"
    if login_user == sys_login and password_user == sys_password:
        print("Успешный вход")
        b = float(input("Напишите число:"))
        if b > 1000:
            i = 0.07
        elif b < 1000:
            i = 0.05
        s = b * (1 - i)
        if s < 100:
            print("скидка 1 %")
        elif s < 1000:
            print("скидка 10 %")
        elif s < 10000:
            print("скидка 21 %")
    else:
        print("Неверный логин или пароль")
if a == 2:
    login_user = input("Введите логин:")
    password_user = input("Введите пароль:")
    sys_login = "5 на"
    sys_password = "30"
    if login_user == sys_login and password_user == sys_password:
        print("Успешный вход")
        c = int(input("Введите коэффициент с:"))
        d = int(input("Введите коэффициент d:"))
        e = int(input("Введите коэффициент e:"))
        x = c * d / e
        if x < 50:
            print("x меньше 50")
        if x > 50:
            print("x больше 50")
    else:
        print("Неверный логин или пароль")
if a == 3:
    login_manager = input("Введите логин:")
    password_manager = input("Введите пароль:")
    sys_login = "aboyudno"
    sys_password = "pickmi"
    if login_manager == sys_login and password_manager == sys_password:
        print("Успешный вход")
        print("Решите пять загадок")
        print("Загадка 1: Кто ходит сидя?")
        s1 = input("Введите ответ:")
        sys_s1 = "шахматист"
        print("Загадка 2: У какого слона нет хобота?")
        s2 = input("Введите ответ:")
        sys_s2 = "у шахматного" and "шахматный"
        print("Загадка 3: Каких камней нет в море")
        s3 = input("Введите ответ:")
        sys_s3 = "сухих"
        print("Загадка 4: Какое слово в словаре написано неправильно?")
        s4 = input("Введите ответ:")
        sys_s4 = "неправильно"
        print("Загадка 5: Где впервые был обнаружен картофель?")
        s5 = input("Введите ответ:")
        sys_s5 = "в земле"
        if s1 == sys_s1 and s2 == sys_s2 and s3 == sys_s3 and s4 == sys_s4 and s5 == sys_s5:
            print("Молодец")
        else:
            print("Не молодец")

    else:
        print("Неверный логин или пароль")