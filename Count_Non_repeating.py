

# count the number of non repeating string in set
num = int(input())
a = set()
for i in range(num):
    stamp = input()
    a.add(stamp) # if the set already has input string, then there is no change in set.
                 # Hence, easier to count non-repeating strings

print(len(a))
