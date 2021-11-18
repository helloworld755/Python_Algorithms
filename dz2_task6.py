# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать
# не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше
# введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.

from random import randint

num = randint(0, 100)
i = 0

while i < 10:
    user_num = int(input('Угадайте число: '))
    if user_num == num:
        print('Вы угадали!')
        i = 10
    else:
        if user_num > num:
            print('Ваше число больше загаданного.')
        else:
            print('Ваше число меньше загаданного.')
        i += 1

print(f'Загаданное число: {num}')
