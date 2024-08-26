tien_goc=float(input('Nhập số tiền đã gửi: '))
so_thang=int(input('Nhập số tháng: '))
ls_nam=float(input('Nhập lãi suất mỗi năm: '))

print('Lãi suất tháng: {}/100/12 = {:,.0f}'.format(ls_nam,ls_nam/100/12))
print('Tiền lãi: {} * {} * {} = {}'.format(tien_goc,so_thang,ls_nam/100/12,tien_goc*so_thang*ls_nam/100/12))
print('Tổng số tiền: {} + {} = {}'.format(tien_goc,tien_goc*so_thang*ls_nam/100/12,tien_goc+tien_goc*so_thang*ls_nam/100/12))