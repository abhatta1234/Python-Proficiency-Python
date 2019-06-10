
#Basic numpy operation


import numpy

inp = numpy.array(input().split(),int)

a = numpy.array([input().split() for _ in range(inp[0])],int)
b = numpy.array([input().split() for _ in range(inp[0])],int)

print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(a//b)
print(numpy.mod(a,b))
print(numpy.power(a,b))

