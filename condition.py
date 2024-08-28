age=input("Please enter your age!\n")
updAge=int(age)

if updAge <=18 and updAge >=1:
    print("Not eligible for vote")
elif updAge >19:
    print("You are eligible for vote")
else:
    print("Invalid access")