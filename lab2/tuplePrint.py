tup = (1,3,5,7,9,2,4,6,8,10)

half = int(len(tup) / 2)

for i in range(half):
    print(tup[i], end = " ")

print("")
for i in range(half, len(tup)):
    print(tup[i], end = ' ')
print("")

