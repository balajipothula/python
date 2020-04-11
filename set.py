num_set = {1, 2, 3, 4}

num_set = {1, 2, 3, 4}

frozen_num_set = frozenset(num_set) ## AttributeError

try:
  print(num_set.remove(3))
  print(num_set.remove(3)) ## KeyError
  
  frozen_num_set.add(5)

# calling remove function 2 times.
except KeyError as e:
  print("system message: " + str(e)) 
  print("user   message: key error")

# adding element to frozen set.
except AttributeError as e:
  print("system message: " + str(e))
  print("user   message: attribute error")

except Exception as e:
  print("system message: " + str(e))
  print("user   message: exception")

finally:
  print("finally block executed") 

while len(num_set) is not 0: print(num_set.pop())




