class A:
  def a(self): print("class A method a")
      
class B(A):    
 #pass
  def a(self): print("class B method b")

# single level inheritance.
b = B()
b.a()
