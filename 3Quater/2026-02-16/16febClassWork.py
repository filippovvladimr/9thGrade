import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(np.dot(array1,array2))
print(array1.shape)


array3 = np.zeros(5, dtype=int)
array4 = np.ones([3,3], dtype=int)
print(array4)