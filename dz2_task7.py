# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input('Введите натуральное число n: '))

while n < 1:
    n = int(input('Введите натуральное число n: '))

summa = 0

for i in range(1, n+1):
    summa += i

if summa == n*(n + 1)/2:
    print('Равенство выполняется: 1+2+...+n = n(n+1)/2')
else:
    print('Равенство не выполняется: 1+2+...+n = n(n+1)/2')