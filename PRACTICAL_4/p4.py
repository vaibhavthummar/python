# Find runner-up from given list
# 20CS097
# vaibhav thummar

n = int(input())
score = map(int, input().split())
print(sorted(list(set(score)))[-2])