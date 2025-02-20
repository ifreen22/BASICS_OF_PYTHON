# SUPER() METHOD

class Grandfather:
    def __init__(self):
        print("Constructor of Grandfather")
    d = 7

class Father(Grandfather):
    def __init__(self):
        print("Constructor of Father")
    e = 6

class Son(Father):
    def __init__(self):
        super().__init__()    # ALSO OUTPUT CONSTRUCTOR OF FATHER
        print("Constructor of Manager")
    f = 5 

c = Son()
print(c.d, c.e, c.f)





# CLASS METHOD 

class Employee:
    a = 1
    b = 2

    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}") # OUTPUT WILL BE NOT AN INSTANT

x = Employee()
x.a = 9   # x.b cant

x.show()