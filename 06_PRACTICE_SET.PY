# 1.Write a program to print multiplication table of a given number using for loop.
# a = int(input("Enter a number : ")) 
# for i in range(1, 11):
#     print(a*i)





# 2. Write a program to greet all the person names stored in a list ‘l’ 
# and which starts with S. 
# l = ["Harry", "Soham", "Sachin", "Sahul"]
# length = len(l)-1

# for i in range(0, length):
#     if(l[i].startswith("S")):
#         print(l[i])






# 3. Attempt problem 1 using while loop.
# i=1
# while(i<=10):
#     print(i*a)
#     i += 1





# 4. Write a program to find whether a given number is prime or not. 
# x = int(input("Enter a number : "))

# i=2
# while(i<x):
#     if(x%i==0):
#         print(x, "is not a prime number")
#         break
#     else:
#         print(x, "is a prime number")
#         break
#     i += 1





# 5. Write a program to find the sum of first n natural numbers using 
# while loop.
# n = int(input("Enter a number : "))
# sum = 0

# for i in range(1, n+1):
#     sum = sum+i

# print("The sum of first n natural numbers are", sum)





# 6. Write a program to calculate the factorial of a given number using 
# for loop. 
# y = int(input("Enter a number : "))
# fact = 1

# for i in range(1, y+1):
#     fact = fact*i

# print("Factorial of", y, "is", fact)





# 7. Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3

# z = int(input("Enter a number : "))

# for i in range(1, z+1):
#     print(" "*(z-i), end="")
#     print("*"*(2*i-1), end="")
#     print("")





# 8. Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3

# b = int(input("Enter a number : "))

# for i in range(1, b+1):
#     print(" "*(b-i), end="")
#     print("*"*i, end="")
#     print("")





# 9. Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * * 





# 10. Write a program to print multiplication table of p using for 
# loops in reversed order.

# p = int(input("Enter a number : "))

# i=10
# while(i>=1):
#     print(p*i)
#     i = i-1

