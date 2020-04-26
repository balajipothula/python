import time
import threading

def hi():
  for _ in range(9):
    time.sleep(1)
    print("hi....!")

def halo():
  for _ in range(9):
    time.sleep(1)
    print("halo..!")

hi    = threading.Thread(target = hi)
halo  = threading.Thread(target = halo)

hi.start()
halo.start()