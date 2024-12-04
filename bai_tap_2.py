while True:
    n = input("Nhập vào số phần tử n trong danh sách: ")
    if not n.isdigit() or int(n) <= 0:  
        print("Yêu cầu nhập lại số nguyên dương!")
    else:
        n = int(n)
        break

# Nhập các giá trị cho danh sách
for i in range(n):
    while True:
        so = input(f"Nhập giá trị số thứ {i + 1}: ")
        
        
        if so.lstrip('-').replace('.', '', 1).isdigit() and so.count('.') <= 1:
            ds_so.append(float(so))  
            break
        else:
            print("Yêu cầu nhập vào số hợp lệ!")


tong = sum(ds_so)
print(f"Tổng các số vừa nhập: {tong}")
