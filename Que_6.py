import numpy as np

arr1 = np.random.randint(1,101,(5,5))
print(arr1)
print("Diagonal:")
print(np.diag(arr1))

print("Greater than 50:")
print(arr1[arr1 > 50])

arr1[arr1 < 30] = 0

print("Modified Array:")
print(arr1)
