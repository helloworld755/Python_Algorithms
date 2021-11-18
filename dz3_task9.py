# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

n = int(input('Количество строк матрицы: '))
m = int(input('Количество столбцов матрицы: '))
a = []

for i in range(n):
    b = []
    for j in range(m):
        b.append(random.randint(0, 100))
    a.append(b)

for i in range(n):
    for j in range(m):
        print(a[i][j], end='  ')
    print()

mins = []

for j in range(m):
    min = max(a[0])
    for i in range(n):
        if a[i][j] < min:
            min = a[i][j]
    mins.append(min)

print(mins)
print(f'Максимальный элемент среди минимальных элементов столбцов: {max(mins)}')