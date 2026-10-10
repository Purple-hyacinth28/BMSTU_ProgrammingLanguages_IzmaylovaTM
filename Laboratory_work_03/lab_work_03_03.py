xn =  float(input('Xbeg='))
xk = float(input('Xend='))
dx = float(input('Dx='))
e =  float(input('Eps='))
print("+--------+--------+-----+")
print("I X I Y I N I")
print("+--------+--------+-----+")
xt = xn
while xt <= xk:
    if abs(xt) < 1:
        an = xt
        n = 0
        y = an
        while True:
            k = (xt ** 2) * (2 * n + 1) / (2 * n + 3)
            an = an * k
            y += an
            n += 1
            if abs(an) < e:
                break
        print(f"I{xt:7.2f} I{y: 7.3f} I{n: 4} I")
    xt += dx
print("+--------+--------+-----+")
#задание полностью выполнено