# Nhập số cần kiểm tra
a = int(input("Nhập một số nguyên dương: "))

# Kiểm tra xem số có phải là số nguyên tố không
if a < 2:
    print(f"{a} không phải là số nguyên tố.")
else:
    la_so_nguyen_to = True
    for i in range(2, int(a ** 0.5) + 1):
        if a%i == 0:
            la_so_nguyen_to = False
            break

    if la_so_nguyen_to:
        print(f"{a} là số nguyên tố.")
    else:
        print(f"{a} không phải là số nguyên tố.")
