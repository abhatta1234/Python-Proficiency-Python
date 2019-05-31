
# initialize list and read in the value of n followed by n lines of command.
# commands are : insert, print, remove,append,sort,pop,reverse
# Iterate through command in order and perform the corresponding operation in your list

num = int(input())
l = []
data = []

for i in range(num):
    val = input().split()
    command = val[0]
    values = val[1:]
    if command != "print":
        operation = "l."+command+"("+ ",".join(values)+")"
        result = eval(operation)
    else:
        print(l)

