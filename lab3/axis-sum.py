import numpy as np

mat = np.ones((3,4))

print("Original Matrix is:")
print(mat)

print("Sum of rows, axis=0 ---> {}".format(np.sum(mat, axis=0)))
print("Sum of cols, axis=1 ---> {}".format(np.sum(mat, axis=1)))
