# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

import random

a = []
for i in range(0, 20):
    a.append(random.randint(-20, 20))

num = 0  # какое число
num_pos = 0  # его позиция в массиве
to_null = 20  # разница с нулем. У искомого числа она минимальна, потому что оно макс. из отрицательных

for i in range(0, 19):
    if a[i] < 0:
        if 0 - a[i] < to_null:
            to_null = 0 - a[i]
            num = a[i]
            num_pos = i

print(a)
print(f'Макс. из отриц.: №{num_pos+1}, значение {num}')