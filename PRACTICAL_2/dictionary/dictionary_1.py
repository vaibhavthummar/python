# Write a Python script to check whether a given key already exists in a dictionary.
# 20CS097
# Vaibhav Thummar

d = {0: 10, 1: 20, 2: 30}
c = 1
if c in d.keys():
    print("Key exists")
else:
    print("Key does not exist")