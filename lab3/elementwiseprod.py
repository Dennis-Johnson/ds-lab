import numpy as np

print("A:")
A = np.arange(6).reshape(2,3)
print(A)

print("B:")
B = np.arange(6).reshape(2,3) + 1
print(B)

print("Element wise product is:")
print(np.multiply(A, B))
