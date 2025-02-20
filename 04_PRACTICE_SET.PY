# 1. Write a program to create a dictionary of Hindi words with values as 
# their English translation. Provide user with an option to look it up!

w1 = {
 "enemy":"dushman",
 "chaman":"phool",
 "goal":"lakshya",
 "cry":"rona" }

w2 = input("Enter the word you want meaning of : ")

print(w1[w2])





# 2. Write a program to input eight numbers from the user and display all 
# the unique numbers (once).
x = set()
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
d = int(input("Enter a number : "))
e = int(input("Enter a number : "))
f = int(input("Enter a number : "))
g = int(input("Enter a number : "))
h = int(input("Enter a number : "))

x.add(a)
x.add(b)
x.add(c)
x.add(d)
x.add(e)
x.add(f)
x.add(g)
x.add(h)

print(x)





# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
a = {"18", 18}
print(a)                        # YES





# 4. What will be the length of following set x: 
z = set() 
z.add(20) 
z.add(20.00) 
z.add('20')      # length of s after these operations?  
print(z)
print(len(z))    # 2   (20==20.0 in python)





# 5. s = {} 
# What is the type of 's'?
s = {}
print(type(s))     # DICTIONARY





# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language 
# as value and use key as their names. Assume that the names are unique.
 
#  favl = {
#   "Ifreen":"Urdu",
#   "Amisha":"English",
#   "Nisha":"Bhojpuri",
#   "Pooja":"Odisaki" }
# print(favl)

d = {}

name = input("Enter friends name : ")
lang = input("Enter lang name : ")
d.update({name : lang})

name = input("Enter friends name : ")
lang = input("Enter lang name : ")
d.update({name : lang})

name = input("Enter friends name : ")
lang = input("Enter lang name : ")
d.update({name : lang})

name = input("Enter friends name : ")
lang = input("Enter lang name : ")
d.update({name : lang})

print(d)





# 7. If the names of 2 friends are same; what will happen to the 
# program in problem 6? 

# NOTE : DICT IS MUTABLE SO JUST BECAUSE CHANGE OF SAME NAME IS PERMANENT
# VALUES SAME HO SAKTI HAI BUT KEY SAME HO TO DIKKAT HO SAKTI HAI





# 9. Can you change the values inside a list which is contained in set S? 
m = {8, 7, 12, "Harry", [1,2]}
# IT CAN NOT BE CHANGE

# PROPERTIES OF SETS 
# 1. Sets are unordered => Element’s order doesn’t matter 
# 2. Sets are unindexed => Cannot access elements by index 
# 3. There is no way to change items in sets. 
# 4. Sets cannot contain duplicate values.

