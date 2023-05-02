def tinhTong(n):
    sum = 0
    for i in n:
        sum += int(i)
    print("Tổng các chữ số của", n, "là", sum)        


# bat dau chay tu day
n = input("Nhập vào một số bất kỳ: ")
tinhTong(n)