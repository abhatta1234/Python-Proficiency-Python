# Given two integer arrays of soze NXP and MXP, concatenate them along axis = 0


import numpy as np

detail = np.array(input().split(),int)

given1 = []
given2 =  []

for _ in range(detail[0]):
    given1.append(list(map(int,input().split())))

for _ in range(detail[1]):
    given2.append(list(map(int,input().split())))

given1 = np.asarray(given1)
given2 = np.asarray(given2)

print(np.concatenate((given1,given2)))



