# Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number_float = input('Введите вещественное число: ')
sum_numbers = 0
i = 0
while i < len(number_float):
    if number_float[i] != '.':
        sum_numbers += int(number_float[i])
    i += 1
print(f'Сумма цифр этого числа равна {sum_numbers}')

