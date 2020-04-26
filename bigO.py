import time
import random

item = random.randrange(65536)

item_array = [item for item in range(65536)]

item_array_len = len(item_array)

# binary search.
head = 0
tail = item_array_len - 1
start_exec_time = time.time_ns()
while head <= tail:
  mid = (head + tail) // 2
  if item == item_array[mid]:
    exec_time = time.time_ns() - start_exec_time
    print(item, " found at index ", mid, "binary search execution time ", exec_time)
    break
  else:
    if item < item_array[mid]:
      tail = mid - 1
    else:
      head = mid + 1

# linear search.
start_exec_time = time.time_ns()
for i in range(item_array_len):
  if item == item_array[i]:
    exec_time = time.time_ns() - start_exec_time
    print(item, " found at index ", i,   "linear search execution time ", exec_time)
    break