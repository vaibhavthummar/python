# Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
# 20CS097
# Vaibhav Thummar

from collections import Counter
list = [2, 4, 2, 8, 14, 11, 12, 13, 14]
tuple = (1, 3, 5, 7, 9, 11, 13)
dictionary = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
for common in (list, tuple):
    occurence_count = Counter(common).most_common(1)[0][0]
    print(f"{occurence_count} repeated {common.count(occurence_count)} times")
value, count = Counter(dictionary.values()).most_common(1)[0]
print(f"{value} repeated {count} times")