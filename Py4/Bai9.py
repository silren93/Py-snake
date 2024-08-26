while True:
    n=int(input('Nhap diem dung: '))
    if n>0:
        break
    else:
        print('Hay nhap diem dung >0: ')
lst_A=[]
for i in range (0, n+1, 2):
    lst_A.append(i) #them phan tu vao cuoi list
print('List cac so chan: ', lst_A)
lst_B=[]
for i in range (1,n+1, 2):
    lst_B.append(i)
print('List cac so le: ', lst_B)
