# По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.

x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))

k = (y1 - y2)/(x1 - x2)
b = y2 - k*x2
print('y = ' + str(k) + 'x + ' + str(b))