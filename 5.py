def xoa_ky_tu_so(xau):
    xau_moi = ""
    for ky_tu in xau:
        if not ky_tu.isdigit():
            xau_moi += ky_tu
    return xau_moi

# Nhập vào xâu từ người dùng
xau = input("Nhap vao xau: ")

# Gọi hàm xoa_ky_tu_so để xóa đi các ký tự số trong xâu
xau_moi = xoa_ky_tu_so(xau)

# In ra màn hình xâu sau khi đã xóa đi các ký tự số
print("Xau sau khi xoa ky tu so: ", xau_moi)
