import time
import datetime
import calendar

print("time in               seconds :", int(time.time()))
print("time in               seconds :", datetime.datetime.now().strftime("%s"))
print("time in               seconds :", calendar.timegm(datetime.datetime.utcnow().utctimetuple()))
print("\n")

nano_seconds  = time.time_ns()
milli_seconds = int(nano_seconds / 10e2)
seconds       = int(nano_seconds / 10e8)

print("nano seconds to       seconds :", seconds)
print("nano seconds to milli seconds :", milli_seconds)
print("nano seconds                  :", nano_seconds)

print("\n")

# local format.
localtime = time.localtime(seconds)
print(time.strftime("%Y_%m_%d_%H_%M_%S", localtime))

# local format.
timestamp = datetime.datetime.fromtimestamp(seconds)
print(timestamp.strftime("%Y_%m_%d_%H_%M_%S"))

# utc format.
utc_time_array = datetime.datetime.utcfromtimestamp(seconds)
print(utc_time_array.strftime("%Y_%m_%d_%H_%M_%S"))


nano_seconds_str = str(nano_seconds)
print(nano_seconds_str[0:10])
print(nano_seconds_str[10:])

print(time.clock())
