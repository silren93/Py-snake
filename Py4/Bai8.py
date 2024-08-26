while True:
    n=int(input('Nhap mot so de kiem tra: '))
    if n>=2:
        break
    else:
        print('Nhap so >=2')
for i in range(2,n):
    if n%i==0:
        print(n, 'Khong phai so nguyen to')
        break
else:
    print(n,'La mot so nguyen to')