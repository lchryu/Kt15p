def sum_even_odd_numbers(array):
    sum_even = 0
    sum_odd = 0
    for num in array:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    return sum_even, sum_odd

# Nhập dãy số từ người dùng
n = int(input("Nhập số lượng số trong dãy: "))
while n <= 2:
    print("Số lượng số trong dãy phải lớn hơn 2. Vui lòng nhập lại.")
    n = int(input("Nhập số lượng số trong dãy: "))

array = []
for i in range(n):
    num = int(input("Nhập số thứ {}: ".format(i + 1)))
    array.append(num)

# Gọi hàm để tính tổng các số chẵn và số lẻ trong dãy số
sum_even, sum_odd = sum_even_odd_numbers(array)

# In tổng các số chẵn và số lẻ ra màn hình
print("Tổng các số chẵn trong dãy là:", sum_even)
print("Tổng các số lẻ trong dãy là:", sum_odd)
