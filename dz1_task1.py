# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

sum = 0
mult = 1

for i in str(input('Введите число ')):
    sum += int(i)
    mult *= int(i)

print(sum)
print(mult)