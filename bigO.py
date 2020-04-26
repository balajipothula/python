import time
import random

limit         = 65536
item          = random.randrange(limit)
item_list     = [item for item in range(limit)]
item_list_len = len(item_list)

# binary search.
head = 0
tail = item_list_len - 1
start_exec_time = time.time_ns()
while head <= tail:
  mid = (head + tail) // 2
  if item == item_list[mid]:
    exec_time = time.time_ns() - start_exec_time
    print(item, " found at index ", mid, "binary search execution time ", exec_time)
    break
  else:
    if item < item_list[mid]:
      tail = mid - 1
    else:
      head = mid + 1

# linear search.
start_exec_time = time.time_ns()
for i in range(item_list_len):
  if item == item_list[i]:
    exec_time = time.time_ns() - start_exec_time
    print(item, " found at index ", i,   "linear search execution time ", exec_time)
    break