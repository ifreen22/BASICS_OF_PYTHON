# 1. Write a python program to display a user entered name followed by Good 
# Afternoon using input () function. 

name = input("Enter your name : ")
print("Good Afternoon", name)
print(f"Good Afternoon {name}")





# 2. Write a program to fill in a letter template given below with name and date.
Name = "Ifreen Siddiqui"
date = "03-11-2024"
print("\t",Name, '''Congratulations you are selected! 
According to your profile and your family backgroud,
you deserve this scholarship, and I appriciate you 
because your number of achievements of awards is very
large by your age, so your scholarship amount will be
transfer in your bank account within 10-15 working 
days.
                                  \n''', date,
                                    "\n Thank you!"      

)





# 3. Write a program to detect double space in a string.
a = "Ifreen  Siddiqui"
print("The word which having double space it's str number is", a.find("  "))
# If the output is -1 that means their are not any "  "




# 4. Replace the double space from problem 3 with single spaces. 
print(a.replace("  "," "))      #only temperory change will be done





# 5. Write a program to format the following letter using escape sequence 
# characters.
letter = "Dear Harry,\n\t This python course is nice.\nThanks!"
print(letter)
