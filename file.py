try:
  f = open('hi', 'r')
  if None != f: print(f.readline())
except IOError as e: print(e)
finally:
  if None != f: f.close()
