
from collections import Counter
given = list(map(int,input().split()))
check = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

Count1 = Counter(arr1)
Count2 = Counter(arr2)

val = 0

for i in check:
    if i in Count1:
        val+=Count1[i]
    if i in Count2:
        val-=Count2[i]

print(val)