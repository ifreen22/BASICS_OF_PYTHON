# 2. The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score.

# def highest(x):
#     i = x[0]
#     n = len(x)
#     while(i<x[n]):
#         if(x[0]<=x[n]):
#             print("The highest score is : ", x[n])
#         else:
#             print("The highest score is : ", x[0])
#     i += 1
#     Next_score = int(input("Enter your score : "))
#     return highest(Next_score)
    

    



# l = []

# score1 = int(input("Enter your game score : "))
# l.append(score1)

# score2 = int(input("Enter your game score : "))
# l.append(score2)

# score3 = int(input("Enter your game score : "))
# l.append(score3)

# highest(l)


# def highest(x):
#     i = x[0]
#     n = len(x)
#     while(i<x[n]):
#         if(x[0]<=x[n]):
#             print("The highest score is : ", x[n])
#         else:
#             print("The highest score is : ", x[0])
#     i += 1
#     Next_score = int(input("Enter your score : "))
#     return highest(Next_score)
    

    





l = [23] 

i = 1
while(i < 100):
    x = int(input("Enter your game score : "))
    l.append(x)
    if(l[0]<=l[i]):
        print("The highest score is : ", l[i])
    else:
        print("The highest score is : ", l[0])
i+=1



# score1 = int(input("Enter your game score : "))
# l.append(score1)

# score2 = int(input("Enter your game score : "))
# l.append(score2)

# score3 = int(input("Enter your game score : "))
# l.append(score3)

# highest(l)