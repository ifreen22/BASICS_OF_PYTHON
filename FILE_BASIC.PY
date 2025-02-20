# TYPE OF FILES

# There are 2 types of files: 
# 1. Text files (.txt, .c, etc) 
# 2. Binary files (.jpg, .dat, etc) 
# Python has a lot of functions for reading, updating, and deleting files. 

# READING A FILE IN PYTHON 
# Open the file in read mode 
# f = open("this.txt", "r") 
# Read its contents 
# text = f.read() 
# Print its contents 
# fprint(text)
# Close the file 
# f.close() 

# OTHER METHODS TO READ THE FILE. 
# f.readline() # Read 1st one line from the file. 

'''MODES OF OPENING A FILE 
r = open for reading 
w = open for writing  
a = open for appending 
+  = open for updating. 
rb will open for read in binary mode. 
rt will open for read in text mode.



WITH STATEMENT 
The best way to open and close the file automatically is the with statement. 
# Open the file in read mode using 'with', which automatically closes the 
file 
with open("this.txt", "r") as f: 
# Read the contents of the file 
text = f.read() 
# Print the contents 
print(text)

'''

f = open("02_practice_set")
# print(f.readline())
# l = f.readlines()
# print(l, type(l))     *LIST OF LINES
print(f.read())
print(f.close())


# f = open("02_practice_set")
# l1 = f.readline()
# print(l1, type(l1)) 

# l2 = f.readline()
# print(l2, type(l2)) 

# l3 = f.readline()
# print(l3, type(l3)) 

# l4 = f.readline()
# print(l4, type(l4)) 

# l5 = f.readline()
# print(l5, type(l5)) 

# f.close()