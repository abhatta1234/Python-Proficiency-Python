

# Given a string s containing only of digits 0-9,commas and dots
# Task to complete regex pattern and use split to split the given string at ", and ."
import re

inp = input()


a = re.split(r',|\.',inp)

for _ in a:
    print(*_,sep="")