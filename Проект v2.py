from random import randint
num = int(input("Введите 1 число в списке:"))
m = int(input("Введите количество чисел в списке:"))
def my_funct(num: int, m: int) -> list[int | float]:
    res = [num]
    for _ in range(m):
        res += [res[-1] + num / randint(1, 10)]
    return res
print(my_funct(num, m))  