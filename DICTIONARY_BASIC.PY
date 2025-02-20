# SYNTAX
a = { 
"key": "value", 
"harry": "code", 
"marks": "100", 
"list": [1, 2, 9] 
} 

print(a["key"])  # Output: "value" 
print(a["list"])  # Output: [1, 2, 9] 



# PROPERTIES OF PYTHON DICTIONARIES
# 1. It is unordered. 
# 2. It is mutable. (like a list, existing dict can be change by permanently)
# 3. It is indexed. 
# 4. Cannot contain duplicate keys.




# DICTIONARY METHODS 
b={"name":"harry",
"from":"india",
"marks":[92,98,96]
    }

print(b)             # b IN THE FORM OF DICT
print(b.items())     # b IN THE FORM OF TUBLE
print(b.keys())      # "name", "from", "marks"{KEYS}
print(b.values())    # VALUES WILL BE PRINT
print(b.update({"from" : "sukoon"}))
print(b.get("marks"))  # IF NOT AVL THAN NONE {IT IS BEST}
print(b["marks"])      # IF NOT AVL THAN ERROR
print(b.copy())        # latest copy
#print(b.clear())      # for remove all thing in a dict
#print(b.pop("name", "naam"))
print(b.popitem())