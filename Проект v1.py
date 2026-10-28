num = int(input("Введите число:"))
flag = False
if num % 2 != 0:
    print("Число нечетное")
    flag = True
else:
    print("число четное")
name = input("Введите свое имя:")
if flag:
    end_message = "нечетное"
else:
     end_message = "четное"
     print(name,"ввел", end_message, "число")