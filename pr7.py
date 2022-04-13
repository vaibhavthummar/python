# Lapindrome

# for loop until T test cases
for T in range(int(input())):
    # Taking input word as list
    lst = list(input())

    # splitting lst into two halves
    splt = len(lst) // 2
    lst1 = lst[:splt]
    if len(lst) % 2 == 0:
        lst2 = lst[splt:]

    # if length of word is odd, ignoring middle term
    else:
        lst2 = lst[splt + 1:]
    lst1.sort()
    lst2.sort()

    # Comparing both the halves
    if lst1 == lst2:
        print('YES')
    else:
        print('NO')


# 20CS097
# Vaibhav thummar