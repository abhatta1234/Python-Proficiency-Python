
# Given a 2_D array with dimension NXM. Your task is to perform the min function over axis 1 and find max of that

import numpy

inp = numpy.array(input().split(),int)

arr = numpy.array([input().split() for _ in range(inp[0])],int)

print(numpy.max(numpy.min(arr ,axis =0)))








