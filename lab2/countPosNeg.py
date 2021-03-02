l = [11, -21, 0, 45, 66, -93]

print("Program to count positive and negative numbers in a given list")
print("Original list --> " + str(l))

pos = len([x for x in l if x > 0])
neg = len([x for x in l if x < 0])

print("Positives = %d, Negatives = %d" % (pos,neg))
