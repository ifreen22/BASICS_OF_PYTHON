class Employee:
    language = "Java"
    salary = 1200000



    def __init__(x):
        print("Hello") # automatically call


    
    def info(self): # MOSTLY USED OF (SELF) IS FOR MAKING A FUNCTION
        print(f"The language is {self.language} and the salary is {self.salary}")



harry = Employee()
print(harry.language, harry.salary)

Ifreen = Employee  
Employee.info(Ifreen)




    



# STATIC METHOD
class Teacher:
    Language = "English"
    Salary = 300000

    @staticmethod
    def infor(): 
        print("Good Morning")

    @classmethod
    def show(cls):
        print(f"The language of class attribute is {cls.Language}")

Jikra = Teacher
Teacher.infor()

Jikra.show()


class student:
    division = "A"
    percentage = 90.78
    roll_no = 13

    def __init__(self, Division, Percentage, Roll_no):
        self.division = Division
        self.percentage = Percentage
        self.roll_no = Roll_no

IFREEN = student("F", 90.40, 13)
print(IFREEN.division, IFREEN.percentage, IFREEN.roll_no)

