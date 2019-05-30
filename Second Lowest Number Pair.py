
# Given the names and grades for each student in a Physics class of N students, store them in a nested list and print
# .....the names(s) of any student(s) having the second lowest grade.
# If there are multiple students with the same grade, order their names alphabetically and print each name on a new line

n = int(input())
Numbers =[]
Name  =[]

for i in range(1,2*n+1):
    if i % 2 == 0:
        Numbers.append(float(input()))
    else:
        Name.append(input())
order = sorted(Numbers)
ND = []
for i in order:
    if i not in ND:
        ND.append(i)
NDR = sorted(ND)
second_highest = (NDR[(1)])
index = []
for j in range(len(Numbers)):
    if Numbers[j] == second_highest:
        index.append(j)
finalnames = []
for i in index:
    finalnames.append(Name[i])
    sortfinal = sorted(finalnames)
for i in sortfinal:
    print(i)











