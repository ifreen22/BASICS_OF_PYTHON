# Write a python function to print multiplication table of a given number. 

def tbl(n):
    for i in range(1, 11):
        print(f"{n}x {i} = {n*i}")
    


a = int(input("Enter a number : "))
tbl(a)