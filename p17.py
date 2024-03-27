sayilar=[1,2,3,4,5,6,7,8,9,10]
tek_sayilar=[x for x in sayilar if x%2!=0]
cift_sayilar=[x for x in sayilar if x%2==0]

print("tek sayilar:",tek_sayilar)
print("cift sayilar:",cift_sayilar)