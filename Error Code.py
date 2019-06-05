
# Given Two numbers, values a and b - perform integer division and print a/b
# In case of ZeroDivision Error or Value Error, print Error Code.


num = int(input())

for i in range(num):
    inp = list(input().split())
    first = inp[0]
    second = inp[1]
    try:
        print(int(int(first)/int(second)))
    except ValueError as e:
        print("Error Code: ",  e )
    except ZeroDivisionError as f:
        print("Error Code: integer division by modulo or zero")

