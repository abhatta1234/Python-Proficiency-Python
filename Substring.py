
# Find a substring from a string

string = input()
sub = input()
num_char = len(sub)
num_loop = (len(string)- num_char) + 1
a = 0
for i in range(num_loop):
    if string[i:num_char] == sub :
        a = a + 1
    num_char+=1
print(a)

