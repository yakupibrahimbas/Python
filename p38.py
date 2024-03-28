sayilar=[]

while True:
    sayi=int(input("Bir sayi girin:"))
    if sayi==0:
        break
    sayilar.append(sayi)

toplam=sum(sayilar)
adet=len(sayilar)
print("sayilarin ortalamasi:",toplam/adet)
