import time

"""
for i in range(9):
  sns = time.time_ns()
  print(time.time_ns() - sns)
"""

for i in range(9): print(abs(time.time_ns() - time.time_ns()))
