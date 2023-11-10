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