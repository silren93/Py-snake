num_1=float(input('Nhập giá trị số thứ nhất: '))
num_2=float(input('Nhập giá trị số thứ hai: '))
#cach1
print('Tổng: ', num_1+num_2)
print('Hiệu: ', num_1-num_2)
print('Tích: ', num_1*num_2)
print('Thương: ', num_1/num_2)

print('Thương %.3f' %(num_1/num_2))

print('{} + {} = {}'.format(num_1,num_2,num_1+num_2))
print('{} / {} = {%.2f}'.format(num_1,num_2,num_1/num_2))