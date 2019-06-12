
#Given a string consisting of alphanumeric characters,spaces and symbols(+-)
#Task is to find substrings of S that contains 2 or more vowels between consonants.

import re

word = input()


a = re.findall(r'(?<=[^(aeiou)])([aeiou]{2,})(?=[^(aeiou)])',word,re.I)

if a:
    for _ in a:
        print(_)
else:
    (print(-1))


