import numpy as np
from math import *

from numpy.ma.core import arccos
from numpy.ma.extras import average

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

# print(np.dot(array1,array2))
# print(array1.shape) //размерность



array3 = np.zeros(5, dtype=int)
array4 = np.ones([3,3], dtype=int)
print(array4[2,1]) or print(array4[2][1])
arrT = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arrT.T)
m = arrT.max()
aver = arrT.mean()
arr5 = np.arange(10,-10,-1, dtype=int)
arr6 = np.linspace(1,6,5)
arr7 = np.random.rand(3,3) *100

matrix1 = np.array([[1,2],[2,3]])
matrix2 = np.array([5,6])

multiply = matrix1.dot(matrix2)
multiply1 = matrix1 @ matrix2
print(multiply1)


# print(arr7)
# print(arr6)
# print(arr5)
# print(array4*5)
#print(array4.sum())

def angleBeetVec(vec1, vec2):
    res = (vec1 @ vec2) / (sqrt(vec1[0]**2 + vec1[1]**2))*(sqrt(vec2[0]**2 + vec2[1]**2))
    return acos(res)

# print(angleBeetVec(np.array([0,1]), np.array([0,1]))

def ALLOrtogonal(Vectors):
    for i in range(len(Vectors)):
        for j in range(i+1,len(Vectors)):
            if np.dot(Vectors[i], Vectors[j]) == 0:
                return Vectors[i],Vectors[j]


vec1 = np.array([0, 1])
vec2 = np.array([1, 0])
vec3 = np.array([0, 4])

Vector = [vec1, vec2, vec3]
print(ALLOrtogonal(Vector))
