# STRING AND TUPLE HAVING ABILITY TO ONLY TEMPERORY CHANGE (IMMUTABLE) 
# LIST HAVING ABILITY TO PERMANENT CHANGE (MUTABLE)


a = (1, 2, 5, 7)
print(type(a))      #tuple, because of their bracket

b = (1)
print(type(b))      #int, because their are only 1 number

c = (1,)
print(type(c))      #tuple, because of single element with comma

d = ()              
print(type(d))      #empty tuple

# IT IS LIKE A LIST BUT IT CAN NOT BE PERMANENT CHANGE (TEMPERORY CAN)
e = (3, "Ifreen", 4.9, 'I', 8, True, 2.3, 4.9)

print(e.count(6))            # ZERO TIME
print(e.count("Ifreen"))     # ONE TIME
print(e.index(4.9))          # FOR FINDING POSITION OF A 1st STRING OR A NUMBER IN A TUPLE
print(2 * e)                 # FOR REPEAT TUPLE
print("Ifreen" in e)         # FOR CHECKING VARIABLE
print(len(e))                # FOR COUNTING NUMBER OF VARIABLE
print(e[2:6])                # NEW TUPLE WILL BE GAIN (SLICING)

print(e)                     # PERMANENT CHANGE CAN NOT 

print(3 in e)

f = (9, 66, 33, 2, 7, 8, 3, 1, 4)
print(min(f))
print(max(f))