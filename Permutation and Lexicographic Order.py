
# Given a String S
# print all the possible permutations of size K of the string in lexicographic sorted order
# Input : A single line containing space separated string S and the integer value K



from itertools import permutations

integers = input().split()

string = sorted(integers[0])
num = int(integers[1])

y = list(permutations(string,num))

for i in y:
    print("".join(i))






