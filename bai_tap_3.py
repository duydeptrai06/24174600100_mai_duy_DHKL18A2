#Nhập vào số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))

# Tạo danh sách A và B
A = [i for i in range(n) if i % 2 != 0]
B = [i for i in range(n) if i % 2 == 0]

# Sắp xếp dãy số theo thứ tự giảm dần
A.sort(reverse=True)
B.sort(reverse=True)

print("Danh sách A (số lẻ nhỏ hơn n):", A)
print("Danh sách B (số chẵn nhỏ hơn n):", B)