Ten_san_pham=str(input('Nhập tên sản phẩm: '))
So_luong=int(input('Nhập số lượng: '))
Don_gia=int(input('Nhập đơn giá: '))
thanh_tien=Don_gia*So_luong
print('Thành tiền: {:,} x {:,} = {:,} VNĐ'.format(So_luong,Don_gia,thanh_tien))
khuyen_mai=0
if thanh_tien>=130000:
    khuyen_mai=int(thanh_tien*0.1)
print('Khuyến mãi: ', khuyen_mai)
print('Thanh toán: {:,} - {:,} = {:,} VNĐ'.format(thanh_tien,khuyen_mai,thanh_tien - khuyen_mai))