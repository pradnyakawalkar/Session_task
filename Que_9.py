import numpy as np

arr3 = np.random.randn(6,6)
print(arr3)

print("shape",arr3.shape)
print("minimum",arr3.argmin())
print("maximum",arr3.argmax())
print("Top Left 3x3:")
print(arr3[:3, :3])


print("Modified Array:")
print(arr3)
print("Mean =", arr3.mean())
