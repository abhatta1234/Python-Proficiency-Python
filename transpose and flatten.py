
# Given a N X M integer array matrix with space separated elements( N = rows and M = Columns)
# Print the transpose and flatten matrix


import numpy as np

num = np.array(input().split(),int)


given = []

for i in range(num[0]):
    given.append(list(map(int,input().split())))

given = np.asarray(given)


print((np.transpose(given)))
print(given.flatten())




