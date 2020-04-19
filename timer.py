import time

while True:
  localtime = time.localtime()
  timer     = time.strftime("%I:%M:%S %p", localtime)
  #print("#",   end="", flush=True)
  print(timer, end="", flush=True)
  print("\r",  end="", flush=True)
  time.sleep(1)
