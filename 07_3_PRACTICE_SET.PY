# Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3 


def ptn(n):
    print("*"*n)
    if(n==0):
        return 
    
    else:
        return ptn(n-1)
    


# def ptn(n):
#     print("*"*n)
#     if(n==0):
#         return 
    
#     else:
#         return ptn(n-1)





n = int(input("Enter a number : "))
print(ptn(n))