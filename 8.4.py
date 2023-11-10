a = int(input("nhap do dai canh a: "))
b = int(input("nhap do dai canh b: "))
c = int(input("nhap do dai canh c: "))
if a+b<c and b+c<b:
    print("day khong phai la tam giac")
else:
    print("day la mot tam giac")
    import math
    p=(a+b+c)/2
    S= math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich tam giac tren la: ",S)
