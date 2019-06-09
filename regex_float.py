
# Detect a floating number using regex

import re

num = int(input())

for i in range(num):
    inp = input()
    if inp == '0':
        print(False)
    else:
        print(bool(re.search(r'^[-+]?\d*\.?\d*$',inp)))

