import random

so_luot = 3
lst_random = []

for _ in range(so_luot):
    while True:
        number = int(input('Nhập vào một số bất kỳ: '))
        if 0 <= number < 100:
            break
        else:
            print('Nhập lại số trong phạm vi từ 0-99: ')
    
    lucky_number = random.randrange(0, 100)
    lst_random.append(lucky_number)
    
    print('Số may mắn của chương trình: ', lucky_number)
    if number in lst_random:
        print('Chúc mừng bạn đã trúng thưởng')
    else:
        print('Chúc bạn may mắn lần sau')
