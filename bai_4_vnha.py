a = float(input("nhập a: "))
b = float(input("nhập b: "))
c = float(input("nhập c: "))
if a + b > c:
   a + c > b
   b + c > a
   print("là tam giác thường")
if a == b == c:
    print("là tam giác đều")
if a**2 + b**2 == c**2:
     a**2 + c**2 == b**2
     b**2 + c**2 == a**2
     print("là tam giác vuông")
if a == b:
    a**2 + b**2 == c**2
    a == c
    a**2 + c**2 == b**2
    b == c
    b**2 + c**2 == a**2
    print("là tam giác vuông cân")
else:
    print("không phải ba cạnh tam giác")   





