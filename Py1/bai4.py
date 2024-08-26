'''
chieu_dai=float(input("Nhập chiều dài: "))
chieu_rong=float(input("Nhập chiều rộng: "))
print("Chu vi hình chữ nhật= ", (chieu_dai+chieu_rong)*2)
print("Diện tích hình chữ nhật= ", chieu_dai*chieu_rong)

'''
chieu_dai, chieu_rong=eval(input('Nhập chiều dài và chiều rộng: '))
print('Chu vi: ({} + {})*2={}'.format(chieu_dai, chieu_rong,(chieu_dai+chieu_rong)*2))
print('Diện tích: {} * {} = {}'.format(chieu_dai,chieu_rong,chieu_dai*chieu_rong))