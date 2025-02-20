# 2. Write a python program using function to convert Celsius to Kelvin. 


def kel(x):
    kelvin = 273.15 + x
    return kelvin

a = float(input("Enter the degree in celsius : "))
print("The value of", a, "in kelvin is", kel(a))