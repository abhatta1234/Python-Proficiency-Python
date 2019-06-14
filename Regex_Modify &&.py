
#Given a text of N lines.
# modify $$ to and and || to or. Both && and || should have space" " on both sides

import re

num = int(input())

for i in range(num):
    word = input()
    a = re.sub(r' &&(?= )',r' and',word)
    print(re.sub(r' \|{2}(?= )',r' or',a))



