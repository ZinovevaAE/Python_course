# �������� ���������, ������� ��������� �� ���� ������������ �����
#  � ���������� ����� ��� ����.
# ������:
# - 6782 -> 23
# - 0,56 -> 11

number_float = input('������� ������������ �����: ')
sum_numbers = 0
i = 0
while i < len(number_float):
    if number_float[i] != '.':
        sum_numbers += int(number_float[i])
    i += 1
print(f'����� ���� ����� ����� ����� {sum_numbers}')

