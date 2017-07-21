file = open("rt2.txt", "r")
x = file.readline()
y = file.read()
file.close()
print(x)
print("First line!")
print(y)
if x == "THIS FILE HAS BEEN ENCRYPTED USING IMES\n":
    print("True!")
else:
    print("False!")
