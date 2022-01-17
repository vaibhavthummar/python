# Write a Python program to add member(s) in a set and clear a set
# 20CS097
# Vaibhav Thummar

def addtoset(set,items):
    for item in items:
        set.add(item)
    return set

set = {"1","2","3","4"}
items = ['a','b','c','d']
#calling function
set = addtoset(set,items)

#printing results
print(set)