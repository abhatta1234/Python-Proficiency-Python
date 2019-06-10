
#Given the Array A and B, both having dimension N X N. Compute the matrix product

import numpy

inp = int(input())

arr1 = numpy.array([input().split() for _ in range(inp)],int)
arr2 = numpy.array([input().split() for _ in range(inp)],int)


print(numpy.dot(arr1,arr2)) # Matrix multiplication is merely a dot product 





