class Add:

  def __init__(self): pass
  
  def add(self, a = None, b = None, c = None):
    if   None != a and None != b and None != c: return a + b + c
    elif None != a and None != b:               return a + b
    elif None != a:                             return a
    return 0

a = Add()

print(a.add(2, 4))
