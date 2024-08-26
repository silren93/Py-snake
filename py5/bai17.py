tu_dien={'one':['số 1','con số 1'],'father':['cha','bố']}
while True:
    print('CT QUẢN LÝ TỪ ĐIỂN')
    print('1. Xem các từ')
    print('2. Cập nhật nghĩa')
    print('3. Thêm từ mới')
    print('4. Xóa từ')
    tac_vu=input('Chọn 1 tác vụ tương ứng: ')
 #cn1: xem   
    if tac_vu=='1':
        print('{:20}{:50}'.format('Từ TA','Các nghĩa TV'))
        for k,v in tu_dien.items():
            print('{:20}{:50}'.format(k,str(v)))
            print('{:20}{:50}'.format(k,', '.join(v)))
#cn2: cập nhật    
    elif tac_vu=='2':
        tu_ta=input('Nhập từ TA cần cập nhật nghĩa: ')
        if tu_ta in tu_dien:
            nghia=tu_dien[tu_ta] 
            nghia_moi=input('Nhập các nghĩa mới cách nhau ,: ')
            lst_nghia_moi=nghia_moi.split(',')
            nghia.extend(lst_nghia_moi)
            tu_dien[tu_ta]=nghia
            print('Cập nhật thành công!')
        else:
            print('Từ chưa tồn tại, vui lòng chọn chức năng thêm mới')
#cn3: thêm
    elif tac_vu=='3':
        tu_ta=input('Nhập từ TA cần thêm: ')
        if tu_ta not in tu_dien:
            nghia=input('Nhập các nghĩa cách nhau bởi ,: ')
            lst_nghia=nghia.split(',')
            tu_dien[tu_ta]=lst_nghia
            print('Thêm thành công!')
        else:
            print('Từ đã tồn tại, vui lòng chọn chức năng khác')
#cn4: xóa
    elif tac_vu=='4':
        tu_ta=input('Nhập từ cần xóa: ')
        if tu_ta in tu_dien:
            del(tu_dien[tu_ta])
            print('Xóa thành công!')
        else:
            print('Không thể xóa do từ không tồn tại')
#cn5: khác tác vụ = thoát
    else: 
        print('Bạn đã thoát khỏi ứng dụng')
        break