input_name=input('Nhap ten can kiem tra: ')
for char in input_name:
    if char=='a' or char=='A':
        print('Trong ten vua nhap co xuat hien ki tu a hay A')
        break
else:
    print('Khong co trong ki tu a or A vua nhap')

