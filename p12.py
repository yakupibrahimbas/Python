sayi1=int(input("1.sayi:"))
sayi2=int(input("2.sayi:"))
sayi3=int(input("3.sayi:"))

if(sayi1>=sayi2)and(sayi1>=sayi3):
    enBuyuk=sayi1
elif(sayi2>=sayi1)and(sayi2>=sayi3):
    enBuyuk=sayi2
else:
    enBuyuk=sayi3
print("En buyuk"+sayi3)            