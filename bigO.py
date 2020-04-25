import time
import random

e = random.randrange(65536)

n_array = [n for n in range(65536)]

n_array_len = len(n_array)

# binary search.
head = 0
tail = n_array_len - 1
start = time.time_ns()
while head <= tail:
  mid = (head + tail) // 2
  if n_array[mid] == e:
    print(e, " found at index ", mid, "execution time ", time.time_ns() - start)
    break
  else:
    if e < n_array[mid]:
      tail = mid - 1
    else:
      head = mid + 1

# linier search.
start = time.time_ns()
for i in range(n_array_len):
  if e == n_array[i]:
    print(e, " found at index ", i,   "execution time ", time.time_ns() - start)
    break
