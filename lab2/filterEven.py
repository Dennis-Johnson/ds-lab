l = [11, -21, 0, 45, 66, -93]

print("Program to remove even elements from the list of given numbers")
print("Original list --> " + str(l))

l = filter(lambda x: x % 2 != 0, l)
print("List -> " + str(list(l)))
