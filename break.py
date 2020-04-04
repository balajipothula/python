available_candies = 9
requested_candies = int(input("How many Candies you want: "))

i = 1

while i <= requested_candies:
  if i > available_candies:
    print("Out of stock")
    break
  print("Candy", i, "Given")
  i += 1

print("Bye")
