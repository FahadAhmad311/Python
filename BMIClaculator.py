#print("")
weight=input("Enter weight in kg")
print(weight)
height=input(("Enter height in meters"))
print(height)
updweight=int(weight)
updheight=float(height)

bmi=updweight/(updheight*updheight)
upbmi=str(bmi)

print("Your bmi is "+upbmi)