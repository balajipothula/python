import time

ns_list = list()

for i in range(10):
  time_now_ns = time.time_ns()
  ns_list.insert(i, time_now_ns)
  if 0 < i and i < 10:
    print("Current NS:", ns_list[i], "| Previous NS:", ns_list[i - 1], "| Difference:", ns_list[i] - ns_list[i - 1])
