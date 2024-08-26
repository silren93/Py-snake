def tao_csc(u0,d,n):
    day_csc=[u0]
    for i in range(1,n):
        x=day_csc[i-1]+d
        day_csc.append(x)
    return day_csc
u0=int(input('Nhập số hạng mở đầu: '))
d=int(input('Nhập công sai: '))
while True:
    n=int(input('Nhập só lượng phần tử muốn hình thành: '))
    if n>0:
        break
print('Dãy cấp số cộng đã hình thành:')
print(tao_csc(u0,d,n))