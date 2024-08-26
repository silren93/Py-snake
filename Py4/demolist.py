lst_so_1=[1,2,3,4,5,6]
lst_so_2=['o','l','m']
lst_so_3=lst_so_1+lst_so_2
print('List số 3: ',lst_so_3)
#Cập nhật lại giá trị
'''lst_so[3]=0
print('List sau khi cập nhật: ',lst_so)'''
#thêm phân tử
lst_so.insert(0,9)
print('List sau khi thêm: ',lst_so)
#xóa thông qua vị trí
lst_so.pop(2)
print('List sau khi xóa phần tử ở vt số 2: ',lst_so)
lst_so.pop()
print('List sau khi xóa: ',lst_so)
del(lst_so[4])
print('List sau khi xóa pt ở vt thứ 4: ',lst_so)