
# Given a 2-D array with Dimension NXM. The next N lines contains M space separated integers
# Sum the given array along axis = 0 and then, find the product of the result


import numpy

inp = numpy.array(input().split(),int)

arr = numpy.array([input().split() for _ in range(inp[0])],int)

print(numpy.prod(numpy.sum(arr ,axis = 0)))








