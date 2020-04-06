import random

x = ['a', 'b', 'c', 'd', 'e']

#print(random.choice(x))

# shuffling.
random.shuffle(x)
#print(x)

# printing random element.
#print(random.random())

s = set()
while 10 > len(s):
  r = random.randrange(1, 20)
  if r not in s:
    s.add(r)

print(s)

print(frozenset(s))

print(tuple(s))

s = set()
s.add(1)
print(s)

s = {1}
print(s)

t = (1,)
print(t)
print(type(t[0]))

t = tuple([1])
print(t)
print(type(t[0]))

