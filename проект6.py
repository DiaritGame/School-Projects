a = float(input("Введите число:"))
if a > 1000:
    i = 0.07
elif a < 1000:
    i = 0.05
price = a * (1 - i)
print(f"Цена со скидкой {price}")