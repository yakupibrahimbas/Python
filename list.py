
urunler=["laptop","mouse","keyboard"]
print(urunler)
print(type(urunler))
urunler.append("telefon")
print(urunler)

ogrenciler1=["Engin","Cavit","Berkay"]
ogrenciler2=["Jacob","Ali","Murat"]

ogrenciler1=ogrenciler2
ogrenciler2[0]="Engin"
print(ogrenciler2)
print(ogrenciler1)
print(ogrenciler2)

sayi1=10
sayi2=20
sayi1=sayi2
sayi2=60
print(sayi2)
print(sayi1)

#referans tip -> list
#deger tip ->int
#stack and  heap 
#referans tip->list

isim="Engin"
print(isim[0])
#devops yazilim gelistirme süreci operasyon vs..
bosListe=[]