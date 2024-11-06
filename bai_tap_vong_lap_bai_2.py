# Nhập giá trị của n
n = int(input("Nhập một số nguyên dương n: "))

# Tính S1
S1 = sum(range(1, n + 1))

# Tính S2
S2 = 1
for i in range(1, n):
    S2 *= i

# Tính S3
S3 = 0
for i in range(1, n + 1):
    S3 += ((-1) ** (i + 1)) / i

# Tính S4
S4 = 0
for i in range(n+1):
    S4 += i / (i+2)
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
