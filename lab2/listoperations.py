l = []

x = int(input('Enter a value to append to list '))
l.append(x)
print(l)

print('Appending to list ')
l.append(2)
l.append(3)
print(l)

print("\nList length %d" % (len(l)))

print("\nSlice list l[0:2] --> " + str(l[0:2]))

l.reverse()
print("\nReversed list --> " + str(l))
print("\nPop %d from list" % (l[-1]))

l.pop()

print("\nlist is now ---> " + str(l))




