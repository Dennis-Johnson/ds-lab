import random
import math
import numpy as np

x = np.zeros(4)
y = np.ones(4)
z = np.array([(1.1,2.0),(3.5,4.5)])
print(x, y, z)
print(x[0].dtype, z[0][0].dtype)

#Sequences
print('\nSequences')
s = np.arange(10,30,5)
t = np.linspace(0, 2, 9)
print(s, t)

#Random numbers
print('\nRandom numbers')
print(random.choice([1,2,3,4,5]))
print(random.choice('Dennis'))
print(random.randrange(25,50))
print(random.randrange(25,50,5))
print(random.random())
print(random.shuffle([1,2,3,4]))

#Matrices
print('\nMatrices')
m = np.arange(15).reshape(3, 5)
print(m)

#Array operations
print('\nArrays')
a = np.array([10,20,30])
b = np.array([1,2,3])
c = a - b
print(c)

#Boolean array
print(a, a < 30)


#Matrix operations
print('\nMatrix operations')
A = np.array( [[1,1],[0,1]] )
B = np.array( [[2,0],[3,4]] )
print(A * B)

# elementwise product
print(A.dot(B))

# matrix product
print(np.dot(A, B))

# another matrix product
b = np.arange(12).reshape(3,4)
print(b.sum(axis=0))
print(b.sum(axis=1))

#Index operations
print("\nIndex operations")
a = np.arange(10) ** 3
print(a)

b = np.arange(20).reshape(5,4)
print(b[2,3])
print(b[-1,:]) # will fetch last row
print(b[:,-1]) # will fetch last col

for row in b:
	print (row) # will print every row

for element in b.flat:
	print (element) # will show all elements of b in 1-D array


# reshaping
print("\nReshaping")
print(b.ravel())
print(b.reshape(4,5))

#stacking
print("\nStacking")
a = np.array([(1,2), (3,4)])
b = np.array([(5,6), (7,8)])

print(np.vstack((a,b)))
print(np.hstack((a,b)))

#Iterating with for loops:
print("\nIterating with for loops:")

#Mapping with values
a = np.array([(3,2,9),(1,6,7)])
s1 = 0
for row in a:
	for col in row:
		s1+=col
print(s1)

#Mapping with index
a = np.array([(3,2,9),(1,6,7)])
s = 0
for i in range(a.shape[0]):
	for j in range(a.shape[1]):
		s += a[i,j]
print(s)


