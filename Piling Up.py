import sys

for i in range(int(input())):

    num = int(input())
    a = list(map(int,input().split()))

    lng  = len(a)
    count = 0

    mxval = max(a[0],a[lng-1])
    chk = sys.maxsize

    while lng!= 0:
        mxval = max(a[0],a[lng-1])

        if a[0] == mxval:
            rmv = 0
        else:
            rmv = lng-1

        if mxval <=chk :
            lng-=1
            chk = mxval
            a.pop(rmv)
        else:
            break

    if lng == 0:
        print("Yes")
    else:
        print("No")







