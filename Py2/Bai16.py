so_diem=float(input('Nhập số điểm: '))
if so_diem < 3.5:
    print('Xếp loại kém')
elif so_diem > 3.5 and so_diem < 5.0:
    print('Xếp loại yếu')
elif so_diem >= 5.0 and so_diem < 6.5:
    print('Xếp loại trung bình')
elif so_diem >= 6.5 and so_diem < 8.0:
    print('Xếp loại khá')
else:
    print('Xếp loại giỏi')
#có thể sắp xếp từ điểm cao tới thấp
    