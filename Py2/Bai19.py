Loai_xe=str(input('Nhập loại xe: '))
pham_vi=int(input('Nhập phạm vi di chuyển: '))
thoi_gian_cho=int(input('Nhập thời gian chờ: '))
if Loai_xe!='4 chỗ' and  Loai_xe!='7 chỗ':
    print('Rất tiếc! Không tìm thấy xe hợp lệ.')
tien_cho = 0
if thoi_gian_cho > 5:
    tien_cho = (thoi_gian_cho - 5)*750

if Loai_xe == '4 chỗ':
    if pham_vi <= 0.5:
        gia_cuoc = 11000
    elif 0.5 < pham_vi <= 30:
        gia_cuoc= 11000 + (pham_vi - 0.5)*17000
    else:
        gia_cuoc= 11000 + 29.5*17000 + (pham_vi-30)*14500


elif Loai_xe == '7 chỗ':
    if pham_vi <= 0.5:
        gia_cuoc = 12000
    elif 0.5 < pham_vi <= 30:
        gia_cuoc = 12000 + (pham_vi - 0.5)*19600
    else:
        gia_cuoc = 12000 + 29.5*19600 + (pham_vi -30)*17100

print('Tiền chờ: ', tien_cho)
print('Tiền cước: ', gia_cuoc)
print('Tổng thanh toán: {} + {} = {}'.format(tien_cho,gia_cuoc,tien_cho+gia_cuoc))