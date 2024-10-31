diem_chuyen_can = float(input("nhập điểm chuyên cần: "))
diem_giua_ki = float(input("nhập điểm giữa kì: "))
diem_cuoi_ki = float(input("nhập điểm cuối kì: "))
diem_trung_binh = (diem_chuyen_can + diem_giua_ki + diem_cuoi_ki ) / 3

if diem_trung_binh >= 9:
 loai = "A"
elif diem_trung_binh >= 7 and diem_trung_binh < 9:
      loai = "B"
elif diem_trung_binh >= 5 and  diem_trung_binh < 7:
      loai = "C"
else:
    loai = "D"
print(f"điểm của sinh viên là: {diem_trung_binh:.2f}")
print(f"xếp loại: {loai}")
