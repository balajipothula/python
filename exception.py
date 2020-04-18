import sys

import inspect

def lineno():
  """get line number"""
  return str(inspect.currentframe().f_back.f_lineno)
  
def filename():
  """get file name"""
  return str(inspect.getframeinfo(inspect.currentframe()).filename)

try:
  a = int(input("Enter a Value: "))
  b = int(input("Enter b Value: "))
  print("a / b = " + str(a / b))
except ValueError as e:
  print("file name: " + filename() + ", line no: " + lineno() + ", system message: " + str(e))
  print("exception   of: " + str(sys.exc_info()[0]))
  print("user   message: value error")
except ZeroDivisionError as e:
  print("file name: " + filename() + ", line no: " + lineno() + ", system message: " + str(e))
  print("exception   of: " + str(sys.exc_info()[0]))
  print("user   message: zero division error")
except Exception as e:
  print("file name: " + filename() + ", line no: " + lineno() + ", system message: " + str(e))
  print("exception   of: " + str(sys.exc_info()[0]))
  print("user   message: exception")
finally:
  print("finally block executed")
