def find_number_in_array(array, k):
    found = False
    for num in array:
        if num == k:
            found = True
            break
    return found

# Nhập dãy số từ người dùng
array = input("Nhập dãy số, cách nhau bởi dấu cách: ").split()
array = list(map(int, array))  # Chuyển đổi chuỗi nhập vào thành list các số nguyên

# Nhập số K từ người dùng
k = int(input("Nhập số K: "))

# Gọi hàm để tìm số K trong dãy số
if find_number_in_array(array, k):
    print("Số", k, "được tìm thấy trong dãy số.")
else:
    print("Số", k, "không được tìm thấy trong dãy số.")
