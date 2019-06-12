
# Given that a valid phone number is a ten digit number starting with 7,8 or 9.
# First line contains integer N, number of input and N lines follow, each some string.
# Validate the given list of numbers as telephone number



import re

loop = int(input())

for i in range(loop):
    string = input()
    if re.match(r'^[7|8|9]\d{9}$',string):
        print("YES")
    else:
        print("NO")








