istenenKredi=10000
hesap=9300
minimumOlmasiGerekenHesap=10000

if hesap>=minimumOlmasiGerekenHesap:
    print("Kreedi almaya uygunsunuz")
    print("odemeler hesaplandi")
elif hesap>=9000:
    print("Mudure sorulacak")
elif hesap>=9000 and hesap<=9500:
    print("Mudureeye sorulacak")        
else:
    print("Kredi almak icin bakiye yetersiz")    
print("islem sonu")

