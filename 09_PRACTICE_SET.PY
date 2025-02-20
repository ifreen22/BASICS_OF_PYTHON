# 1. Create a class “Programmer” for storing information of few programmers 
# working at Microsoft.

# class programmer:
#     language = "Java"
#     professional_lang = "English"
#     Experience = "0-2 Years"

# Ifreen = programmer()
# print(Ifreen.language, Ifreen.professional_lang, Ifreen.Experience)





# 2. Write a class “Calculator” capable of finding square, cube and square root of a 
# number.

# class calculator:
#     #square = 1
#     #cube = 2.3
#     #square_root = 4.6

#     def __init__(self, n):
#         self.n = n

#     def square(self):
#         print(f"The square is {self.n*self.n}")

#     def cube(self):
#         print(f"The cube is {self.n*self.n*self.n}")

#     def sq_root(self):
#         print(f"The cube is {self.n**1/2}")

# a = calculator(4)
# a.square()
# a.cube()
# a.sq_root()





# 3. Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute? 

# NO, CLASS ATTRIBUTE CANT BE CHANGE
# BUT, THE SPICIFIC OBJECT WILL CHANGE ACCORDING TO INSTANT RULE, SO LATEST VALUE WILL BE SHOWN IN OUTPUT





# 4. Add a static method in problem 2, to greet the user with hello. 

# class calculator:
#     #square = 1
#     #cube = 2.3
#     #square_root = 4.6

#     def __init__(self, n):
#         self.n = n

#     def square(self):
#         print(f"The square is {self.n*self.n}")

#     def cube(self):
#         print(f"The cube is {self.n*self.n*self.n}")

#     def sq_root(self):
#         print(f"The cube is {self.n**1/2}")

#     @staticmethod
#     def greet():
#         print("Hello")

# a = calculator(4)
# a.square()
# a.cube()
# a.sq_root()
# a.greet()





# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

class Train:
    name = "ifreen"
    age = 23
    train_name = "deccan"



    def __init__(self, Name, Age, Train_name):
        self.name = Name
        self.age = Age
        self.train_name = Train_name
        

pessanger1 = Train("Ifreen", 17, "Deccan")
print(pessanger1.name, pessanger1.age, pessanger1.train_name)