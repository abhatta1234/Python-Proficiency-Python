from collections import defaultdict

arr = list(map(int,input().split()))

arr1 = [input() for i in range(arr[0])]
arr2 = [input() for i in range(arr[1])]

d = defaultdict(list)

for i in range(arr[0]):
    d[arr1[i]].append(i+1)

for i in arr2:
    if d[i]:
        print(*d[i])
    else:
        print(-1)