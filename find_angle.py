#  ABC is a right triangle,90  at B.
# Point M is the midpoint of hypotenuse .
# You are given the lengths  AB and BC .
# find angle MBC in degrees

import math

b1 = int(input())
b2 = int(input())

a_r = math.atan(b1/b2)
a_deg = math.degrees(a_r)
print(round(a_deg),chr(176),sep='')

