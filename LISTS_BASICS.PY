# IT IS LIKE A STRUCTURE WHICH IS ALREADY IN C LANGUAGE
# LIST CANT BE CHANGE AND STRING CAN NOT BE CHANGE ONLY FOR TEMPERORY CHANGE DONE IN A STRING
list = [3, "Ifreen", 4.9, 'I', 8, True, 2.3]
print(list[1])
print(list[5])
print(list[ : 3])
list.append("Ifreen") #FOR ADDING A NUMBER OR STRING AT LAST POSITION
print(list)
list.remove(4.9)
print(list)



# ONLY FOR INT, NOT FLOAT AND NOT STRING
list1 = [9, 66, 33, 2, 7, 8, 3, 1, 4]
list1.sort()        # FOR INCREASING ORDER
print(list1)  
list1.reverse()     #FOR decreasing order
print(list1)
list1.insert(2,100)   #FOR ADDING A NUMBER OR A STRING IN A GIVEN POSITION OF A LIST
print(list1)
list1.pop(2)        #FOR SKIP OR REMOVE A STRING/NUMBER (POSITION) FROM LIST
print(list1)
list1.remove(66)    #FOR REMOVE DIRECT VALUE OR A STRING
print(list1)

list.insert(3,"anjali")
print(list)