from time import sleep
from threading import Thread

class Thread1(Thread):
  def run(self):
    for i in range(9): print("I am in Thread1"); sleep(1)

class Thread2(Thread):
  def run(self):
    for i in range(9): print("I am in Thread2"); sleep(1)

t1 = Thread1()
t2 = Thread2()

t1.start()
sleep(.2)
t2.start()

t1.join()
t2.join()

print("I am in Main Thread")
