import random

item          = random.randrange(9)
item_list     = [item for item in range(9)]
item_list_len = len(item_list)
item_iter     = iter(item_list) # creating an iterator object from iter.

for _ in range(item_list_len):
  print(next(item_iter))

for item in item_list:
  print(item)

item_iter = iter(item_list)
for _ in range(item_list_len):
  print(item_iter.__next__())

item_iter = iter(item_list)
while True:
  try:
    item = next(item_iter)
    print(item)
  except StopIteration as e:
    print("end of the list")
    break
  finally:
    pass