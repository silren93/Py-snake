def tao_day_f(n):
    day_f=[0,1]
    for i in range(2,n):
        x=day_f[i-2]+day_f[i-1]
        day_f.append(x)
    return day_f

while True:
    n=int(input('Nhập số lượng phần tử muốn hình thành: '))
    if n>2:
        break
print('Dãy F đã tạo: ')
print(tao_day_f(n))