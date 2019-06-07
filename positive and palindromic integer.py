

# Given a space separated list of integer, print True if all integers are Positive and if any is palindromic
# Input : First line contains the number of integer and second line contains the list of integers

num = int(input())

lis = list(map(int,input().split()))

a = False

for i in lis:
    if i > 0:
        if str(i) == str(i)[::-1]:
            a = True
    else:
        a = False

print(a)










