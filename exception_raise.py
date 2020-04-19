import sys

divisors = ['a', 0, 2]

for d in divisors:
  try:
    print("\n")
    if 0 == d: raise ZeroDivisionError("raising zero division error")
    print("divisor is    : " + str(d))
    print("4 divided by "    + str(d) + ": " + str(4 / int(d)))
  except ValueError as e:
    print("system message: " + str(e))
    print("user   message: " + "value error")
  except ZeroDivisionError as e:
    print("system message: " + str(e))
    print("user   message: " + "zero division error")
  except Exception as e:
    print("system message: " + str(e))
    print("user   message: " + "exception")
  finally:
    print("finally block executed")

print("\n")
print("EoS")
