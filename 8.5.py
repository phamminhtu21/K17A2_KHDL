a = int(input("Nhap nam: "))
if ((a%4==0) and (a%100!=0) or (a%400==0)):
    print("nam", a, "la nam nhuan")
else:
    print("nam", a, "khong phai la nam nhuan")