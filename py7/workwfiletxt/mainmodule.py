duong_dan='files/QueHuong.txt'
from libs.module import *
while True:
    print('CT XU LY FILE VAN BAN')
    print('1. Xem noi dung file')
    print('2. Them noi dung moi vao file')
    print('3. Thong ke file: ')
    tac_vu=input('Nhap 1 tac vu tuong ung: ')
    if tac_vu=='1':
        noi_dung_file=read_file(duong_dan)
        print(noi_dung_file)