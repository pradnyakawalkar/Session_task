import numpy as np

arr = np.array([[10, 20, 30, 40],
[50, 60, 70, 80],
[90, 100, 110, 120]])

print("First row:")
print(arr[0])
print("\n")
print("Last column:")
print(arr[:,-1])
print("\n")
print("Center 2x2 matrix:")
print(arr[0:2,1:3])
print("\n")
print("Even number:")
print(arr[arr % 2 == 0])
