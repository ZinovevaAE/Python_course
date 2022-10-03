# Реализуйте алгоритм перемешивания списка.
from random import randint, random

len_list = 30
list_1 = []
for i in range(len_list):
    list_1.append(i)
print(f'Список: {list_1}')
for i in range(len_list - 1, 0, -1):
    random_i = randint(0, i + 1)
    list_1[i], list_1[random_i] = list_1[random_i], list_1[i]
print(f'Перемешанный список: {list_1}')