# Nhập tọa độ điểm M và thông tin hình tròn
x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))
a = float(input("Nhập tọa độ x của tâm I: "))
b = float(input("Nhập tọa độ y của tâm I: "))
R = float(input("Nhập bán kính R: "))
# Tính khoảng cách từ điểm M đến tâm I
khoang_cach = (x - a) ** 2 + (y - b) ** 2
ban_kinh_binh_phuong = R ** 2
if khoang_cach <= ban_kinh_binh_phuong:
    print("điểm M thuộc đường tròn:{True3}")
else:
    print("điểm M không thuộc đường tròn:{False}")

    
   


