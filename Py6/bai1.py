def tinh_bmi(can_nang, chieu_cao):
    bmi=can_nang/(chieu_cao**2)
    return bmi
def loi_khuyen(cs_bmi):
    if 0<cs_bmi<18:
        print('Ốm vậy, ăn nhìu lơnnnn')
    elif 18<=cs_bmi<25:
        print('Cân đối, giữ vậy nhé')
    else:
        print('Thừa cân, cần ăn uống tập luyện theo chế độ')
nang=float(input('Nhập cân nặng (kg): '))
cao=float(input('Nhập chiều cao (m): '))
bmi=tinh_bmi(nang,cao)
print('Chỉ số BMI của bạn: %.1f'%(bmi))
loi_khuyen(bmi)