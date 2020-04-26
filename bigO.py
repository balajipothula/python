import time
import random

item = random.randrange(65536)

n_array = [n for n in range(65536)]

n_array_len = len(n_array)

# binary search.
head = 0
tail = n_array_len - 1
start = time.time_ns()
while head <= tail:
  mid = (head + tail) // 2
  if n_array[mid] == item:
    print(item, " found at index ", mid, "binary search execution time ", time.time_ns() - start)
    break
  else:
    if item < n_array[mid]:
      tail = mid - 1
    else:
      head = mid + 1

# linier search.
start = time.time_ns()
for i in range(n_array_len):
  if item == n_array[i]:
    print(item, " found at index ", i,   "linier search execution time ", time.time_ns() - start)
    break
