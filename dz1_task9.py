# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num_1 = int(input('Число 1: '))
num_2 = int(input('Число 2: '))
num_3 = int(input('Число 3: '))

if (num_1 < num_2 and num_1 > num_3) or (num_1 > num_2 and num_1 < num_3):
    print('Среднее - ' + str(num_1))
elif (num_2 < num_1 and num_2 > num_3) or (num_2 > num_1 and num_2 < num_3):
    print('Среднее - ' + str(num_2))
elif (num_3 < num_1 and num_3 > num_2) or (num_3 > num_1 and num_3 < num_2):
    print('Среднее - ' + str(num_3))
else:
    print('В введенных данных есть повторы')
