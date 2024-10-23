t = int(input("Nhap thoi gian su dụng bong den (s): "))
if t > 0:
  #đổi giây ra giờ
  h = t/3600
  print(f"số giờ điện đã dùng là {h}")
else:
  print("số giây sử dụng không hợp lệ")
hieu_dien_the = 220
cuong_do_dong_dien = 2.7
cong_suat = t*hieu_dien_the*cuong_do_dong_dien/3600*1000
tien_phai_tra = cong_suat * 7000
print(f"Tien dien phai tra: {tien_phai_tra}")