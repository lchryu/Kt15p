while True:
    try:
        num = int(input("Nhập một số nguyên dương: "))
        if num > 0:
            print("Số bạn đã nhập là:", num)
            break
        else:
            print("Bạn cần nhập một số nguyên dương. Vui lòng nhập lại.")
    except ValueError:
        print("Bạn cần nhập một số nguyên dương. Vui lòng nhập lại.")

'''
Đoạn mã trên sử dụng vòng lặp while vô hạn
để liên tục yêu cầu người dùng nhập một số.
Nếu giá trị nhập vào là một số nguyên dương đúng định dạng, 
thì giá trị đó sẽ được in ra màn hình và vòng lặp sẽ dừng lại bằng cách sử dụng lệnh break. 
Nếu giá trị nhập vào không phải số nguyên dương, hoặc không phải một số hợp lệ, 
thì thông báo lỗi sẽ được in ra và vòng lặp sẽ tiếp tục yêu cầu người dùng nhập lại.
'''



