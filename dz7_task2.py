# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import random


def sort(left, right):
    sorted = []
    left_i = 0
    right_i = 0

    for i in range(len(left) + len(right)):
        if left_i < len(left) and right_i < len(right):
            if left[left_i] <= right[right_i]:
                sorted.append(left[left_i])
                left_i += 1
            else:
                sorted.append(right[right_i])
                right_i += 1

        elif left_i == len(left):
            sorted.append(right[right_i])
            right_i += 1
        elif right_i == len(right):
            sorted.append(left[left_i])
            left_i += 1

    return sorted


def res_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m) // 2

    left = res_sort(m[:mid])
    right = res_sort(m[mid:])

    return sort(left, right)


a = 0
b = 50
n = int(input("Введите длину массива: "))

mas = [round(random()*50, 2) for x in range(n)]

print(mas)
print(res_sort(mas))
