def xem_du_lieu(du_lieu):
    print('{:15}{:15}'.format('Username','Password'))
    for k,v in du_lieu.items():
        print('{:15}{:15}'.format(k,v))
def check_upper(text): 
    for _char in text:
        if _char.isupper():
            return True
    return False
def check_lower(text):
    for _char in text:
        if _char.islower():
            return True
    return False
def check_number(text):
    for _char in text:
        if _char.isdigit():
            return True
    return False
def check_pass(password):
    if len(password)>=8 and check_upper(password) and check_lower(password) and check_number(password) and not password.isalnum():
        return True
    return False
def them_tai_khoan(du_lieu):
    username=input('Nhập username cần thêm: ')
    if username not in du_lieu:
        password=input('Nhập mật khẩu: ')
        if check_pass(password):
            du_lieu[username]=password
            print('Thêm user thành công')
        else:
            print('Vui lòng thử lại do mật khẩu không hợp lệ!')
    else:
        print('Username đã tồn tại. Vui lòng chọn chức năng cập nhật')
def cap_nhat(du_lieu):
    username=input('Nhập username cần cập nhật: ')
    if username in du_lieu:
        old_pass=du_lieu[username] #lay pass cu de so sanh
        enter_pass=input('Nhập mật khẩu hiện tại của bạn')
        if old_pass==enter_pass:
            new_pass=input('Nhập mật khâu mới')
            if check_pass(new_pass):
                du_lieu[username]=new_pass
                print('Cập nhật thành công')
            else:
                print('Mật khẩu mới không hợp lệ!')
        else:
            print('Không thể cập nhật tài khoản do sai mật khẩu')
    else:
        print('Username không tồn tại, vui lòng chọn chức năng thêm mới')
def xoa_tai_khoan(du_lieu):
    username=input('Nhập usename cần xóa: ')
    if username in du_lieu:
        password=input('Nhập mật khẩu: ')
        if password==du_lieu[username]:
            del(du_lieu[username])
            print('Xóa thành công')
        else:
            print('Không thể xóa do mật khẩu không chính xác')
    else:
        print('Username không tồn tại')
tai_khoan={'user01':'abc@123'}
while True:
    print('CT QUẢN LÝ TÀI KHOẢN')
    print('1. Xem tài khoản')
    print('2. Thêm tài khoản')
    print('3. Cập nhật tài khoản')
    print('4. Xóa tài khoản')
    tac_vu=input('Chọn 1 tác vụ tương ứng: ')
    if tac_vu=='1':
        xem_du_lieu(tai_khoan)
    elif tac_vu=='2':
        them_tai_khoan(tai_khoan)
    elif tac_vu=='3':
        cap_nhat(tai_khoan)
    elif tac_vu=='4':
        xoa_tai_khoan(tai_khoan)
    else:
        break
