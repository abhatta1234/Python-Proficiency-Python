
# Symmetric difference - indicates the value that exist in either M or N but not exist in both

inp1 = int(input())
inp2 = list(map(int,input().split()))
inp3 = int(input())
inp4 = list(map(int,input().split()))

set1 = set(inp2) # converting list to input
set2 = set(inp4)

diff1 = set()
diff2= set() # initializing sets
diff3 = set()

diff1 = set1.union(set2)
diff2 = set2.intersection(set1)
diff3 = sorted(diff1.difference(diff2)) # difference: Exist in diff1 but not in diff2

for i in diff3:
    print(i)
