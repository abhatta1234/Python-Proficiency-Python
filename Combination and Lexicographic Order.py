
# Given a String S
# Input : A single line containing space separated string S and the integer value K
# print all the possible combinations, up to size K of the string in lexicographic sorted order



from itertools import combinations

integers = input().split()

string = sorted(integers[0])
num = int(integers[1])

for i in range(num):
    y = list(combinations(string,i+1))
    for a in y:
        print("".join(a))






