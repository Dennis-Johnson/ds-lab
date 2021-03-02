tup = (12, 7, 38, 56, 78 )

even = [x for x in tup if x % 2 == 0]
new_tup = tuple(even)
print("Tuple with even numbers is --> " + str(new_tup))
