# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_1 = input('Введите букву 1: ')
letter_2 = input('Введите букву 2: ')

print(letter_1.lower() + ' - ' + str(alphabet.find(letter_1.lower()) + 1))  # реальный номер по порядку
print(letter_2.lower() + ' - ' + str(alphabet.find(letter_2.lower()) + 1))  # реальный номер по порядку
if alphabet.find(letter_1.lower()) > alphabet.find(letter_2.lower()):
    print('Между введенными буквами ' + str(alphabet.find(letter_1.lower()) - alphabet.find(letter_2.lower()) - 1) + ' букв')
else:
    print('Между введенными буквами ' + str(alphabet.find(letter_2.lower()) - alphabet.find(letter_1.lower()) - 1) + ' букв')
