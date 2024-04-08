import re

def tinh_tong_so(string):
    # Tìm tất cả các số trong chuỗi sử dụng biểu thức chính quy
    numbers = re.findall(r'-?\d+', string)

    # Khởi tạo tổng các số dương và tổng các số âm
    tong_duong = 0
    tong_am = 0

    # Tính tổng các số dương và tổng các số âm
    for num in numbers:
        num = int(num)
        if num > 0:
            tong_duong += num
        else:
            tong_am += num

    return tong_duong, tong_am

chuoi = "-100#^sdfkj8902w3ir021@swf-20"
tong_duong, tong_am = tinh_tong_so(chuoi)

print("Tổng các số dương trong chuỗi:", tong_duong)
print("Tổng các số âm trong chuỗi:", tong_am)
