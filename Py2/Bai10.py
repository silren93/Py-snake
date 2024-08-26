so_tien=int(input('Nhập vào số tiền muốn đổi: '))
so_to_500k=so_tien//500000
so_tien%=500000
#so_tien= so_tien%500000
so_to_200k=so_tien//200000
so_tien%=200000
so_to_100k=so_tien//100000
so_tien%=100000
so_to_50k=so_tien//50000
so_tien%=50000
print('Số tờ 500k: ',so_to_500k)
print('Số tờ 200k: ',so_to_200k)
print('Số tờ 100k: ',so_to_100k)
print('Số tờ 50k: ',so_to_50k)
print('Số tiền còn lại: ',so_tien)

