# calculating factorial of a number.
def factorial(n):
  """calculating factorial of a number"""
  if 1 == n:
    return 1
  else:
    return n * factorial(n - 1)

n = 4
print(factorial.__doc__)
print(str("factorial of {} is: {}").format(n, factorial(n)))
