while True:
    num = input("Nhập vào một số nguyên: ")
    try:
        num = int(num)
        if num < 0:
            print("Số bạn nhập không phải là số âm. Vui lòng nhập lại.")
        else:
            print("Bạn vừa nhập số ", num)
            break
    except ValueError:
        try:
            num = float(num)
            print("Số bạn nhập là số thực.")
            break
        except ValueError:
            print("Bạn đã không nhập một số hợp lệ. Vui lòng nhập lại.")
