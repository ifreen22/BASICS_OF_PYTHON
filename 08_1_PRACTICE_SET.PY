# 1. Write a program to read the text from a given file ‘poems.txt’ and 
# find out whether it contains the word ‘twinkle’.

f = open("poems.txt")
x = f.read()
# y = x.lower()

if("TWINKLE" in x):
    print("The word twinkle is present in poems.txt file")

else:
    print("The word twinkle is not present in poems.txt file")


f.close()