import numpy as np

#-------------------------------------------------
print("a) Array with float32 data type:")
fl = np.ones((1,3), dtype = np.float32)
print(fl)

#------------------------------------------------
tup = (11, 22, 23, 24, 55, 67)
print("\nb) Creating np array from the tuple")
print(tup)

tupArr = np.array(tup)
print(tupArr)

#------------------------------------------------
print("\nc) Creating a 3x4 matrix of zeros")
mat3x4 = np.zeros((3,4))
print(mat3x4)

#------------------------------------------------
print("\nd) Sequence of integers from 0-20 with step size 5")
seq = np.arange(0,20+1,5) #end is non-inclusive
print(seq)


#------------------------------------------------
print("\ne) Reshape 3x4 matrix into a 2x2x3 matrix:")
reshapemat = np.random.rand(3,4)
print("Original matrix:", reshapemat)
reshapemat = np.reshape(reshapemat, (2,2,3))
print("Afer reshape: ", reshapemat)
 
#------------------------------------------------
mat = np.arange(9).reshape(3,3)
print("Find min and max in the matrix: ", mat)

print("\nMax = {}, Min = {}".format(np.max(mat), np.min(mat)))
print("Row wise max = {}, min = {}".format(str(np.max(mat, axis=0)), np.min(mat, axis = 0)))
print("Col wise max = {}, min = {}".format(str(np.max(mat, axis=1)), np.min(mat, axis = 1)))
print("Sum of all elements = {}".format(np.sum(mat)))
