
# find the average for each student
# fist line contains N and X separated by space
# Next X lines contains the space separated marks obtained by students in particular subject.
# Print the averages of all students on separate lines, up to 1 decimal place.




import statistics

num = list(map(int,input().split()))

collection = []

for i in range(num[1]):
    data = list(map(float,input().split()))
    collection.append(data)


Dataset = list(zip(*collection))

for i in Dataset:
    print(round(statistics.mean(i),1))

