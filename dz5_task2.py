# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import UserList


# объявление класса

class Num16(UserList):
    def sum(self, obj):
        num1 = int(''.join(self), 16)
        num2 = int(''.join(obj), 16)
        return Num16(hex(num1 + num2)[2:].upper())

    def mult(self, obj):
        num1 = int(''.join(self), 16)
        num2 = int(''.join(obj), 16)
        return Num16(hex(num1 * num2)[2:].upper())

# код программы

a = Num16(input('Введите первое число в 16-ричном формате: '))
b = Num16(input('Введите второе число в 16-ричном формате: '))

#a = Num16('A2')
#b = Num16('C4F')

print(a.sum(b))
print(a.mult(b))
