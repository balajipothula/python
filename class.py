class A:
  def __init__(self): print("class A constructor")
  def a(self): print("class A method a")
      
class B(A):
  def __init__(self):
    super().__init__()
    print("class B constructor")
    
  def b(self): print("class B method b")

class C(B):
  def __init__(self): print("class C constructor")
  def c(self): print("class C method c")

class D(A, B):
  def __init__(self): print("class D constructor")
  def d(self): print("class D method d")

# single level inheritance.
b = B()
b.a()
b.b()

print("\n")

# multi level inheritance.
c = C()
c.a()
c.b()
c.c()

print("\n")

# multiple inheritance.
d = D()
d.a()
d.b()
d.d()
