# Nhập số cần kiểm tra
o = int(input("Nhập một số nguyên dương: "))

# Tính tổng các ước của số
sum_tong_cac_uoc = 0
for i in range(1, o):
    if o % i == 0:
        sum_tong_cac_uoc += i

# Kiểm tra nếu tổng các ước bằng số nhập vào
if sum_tong_cac_uoc == o:
    print(f"{o} là số hoàn hảo.")
else:
    print(f"{o} không phải là số hoàn hảo.")
