# Определить, является ли год, который ввел пользователем, високосным или не високосным.

if int(input('Введите год: ')) % 4 == 0:
    print('Год високосный')
else:
    print('Год не високосный')