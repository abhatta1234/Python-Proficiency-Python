
#Validate a Credit Card: must start with 4,5 or 6 | must contain only 16 digits | must only consist digits(0-9)
# May have digits in group of 4, separated by one hyphen("-") | must not use any other separator like " ","_" etc
# Must not have 4 or more consecutive repeated digits

import re

num = int(input())

for i in range(num):
    status = "Invalid"
    cardnum = input()
    if re.search(r'^[4|5|6]', cardnum):

        if re.search(r'[\d{16}]' ,cardnum):

            if re.search(r'^\d{4}[-]?\d{4}[-]?\d{4}[-]?\d{4}$' ,cardnum):

                if not re.search(r'(\d)\1{3,}' ,cardnum.replace("-" ,"")):
                    status = "Valid"
    print(status)