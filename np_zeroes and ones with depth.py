
# Example Input : 3 3 3, where it denotes depth,row and column

# Using the given input parameter print each using np.zeros and np.ones to the appropriate depths

import numpy as np

inp = list(map(int,input().split()))

print(np.zeros(inp, dtype = np.int))
print(np.ones(inp, dtype = np.int))
