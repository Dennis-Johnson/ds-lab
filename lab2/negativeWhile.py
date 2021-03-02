l = [11, -21, 0, 45, 66, -93]

print("Program to print negative numbers in the list using a while loop")
print("Original list --> " + str(l))

counter = 0

while True:
    if counter >= len(l):
        break

    if l[counter] < 0:
        print(l[counter])
    counter += 1
