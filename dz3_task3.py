# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = []
a_max = 0  # макс. значение
a_min = 0  # мин. значение
n_max = 0  # номер макс. значения
n_min = 0  # номер мин. значения

for i in range(0, 19):
    a.append(random.randint(0, 100))
    if a[i] == max(a):
        n_max = i
    if a[i] == min(a):
        n_min = i

print(a)
print(f'Макс: №{n_max+1} - значение {a[n_max]}, Мин: №{n_min+1} - значение {a[n_min]}')

# замена
a_max = max(a)
a_min = min(a)

a[n_max] = a_min
a[n_min] = a_max

print(a)
print(f'Мин: №{n_max+1} - значение {a[n_max]}, Макс: №{n_min+1} - значение {a[n_min]}')
