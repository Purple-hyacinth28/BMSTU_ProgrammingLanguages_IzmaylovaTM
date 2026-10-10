from math import sqrt


try:
    x = float(input("Введите значение X = "))
    r = 2
    if -10 <= x <= -6:
        y = 2-sqrt(r ** 2 - (x + 8) ** 2)
    elif -6 <= x <= -4:
        y = 2
    elif -4 <= x <= 2:
        k = (-1 - 2) / (2 - (-4))
        y = k * x
    elif 2 <= x <= 4:
        k = (-1 - 1) / (2 - 4)
        b = 1 - k * 4
        y = k * x + b
    if x < -10 or x > 4:
        print("Вышли за пределы определения функции")
    else:
        print(f"X = {x:.2f} Y = {y:.2f}")
except:
    print("Ошибка")
#задание сделано до конца :)

