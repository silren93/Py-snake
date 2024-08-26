n = int(input("Nhập số nguyên n: "))

#tinh tong cac so chan
tong_chan=0
str_tong_chan="B="
for i in range(2, n+1, 2):
    #tong_le=tong_le+i
    tong_chan+=i
    str_tong_chan+=str(i)+'+'
ket_qua=str_tong_chan.rstrip('+') + "=" #loai bo dau + dang bi du va ghep dau = vao bieu thuc tra ket qua
print(ket_qua, tong_chan)
#tinh tich
tich=1
str_tich="C="
for i in range(1,n+1):
    #tong_le=tong_le+i 
    tich*=i
    str_tich+=str(i)+'*'
ket_qua=str_tich.rstrip('*') + "=" #loai bo dau + dang bi du va ghep dau = vao bieu thuc tra ket qua