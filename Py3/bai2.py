input_name=input('Nhap ho ten de xu ly: ')
'''for char in input_name:
    if char==' ':
        break
    else:
        print(char, end=',')
'''
for char in input_name:
    if char==' ':
        continue
    print(char,end=',')