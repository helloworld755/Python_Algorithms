# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках практического
# задания первых трех уроков.

# Урок 3, задание 1
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел
# в диапазоне от 2 до 9.

import timeit


def my_prog_1():
    n = 0

    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                n += 1
                #print(f'{i} кратно {j}')

    #print(f'Общее количество: {n}')

def my_prog_2():
    n = 0

    a = list(range(2, 100))
    b = list(range(2, 10))
    for i in a:
        for j in b:
            if i % j == 0:
                n += 1
                #print(f'{i} кратно {j}')

    #print(f'Общее количество: {n}')


print(timeit.timeit('my_prog_1()',
                    setup='from __main__ import my_prog_1',
                    number=100000))

print(timeit.timeit('my_prog_2()',
                    setup='from __main__ import my_prog_2',
                    number=100000))

# Вторая реализация (my_prog_2) в 1,24 раза быстрее первой (my_prog_1).
# Алгоритм сложности: O(n^2).
# С ростом объема входных данных в 10 раз функция будет работать не более чем в 100 раз дольше.
