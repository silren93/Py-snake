import math
a=int(input('Nhập a= '))
b=int(input('Nhập b= '))
c=int(input('Nhập c= '))
if a==0:
    if b==c==0:
        print('Phương trình có vô số nghiệm')
    elif b==0:
        print('Phương trình vô nghiệm')
    else:
        print('Phương trình có 1 nghiệm x=%.1f'%(-c/b))

delta=b**2-4*a*c
if(delta<0):
    print('Phương trình vô nghiệm')
elif(delta==0):
    print('Phương trình có nghiệm kép: x=%.1f'%-b/(2*a))
else:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print('Phương trình có 2 nghiệm phân biệt:\nx1=%.1f'%x1,'\nx2=%.1f'%x2)
