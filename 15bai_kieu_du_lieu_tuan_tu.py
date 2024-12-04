
# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Tạo danh sách A chứa các số lẻ nhỏ hơn n
A = [i for i in range(n)
      if i % 2 != 0]

# Tạo danh sách B chứa các số chẵn nhỏ hơn n
B = [i for i in range(n)
      if i % 2 == 0]

# Sắp xếp các danh sách A và B theo thứ tự giảm dần
A.sort(reverse=True)
B.sort(reverse=True)

# In ra danh sách A và B
print("Danh sách A (số lẻ):", A)
print("Danh sách B (số chẵn):", B)


#bài6
# Nhập kích thước của ma trận (m hàng, n cột)
m = int(input("Nhập số lượng hàng m: "))
n = int(input("Nhập số lượng cột n: "))

# Khởi tạo ma trận A
A = []

# Nhập giá trị cho từng phần tử trong ma trận
print("Nhập các phần tử cho ma trận A:")
for i in range(m):
    # Nhập một dòng dữ liệu và chuyển thành danh sách các số
    row = list(map(int, input(f"Nhập phần tử cho hàng {i+1} (cách nhau bằng dấu cách): ").split()))
    A.append(row)

# In ra ma trận
print("Ma trận A là:")
for row in A:
    print(row)

#bài8 Viết chương trình đảo vị trí hai cột i, j của ma trận A kích cỡ m*n
# Nhập kích thước của ma trận (m hàng, n cột)
m = int(input("Nhập số lượng hàng m: "))
n = int(input("Nhập số lượng cột n: "))

# Khởi tạo ma trận A
A = []

# Nhập giá trị cho từng phần tử trong ma trận
print("Nhập các phần tử cho ma trận A:")
for i in range(m):
    # Nhập một dòng dữ liệu và chuyển thành danh sách các số
    row = list(map(int, input(f"Nhập phần tử cho hàng {i+1} (cách nhau bằng dấu cách): ").split()))
    A.append(row)

# Nhập chỉ số của hai cột cần đảo
i = int(input("Nhập chỉ số cột i cần đảo: "))
j = int(input("Nhập chỉ số cột j cần đảo: "))

# Đảo vị trí hai cột i và j
for row in A:
    row[i], row[j] = row[j], row[i]

# In ra ma trận sau khi đảo cột
print("Ma trận A sau khi đảo cột:")
for row in A:
    print(row)



#bai9
import numpy as np

# Nhập kích thước của ma trận (m hàng, n cột)
m = int(input("Nhập số lượng hàng m: "))
n = int(input("Nhập số lượng cột n: "))

# Khởi tạo và nhập ma trận A
A = []
print("Nhập ma trận A:")
for i in range(m):
    row = list(map(int, input(f"Nhập phần tử cho hàng {i+1}: ").split()))
    A.append(row)

# Khởi tạo và nhập ma trận B
B = []
print("Nhập ma trận B:")
for i in range(m):
    row = list(map(int, input(f"Nhập phần tử cho hàng {i+1}: ").split()))
    B.append(row)

# Chuyển ma trận A và B thành dạng numpy array để tiện xử lý
A = np.array(A)
B = np.array(B)

# Tính tổng của hai ma trận A và B
sum_matrix = A + B
print("\nTổng của hai ma trận A và B là:")
print(sum_matrix)

# Tính hiệu của hai ma trận A và B
diff_matrix = A - B
print("\nHiệu của hai ma trận A và B là:")
print(diff_matrix)

# Nhập một số k và tính tích của ma trận A với k
k = int(input("\nNhập số k để nhân với ma trận A: "))
product_k_matrix = A * k
print(f"\nTích của ma trận A với số {k} là:")
print(product_k_matrix)

# Tính tích của hai ma trận A và B
# Chỉ có thể tính tích ma trận nếu số cột của ma trận A bằng số hàng của ma trận B
if A.shape[1] == B.shape[0]:
    product_AB = np.dot(A, B)
    print("\nTích của hai ma trận A và B là:")
    print(product_AB)
else:
    print("\nKhông thể tính tích của hai ma trận A và B (số cột của A không bằng số hàng của B).")

# Tính ma trận đối xứng của ma trận A (ma trận chuyển vị)
transpose_A = A.T
print("\nMa trận đối xứng của ma trận A (ma trận chuyển vị) là:")
print(transpose_A)

