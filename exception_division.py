dividend = None
divisor  = None

while True:

  try:

    dividend = int(input("enter a dividend: "))
    divisor  = int(input("enter a divisor : "))

    if 0 > dividend:
      print("enter positive value")
      continue
    break

    if 0 == divisor:
      print("division not possible")
      continue
    break

  except ZeroDivisionError as e:
    print("zero division error")

result = dividend / divisor

print(result)
