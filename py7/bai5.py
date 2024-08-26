import math
def tinh_c(n,k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
n=int(input('Nhap diem dung cua tam giac Pascal: '))
for j in range (0,n+1):
    for i in range(0,j+1):
        print(tinh_c(j,i),end='\t')
    print('\n')