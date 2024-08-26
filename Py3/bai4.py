while True:
    x=int(input('Nhap so nguyen x: '))
    y=int(input('Nhap so nguyen y: '))
    if x<y:
        break
    else:
        print('Vui long nhap x<y: ')
s=0
for i in range (x, y+1):
    s+=i**2
print('Tong binh phuong tu {} den {} = {}'.format(x,y,s))
'''
tong= sum(i**2 for i in range(x, y+1))
print('Tong binh phuong cac so tu x den y: ', tong)
'''