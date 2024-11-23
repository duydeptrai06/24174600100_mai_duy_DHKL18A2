import math

# Nhập vào số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))

if n >= 6:
    S = 0
    for k in range(6, n + 1):
        S += math.sqrt(k ** 2 + 1) / (2 * k)
    print(f"Tổng S là: {S}")
else:
    print("n phải lớn hơn hoặc bằng 6.")






