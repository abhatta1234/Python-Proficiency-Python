
# In an array, some number repeats K times, while only one never repeats
# Find a non-repeating number


group = int(input())
inp = list(map(int,input().split()))

set1 = set()
non = set(inp)



captain = int(((sum(non)*group)-sum(inp))/(group-1))

print(captain)