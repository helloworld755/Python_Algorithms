# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import UserList


# класс предприятия

class Company(object):
    def __init__(self, name, income):
        self.name = name  # string
        self.income = income  # list

    def avg_income(self):
        return sum(self.income) / len(self.income)


# начало программы

n = int(input('Количество предприятий: '))
c_list = UserList([])  # список компаний

# ввод данных о предприятиях

for i in range(n):
    c_name = input(f'Название компании №{i + 1}: ')
    c_inc = []
    for j in range(4):
        c_inc.append(float(input(f'Прибыль компании №{i + 1} за квартал №{j + 1}: ')))
    c_list.append(Company(c_name, c_inc))

# средняя прибыль предприятия за год

all_avg = 0
for i in range(n):
    all_avg += c_list[i].avg_income()
all_avg /= n
print(f'\nСредняя прибыль за год для всех предприятий: {all_avg}')

# у кого прибыль выше среднего, и у кого ниже

print(f'\nПрибыль выше среднего: ')
for i in range(n):
    if c_list[i].avg_income() > all_avg:
        print(c_list[i].name)

print('\nПрибыль ниже среднего (или равна среднему): ')
for i in range(n):
    if c_list[i].avg_income() <= all_avg:
        print(c_list[i].name)
