
# Decrypt Matrix Script

import numpy as np
import re

num = np.array(input().split(),int)
a = []
for i in range(num[0]):
    a.append(input())
b =[]
for j in range(num[1]):
    for i in range(num[0]):
        b.append(a[i][j])
c = ''.join(b)


d = re.sub(r'((?<=[\w])([\W]+)(?=[\w]))',' ', c)

print(d)


