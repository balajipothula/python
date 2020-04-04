class Interface1:

  def interface_method(self):
    print("iam in interface1 method")


class Interface2:

  def interface_method(self):
    print("iam in interface2 method")

    
class Sample:

  def sample_method(self, interface):
    interface.interface_method()

sample = Sample()

interface1 = Interface1()
sample.sample_method(interface1)

interface2 = Interface2()
sample.sample_method(interface2)
