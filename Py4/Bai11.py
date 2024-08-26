lst_animal_name=['monkey','bee','elephant','dog','bear','pig','bear']
search_name=input('Nhập tên của con thú: ')
if search_name.lower() in lst_animal_name:
    so_lan=lst_animal_name.count(search_name.lower())
    print(search_name,'xuất hiện: ',so_lan,'lần')
else:
    print('Name is not available')