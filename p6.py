#set
studentSet={"Engin","Derin","Baby","Coni"}
print(studentSet)

for student in studentSet:
    print(student)

print("Derin" in studentSet)   

if "Derin" in studentSet:
    print("Listede var")
else:
    print("Listede yok")
    studentSet.update(["Merve","Mert","Selin"])
    print(studentSet)

    studentSet.remove("Selin")
    print(len(studentSet))
    studentSet.remove("Selin")
    print(len(studentSet))

 #   x=studentSet.clear
    print(len(studentSet))
    print(studentSet)