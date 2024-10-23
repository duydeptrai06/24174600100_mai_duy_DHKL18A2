import math 

#Nhập bán kính và chiều cao 
r = float(input("Nhap ban kinh"))
h = float(input("Nhap chieu cao"))
if h>0 and r>0:
 print("bán kính hoặc chiều cao không âm")
else:
 print("gia tri nhap khong thoa man")

#Tính diện tích xung quanh và diện tích toàn phần và thể tich hình trụ
dien_tich_xung_quanh = 3.14 * 2 * r * h
dien_tich_toan_phan = 3.14 * r ** 2 * h
the_tich_hinh_tru = 3.14 * r ** 2 * h

#Làm tròn 
dien_tich_toan_phan = round(dien_tich_toan_phan, 2)
dien_tich_xung_quanh = round(dien_tich_xung_quanh, 2)
the_tich_hinh_tru = round(the_tich_hinh_tru, 2)

#In kết quả
print("dien tich xung quanh la:",dien_tich_xung_quanh)
print("dien tich toan phan la:",dien_tich_toan_phan)
print("the tich hinh tru la:",the_tich_hinh_tru) 