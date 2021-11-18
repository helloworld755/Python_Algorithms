# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.

import sys

# Урок 3, задача 8
# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
# в последнюю ячейку строки. В конце следует вывести полученную матрицу.

a = []

for i in range(5):
    b = []
    for j in range(3):
        b.append(int(input(f'Введите элемент {i + 1}-{j + 1}: ')))
    b.append(b[0] + b[1] + b[2])
    a.append(b)

for i in range(5):
    print()
    for j in range(4):
        print(a[i][j], end='  ')


# подсчет памяти
sum_var = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(i) + sys.getsizeof(j)
print(sum_var)

# Python 3.9.5
# Windows, 64-разрядная ОС

# Запуск позволил определить, что объем памяти - 264 байта
# Под списки отведено 120 и 88 байт, под остальные переменные (int) - 28 байт
# Объем под переменные зависит от счетчика ссылок на объект, ссылки на тип объекта, версии Python

# Общие выводы в первой задаче
