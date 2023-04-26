# Nhập điểm của học sinh từ người dùng
diem = float(input("Nhap diem cua hoc sinh: "))

# Xếp loại học lực dựa trên giá trị điểm
if diem >= 9.0:
    xep_loai = "Xuat sac"
elif diem >= 8.0:
    xep_loai = "Gioi"
elif diem >= 7.0:
    xep_loai = "Kha"
elif diem >= 5.0:
    xep_loai = "Trung binh"
else:
    xep_loai = "Yeu"

# In ra màn hình xếp loại học lực của học sinh
print("Xep loai hoc luc: ", xep_loai)
