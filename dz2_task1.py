# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные
# для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать
# ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления
# на ноль, если он ввел 0 в качестве делителя.

import operator
opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

oper = input('Введите знак операции: ')

while oper != '0':
    if oper in opers:
        num_1 = float(input('Введите число 1: '))
        num_2 = float(input('Введите число 2: '))
        while oper == '/' and num_2 == 0:
            print('Ошибка: Деление на ноль!')
            num_2 = float(input('Введите число 2: '))
        print(opers[oper](num_1, num_2))
    else:
        print('Ошибка: Введен неверный знак операции!')
    oper = input('Введите знак операции: ')

print('Завершение программы')
