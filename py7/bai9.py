def xem_du_lieu(du_lieu):
    print('{:15}{:15}'.format('Username','Password'))
    for k,v in du_lieu.items():
        print('{:15}{:15}'.format(k,v))
def check_upper(text): #kiem tra trong mk co ki tu hoa hay khong
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
        return  True
    return False
def them_tai_khoan(du_lieu):
    username=input('Nhap username can them: ')
    if username not in du_lieu:
        password=input('Nhap password: ')
        if check_pass(password):
            du_lieu=[username]=password
            print('Them user thanh cong')
        else:
            print('Vui long thu lai do password khong hop le')
    else:
        print('Username da ton tai vui long chon chuc nang cap nhat')
