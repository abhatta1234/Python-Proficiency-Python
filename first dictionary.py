
# Create a dictionary to store marks of the student
# Find the average of the mark for a student called to 2 decimal precision


if __name__ == '__main__':
    n = int(input())
    student_marks = {}  # Creating the dictionary
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line)) # list of the number being passed as float
        student_marks[name] = scores
    query_name = input()

data = student_marks.get(query_name)

mean = sum(data)/len(data)

print('%.2f'%mean) # Printing the final answer by setting the precision to the two decimal place.