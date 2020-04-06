num_list = [1, 2, 3, 4, 5, 6, 7, 8]

even_num_list = list(filter(lambda x: (0 == x % 2), num_list))
oddd_num_list = list(filter(lambda x: (1 == x % 2), num_list))

print(even_num_list)
print(oddd_num_list)

even_num_list = [x for x in range(8) if 0 == x % 2]
oddd_num_list = [x for x in range(8) if 1 == x % 2]

print(even_num_list)
print(oddd_num_list)

pow2 = [2 ** p for p in range(10)]
print(pow2)

pow2 = [2 ** p for p in range(10) if p > 4]
print(pow2)
