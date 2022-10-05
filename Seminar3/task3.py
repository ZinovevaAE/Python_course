# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

float_list = [1.1, 1.2, 3.6, 5, 10.02]
max_fr_part = float_list[0] % 1
min_fr_part = float_list[0] % 1
for j in float_list:
    if (j % 1) < min_fr_part:
        min_fr_part = j % 1
    if (j % 1) > max_fr_part:
        max_fr_part = j % 1
print(float_list)
print(f"Разница между максимальным и минимальным значением дробной части элементов: {max_fr_part - min_fr_part} ")