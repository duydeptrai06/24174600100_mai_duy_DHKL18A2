import math

# Hàm tìm tất cả các số chính phương nhỏ hơn n
def perfect_squares_less_than(n):
    squares = []
    i = 1
    while i * i < n:
        squares.append(i * i)
        i += 1
    return squares

# Nhập giá trị của n
n = int(input("Nhập một số nguyên dương n: "))
perfect_squares = perfect_squares_less_than(n)
print(f"Các số chính phương nhỏ hơn {n} là: {perfect_squares}")

