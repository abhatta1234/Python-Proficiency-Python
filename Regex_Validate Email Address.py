

# Validate email address from a given list of email addresses.


import re

loop = int(input())

for i in range(loop):
    inp = input().split()
    email = inp[1]
    mat = re.match(r"<[A-Za-z](\w|\.|-)+@[A-Za-z]+\.[A-Za-z]{1,3}>",email)
    if mat:
        print(" ".join(inp))










