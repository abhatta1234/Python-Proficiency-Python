
# Find the average of the student marks
#Column Name : ID,MARKS,CLASS,NAME and it can appear in any order
#Input: first line-total number of students, second line - names of column  in any order and next N lines values of
# marks,IDs,name and class in respective order.


students = int(input())

inx = list(input().split())

column = [i.upper() for i in inx]

a = column.index("MARKS")

col_marks = []

for i in range(students):
    inp = list(input().split())
    col_marks.append(int(inp[a]))


add= sum(col_marks)

average = add/students

print("%.2f"%average)

