from random import randint
n = int(input("Задайте количество элементов в массиве (N<=30) N: "))
if n > 30:
    n = 30
a = [randint(-50, 50) for i in range(n)]
min1 = a[0]
print("Начальное состояние массива")
print(a)
for i in a:
    if abs(i) < abs(min1):
        min1 = i
print(f"Минимальный по модулю элемент: {min1}")
summa = 0
if 0 in a:
    index_1 = a.index(0)
    summa = sum([abs(i) for i in a[index_1:]])
print(f"Суммв элементов, которые идут после первого элемента равного нулю {summa}")
a_chet = a[::2]
a_nechet = a[1::2]
a = a_chet
a.extend(a_nechet)
print("Преобразованный массив")
print(a)
#задание полностью выполнено

