i = int(0)
while i < 9:
  print(i)
  if i == 6:
    break
  i += 1

i = int(0)
while i < 9:
  i += 1
  if i % 2 == 0:
    continue
  print(i)
