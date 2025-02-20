
# A string always start with zeroth number (for a)
# 0=I, 1=f, 2=r...
# -1=n, -2=e, -3=e...
# NOTE : A STRING CAN NOT BE CHANGED



# PRESENTATION OF A STRING
a = 'Ifreen'
b = "Ifreen"
c = '''Ifreen'''

print(a, b, c)     # all are same

length = len(a)    #for counting number of character in a string
print(length)   

nameshort = a[0:3]   # for typing sub character
char = a[5]          # also write a[-1]
print(nameshort)
print(char)
print(a[-5:-1])      #If both are negative
print(a[1:5])        #So convert into this
print(a[ :6])        #kuchh nhi means start with zero = a[0:6]
print(a[1: ])        #kuchh nhi means end with last char = a[1:len(a)]

x = "amazing"
print(x[1:6:2])      #1st solve x[1:6] = "mazin", than solve in that continuous by 2 = "mzn"
y = "bravewomen"
print(y[1:8:3])

print(y.endswith("men"))       #True (for checking char)
print(a.startswith("ifr"))     #False because i was capital I
print(x.capitalize())          #only 1st character will be capital
print(a.find("ree"))           #for finding 1st  char number in a string
print(a.replace("free","s"))   #for replacing the string
print(x.upper())               #for convert all char in CAPITAL
print(a.lower())               #for convert all char in SMALL
print(a.swapcase())            #small char convert to capital and capital convert to small
print(x.count("a"))            #for counting number of char in a string
print(x.isdigit())             #if in the string is only digit than True
print(x.isdecimal())           #if in the string is only decimal than True



#SCAPE SEQUENCE CHARACTER
# THESE ALL ARE APPLICABLE FOR ONLY A STRING
# 1) \n = for next line 
# 2) \t = for tab space ("    ") 
# 3) \' = \
# 4) \\ = \


m = "Ifreen "
n = "Siddiqui"
print(m + n)         # FOR ADDING
print(m * 2)         # FOR REPEATING
print("n" in m)      # FOR CHECKING A STRING
print("i" not in m)  # FOR CHECKING A STRING
