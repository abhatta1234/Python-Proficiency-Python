# Function to test whether the given year is leap or not:

def is_leap(year):
    leap = False
    if year % 100 ==0:
        if year % 400 == 0:
            leap = True
    elif year % 4 == 0:
        leap = True
    else:
        leap = False

    return leap
    print(leap)

year = int(input())
print(is_leap(year))