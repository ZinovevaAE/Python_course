# �������� ��������� ���. �������� ���������� ����������� 
# �(X ? Y ? Z) = �X ? �Y ? �Z ��� ���� �������� ��������.

for i in 0, 1:
    for j in 0, 1:
        for k in 0, 1:
            if not(i or j or k) == (not(i) and not(j) and not(k)):
                print(f'��� {i},{j},{k} �������')
            else:
                print('�� �������')