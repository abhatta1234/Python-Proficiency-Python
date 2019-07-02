
#Happy LadyBugs Problem:

for i in range(int(input())):
    lent = int(input())
    string = list(input())
    noustring = list(filter( lambda a:a != "_",string))
    nrstring = sorted(list(set(noustring)))
    result = "NO"
    if len(string) - len(noustring) >= 1:
        if all( string.count(i)>= 2 for i in nrstring):
            result = "YES"
    elif len(noustring) == 0:
            result = "YES"
    elif len(string) == len(set(string)):
        result = "NO"
    else:
        if len(string) == len(noustring):
            if all(string [i] == string[i-1] or string [i] == string [i+1] for i in range(1,len(string)-1)):
                if string[len(string)-1] == string[len(string)-2]:
                    result = "YES"
    print(result)

