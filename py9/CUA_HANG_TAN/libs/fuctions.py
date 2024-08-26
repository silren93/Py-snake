import csv
from datetime import datetime
def read_file(_path):
    f=open(_path,'r',encoding='utf-8')
    content=[]
    for row in csv.reader(f):
        content.append(row)
    f.close()
    return content
def print_content(content):
    for row in content:
        print('{:20}{:20}{:15}{:15}{:20}{:20}{:35}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
def write_file(_path,content):
    f=open(_path,'a',encoding='utf-8',newline='')
    csv.writer(f).writerows(content)
    f.close()
def them_don_hang(content):
    don_hang_cuoi=content[-1] #lay thong tin cua don hang cuoi cung
    ma_don=don_hang_cuoi[0] #lay ma don
    ma_don=int(ma_don)+1
    new_order=[] #luu tat ca cac mat hang da order
    loai_thuc_pham={'1':['Gà rán',45000,'miếng'],
                    '2':['Coca Cola',14000,'chai'],
                    '3':['Khoai tây chip',45000,'gram'],
                    '4':['Xiên que đồng giá',15000,'que']} #luu thong tin cua cac mat hang dang ban
    while True:
        tt=input('Nhan y de tiep tuc order: ')
        if tt=='y':
            chon_tp=('1. Chọn gà rán, 2. Chọn Coca Cola, 3.Chọn khoai tây chip, 4. Chọn xiên que đồng giá: ')
            if chon_tp=='1':
                thong_tin=loai_thuc_pham['1'] #lay thong tin: ten tp, gia, dvt (lấy list)
            elif chon_tp=='2':
                thong_tin=loai_thuc_pham['2']
            elif chon_tp=='3':
                thong_tin==loai_thuc_pham['3']
            else:
                thong_tin=loai_thuc_pham['4']
            ten_tp=thong_tin[0]
            gia=thong_tin[1]
            dvt=thong_tin[2]
            so_luong=int(input('Nhap so luong: '))    
            thanh_tien=gia*so_luong
            ngay_order=datetime.now()
            order_info=[ma_don,ten_tp,so_luong,dvt,gia,thanh_tien,ngay_order] #luu thong tin cua tung mat hang
            new_order.append(order_info)
        else:
            break
    return