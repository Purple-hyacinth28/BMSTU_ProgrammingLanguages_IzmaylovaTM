from math import sin, pi, tan
try:
    a = float(input("Введите параметр а: "))
    x = float(input("Введите значение x: "))
    z1 = sin(pi / 2 + 3 * a) / (1 - sin(3 * a - pi))
    z2 = 1 / tan(5 / 4 * pi + 3 / 2 * a)
    print(f"{a:.2f} {x:.2f} {z1:.4f}")
    print(f"{x:.2f} {z2:.4f}")
except:
    print("Произошла ошибка")
#все сделано ;)