from datetime import datetime
import time



now = datetime.now()

Y = now.strftime("%Y")
m = now.strftime("%m")
d = now.strftime("%d")
H = now.strftime("%H")
M = now.strftime("%M")
S = now.strftime("%S")
Z = now.strftime("%")

today = now.strftime("%d-%m-%YT%H:%M:%S")
print(today)


print(now.microsecond)


time_ns = time.time_ns()
print(time_ns)


date     = datetime.fromtimestamp(time_ns // 1e9)
print(date)

date_str = date.strftime("%d-%m-%YT%H:%M:%S")
print(date_str)

nanosecond_precision = str(int(time_ns % 1e9)).zfill(9)
print(nanosecond_precision)

