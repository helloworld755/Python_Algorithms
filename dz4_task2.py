# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена

import timeit

def no_erat(n):
    a = [2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in a:
            if j*j-1 > i:
                a.append(i)
                break
            if i % j == 0:
                break
        else:
            a.append(i)
    #print(a)


def erat(n):
    b = list(range(n + 1))
    b[1] = 0
    a = []

    i = 2
    while i <= n:
        if b[i] != 0:
            a.append(b[i])
            for j in range(i, n + 1, i):
                b[j] = 0
        i += 1
    #print(a)


print(timeit.timeit(f'no_erat(100)',
                    setup='from __main__ import no_erat',
                    number=100000))

print(timeit.timeit(f'erat(100)',
                    setup='from __main__ import erat',
                    number=100000))

# Время работы алгоритма без решета Эратосфена: 2.3397715, с решетом Эратосфена: 2.7888819
# Алгоритм сложности: O(n^2).
# С ростом объема входных данных в 10 раз функция будет работать не более чем в 100 раз дольше.
