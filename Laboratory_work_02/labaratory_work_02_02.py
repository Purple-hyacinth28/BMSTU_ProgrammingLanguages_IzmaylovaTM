from math import sqrt
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
r = float(input("Введите значение r: "))
a = 8
b = 3
if x <= 0 and y <= 0 and y >= -b and x >= -a and x **2 + y ** 2 <= r ** 2:
    print(f" {x:7.2f}   {y:7.2f}  попадает в область")
elif y >= 0 and y <= b and x <= a and x >= 0 and x**2 + y ** 2 >= r **2 :
    print(f" {x:7.2f}   {y:7.2f}  попадает в область")
else:
    print(f" {x:7.2f}   {y:7.2f}  не попадает в область")
#задание сделано до конца!!!