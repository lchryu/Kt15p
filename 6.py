def xoa_ky_tu_giong_nhau(xau):
    xau_moi = ""
    ky_tu_truoc = ''
    for ky_tu in xau:
        if ky_tu != ky_tu_truoc:
            xau_moi += ky_tu
        ky_tu_truoc = ky_tu
    return xau_moi

# Nhập vào xâu từ người dùng
xau = input("Nhập vào xâu: ")

# Gọi hàm xoa_ky_tu_giong_nhau để xóa các ký tự giống nhau liền kề trong xâu
xau_moi = xoa_ky_tu_giong_nhau(xau)

# In ra màn hình xâu sau khi đã xóa các ký tự giống nhau liền kề
print("Xâu sau khi xóa các ký tự giống nhau liền kề: ", xau_moi)
