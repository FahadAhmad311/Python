age= input("Enter your age")
print(type(age))

age_updated=int(age)
print(type(age_updated))

if(age_updated < 15):
    print(" Not Eligible")

elif(age_updated >15 and age_updated <=30):
    print(" You are eligible")

elif(age_updated > 31 and age_updated <=50 ):
    print(" You are Overage")      

else:
    print("Invalid Input")    