import datetime as dt;

from datetime import datetime
from datetime import date
from datetime import time

now = datetime.now()
print(now)

today = date.today()
print(today)

custom_date = date(year=2019, month=4, day=13)
print(custom_date)

today = date.today()
print(today)

timestamp = date.fromtimestamp(1326244364)
print(timestamp)

this = date.today() 
print(this.year)
print(this.month)
print(this.day)

now = datetime.now()
print(now.strftime("%Y-%m-%dT%H:%M:%S"))
print(now.strftime("%d %B %Y %H:%M:%S"))
