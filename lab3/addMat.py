import numpy as np

A = np.arange(6).reshape(3,2)
B = np.random.randn(3,2)

print("A:", A)
print("B:", B)

print("\nSum of A, B: ")
print(np.add(A, B))

