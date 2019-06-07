
# You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight....)
# Task is to sort the data based on the Kth attribute and print the final resulting table

num = list(map(int,input().split()))

a = []

for i in range(num[0]):
    a.append(list(map(int,input().split())))

index = int(input())

def takeindex(elem):
    return elem[index]

a = sorted(a, key =takeindex)

for _ in a:
    print(*_)


# The printing of the list of list can also be done using the following method:

#for i in a:
    #for b in i :
        #print(b, end = " ")
    #print()









