#====Nested if else

x =10

if x >= 0:
    print("X is a negative")
else:
    print(" x is positive")
    if(x%2)==0:
        print("x is even")
    else:
        print("X is odd")

name = input("Enter a name: ")

if name == "Max":
    print("Name Entered is: ", name)

elif name =="Leo":
    print("Name Entered is : ", name)

elif name == "Eli":
    print(" Name Entered is : ", name)

else:
    print(" The  Name Entered is Invalid")