from math import sqrt
x = -10
xk = 4
dx = float(input("Введит езначение dx "))
print(f"Xbeg = {x:.2f} Xend = {xk:.2f}")
print(f"Dx = {dx:.2f}")
print("+--------+--------+")
print("I   X    I    Y   +")
print("+--------+--------+")
while x <= xk:
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
        print(f"I  {x:.2f} I  {y:.2f} I")
    x += dx
print("+--------+--------+")
#Задание сделано до конца!!!!!




# from math import sqrt
# xn = -10
# x = 4
# dx = float(input("Введит езначение dx "))
# while x >= xn:
#     r = 2
#     if -10 <= x <= -6:
#         y = 2-sqrt(r ** 2 - (x + 8) ** 2)
#     elif -6 <= x <= -4:
#         y = 2
#     elif -4 <= x <= 2:
#         k = (-1 - 2) / (2 - (-4))
#         y = k * x
#     elif 2 <= x <= 4:
#         k = (-1 - 1) / (2 - 4)
#         b = 1 - k * 4
#         y = k * x + b
#     if x < -10 or x > 4:
#         print("Вышли за пределы определения функции")
#     else:
#         print(f"x: {x:.2f}, y = {y:.2f}")
#     x -= dx

# from math import sqrt
# xn = -10
# xk = 4
# dx = float(input("Введит езначение dx "))
# print(f"Xbeg = {xn:.2f} Xend = {xk:.2f}")
# print(f"Dx = {dx:.2f}")
# print("+--------+--------+")
# print("I   X    +    Y   +")
# print("+--------+--------+")
# for x in [xn + dx * i for i in range(int((xk - xn) // dx) + 2)]:
#     r = 2
#     if -10 <= x <= -6:
#         y = 2-sqrt(r ** 2 - (x + 8) ** 2)
#     elif -6 <= x <= -4:
#         y = 2
#     elif -4 <= x <= 2:
#         k = (-1 - 2) / (2 - (-4))
#         y = k * x
#     elif 2 <= x <= 4:
#         k = (-1 - 1) / (2 - 4)
#         b = 1 - k * 4
#         y = k * x + b
#     if x < -10 or x > 4:
#         print("Вышли за пределы определения функции")
#     else:
#         print(f"I  {x:.2f} I  {y:.2f} I")
# print("+--------+--------+")