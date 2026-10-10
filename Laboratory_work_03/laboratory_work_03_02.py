from random import uniform
x_1 = [uniform(-10, 10) for i in range(10)]
y_1 = [uniform(-10, 10) for i in range(10)]
a = 8
b = 3
r = 4
print("     X       Y       RES ")
print("-------------------------")
for i in range(10):
    x = x_1[i]
    y = y_1[i]
    if x <= 0 and y <= 0 and y >= -b and x >= -a and x **2 + y ** 2 <= r ** 2:
        print(f" {x:7.2f}   {y:7.2f}  Yes")
    elif y >= 0 and y <= b and x <= a and x >= 0 and x**2 + y ** 2 >= r **2 :
        print(f" {x:7.2f}   {y:7.2f}  Yes")
    else:
        print(f" {x:7.2f}   {y:7.2f}  NO")
#задание сделано до конца :))