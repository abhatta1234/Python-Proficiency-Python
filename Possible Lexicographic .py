

# Code to print all possible co-ordinates for the given integer on a 3D grid(i,j,k).
# sum of i+j+k != n
# print list in lexicographic increasing order


x = int(input())
y = int(input())
z = int(input())
n = int(input())


matrix = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            a = [i,j,k]
            matrix.append(a)

final_matrix = []

for i in matrix:
    if sum(i) != n:
        final_matrix.append(i)

print(final_matrix)

