
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









