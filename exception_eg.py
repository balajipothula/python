import sys
import inspect

divisors = ['a', 0, 2]

for d in divisors:
  try:
    print("\n")
    print("divisor is    : " + str(d))
    print("4 divided by "    + str(d) + ": " + str(4 / int(d)))
  except Exception as e:
    print("system message: " + str(e))
    print("exception   of: " + str(sys.exc_info()[0]))
  finally:
    print("finally block executed")

print("\n")
print("EoS")
