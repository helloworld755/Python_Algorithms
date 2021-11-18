# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках.

from random import randint


# без сортировки
def mediana(l: list):
    for i in range(len(l)):
        less = 0
        more = 0
        eq = 0

        for j in range(len(l)):
            if l[j] < l[i]:
                less += 1
            elif l[j] > l[i]:
                more += 1
            else:
                eq += 1

        eq -= 1

        if less == more or less+eq == more or less == more+eq:
            med = l[i]

    return med


m = int(input("Введите натуральное число: "))
n = 2 * m + 1
a = 0
b = 5

mas = [randint(a, b) for x in range(n)]

print(mas)
print(mediana(mas))
print(sorted(mas))  # для проверки
