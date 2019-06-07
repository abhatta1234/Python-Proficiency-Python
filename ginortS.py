
# Given a String S
# Sort the given string as follows: all sorted lower case before upper case, all sorted uppercase letters are ahead of
#digits and all sorted odd digits are ahead of sorted even digits and output the sorted string

alphanum = input()


upper = []
lower = []
odd = []
even = []

for i in alphanum:
    if i.isupper():
        upper.append(i)
    elif i.islower():
        lower.append(i)
    elif (int(i)%2 == 1):
        odd.append(i)
    else:
        even.append(i)

Combo = (sorted(lower)+sorted(upper)+ sorted(odd)+sorted(even))

for i in Combo:
    print(i,end="")

