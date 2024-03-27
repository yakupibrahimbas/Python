sozluk={
    "book":"kitap",
    "table":"masa",
}
print(sozluk["book"])
sozluk["pencil"]="kalem"
print(sozluk)

sozluk2=dict(kitap='book',masa='table')
print(sozluk2)
del(sozluk["book"])
print(len)