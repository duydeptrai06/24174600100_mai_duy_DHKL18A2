ds_hang_hoa = []


def nhap_hang_hoa():
    try:
        ma_hang = input("Nhập mã hàng: ")
        ten_hang = input("Nhập tên hàng: ")
        don_vi_tinh = input("Nhập đơn vị tính: ")
        don_gia = float(input("Nhập đơn giá: "))
        so_luong = int(input("Nhập số lượng: "))
        thanh_tien = don_gia * so_luong
        thue_vat = thanh_tien * 0.1
        hang_hoa = {
            "ma_hang": ma_hang,
            "ten_hang": ten_hang,
            "don_vi_tinh": don_vi_tinh,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "thanh_tien": thanh_tien,
            "thue_vat": thue_vat
        }
        ds_hang_hoa.append(hang_hoa)
        print("Đã thêm mặt hàng thành công!")
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng cho đơn giá hoặc số lượng!")


def xem_danh_sach_hang_hoa():
    if not ds_hang_hoa:
        print("Danh sách hàng hóa trống!")
        return
    print(f"{'Mã hàng':<15}{'Tên hàng':<20}{'ĐVT':<10}{'Đơn giá':<10}{'Số lượng':<10}{'Thành tiền':<15}{'Thuế VAT':<10}")
    print("-" * 80)
    for hang in ds_hang_hoa:
        print(f"{hang['ma_hang']:<15}{hang['ten_hang']:<20}{hang['don_vi_tinh']:<10}{hang['don_gia']:<10}{hang['so_luong']:<10}{hang['thanh_tien']:<15}{hang['thue_vat']:<10}")


def xoa_hang_hoa():
    try:
        ma_hang = input("Nhập mã hàng cần xóa: ")
        for hang in ds_hang_hoa:
            if hang["ma_hang"] == ma_hang:
                ds_hang_hoa.remove(hang)
                print("Đã xóa mặt hàng thành công!")
                return
        print("Không tìm thấy mặt hàng!")
    except Exception as e:
        print(f"Lỗi: {e}")


def sua_hang_hoa():
    
        ma_hang = input("Nhập mã hàng cần sửa: ")
        for hang in ds_hang_hoa:
            if hang["ma_hang"] == ma_hang:
                print("Nhập thông tin mới (bỏ trống để giữ nguyên):")
                ten_hang = input("Tên hàng: ")
                if ten_hang:
                    hang["ten_hang"] = ten_hang
                don_vi_tinh = input("Đơn vị tính: ")
                if don_vi_tinh:
                    hang["don_vi_tinh"] = don_vi_tinh
                don_gia = input("Đơn giá: ")
                if don_gia:
                    hang["don_gia"] = float(don_gia)
                so_luong = input("Số lượng: ")
                if so_luong:
                    hang["so_luong"] = int(so_luong)
                hang["thanh_tien"] = hang["don_gia"] * hang["so_luong"]
                hang["thue_vat"] = hang["thanh_tien"] * 0.1
                print("Đã cập nhật thông tin mặt hàng!")