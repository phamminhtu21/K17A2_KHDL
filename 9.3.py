def tinh_bmi (chieu_cao , can_nang):
    bmi=can_nang/(chieu_cao*chieu_cao)
def phan_loai(bmi):
    if bmi < 18.5:
        return "thieu can"
    elif 18.5 <= bmi < 24.99:
        return "binh thuong"
    elif 24.99 <= bmi >= 25:
        return "thua can"
    else :
        return "beo phi"
trong_luong=float(input("nhap can nang(kg):"))
chieu_cao=float(input("nhap chieu cao(m):"))
print(tinh_bmi)
print(phan_loai)