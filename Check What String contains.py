
# Check what string contains:
# Order : alphanumeric,alphabetical,digits,lowercase,uppercase

s = input()

alnum = False
alpha = False
digit = False
lower = False
upper = False



for i in s:
    if i.isalnum():
        alnum = True
        if i.isalpha():
            alpha = True
            if i.isupper():
                upper = True
            else:
                lower = True
        else:
            digit = True

print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)