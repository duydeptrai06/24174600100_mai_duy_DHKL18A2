# Hàm kiểm tra một số có phải là số nguyên tố không?
a = int(input("nhập một số nguyên tố: "))
if a < 2:
        print("False")
for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
    
         print("True")

# Hàm tìm tất cả các số nguyên tố nhỏ hơn n
n = int(input("nhập các số nhỏ hơn: "))
so_nguyen_to = []
for i in range(2, n):
        if so_nguyen_to(i):
            so_nguyen_to (i)
        print("là số nguyên tố")

# Nhập giá trị của n
n = int(input("Nhập một số nguyên dương n: "))
so_nguyen_to = so_nguyen_to(n)
print(f"Các số nguyên tố nhỏ hơn {n} là: {so_nguyen_to}")
