import math

#Nhập vào giá trị x
x =float(input("Nhap vao gia tri x"))
if x != 0:
    print("giá trị x thỏa mãn")
else:
    print("giá trị x không thỏa mãn")
#Tính giá trị của biểu thức
gia_tri_cua_bieu_thuc = (-x) + (x ** 2) ** (1/2) / (x ** 4 + 1) ** (1/7)
#Làm tròn 
gia_tri_cua_bieu_thuc = round(gia_tri_cua_bieu_thuc, 2)
#In kết quả
print("gia tri bieu thuc la:" , gia_tri_cua_bieu_thuc)
                                                                