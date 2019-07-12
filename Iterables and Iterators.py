from itertools import combinations

n = int(input())
arr = input().split()
slice = int(input())

result = list(combinations(arr, slice))
count = 0

for i in result:
    if "a" in i:
        count += 1

print(count / len(result))