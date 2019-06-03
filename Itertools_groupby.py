
# Given a string S
# Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrence of
# the character 'c' with (X,c) in the string



from itertools import groupby


for k,c in groupby(input()):
    a = (len(list(c)),int(k))
    print(a,end = " ")
