# Задайте список из n чисел последовательности 
# (1 + 1/n)^n и выведите на экран их сумму.

num_n = int(input('Введите число '))
list_num = []
sum_list_num = 0
for i in range(1, num_n + 1):
    list_num.append(round((1 + 1 / i) ** i, 2))
    sum_list_num += list_num[i - 1]
print(list_num)
print(sum_list_num)
