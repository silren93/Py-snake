a=int(input('Nhập a: '))
b=int(input('Nhập b: '))
if(a==b==0):
    print('Phương trình vô số nghiệm')
elif (a==0 and b!=0):
    print('Phương trình vô nghiệm')
else:
    print('Nghiệm của phương trình {}x + ({}) = 0 có nghiệm là x= {:,}'.format(a,b, -b/a))