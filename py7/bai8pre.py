def xem_du_lieu(du_lieu):
    print('{:15}{:15}{:15}{:15}'.format('Mã gói','Giá tiền','Dung lượng', 'Thời hạn'))
    for k,v in du_lieu.items():
        print('{:15}{:15}{:15}{:15}'.format(k,str(v[0]),str(v[1]),str(v[2])))
def them_goi_cuoc(du_lieu):
    ma_goi=input('Nhập mã gói mới: ')
    if ma_goi not in du_lieu:
        gia=int(input('Nhập giá cho gói cước mới: '))
        dung_luong=float(input('Nhập dung lượng: '))
        thoi_han=int(input('Nhập thời hạn cho gói cước: '))
        du_lieu[ma_goi]=[gia,dung_luong,thoi_han]
        print('Thêm mới thành công')
    else:
        print('Mã gói cước đã tồn tại, vui lòng chọn chức năng cập nhật')
def cap_nhat(du_lieu):
    ma_goi=input('Nhập mã gói cước cần cập nhật: ')
    if ma_goi in du_lieu:
        chi_tiet_goi=du_lieu[ma_goi]
        gia=chi_tiet_goi[0]
        dung_luong=chi_tiet_goi[1]
        thoi_han=chi_tiet_goi[2]
        cn_gia=input('Nhấn 1 để cập nhật giá: ')
        if cn_gia=='1':
            gia=int(input('Nhập giá mới: '))
        cn_dl=input('Nhấn 1 để cập nhật dung lượng: ')
        if cn_dl=='1':
            dung_luong=float(input('Cập nhật dung lượng: '))
        cn_th=input('Nhấn 1 để cập nhật thời hạn: ')
        if cn_th=='1':
            thoi_han=input('Cập nhật thời hạn mới: ')
        du_lieu[ma_goi]=[gia,dung_luong,thoi_han]
        print('Cập nhật thành công')
    else:
        print('Gói cước chưa tồn tại, vui lonfg chọn chức năng thêm mới')
def tinh_dung_luong_tb(du_lieu):
    print('{:15}{:15}'.format('Mã gói','DLTB'))
    for k,v in du_lieu.items():
        print('{:15}{:15}'.format(k,str(v[1]/v[2])))
goi_cuoc={'D3':[15000,3,3],'DT30':[30000,7,7],'M50':[50000,1.2,30]}
while True: 
    print('CT QUẢN LÝ GÓI CƯỚC DI ĐỘNG')
    print('1. Xem gói cước')
    print('2. Thêm gói cước')
    print('3. Cập nhật gói cước')
    print('4. Tính dung lượng trung bình/ngày')
    tac_vu=input('Chọn 1 tác vụ tương ứng')
    if tac_vu=='1':
        xem_du_lieu(goi_cuoc)
    elif tac_vu=='2':
        them_goi_cuoc(goi_cuoc)
    elif tac_vu=='3':
        cap_nhat(goi_cuoc)
    elif tac_vu=='4':
        tinh_dung_luong_tb(goi_cuoc)
    else:
        break