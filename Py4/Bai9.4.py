lst_stu=[['SV1','Tran Van A','Toan',8.9],['SV2','Nguyen Thi B','Van',8.9]]
print('{:15}{:30}{:15}{:5}'.format('Ma SV','Ten SV','Ten MH','Diem'))
for stu in lst_stu:
    print('{:15}{:30}{:15}{:5}'.format(stu[0],stu[1],stu[2],stu[3]))