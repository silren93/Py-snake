or_list=[1,2,5,2,5,7,4,6,-3,55,12,0]
lst_tang_2=[x+2 for x in or_list]
print('List sau khi tăng 2 đơn vị: ',lst_tang_2)
lst_so_am=[x for x in or_list if x<0]
print('List các số âm: ',lst_so_am)
lst_thay_the=[x if x>0 else 0 for x in or_list]
print('List thay thế số âm bởi số 0: ',lst_thay_the)