# ������� �����. ��������� ������ ����� ���������, 
# � ��� ����� ��� ������������� ��������.
# ������:
# - ��� k = 8 ������ ����� ��������� ���:
#  [-21 ,13, -8, 5, ?3, 2, ?1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [�������������]

num = int(input("������� ����� "))
list_Fibonachi = []

def Func_Fibonachi(k):
    if k == 1 or k == 2:
        return 1
    else:
        return Func_Fibonachi(k - 1) + Func_Fibonachi(k - 2)

for i in range(-num, num + 1):
    if i < 0:
        list_Fibonachi.append(((-1) ** (-i + 1)) * Func_Fibonachi(-i))
    if i == 0:
        list_Fibonachi.append(i)
    if i > 0:
        list_Fibonachi.append(Func_Fibonachi(i))
print(list_Fibonachi)