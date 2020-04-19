import time

while True:
  print(time.strftime("%H:%M:%S"), end = "", flush = True)
  print("\r", end = "", flush = True)
  time.sleep(1)
