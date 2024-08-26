lst_user_input=[]
while True:
    x=int(input('Nhap gia tri so cua ban: '))
    lst_user_input.append(x)
    _continue=input('Nhap Y hoac y de tiep tuc: ')
    if _continue!='y' and _continue!='Y':
        break
print('List cac so da chon: ',lst_user_input)