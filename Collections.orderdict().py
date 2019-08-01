#Given a list of N items together with their prices that consumer bought on a particular day, print each item_name and
# net_price( Quantity of item sold multiplied by the price of each item) in order of its first occurence.

from collections import defaultdict

num = int(input()) # taking input for number of items

d = defaultdict(list) #creating defuault dictionary list

for i in range(num): # appending the value to list of key as it comes
    inp = input().rpartition(" ")
    d[inp[0]].append(int(inp[2]))

for k,v in d.items(): # printing the items and net price in order of occurence
    print(k , sum(v))