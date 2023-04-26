def la_nam_nhuan(nam):
    if nam % 400 == 0:
        return True
    elif nam % 4 == 0 and nam % 100 != 0:
        return True
    else:
        return False

# Nhập vào năm từ người dùng
nam = int(input("Nhap vao nam: "))

# Gọi hàm la_nam_nhuan để kiểm tra năm có phải là năm nhuận hay không
if la_nam_nhuan(nam):
    print(nam, "la nam nhuan.")
else:
    print(nam, "khong la nam nhuan.")
