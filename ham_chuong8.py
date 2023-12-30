def chuong8_bai1():
    print("Bài toán tìm số lớn nhất và nhỏ nhất.")
a=int(input("Nhập số a:"))
b=int(input("Nhập số b:"))
c=int(input("Nhập số c:"))
d=int(input("Nhập số d:"))
g=0
h=0
while(g<a)or(g<b)or(g<c)or(g<d):
    g+=1
h=g
while(h>a)or(h>b)or(h>c)or(h>c):
    h-=1
print("max =",g)
print("min =",h)
def chuong8_bai2():
    a=int(input("Nhập số:"))
print("Giá trị tuyệt đối của",a,"là:","|",a,"|=",abs(a))
def chuong8_bai3():
    print("Giải phương trình ax+b=0")
a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm.")
    else: print("Phương trình vô nghiệm.") 
else: 
    print('Nghiệm của phương trình là: x = ', -b/a)
def chuong8_bai4():
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
def chuong8_bai5():
    a = int(input("Nhap nam: "))
if ((a%4==0) and (a%100!=0) or (a%400==0)):
    print("nam", a, "la nam nhuan")
else:
    print("nam", a, "khong phai la nam nhuan")

def chuong8_bai6():
    loai_xe=int(input("Cho biết loại xe là 4/7 ?"))
    so_km=float(input("Nhập số km chạy bằng = "))
    time_cho=float(input("Cho biết thời gian chờ (phút chờ) = "))
    tien_cuoc=float(0)
    tien_di_chuyen=float(0)
    if time_cho >=5:
        tien_cho=(time_cho-5)*0.8
    else:
        tien_cho=0
    if loai_xe==4:
        if so_km <=0.8:
            tien_di_chuyen=0.8*11000
        elif so_km <=20:
            tien_di_chuyen=0.8*11000+(20-so_km)*12100
        else:
            tien_di_chuyen=0.8*11000+(20-0.8)*12100+(so_km-20)*10000
        tien_cuoc=tien_cho+tien_di_chuyen
        print("Cước phí xe taxi 4 chỗ của quý khách là %0.2f"%tien_cuoc)
    if loai_xe==7:
        if so_km <=0.8:
            tien_cuoc+tien_cho+0.8*13000
        elif so_km <=30:
            tien_cuoc=tien_cho+0.8*13000+(30-so_km)*14100
        else:
            tien_cuoc=tien_cho+0.8*13000+(30-0.8)*14100+(so_km-30)*12000
        tien_cuoc=tien_cho+tien_di_chuyen
        print("Cước phí xe taxi 7 chỗ của quý khách là %0.2f"%tien_cuoc)

def chuong8_bai7():
    a=eval(input("Nhập số KWh tiêu thụ:"))
if a>=0:
    if a<=50:
       print("Tổng số tiền phải trả là:",a*1678,"đồng.")
    elif a<=100:
       print("Tổng số tiền phải trả là:",50*1678+(a-50)*1734,"đồng.")
    elif a<=200:
       print("Tổng số tiền phải trả là:",50*(1678+1734)+(a-100)*2014,"đồng.")
    elif a<=300:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014)+(a-200)*2536,"đồng.")
    elif a<=400:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014+2536)+(a-300)*2834,"đồng.")
    else:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014+2536+2834)+(a-400)*2927,"đồng.")     
else:
   print("Số KWh không hợp lệ.")
     
def chuong8_bai8():
    print("Các mã loại phòng cho bạn:")
print("1-Standard")
print("2-Superior Garden View")
print("3-Superior Ocean View")
print("4-Garden View Bungalow")
print("5-Pool View Bungalow")
print("6-Family Room")
print("7-Beach Front Bungalow")
print("8-VIP sea View")
a=eval(input("Nhập mã loại phòng:"))
b=eval(input("Nhập số đêm:"))
if a>0&a<=8:
    if a==1: c=1260000
    elif a==2: c=1550000
    elif a==3: c=1830000
    elif a==4: c=1830000
    elif a==5: c=2120000
    elif a==6: c=2120000
    elif a==7: c=2540000
    elif a==8: c=4800000
    else: 
        print("Vui lòng chọn lại mã loại phòng.")
