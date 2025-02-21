# Q.1) PROGRAM TO CALCULATE AREA OF A CIRCLE AND TRIANGLE

r = int(input("Enter the value of radius : "))
a = int(input("Enter the value of 1st side of a triangle : "))
b = int(input("Enter the value of 2nd side of a triangle : "))
c = int(input("Enter the value of 3rd side of a triangle : "))

print(f"Area of a circle is {3.142*r*r}")
print("Area of a triangle is", (a*b*c)/(4*r))