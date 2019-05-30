

# Find the Second highest Number in the given List:


score = list(map(int,input().split()))

a = sorted(score)



final = []

for i in a :
    if i not in final:
        final.append(i)


print(final[(len(final)-2)])



