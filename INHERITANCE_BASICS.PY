# INHERITANCE 

class Employee:
    a = 1

class coder(Employee):
    b = 2

x = Employee()
print(x.a)   # x.b cant

y = coder()
print(y.a, y.b)





# MULTIPLE INHERITANCE 

class Principle:
    l = 10

class Teacher:
    m = 9

class Student(Principle, Teacher):
    n= 8

z = Student()
print(z.l, z.m, z.n)





# MULTILEVEL INHERITANCE 

class Grandfather:
    d = 7

class Father(Grandfather):
    e = 6

class Son(Father):
    f = 5 

c = Son()
print(c.d, c.e, c.f)

