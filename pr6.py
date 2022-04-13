# Some words may repeat

from collections import Counter
l=[]
for i in range(int(input())):
    l.append(input())

c=Counter(l)
print(len(c))
for i in c:
    print(c.get(i),end=' ')
print()


# 20CS097
# Vaibhav thummar