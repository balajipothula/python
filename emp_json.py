import io
import os
import json

from os import path
from os import access

try:
  cwd        = os.getcwd()
  file_name  = "emp_json.json"
  file_path  = cwd + os.sep + file_name
  if not path.exists(file_path) or not path.isfile(file_path) or not os.access(file_path, os.R_OK):
    print("file not exist")
  else:
    f   = io.open(file_path, mode = "rt", encoding = "UTF-8") # opening json file.
    emp = json.load(f) # returns json object as a dictionary.
    print(emp["name"])
except IOError as e:
  print("system message: " + str(e))
  print("user   message: io error")
except Exception as e:
  print("system message: " + str(e))
  print("user   message: exception")
finally:  
  try:
    f.close() # closing file.
  except NameError as e:
    print("system message: " + str(e))
    print("user   message: name error")
  finally:
    pass
