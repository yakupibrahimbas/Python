n=int(input("n sayisi:"))
toplam=0
for i in range(n):
    if i%2==1:
        toplam+=i
print("tek sayilar:",toplam)        