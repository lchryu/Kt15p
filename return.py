import os 
os.system("clear")
def tinhTong(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum       


# bat dau chay tu day
n = input("Nhập vào một số bất kỳ: ")
print(tinhTong(n))