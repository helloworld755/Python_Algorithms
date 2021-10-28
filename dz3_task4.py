# Определить, какое число в массиве встречается чаще всего.

import random

a = []
for i in range(0, 20):
    a.append(random.randint(0, 10))

print(a)

num = 0  # какое число
num_times = 0  # сколько раз

for i in range(0, 20):
    if a.count(a[i]) > num_times:
        num_times = a.count(a[i])
        num = a[i]

print(f'Число {num} встречается {num_times} раз')
