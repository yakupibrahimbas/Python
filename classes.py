class Matematik:
    def__init__(self):
    print("Matematik basladi")
    def topla(self,sayi1,sayi2):
        return sayi1+sayi2
    def cikar(self,sayi1,sayi2):
        return sayi1-sayi2

matematik=Matematik()
sonuc=matematik.topla(3,5)
print("Sonuc:"+str(sonuc))    