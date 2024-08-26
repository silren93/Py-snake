danh_ba={'0989741258':'Johnny','0903852147':'Katherine','0903712712':'Johnny'}
print('CT QUẢN LÝ DANH BẠ')
while True:
    print('1. Xem danh bạ')
    print('2. Cập nhật danh bạ')
    print('3. Thêm liên hệ mới')
    print('4. Xóa liên hệ')
    print('5. Tìm kiếm')
    tac_vu=input('Nhấn 1 tác vụ tương ứng: ')
#cn1: xem danh bạ đt
    if tac_vu=='1':
        print('Bạn đã chọn chức năng xem danh bạ: ')
        print('{:15}{:15}'.format('SĐT','Tên'))
        for k,v in danh_ba.items():
            print('{:15}{:15}'.format(k,v))
#cn2: cập nhật tên qua sđt
    elif tac_vu=='2':
        sdt=input('Nhập sđt cần cập nhật: ')
        if sdt in danh_ba:
            ten=input('Nhập tên mới: ')
            danh_ba[sdt]=ten #câu lệnh cập nhật
            print('Cập nhật thành công')
        else:
            print('SĐT chưa tồn tại, cần chon chức năng thêm mới')
#cn3: thêm mới sđt
    elif tac_vu == '3':
        sdt=input('Nhập số điện thoại cần thêm: ')
        if sdt not in danh_ba:
            ten=input('Nhập tên để lưu trữ: ')
            danh_ba[sdt]=ten #câu lệnh thêm
            print('Thêm thành công')
        else:
            print('SĐT đã tồn tại, vui lòng chọn chức năng cập nhật')
#cn4: xóa số ^^
    elif tac_vu == '4':
        sdt=input('Nhập số điện thoại cần xóa: ')
        if sdt in danh_ba:
            del(danh_ba[sdt])
            print('Xoá thành công')
        else:
            print('Không thực hiện xóa do sđt chưa tồn tại')
#cn5: tìm sdt qua tên
    elif tac_vu == '5':
        result={}
        ten=input('Nhập tên cần tìm: ')
        for k,v in danh_ba.items():
            if ten == v:
                result[k]=v
        if len(result)>0:
            print('{:15}{:15}'.format('SĐT','Tên'))
            for k,v in result.items():
                print('{:15}{:15}'.format(k,v))
        else:
            print('Không tìm thấy dữ liệu')
    else:
        print('Bạn chọn thoát khỏi ứng dụng')
        break
    