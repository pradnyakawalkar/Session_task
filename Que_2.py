import numpy as np

arr = np.random.randint(1,51,20)

print("Array:", arr)
print("Minimum:",arr.min())
print("Indexof minimum:",arr.argmin())
print("Maximum:",arr.argmax())
print("sum:",arr.sum())
print("mean:",arr.mean())
print("Standard Deviation:",arr.std())