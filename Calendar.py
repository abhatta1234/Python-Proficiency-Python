
# Given the date in mm dd yyyy as input, find the corresponding day of the week

import calendar

inp = list(map(int,input().split()))

year = inp[2]
month = inp[0]
day = inp[1]


index_week = calendar.weekday(year,month,day)


print((calendar.day_name[index_week]).upper())
