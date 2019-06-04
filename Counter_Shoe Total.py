
# There are N number of costumers willing to pay X amount for given shoes, if available.
# Find the total earning>
# Input: First Line - number of shoes , Second Line - list containing the size of each shoe he has
# Third Line - Number of costumer , Fourth Line - Spaced input for Size and Price



from collections import Counter

num_shoes = int(input())

list_shoes =Counter(map(int,input().split()))

num_costumer = int(input())


total = 0

for i in range(num_costumer):
    size, amount = map(int,input().split())

    if list_shoes[size]:
        list_shoes[size]-=1
        total+=amount

print(total)



