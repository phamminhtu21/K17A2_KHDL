def tinh_S(n, x):
    # Tính giá trị A = (x^2 + x + 1)^n + (x^2 - x + 1)^n
    result = (x**2 + x + 1)**n + (x**2 - x + 1)**n
    return result

# Sử dụng phương thức
n = int(input("Nhập giá trị n: "))
x = float(input("Nhập giá trị x: "))

ket_qua = tinh_S(n, x)
print(f"Kết quả: {ket_qua}")