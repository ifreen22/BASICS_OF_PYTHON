'''WRITE FILES IN PYTHON 
In order to write to a file, we first open it in write or append mode after which, we use 
the python’s f.write() method to write to the file! 
# Open the file in write mode 
f = open("this.txt", "w") 
# Write a string to the file 
f.write("this is nice") 
# Close the file 
f.close()
'''

st = "I am unique"

x = open("01_PRACTICE_SET", "w")
# ALERT = NOT USE THE FUNCTION FOR TYPE WHICH FILE NAME ALREADY EXIST,
# BECAUSE IT WILL DELETE ALL THE CONTENT OF THAT FILE AND ONLY ADD 
# WILL THE CONTENT WHICH THEY WANT
print(x.write(st))
print(x.close())

y = open("02_practice_set", "a")
y.write(st)
y.close()