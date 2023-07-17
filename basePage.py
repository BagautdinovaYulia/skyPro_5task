a = int(input("Стаж:"))
b = int(input("Больничный(1-брал, 0-не брал):"))

if a > 3:
    if b == 1:
        print("Премия 30%")
    else:
        print("Премия 33%")
elif 1.5 <= a <= 3:
    if b == 1:
        print("Премия 15%")
    else:
        print("Премия 17%")
else:
    print("Без премии")