else: print("Vui lòng chọn lại mã loại phòng.") 
if b==1:
    print("Giá  tiền phải trả là:",c,"đồng.")
elif b==2:
    print("Giá  tiền phải trả là:",c*b*0.75,"đồng.") 
elif b==3:
    print("Giá  tiền phải trả là:",c*b*0.75,"đồng.") 
elif b>=4:
    print("Giá  tiền phải trả là:",c*b*0.7,"đồng.")       
else:
    print("Vui lòng nhập lại số đêm.")

def chuong8_bai9():
     a = int(input("nhap so a: "))
for i in range(a,0,-1):
    print(i)

def chuong8_bai10():
    print("Nhập n:")
n=eval(input(""))
print("Nhập x:")
x=eval(input(""))
s=(x*x+1)**n
print("(S=x*x+1)^n =",s)

def chuong8_bai11():
    n=float(input("số nguyên"))
x=float(input("số thực"))
a=(x*x +x +1)**n + (x*x -x +1)**n
print(a) 

def chuong8_bai12():
    n = int(input("Nhập số n = "))
flag = True 
if n < 2 :
    print(n, "Không nguyên tố !!!")
else:
    for i in range(2, n):
        if n%i == 0:
            flag = False
            break
    if flag:
        print(n, " là số nguyên tố")
    else:
        print(n, " không phải là số nguyên tố!!!") 

def chuong8_bai13():
    n = int(input("nhập số N: "))
def A(n):
    j = []
    a = 0
    for i in range(1,n):
        j.append(i)
    for v in j:
        a = a + v
    return print("A = ",a)
def B(n):
    j = []
    a = 0
    for i in range(1,n):
        if i%2==0:
            j.append(i)
    for v in j:
        a = a + v
    return print("B = ",a)
def C(n):
    j = []
    a = 1
    for i in range(1,n):
        j.append(i)
    for v in j:
        a = a*v
    return print("C = ",a)
def D(n):
    j = []
    a = 1
    for i in range(1,n):
        if i%3==0:
            j.append(i)
    for v in j:
        a = a + v
    return print("D = ",a)
def E(n):
    j = []
    a = 0
    for i in range(2,n+1):
        if i>0:
            for k in range(2,int(math.sqrt(i))+1):
                if i%k ==0:
                    break
            else:
                j.append(i)
    for v in j:
        a = a + v
    print("E = ",a)    
def F(n):
    j = []
    a = 1
    for i in range(1,n):
        j.append(i**-1)
    for v in j:
        if i%2==0:
            a = a + v
        else:
            a = a - v 
    return print("F = ",a - 1)
A(n)
B(n)
C(n)
D(n)
E(n)
F(n)

def chuong8_bai14():
    a = int(input("nhập số nguyên N: "))
b = 0
for i in range(1, a+1):
    print("nhập số hạng thứ:", i)
    b1 = int(input())
    b = b + b1
print("tổng",a,"số hạng là ", b)

def chuong8_bai15():
    a = True
S = 0
while a:
    print("nhập số nguyên N: ")
    b = int(input())
    S = S + b
    if b ==0:
        a = False
        break
print("tổng số hạng vừa nhập là: ",S)

def chuong8_bai16():
    a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
while(a*b!=0):
    if a>b:
        a%=b
    else:
        b%=a
print(a+b) 

def chuong8_bai17():
    a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = a*b
for i in range (b, c+1):
    if i%a == 0 and i%b == 0:
        d = i
        break
print(i)

def chuong8_bai18():
    print("Nhập vào số N lớn hơn 0: ")
n = int(input())
tong = 0
for i in range(1, n):
    if (n % i == 0):
        tong += i
if (tong == n):
    print(n, " là số hoàn hảo")
else:
    print(n, " không phải là số hoàn hảo")

def chuong8_bai19():
    n = 20
for i in range(n, 0, -1):
    if i % 2 != 0:
        print(i, end= " ")
