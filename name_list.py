name_list = ["Ram", "Sam", "Raj", "Jak", "Pal", "Bob", "Tom"]

print(name_list[0])
print(name_list[-1])
print(name_list[2:5]) # ['Raj', 'Jak', 'Pal']
print(name_list[-6:-3]) # ['Sam', 'Raj', 'Jak']
print(name_list)

for name in name_list:
  print(name)

name = str("Pall")
if name in name_list:
  print('Person "' + name + '" was found')
else:
  print('Person "' + name + '" was not found')
