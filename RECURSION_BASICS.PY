def sumofn(n):
    if(n==1):
        return 1

    else:
        return n+sumofn(n-1)
    

def numofn(n):
    print(n)
    if(n==1):
        return 0
    
    return numofn(n-1)
    

def fact(n):
    if(n==0 or n==1):
        return 1

    return n*fact(n-1)
    


    
    




a = int(input("Enter a number : "))
print(sumofn(a))
print(numofn(a))
print(fact(a))
