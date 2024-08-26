def tim_uoc(so):
    lst_uoc=[]
    for i in range(1,so):
        if so%i==0:
            lst_uoc.append(i)
    return lst_uoc
while True:
    a,b=eval(input('Nhập 2 số điểm kiểm tra: '))
    if a>0 and b>0:
        break
uoc_a=tim_uoc(a)
uoc_b=tim_uoc(b)
print('Các ước của a: ',uoc_a)
print('Tổng các ước của a: ',sum(uoc_a))
print('Các ước của b: ', uoc_b)
print('Tổng các ước của b: ',sum(uoc_b))
if sum(uoc_a)==b and sum(uoc_b)==a:
    print('{} và {} là 2 số thân thiết'.format(a,b))
else:
    print('{} và {} không là 2 số thân thiết'.format(a,b))