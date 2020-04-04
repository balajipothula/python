try:
  a = int(input("Enter a Value: "))
  b = int(input("Enter b Value: "))
  print("a / b = " + str(a / b))
except ValueError as e:
  print("system message: " + str(e))
  print("user   message: value error")
except ZeroDivisionError as e:
  print("system message: " + str(e))
  print("user   message: zero division error")
except Exception as e:
  print("system message: " + str(e))
  print("user   message: exception")
finally:
  print("finally block executed")
