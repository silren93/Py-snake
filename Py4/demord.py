import random
lst_ngau_nhien=[]
while True:
    n=int(input('Nhập số lượng phần tử cần lấy: '))
    if n>0:
        break
    else:
        print('Số lượng phần tử cần >0: ')
for i in range (0,n):
    x=random.randrange(0,101)
    lst_ngau_nhien.append(x)
print('List các số ngẫu nhiên: ', lst_ngau_nhien)