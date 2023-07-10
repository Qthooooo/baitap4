value = float(input("Nhập giá trị: "))

if value > 10 and value > 0:
    print("Giá trị lớn hơn 10 và là số dương")
elif value <= 10 and value > 0:
    print("Giá trị nhỏ hơn hoặc bằng 10 và là số dương")
elif value < 0:
    print("Giá trị là số âm")
else:
    print("Giá trị bằng 0")