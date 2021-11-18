# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел
# в диапазоне от 2 до 9.

n = 0

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            n += 1
            print(f'{i} кратно {j}')

print(f'Общее количество: {n}')


# а если надо через массивы, то так:

n = 0

a = list(range(2, 100))
b = list(range(2, 10))
for i in a:
    for j in b:
        if i % j == 0:
            n += 1
            print(f'{i} кратно {j}')

print(f'Общее количество: {n}')