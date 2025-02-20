def avg (a, b, c):     # FUNCTION DEFINITION
    average = (a+b+c)/3
    print(average)

def avg2():            # FUNCTION DEFINITION
    x = int(input("Enter a number : "))
    y = int(input("Enter a number : "))
    z = int(input("Enter a number : "))

    average2 = (x+y+z)/3
    print(average2)

def greet(name): 
    gr = "Hello "+ name 
    return gr  

def greet1(n = "stranger"):
    return n 







avg(5, 3, 4)                 # FUNCTION CALL

avg2()
 
print(greet("Ifreen"))

print(greet1("Ifreen"))      # STRING IS MUTABLE
print(greet1())
