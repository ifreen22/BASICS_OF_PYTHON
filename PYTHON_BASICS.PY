"""
A) COMMENTS
# Single line comment
Multiple lines comments are already mention (Ctrl + /)

B) USING PYTHON AS A CALCULATOR
When we run a code than their are a TERMINAL option so tap on that option,
than it is like a calculator (8+9) and print("Ifreen")

C) RULES OF VARIABLE NAME :
1) Small a and capital A are differnt
2) int ____;   (only alphabet or "_" and digit)
3) No comma and blank space on that
4) A variable name  can not start with a digit

D) DATA TYPES
1. Integers 
2. Floating point numbers 
3. Strings 
4. Booleans(True, False)
5. None  

E) OPERATORS IN PYTHON
1. Arithmetic operators: +, -, *, / etc. 
2. Assignment operators:  =, +=, -=, *=, /=, %=, **=, etc. 
3. Comparison operators: ==, >, >=, <=, <, != etc. 
4. Logical operators: and (&), or(/), not(!). 

F) FOR MULTILINE PRINT
print('''Ifreen
Imdadur
Rahman
Siddiqui''')

G) RESULT OF OPERATIONS
int op int = int
float op float = float
int op float = float

H) There are many functions to convert one data type into another
str(31)    * integer to string conversion 
int("32")  * string to integer conversion 
float(32)  * integer to float conversion 

I) CONVERSION OF DATA TYPE
str(31)    =>"31"   # integer to string conversion 
int("32")  => 32    # string to integer conversion 
float(32)  => 32.0  # integer to float conversion 

J) ADDITION OF 2 STRING
print("Ifreen" + " Siddiqui") = Ifreen Siddiqui

I) FOR INCREMENT DECREMENT 
a += 9 
a++ (WRONG, Syntax error)

"""

print("Ifreen")
print("Siddiqui")
print("Ifreen" + " Siddiqui")



# a, b, c, d, e = 5, 2, "Ifreen", 22.22, False
a = 5        # a IS AN INTIGER
b = 2        # b IS AN INTIGER
c = "Ifreen" #DOUBLE CUMS MEANS STRING
d = 22.22    #DECIMLE MEANS FLOAT 
e = False    # e IS AN BOOLEAN VARIABLE


# ARITHEMATIC OPERATORS
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)    # a race to the power b

print("Her name is", a+b, "Ifreen Siddiqui" ) #string
print(c, e) # string & boolean


# LOGICAL AND RELATIONAL OPERATORS
print(a>b)
print(a!=9)
print(a>=5 & a>=b) #(T & T = T)
print(a>d / b>=a)  #(F / F = F)


# ASSIGEMENT OPERATORS
x = 5
x += 20
print(x)
x *= 6
print(x)
x /= 20
print(x)





print('''MY 
NAME
IS
IFREEN
SIDDIQUI''')



A = 31
B = ("Ammi, Abba")
C = 99.99
D = True
print(type(A))
print(type(B))
print(type(C))
print(type(D))


s = int(input("Enter the side of the square : "))
print("Area of the square is", s * s)
print("Perimeter of the square is", 4 * s)



f = 31        #integer
g = str(31) 
j = float(31)
h = "32"      #string
i = int("32")

print(type(f), type(g), type(j), type(h), type(i))
# print(f + g)  {IMPOSSIBLE BECAUSE STRING OP INT}
# print(i + j)  {IMPOSSIBLE BECAUSE STRING OP INT}
