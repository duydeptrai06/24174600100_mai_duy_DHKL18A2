import math
x = input("Nhap gia tri x: " )
x = float(x)
if x <= 0:
    print("gia tri khong thoa man")
else:
    print("gia tri thoa man")
f_x = math.log(x, 4 ) + math.log(x, 2)
print("Gia tri can tim f(x) ={f_x:.2f}")

