def tinh_S(n,x):
    result = (x**2+1)**n
    return result
x=int(input("nhap vao x"))
n=float(input("nhap vao n"))
ket_qua = tinh_S(n,x)
print(f"kết quả : {ket_qua} ")