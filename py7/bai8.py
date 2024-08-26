def xem_du_lieu(du_lieu):
    print('{:15}{:15}{:15}{:15}'.format('Ma goi','Gia tien','Dung luong','Thoi han'))
    for k, v in du_lieu.items():
        print('{:15}{:15}{:15}{:15}'.format(k,str(v[0]),str(v[1]),str(v[2])))
def them_goi_cuoc(du_lieu):
    ma_goi=input('Nhap ma goi moi: ')
    if ma_goi not in du_lieu:
        gia=int(input('Nhap gia cho goi cuoc: '))
        dung_luong=float(input('Nhap dung luong'))
        thoi_han=int(input('Nhap thoi han cho goi cuoc: '))
        du_lieu[ma_goi]=[gia,dung_luong,thoi_han]
        print('Them moi thanh cong')
def cap_nhat_goi_cuoc(du_lieu):
    ma_goi= input('Nhap ma goi cuoc muon cap nhat: ')
    if ma_goi in du_lieu:
    #luu lai gia tri cu
        chi_tiet_goi=du_lieu[ma_goi]
        gia=chi_tiet_goi[0]
        dung_luong=chi_tiet_goi[1]
        thoi_han=chi_tiet_goi[2]
    
        cn_gia=input('Nhan 1 de cap nhat gia: ')
        if cn_gia=='1':
            gia=int(input('Nhap gia moi: '))
        cn_dl=input('Nhap 1 de cap nhat thoi han: ')
        if cn_th=='1':
            thoi_han=int(input('Cap nhat thoi han moi: '))
        du_lieu=[ma_goi]=[gia,dung_luong,thoi_han]
        print('Cap nhat thanh cong')
    else:
        print('Ma goi cuoc da ton tai, vui long chon chuc nang cap nhat')

def tinh_dung_luong_ngay(du_lieu):
    for ma_goi, thong_tin in du_lieu.items():
        dung_luong= thong_tin[1]
        thoi_han= thong_tin[2]
        dung_luong_ngay= dung_luong / thoi_han
        print('Dung luong/ngay cua goi {} la: {}'.format(ma_goi, dung_luong, dung_luong_ngay)) 
goi_cuoc={'D3':[15000,3,3],'DT30':[30000,7,7],'M50':[50000,1.2,30]}
while True:
    print('CT QUAN LY GOI CUOC DI DONG')
    print('1. Xem goi cuoc')
    print('2. Them goi cuoc')
    print('3. Cap nhat gi cuoc')
    print('4. Tinh dung luong trung binh/ngay')
    tac_vu=input('Chon 1 tac vu tuong ung: ')
    if tac_vu=='1':
        xem_du_lieu(goi_cuoc)
    elif tac_vu=='2':
        them_goi_cuoc(goi_cuoc)
    elif tac_vu=='3':
        cap_nhat_goi_cuoc(goi_cuoc)
    elif tac_vu=='4':
        tinh_dung_luong_ngay(goi_cuoc)
    else:
        print('Lua chon khong hop le! Vui long nhap lai.')
        break
