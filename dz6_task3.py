# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.

import sys

# Урок 3, задача 9
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

# подсчет памяти
sum_var = sys.getsizeof(n) + sys.getsizeof(m) + sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(i) + sys.getsizeof(j) + sys.getsizeof(mins) + sys.getsizeof(min)
print(sum_var)

# Python 3.9.5
# Windows, 64-разрядная ОС

# Запуск позволил определить, что объем памяти - от 396 байт (для матрицы 1x1) до, например, 692 (для матрицы 10х10).
# Ограничений для количества строк и столбцов не установлено. Под переменные типа int - 28 байт,
# под списки из 10 элементов по 184 байта. Объем под переменные зависит от счетчика ссылок на объект,
# ссылки на тип объекта, версии Python

# Общие выводы в первой задаче
