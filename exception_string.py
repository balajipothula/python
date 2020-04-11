import inspect

def lineno():
  """get line number"""
  return inspect.currentframe().f_back.f_lineno
  
def filename():
  """get file name"""
  return inspect.getframeinfo(inspect.currentframe()).filename

try:
  name = 'BALAJI POTHULA'
  print('Full  Name: ' + name)
  print('First Name: ' + name[0:6])
  print('Last  Name: ' + name[7:len(name)])
  
  print(filename())
  print(lineno())
  print(inspect.getframeinfo(inspect.currentframe()).lineno)
  

  #print('Last  Char: ' + name[len(name)]) ## IndexError

  #print('Float Char: ' + name[1.5])       ## TypeError

  #del name                                ## NameError
  #print('Full  Name: ' + name)            ## NameError

except IndexError as e:
  print("system message: " + str(e))
  print("user   message: index error")
  
except TypeError as e:
  print("system message: " + str(e))
  print("user   message: type error")
  
except NameError as e:
  print("system message: " + str(e))
  print("user   message: name error")

except Exception as e:
  print("system message: " + str(e))
  print("user   message: exception")

finally:
  print("finally block executed")
