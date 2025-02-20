# PROPERTIES OF SETS 
# 1. Sets are unordered => Element’s order doesn’t matter 
# 2. Sets are unindexed => Cannot access elements by index 
# 3. There is no way to change items in sets. 
# 4. Sets cannot contain duplicate values. 


a = {}             # EMPTY DICTIONARY (INTERVIEW QUESTION)
b = set()          # EMPTY SET (IMP FOR USER RELATED OUTPUT)

s = {1, 5, 32, 1, "IFREEN", 5.9, 0, 0} 
print(s)           # DOUBLE THINGS PRINT WILL BE ONLY 1 TIME


# METHODS OF SETS
c = {2, 0, 9, 8, 7, 6, 4}

print(len(c))           # FOR NUMBER OF ELEMENTS
c.remove(0)             # FOR REMOVE ELEMENT
print(c)                # ITS PRINTING PROCESS IS SAME AS LIST
c.add(22)               # ADD A ELEMENT IN SET
print(c)
# c.clear()             # FOR REMOVE ALL THE ELEMENTS FROM SET




# MATHEMATICAL TOOLS IN A SET 
s1 = {1, 45, 78}
s2 = {7, 8, 1, 78, 38, 23}     # SUBSETS OF S2 = {7}, {7,8,1,78}, {38, 23}
print(s1.union(s2))            # UNION = S1 + S2 (COMMON ELEMENTS ONLY 1 TIME)
print(s1.intersection(s2))     # ONLY COMMON ELEMENTS
print(s1-s2)                   # VOH S1 KE ELEMENTS JO S2 ME NA HO
print(s1.issuperset({1, 45}))  # TO CHECK S1 IS SUPERSET OR NOT
print({1}.issubset(s1))        # GIVEN SET IS SUBSET OF S1 OR NOT
