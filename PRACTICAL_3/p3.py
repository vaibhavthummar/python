# Find Captain Room Number
# 20CS097
# vaibhav thummar

k = int(input())
room_number = list(map(int, input().split()))
captain_room_number = (sum(set(room_number)) * k - sum(room_number))  // (k - 1)
print(captain_room_number)