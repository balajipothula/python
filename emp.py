class Emp:

  org = "InfoSys"

  def __init__(self): pass

  def set_no(self, no):     self.no   = no
  def set_name(self, name): self.name = name
  def set_sal(self, sal):   self.sal  = sal
 
  def get_no(self):    return self.no
  def get_name(self):  return self.name
  def get_sal(self):   return self.sal
  
  @classmethod
  def get_org(cls):    return cls.org
  
  @staticmethod
  def class_info():    return "This is Emp Class"

  def to_string(self): return dict(org = Emp.get_org(), sal = str(self.sal), name = self.name, no = str(self.no))
  
  def __str__(self):   return str(self.no)

  def equals(self, e):
    if self is None or e is None or self.no != e.no or self.name != e.name or self.sal != e.sal: return False
    return True

print(Emp.class_info())

e1 = Emp()
e2 = Emp()

e1.set_no(101)
e1.set_name("Ram")
e1.set_sal(98765.43)

e2.set_no(101)
e2.set_name("Ram")
e2.set_sal(98765.43)

print(e1.to_string())
print(e2.to_string())

# e2 = None

if not e1.equals(e2):
  print("e1 and e2 are not equal")
else:
  print("e1 and e2 are equal")

print(e1, id(e1), hex(id(e1)))
print(e2, id(e2), hex(id(e2)))

e1 = None
e2 = None

print(id(e1))
print(id(e2))


print(e1)



class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
