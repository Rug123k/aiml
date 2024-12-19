# Take three numbers from the user and find the largest among them.

x=int(input("Enter a number x"))

y=int(input("Enter a number y"))

z=int(input("Enter a number z"))

if x>y & x>z:
    print("x is greater")
elif y>z:
    print("y is gretarer")
else:
    print("z is greatarer")