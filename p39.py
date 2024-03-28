liste=[10,20,30,40,50]

toplam=0
adet=len(liste)

for sayi in liste:
    toplam+=sayi

ortalama=toplam/adet
print("Sayilarin Ortalamasi:",ortalama)