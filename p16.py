def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)

sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
print("Faktöriyel:", faktoriyel(sayi))
