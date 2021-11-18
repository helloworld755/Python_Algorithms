# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a = []
for i in range(0, 10):
    a.append(random.randint(0, 100))

min_pos = 0
max_pos = 0

for i in range(0, 10):
    if a[i] == max(a):
        max_pos = i
    if a[i] == min(a):
        min_pos = i

if max_pos > min_pos:
    result = sum(a[min_pos+1:max_pos])
else:
    result = sum(a[max_pos+1:min_pos])

print(a)
print(f'Сумма элементов между макс. и мин. не включительно: {result}')
