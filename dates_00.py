
import datetime
from datetime import datetime as dt


now = dt.now()

print(dt.hour)

print('----------------')

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


print('----------------')

# create timestamp in this moment
ahora = dt.now().timestamp()
print("Now ->", ahora)

# create date in this moment
ahora = dt.now()
print("Now ->", ahora)

timestamp = now.timestamp()

# create timestamp from date
print(timestamp)


year_2024 = dt(2024, 1, 1, 0, 5)

# create date
print(year_2024)

# create date from timestamp
print(dt.fromtimestamp(timestamp))
print('----------------')



def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
  

print_date(now)

print('------------')

from datetime import time


current_time = time(21, 6, 10)

print(current_time.hour)
print(current_time.min)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(2023, 8, 3)

print(current_date.year)
print(current_date.month)
print(current_date.day)


current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year + 1, current_date.month, current_date.day)

# current_date.year = current_date.year 

print(current_date)

# diff = year_2024 - current_date

print(year_2024 - now)

print(year_2024.date() - current_date)

# with time slots
from datetime import timedelta


star_time_delta = timedelta(200, 100, 100, weeks = 10)

end_time_delta = timedelta(300, 100, 100, weeks = 13)

print(end_time_delta - star_time_delta)
print(end_time_delta + star_time_delta)
# print(end_time_delta * star_time_delta) # Error
# print(end_time_delta / star_time_delta) # Error





