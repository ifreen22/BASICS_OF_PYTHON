a = int(input("Enter your age : "))

if (a>=18 and a<30):
    print("congratulation, you are eligible for this scholarship program")
    print("You are eligible for voting")

elif(a>=30):
    print("Sorry, you are not eligible")

elif(a<0):
    print("You are entering the invalid age")

else:
    print("Sorry, you are not eligible")