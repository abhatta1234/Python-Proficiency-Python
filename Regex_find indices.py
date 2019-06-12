
# You are given a string S
# Task to find the indices of start and end of string k in S

import re
string = input()
pattern = input()

collection = re.finditer(r'(?={})'.format(pattern),string)

if re.search(pattern,string):
    for _ in collection:
        print((_.start(), (_.end() + len(pattern)) - 1))
else:
    print((-1,-1))






