from random import randint
def massiv_sosed(a, i, j, n):
    b = []
    if n - 1 >= i - 1 >= 0 and  n - 1 >= j - 1 >= 0:
        b.append(a[i - 1][j - 1])
    if n - 1 >= i - 1 >= 0 and  n - 1 >= j >= 0:
        b.append(a[i - 1][j])
    if n - 1 >= i - 1 >= 0 and  n - 1 >= j + 1 >= 0:
        b.append(a[i - 1][j + 1])
    if n - 1 >= i >= 0 and  n - 1 >= j - 1 >= 0:
        b.append(a[i][j - 1])
    if n - 1 >= i >= 0 and  n - 1 >= j + 1 >= 0:
        b.append(a[i][j + 1])
    if n - 1 >= i + 1 >= 0 and  n - 1 >= j - 1 >= 0:
        b.append(a[i + 1][j - 1])
    if n - 1 >= i + 1 >= 0 and  n - 1 >= j >= 0:
        b.append(a[i + 1][j])
    if n - 1 >= i + 1 >= 0 and  n - 1 >= j + 1 >= 0:
        b.append(a[i + 1][j + 1])
    return b

def summa_abs(a, n):
    summa = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                summa += abs(a[i][j])
    return summa
def count_minors(a, n):
    count_minim = 0
    for i in range(n):
        for j in range(n):
            b =  massiv_sosed(a, i, j, n)
            flag = 1
            for k in b:
                if a[i][j] >= k:
                    flag = 0
                    break
            if flag:
                count_minim += 1
    return count_minim

def printer_matrix(a, n):
    for i in range(n):
        for j in range(n):
            print(a[i][j], end= " ")
        print()

n = int(input("Введите размер матрицы (n * n): "))
a = [[randint(-10, 10)for i in range(n)]for i in range(n)]
print("Массив")
printer_matrix(a, n)
count_minim = count_minors(a, n)
print("Количесвто локальных минимумов: ")
print(count_minim)
sum = summa_abs(a, n)
print("Сумма элементов над главной диагональю")
print(sum)
#все сделано !!! :)