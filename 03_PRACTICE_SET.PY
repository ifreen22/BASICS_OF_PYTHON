# 1. Write a program to store seven fruits in a list entered by the user. 

a = input("Enter a fruite name : ")
b = input("Enter a fruite name : ")
c = input("Enter a fruite name : ")
d = input("Enter a fruite name : ")
e = input("Enter a fruite name : ")
f = input("Enter a fruite name : ")
g = input("Enter a fruite name : ")

frts = []
frts.append(a)
frts.append(b)
frts.append(c)
frts.append(d)
frts.append(e)
frts.append(f)
frts.append(g)

print("The 7 fruites are", frts)





# 2. Write a program to accept marks of 6 students and display them in 
# a sorted manner.
list1 = [78, 88, 95, 45, 67, 72]
list1.sort()
print(list1)





# 3. Check that a tuple type cannot be changed in python.
m = (3, "Ifreen", 4.9, 'I', 8, True, 2.3, 4.9)





# 4. Write a program to sum a list with 4 numbers.
list2 = [2, 9, 8, 6]
print(sum(list2))
# print(list2[0] + list2[1] + list2[2] + list2[3])





# 5. Write a program to count the number of zeros in the following tuple: 
n = (7, 0, 8, 0, 0, 9)
print(n.count(0))