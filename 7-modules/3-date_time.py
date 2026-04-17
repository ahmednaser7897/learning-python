# ---------------------------------------------
# --- Modules->Date & Time  ----
# ---------------------------------------------

# [1] The datetime module provides classes for manipulating dates and times
# [2] The datetime module has several classes, including:
# [3] datetime.datetime: represents a specific date and time
# [4] datetime.date: represents a date (year, month, day)
# [5] datetime.time: represents a time (hour, minute, second, microsecond)
# [6] datetime.timedelta: represents a duration, the difference between two dates or times
# [7] datetime.now(): returns the current date and time
# [8] datetime.today(): returns the current date and time (same as now())
# [9] datetime.strptime(): parses a string into a datetime object
# [10] datetime.strftime(): formats a datetime object into a string
# [11] datetime.min: the earliest representable date and time
# [12] datetime.max: the latest representable date and time
# [13] datetime.fromtimestamp(): creates a datetime object from a timestamp
# [14] datetime.fromisoformat(): creates a datetime object from an ISO 8601 string
# [15] datetime.utcnow(): returns the current UTC date and time


import datetime
# print(datetime) #<module 'datetime' from 'C:\\Users\\ahmednaser\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\datetime.py'>
# print(dir(datetime)) 
# print(dir(datetime.datetime)) 

# prints the current date and time
print(datetime.datetime.now())

# prints the current year, month, day, hour, minute, second, microsecond
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

#prints start and end of the datetime module
print(datetime.datetime.min) #0001-01-01 00:00:00
print(datetime.datetime.max) #9999-12-31 23:59:59

# prints the current  time
print(datetime.datetime.now().time())

#prints start and end of the time module
print(datetime.time.min) #00:00:00
print(datetime.time.max) #23:59:59.999999

#print spacific date and time
print(datetime.datetime(2020, 5, 17, 15, 30, 45)) #2020-05-17 15:30:45


date_of_birth = datetime.datetime(1990, 1, 1)
print(date_of_birth) #1990-01-01 00:00:00
date_now = datetime.datetime.now()
age = date_now - date_of_birth
print(f"my birthday is {date_of_birth} and today is {date_now} and my age is {age.days} days") #11323 days, 0:00:00


# ---------------------------------------------
# --- Modules->Date & Time Formatting ---------
# ---------------------------------------------
#https://www.geeksforgeeks.org/python/python-strftime-function/
import datetime
print("-"*10+"Date & Time Formatting"+ "-"*10)


date =datetime.datetime(2020, 5, 17, 15, 30, 45)
print(date) #2020-05-17 15:30:45
# format the date and time using strftime() method
#[%Y] Year with century as a decimal number.   2020
#[%y] Year without century as a decimal number.   20
#[%m] Month as a zero-padded decimal number.
#[%d] Day of the month as a zero-padded decimal number.
#[%H] Hour (24-hour clock) as a zero-padded decimal number.
#[%M] Minute as a zero-padded decimal number.
#[%S] Second as a zero-padded decimal number.
#[%A] Weekday as locale’s full name.    Monday
#[%a] Weekday as locale’s abbreviated name.    Mon
#[%B] Month as locale’s full name.   January
#[%b] Month as locale’s abbreviated name.   Jan
#[%w] Weekday as a decimal number, where Monday is 0 and Sunday is 6.
#[%p] Locale’s equivalent of either AM or PM.
#[%I] Hour (12-hour clock) as a zero-padded decimal number.
#[%j] Day of the year as a zero-padded decimal number.
#[%U] Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number.
#[%W] Week number of the year (Monday as the first day of the week) as a zero-padded decimal number.
#[%c] Locale’s appropriate date and time representation.

print(date.strftime(r"%Y-%m-%d %H:%M:%S")) #2020

print(date.strftime(r"%Y/%m/%d %H:%M:%S")) #2020/05/17 15:30:45

print(date.strftime(r"%I %p %S")) #03 PM 45


print(date.strftime(r"%A %m %Y %H, %I %p %S")) #Sunday 05 2020 15, 03 PM 45


