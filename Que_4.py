import numpy as np

arr = np.arange(1,25)

A1 = arr.reshape(4,6)

A2 = arr.reshape(3,8)

A3 = arr.reshape(2,3,4)

print(A1)
print("\n")
print(A2)
print("\n")
print(A3)

print("\n")

print(A1.shape)
print(A2.shape)
print(A3.shape)