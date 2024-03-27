vize=int(input("vize notu: "))
final=int(input("final notu: "))

vizeSon=(vize*40)/100
finalSon=(final*60)/100

toplam=vizeSon+finalSon
if toplam<50 :
    print("kaldiniz")
else:
    print("gectiniz")    