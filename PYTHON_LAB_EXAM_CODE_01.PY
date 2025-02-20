# PYTHON PROGRAM TO OBTAIN MARKS IN COMPUTER OF SOME STUDENTS AND FIND MEAN, 
# MEADIAN AND MODE.THE MARKS ARE GIVEN AS...
# 84, 95, 76, 54, 96, 88, 91, 92, 95, 75, 91, 97, 80


import statistics  

list = [84, 95, 76, 54, 96, 88, 91, 92, 95, 75, 91, 97, 80]

list.sort()

mean_value = sum(list) / len(list)

n = len(list)
if n % 2 != 0:  
    median_value = list[n // 2]  
else:  
    median_value = (list[n // 2 - 1] + list[n // 2]) / 2  

mode_value = statistics.mode(list)

print(f"Sorted Marks: {list}")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")



# PROGRAM TO GENERATE RANDOM NUMBERS FROM 1 TO 20 AND APPEND THEM TO THE LIST

list2 = []
i=1
while(i<=20):
    list2.append(i)
    i+=1


print(list2)



