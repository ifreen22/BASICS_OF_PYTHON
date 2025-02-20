# 6. Write a python function which converts inches to cms. 

def con(inch):
    cms = inch*2.5
    return cms



a = int(input("Enter a number in inch : "))
print("The value of", a, "in cms is", con(a))