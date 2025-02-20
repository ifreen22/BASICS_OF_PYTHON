class student:
    name = "Ifreen"
    std = 1
    division = "A"
    roll_no = 2
    percentage = 90
    grade = "A"



for i in range(1, 101):
    studenti = student()
    Name = (input("Enter the full name of student : "))
    studenti.name = Name  # sabse uper vala name ifreen matter nhi karta,
    # Agar instant vale me name na likha jae phir sabse uper vala matter karega
    

    Std = int(input("Enter standard of the student : "))
    studenti.std = Std
    

    Division = (input("Enter the division of the student : "))
    studenti.division = Division
    

    Roll_no = int(input("Enter the roll number of the student : "))
    studenti.roll_no = Roll_no
    

    Percentage = float(input("Enter the percentage o the student : "))
    studenti.percentage = Percentage
    

    Grade = (input("Enter the grade of the student : "))
    studenti.grade = Grade

    print("\n")
    # print(f"The name of student{i} is", studenti.name)
    # print(f"The standard of the student{i} is", studenti.std)
    # print(f"The division of the student{i} is", studenti.division)
    # print(f"The roll number of the student{i} is", studenti.roll_no)
    # print(f"The percentage of the student{i} is", studenti.percentage)
    # print(f"The grade of the student{i} is", studenti.grade)

    print(f"The detail of student-{i}")

    print("Name : ", studenti.name)
    print("Standard : ", studenti.std)
    print("Division : ", studenti.division)
    print("Roll number : ", studenti.roll_no)
    print("Percentage : ", studenti.percentage)
    print("Grade : ", studenti.grade) 