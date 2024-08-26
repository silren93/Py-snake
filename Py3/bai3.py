n = int(input("Nhập số nguyên n: "))

# Tính A = tổng các số lẻ nhỏ hơn hay bằng n
A = sum(i for i in range(1, n+1, 2))

# Tính B = tổng các số chẵn nhỏ hơn hay bằng n
B = sum(i for i in range(0, n+1, 2))

# Tính C = tích các số từ 1 đến n
C = 1
for i in range(1, n+1):
    C *= i

# Tính D = tích các số chia hết cho 3 nhỏ hơn hay bằng n
D = 1
for i in range(3, n+1, 3):
    D *= i

print("A = tổng các số lẻ nhỏ hơn hay bằng n: ", A)
print("B = tổng các số chẵn nhỏ hơn hay bằng n: ", B)
print("C = tích các số từ 1 đến n: ", C)
print("D = tích các số chia hết cho 3 nhỏ hơn hay bằng n: ", D)
