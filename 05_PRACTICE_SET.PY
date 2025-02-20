# 1. Write a program to find the greatest of four numbers entered by the user. 
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
d = int(input("Enter a number : "))

if(a>b and a>c and a>d):
    print(a, "is the greatest number")

elif(b>a and b>c and b>d):
    print(b, "is the greatest number")

elif(c>a and c>b and c>d):
    print(c, "is the greatest number")

else:
    print(d, "is the greatest number")





# 2. Write a program to find out whether a student has passed or failed 
# if it requires a total of 40% and at least 33% in each subject to 
# pass. Assume 3 subjects and take marks as an input from the user. 

p = int(input("Enter your physics score : "))
c = int(input("Enter your chemistry score : "))
m = int(input("Enter your maths score : "))

if(40/100*(p+c+m)>=40 and p>=33 and c>=33 and m>=33):
    print("Congratulations, you are pass")

else:
    print("Sorry, you are fail")





# 3. Write a program to find whether a given username contains less than 
# 10 characters or not. 

u = (input("Enter a username : "))
    
if(len(u)<10):
    print("Congrats, your username is valid")

else:
    print("Invalid username")





# 4. Write a program which finds out whether a given name is present 
# in a list or not.

t = ("Ifreen", 99, 56.35, "Amisha", "Nisha", "Pooja", "pc", "Atif")
f = input("Enter a name : ")

if(f in t):
    print("Yes, the given name is present in the list")

else:
    print("No, the given name is not present in the list")





# 5. Write a program to calculate the grade of a student from his marks 
# from the scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F 

marks = float(input("Enter your marks : "))

if(marks>90 and marks<=100):
    print("Ex Grade")

elif(marks>80 and marks<=90):
    print("A Grade")

elif(marks>70 and marks<=80):
    print("B Grade")

elif(marks>60 and marks<=70):
    print("C Grade")

elif(marks>50 and marks<=60):
    print("D Grade")

else:
    print("Sorry, you are fail")





# 6. Write a program to find out whether a given post is talking about 
# “Harry” or not. 
post = input("Enter a post : ")

if("Harry".lower() in post.lower()):   # also valid for a list (in)
    print("Yes, the post is talking about Harry")

else:
    print("No, the post is talking about another topic")