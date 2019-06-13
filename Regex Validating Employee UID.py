
#Validating UID
#Valid UID : at least 2 uppercase English Alphabet, at least 3 digits, should only contain alphanumeric characters
#No characters should repeat and Exactly 10 characters in a valid UID.



import re

num = int(input())

for i in range(num):
    status = "Invalid"
    word = "".join(sorted(input()))

    if re.search(r"[A-Z]{2,}",word):

        if re.search(r"[0-9]{3,}",word):

            if re.search(r"^\w{10}$",word):

                if not(re.search(r'(.)\1+',word)):

                    status = "Valid"
    print(status)