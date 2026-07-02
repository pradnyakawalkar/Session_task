import numpy as np
arr = np.random.randint(20,80,(4,5))
print(arr)

print("minimum:",arr.min())
print("maximum:",arr.max())
print("sum:",arr.sum())
print("mean:",arr.mean())
print("standard Deviation:",arr.std())
print("row sum:",arr.sum(axis=1))
print("colum sum:",arr.sum(axis=0))


