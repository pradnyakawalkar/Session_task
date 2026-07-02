import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(A)
print("\n")
print(B)
print("Element-wise multiplication:", A*B)
print("Matrix multiplication:",np.dot(A,B))

# Difference:
# * multiplies corresponding elements.
# @ performs actual matrix multiplication.