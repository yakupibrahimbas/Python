sayi=int(input("Sayi: "))
faktoriyel=1
if sayi<0:
    print("Negatif olmaaaz")
elif sayi==0:
    print("Sonuc:1")
else:
    for i in range(1,sayi+1):
        faktoriyel=faktoriyel*i
        print("Sonuc:",faktoriyel)    