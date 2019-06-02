
# Check whether the given set is a subset of the other or not:
# The first input is the number of the cases
# It checks whether A is subset of B or not

cases = int(input())



for i in range(cases):
    num_elements = int(input())
    A = list(map(int, input().split()))
    givenset = set(A)

    num_elements = int(input())
    B = list(map(int,input().split()))
    subset = set(B)

    if len(givenset.intersection(subset)) == len(givenset):
        print(True)
    else:
        print(False)





