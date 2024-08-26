'''
Bài 7: Viết hàm nhập lần lượt các phần tử của list (nhấn 1 để tiếp tục - nhấn bất kì để dừng
Sử dụng: 
-map để tạo ra list mới gồm các phần tử có giá trị gấp 2 lần các phần tử trong list cũ
-filter để lọc ra các số nguyên tố trong list cũ.
-reduce để tính tích các phần tử trong list
'''
from functools import reduce
or_list=[15,1,9,3,2,4,-8,1223,0,-44]
lst_double=list(map(lambda x:x*2,or_list))
print('List có giá trị gấp đôi: ',lst_double)
def check_prime(so):
    if so<2:
        return False
    elif so==2:
        return True
    else:
        for i in range(2,so):
            if so%i==0:
                return False
        else:
            return True
lst_prime=list(filter(check_prime,or_list))
print('List các số nguyên tố: ',lst_prime)
tich=reduce(lambda x,y : x*y, or_list)
print('Tích các pt trong list: ',tich)