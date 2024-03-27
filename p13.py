sehirler=["Ankara","Istanbul","Izmir"]
print(sehirler[0])

for sehir in sehirler:
    print(sehir[0:1])

for sehir in sehirler:
    if sehir=="Ankara":
        continue
     #   print(sehir+"icin kod="+sehir[0:3])
      #  print("*******")